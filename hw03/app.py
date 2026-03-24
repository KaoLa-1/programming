import streamlit as st
import cv2
import numpy as np
from PIL import Image
import os
from src.face_recognition_core import FaceRecognitionCore

# 初始化人脸识别核心
face_recognizer = FaceRecognitionCore()

# 页面标题
st.title("人脸识别系统")

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
        
        # 添加到已知人脸
        if face_recognizer.add_known_face(image_path, name):
            st.success(f"成功添加 {name} 的人脸")
        else:
            st.error("无法检测到人脸，请上传清晰的人脸图片")

# 主页面
st.subheader("人脸识别")

# 上传待识别图片
uploaded_test_image = st.file_uploader("上传待识别图片", type=["jpg", "jpeg", "png"])

if uploaded_test_image:
    # 读取图片
    image = Image.open(uploaded_test_image)
    image_array = np.array(image)
    
    # 显示原始图片
    st.subheader("原始图片")
    st.image(image, use_column_width=True)
    
    # 识别人脸
    face_locations, face_names = face_recognizer.recognize_faces(image_array)
    
    # 绘制人脸框
    result_image = face_recognizer.draw_faces(image_array, face_locations, face_names)
    
    # 显示识别结果
    st.subheader("识别结果")
    st.image(result_image, use_column_width=True)
    
    # 显示识别到的人脸
    st.subheader("识别到的人脸")
    for name in set(face_names):
        st.write(f"- {name}")