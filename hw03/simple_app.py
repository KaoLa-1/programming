import streamlit as st
import cv2
import numpy as np
from PIL import Image
import os

# 页面标题
st.title("简易人脸识别系统")

# 侧边栏
with st.sidebar:
    st.header("设置")
    
    # 添加已知人脸
    st.subheader("添加已知人脸")
    name = st.text_input("姓名")
    uploaded_image = st.file_uploader("上传人脸图片", type=["jpg", "jpeg", "png"])
    
    if uploaded_image and name:
        # 保存上传的图片
        image_path = os.path.join("images", f"{name}.jpg")
        with open(image_path, "wb") as f:
            f.write(uploaded_image.getbuffer())
        st.success(f"成功添加 {name} 的人脸")

# 主页面
st.subheader("人脸检测")

# 上传待识别图片
uploaded_test_image = st.file_uploader("上传待识别图片", type=["jpg", "jpeg", "png"])

if uploaded_test_image:
    # 读取图片
    image = Image.open(uploaded_test_image)
    image_array = np.array(image)
    
    # 显示原始图片
    st.subheader("原始图片")
    st.image(image, use_column_width=True)
    
    # 转换为灰度图
    gray = cv2.cvtColor(image_array, cv2.COLOR_RGB2GRAY)
    
    # 加载人脸检测器
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    # 检测人脸
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # 绘制人脸框
    result_image = image_array.copy()
    for (x, y, w, h) in faces:
        cv2.rectangle(result_image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(result_image, "Person", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    
    # 显示检测结果
    st.subheader("检测结果")
    st.image(result_image, use_column_width=True)
    
    # 显示检测到的人脸数量
    st.subheader("检测到的人脸数量")
    st.write(f"共检测到 {len(faces)} 个人脸")