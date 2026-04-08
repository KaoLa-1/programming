import sys
import os

# 添加用户目录到Python路径
sys.path.insert(0, os.path.expanduser(r'~\AppData\Roaming\Python\Python313\site-packages'))

from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments
from peft import LoraConfig, get_peft_model
from datasets import load_dataset
import torch

# 加载模型和分词器
model_name = "meta-llama/Llama-5-8B"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16,
    device_map="auto"
)

# 配置LoRA
lora_config = LoraConfig(
    r=8,
    lora_alpha=32,
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj"],
    lora_dropout=0.05,
    bias="none"
)

# 创建PEFT模型
model = get_peft_model(model, lora_config)

# 加载数据集
dataset = load_dataset('json', data_files={'train': 'train_data.jsonl', 'validation': 'valid_data.jsonl'})

# 预处理数据
def preprocess_function(examples):
    inputs = []
    for item in examples['translation']:
        # 构建翻译任务的输入格式
        input_text = f"Translate English to Chinese: {item['en']}\nChinese:"
        inputs.append(input_text)
    
    # 分词
    tokenized = tokenizer(inputs, padding='max_length', truncation=True, max_length=128)
    
    # 构建标签
    labels = []
    for i, item in enumerate(examples['translation']):
        # 标签是中文翻译
        label_text = item['zh']
        label_tokens = tokenizer(label_text, padding='max_length', truncation=True, max_length=128)['input_ids']
        # 替换padding为-100，这样在计算损失时会被忽略
        label_tokens = [token if token != tokenizer.pad_token_id else -100 for token in label_tokens]
        labels.append(label_tokens)
    
    tokenized['labels'] = labels
    return tokenized

# 处理数据集
tokenized_dataset = dataset.map(preprocess_function, batched=True)

# 配置训练参数
training_args = TrainingArguments(
    output_dir="./results",
    evaluation_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=2,
    per_device_eval_batch_size=2,
    num_train_epochs=3,
    weight_decay=0.01,
    logging_dir="./logs",
    logging_steps=10,
    save_strategy="epoch",
    fp16=True
)

# 导入Trainer
from transformers import Trainer

# 创建Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset['train'],
    eval_dataset=tokenized_dataset['validation'],
    tokenizer=tokenizer
)

# 开始训练
print("开始训练...")
trainer.train()

# 保存模型
print("保存模型...")
model.save_pretrained("./fine-tuned-llama5")
tokenizer.save_pretrained("./fine-tuned-llama5")

print("微调完成！")
