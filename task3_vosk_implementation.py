#!/usr/bin/env python3
# 任务三：基于Vosk的语音识别实现

import os
import sys
import json
from vosk import Model, KaldiRecognizer
import pyaudio

# 函数：安装Vosk库和依赖
def install_dependencies():
    print("正在安装Vosk库和依赖...")
    os.system(f"{sys.executable} -m pip install vosk pyaudio")
    print("安装完成")

# 函数：下载中文模型
def download_chinese_model():
    model_dir = "model"
    if not os.path.exists(model_dir):
        print("正在下载中文模型...")
        # 使用requests库下载文件
        import requests
        import zipfile
        url = "https://alphacephei.com/vosk/models/vosk-model-small-cn-0.22.zip"
        response = requests.get(url, stream=True)
        with open("model.zip", "wb") as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        # 使用Python内置的zipfile解压
        with zipfile.ZipFile("model.zip", "r") as zip_ref:
            zip_ref.extractall("model")
        os.remove("model.zip")
        print("模型下载完成")
    else:
        print("模型已存在，跳过下载")

# 函数：实时语音识别
def real_time_recognition():
    # 加载模型
    model = Model("model/vosk-model-small-cn-0.22")
    recognizer = KaldiRecognizer(model, 16000)
    
    # 打开麦克风
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
    stream.start_stream()
    
    print("开始语音识别，请说话...")
    print("按Ctrl+C退出")
    
    try:
        while True:
            data = stream.read(4000)
            if len(data) == 0:
                break
            if recognizer.AcceptWaveform(data):
                result = json.loads(recognizer.Result())
                print(f"识别结果: {result['text']}")
            else:
                # 可以在这里处理中间结果
                pass
    except KeyboardInterrupt:
        print("\n语音识别已停止")
    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()

# 函数：从音频文件识别
def recognize_from_file(file_path):
    if not os.path.exists(file_path):
        print(f"文件不存在: {file_path}")
        return
    
    # 加载模型
    model = Model("model/vosk-model-small-cn-0.22")
    recognizer = KaldiRecognizer(model, 16000)
    
    # 读取音频文件
    import wave
    wf = wave.open(file_path, "rb")
    
    print(f"正在识别文件: {file_path}")
    
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            print(f"识别结果: {result['text']}")
    
    # 处理最后一部分
    result = json.loads(recognizer.FinalResult())
    print(f"最终识别结果: {result['text']}")
    
    wf.close()

if __name__ == "__main__":
    # 安装依赖
    install_dependencies()
    
    # 下载中文模型
    download_chinese_model()
    
    # 选择识别模式
    print("\n请选择识别模式:")
    print("1. 实时麦克风识别")
    print("2. 从音频文件识别")
    print("3. 退出")
    
    choice = "1"  # 启用实时麦克风识别
    print(f"选择了选项: {choice}")
    
    if choice == "1":
        real_time_recognition()
    elif choice == "2":
        file_path = input("请输入音频文件路径: ")
        recognize_from_file(file_path)
    elif choice == "3":
        print("退出程序")
    else:
        print("无效选项")