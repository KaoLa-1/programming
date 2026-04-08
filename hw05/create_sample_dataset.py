import json

# 创建模拟的英文-中文平行语料库
sample_data = [
    {"translation": {"en": "Hello, how are you?", "zh": "你好，你怎么样？"}},
    {"translation": {"en": "I am fine, thank you.", "zh": "我很好，谢谢。"}},
    {"translation": {"en": "What is your name?", "zh": "你叫什么名字？"}},
    {"translation": {"en": "My name is John.", "zh": "我的名字是约翰。"}},
    {"translation": {"en": "Nice to meet you.", "zh": "很高兴认识你。"}},
    {"translation": {"en": "Where are you from?", "zh": "你来自哪里？"}},
    {"translation": {"en": "I am from China.", "zh": "我来自中国。"}},
    {"translation": {"en": "What do you do?", "zh": "你是做什么的？"}},
    {"translation": {"en": "I am a student.", "zh": "我是一名学生。"}},
    {"translation": {"en": "How old are you?", "zh": "你多大了？"}},
    {"translation": {"en": "I am 20 years old.", "zh": "我20岁了。"}},
    {"translation": {"en": "Do you like Chinese food?", "zh": "你喜欢中国食物吗？"}},
    {"translation": {"en": "Yes, I love it.", "zh": "是的，我很喜欢。"}},
    {"translation": {"en": "What is your favorite color?", "zh": "你最喜欢的颜色是什么？"}},
    {"translation": {"en": "My favorite color is blue.", "zh": "我最喜欢的颜色是蓝色。"}},
    {"translation": {"en": "Where do you live?", "zh": "你住在哪里？"}},
    {"translation": {"en": "I live in Beijing.", "zh": "我住在北京。"}},
    {"translation": {"en": "What time is it?", "zh": "现在几点了？"}},
    {"translation": {"en": "It is 3 o'clock.", "zh": "现在3点了。"}},
    {"translation": {"en": "Good morning!", "zh": "早上好！"}},
    {"translation": {"en": "Good afternoon!", "zh": "下午好！"}},
    {"translation": {"en": "Good evening!", "zh": "晚上好！"}},
    {"translation": {"en": "Good night!", "zh": "晚安！"}},
    {"translation": {"en": "Thank you very much.", "zh": "非常感谢。"}},
    {"translation": {"en": "You're welcome.", "zh": "不客气。"}},
    {"translation": {"en": "Sorry.", "zh": "对不起。"}},
    {"translation": {"en": "That's okay.", "zh": "没关系。"}},
    {"translation": {"en": "See you later.", "zh": "待会儿见。"}},
    {"translation": {"en": "Goodbye!", "zh": "再见！"}},
    {"translation": {"en": "Have a nice day.", "zh": "祝你有愉快的一天。"}}
]

# 保存为训练数据和验证数据
train_data = sample_data[:25]
valid_data = sample_data[25:]

def save_data(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        for item in data:
            f.write(json.dumps(item, ensure_ascii=False) + '\n')

save_data(train_data, 'train_data.jsonl')
save_data(valid_data, 'valid_data.jsonl')

print(f"训练数据大小: {len(train_data)}")
print(f"验证数据大小: {len(valid_data)}")
print("数据准备完成！")
