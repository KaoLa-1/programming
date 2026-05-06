# Chest X-Ray Pneumonia Classification (Assignment hw07)

本项目是一个基于卷积神经网络 (CNN) 的深度学习项目，旨在通过胸部 X 光图像自动识别肺炎[cite: 1, 2]。项目完全在 Google Colab 环境下运行，利用 TensorFlow 和 Keras 框架构建[cite: 2]。

## 📋 提交内容清单
根据 **hw07** 任务要求，本项目已包含以下核心产出[cite: 1, 2]：
*   **训练日志 (Training Logs)**: 包含完整的 12 个 Epoch 的训练过程记录[cite: 2]。
*   **性能评估图表**: 包含 Loss 和 Accuracy 随 Epoch 变化的训练曲线[cite: 2]。
*   **混淆矩阵 (Confusion Matrix)**: 详细展示模型对 Normal 与 Pneumonia 类别的分类表现[cite: 2]。
*   **模型权重文件**: 训练完成的 `.h5` 格式模型文件[cite: 2]。

## 🛠️ 环境准备
*   **开发平台**: Google Colab[cite: 2]。
*   **主要依赖库**:
    *   `TensorFlow 2.x` / `Keras` (模型构建)[cite: 2]
    *   `Scikit-learn` (性能指标评估)[cite: 2]
    *   `Matplotlib` / `Seaborn` (结果可视化)[cite: 2]
*   **数据挂载**: 数据集存储于 Google Drive 路径 `/content/drive/MyDrive/kaggle_data/`[cite: 2]。

## 🏗️ 模型架构
为了平衡计算效率与特征提取能力，模型采用了以下结构[cite: 2]：
1.  **卷积层 (Convolutional Layers)**: 三组卷积操作（32, 64, 128 滤波器），用于逐级提取图像的边缘、纹理及复杂特征[cite: 2]。
2.  **池化层 (Pooling)**: 最大池化层用于降低维度并增强特征不变性[cite: 2]。
3.  **全连接层 (Dense)**: 包含 512 个神经元的隐藏层[cite: 2]。
4.  **正则化 (Dropout)**: 加入 `Dropout(0.5)` 以减少模型对特定神经元的依赖，防止过拟合[cite: 2]。
5.  **输出层**: Sigmoid 激活函数，用于二分类预测[cite: 2]。

## 🚀 核心流程
*   **数据处理**: 使用 `ImageDataGenerator` 进行实时数据增强（包括旋转、缩放、水平翻转），提高模型泛化能力[cite: 2]。
*   **模型训练**: 配置为 12 个 Epoch，优化器使用 Adam，损失函数为 Binary Cross-entropy[cite: 2]。
*   **自动保存**: 训练后的模型自动保存至 `MyDrive/hw07/trained_pneumonia_model.h5`[cite: 2]。

## 📂 文件夹结构说明
*   `hw07_pneumonia.ipynb`: 核心训练脚本[cite: 1, 2]。
*   `README.md`: 项目说明文档。
*   `trained_pneumonia_model.h5`: 预训练模型权重[cite: 2]。

---
*本项目为学术作业 hw07 成果，仅供学习与交流使用。*
