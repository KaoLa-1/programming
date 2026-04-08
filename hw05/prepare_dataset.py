import sys
import os

# 添加用户目录到Python路径
sys.path.insert(0, os.path.expanduser(r'~\AppData\Roaming\Python\Python313\site-packages'))

from datasets import load_dataset
import json
import random

# 加载WMT14英文-中文平行语料库
dataset = load_dataset('wmt14', 'zh-en')

# 预处理数据
def preprocess_function(examples):
    return {
        'translation': examples['translation']
    }

# 处理训练数据
train_data = dataset['train'].map(preprocess_function, batched=True)
valid_data = dataset['validation'].map(preprocess_function, batched=True)

# 保存数据
def save_data(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        for item in data:
            f.write(json.dumps(item, ensure_ascii=False) + '\n')

# 保存前100万条数据用于微调
train_samples = min(1000000, len(train_data))
train_subset = train_data.select(range(train_samples))

print(f"训练数据大小: {len(train_subset)}")
print(f"验证数据大小: {len(valid_data)}")

# 保存数据
save_data(train_subset, 'train_data.jsonl')
save_data(valid_data, 'valid_data.jsonl')

print("数据准备完成！")
