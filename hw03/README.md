# 人脸识别系统

基于 face_recognition 和 Streamlit 的人脸识别系统，用于人脸检测和识别。

## 功能特点

- 人脸检测：检测图片中的人脸位置
- 人脸识别：识别图片中的人脸身份
- 支持添加已知人脸到系统中
- 提供友好的 Web 界面

## 环境要求

- Python 3.7+
- 主要依赖：
  - face_recognition
  - Streamlit
  - OpenCV
  - NumPy

## 安装步骤

1. 克隆项目到本地

2. 安装依赖：
   ```bash
   pip install face_recognition streamlit opencv-python numpy
   ```

## 使用方法

1. 运行 Streamlit 应用：
   ```bash
   streamlit run app.py
   ```

2. 在浏览器中打开应用界面

3. 在侧边栏添加已知人脸：
   - 输入姓名
   - 上传清晰的人脸图片

4. 在主页面上传待识别图片，系统会自动检测和识别人脸

## 项目结构

- `app.py`：Streamlit 应用入口
- `src/face_recognition_core.py`：人脸识别核心功能
- `images/`：存储已知人脸图片
- `models/`：存储模型文件

## 注意事项

- 上传的人脸图片应清晰，正面朝向镜头
- 识别 accuracy 取决于训练数据的质量和数量
- 首次运行时，系统会下载必要的模型文件