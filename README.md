# AI-Learning

这是我的 Python、机器学习与深度学习学习仓库。

本项目记录了一个持续 30 天的 AI 基础学习计划，从 Python 编程基础开始，逐步学习数据分析、机器学习和 PyTorch，并最终完成基于 CNN 的 MNIST 手写数字识别项目。

## 学习路线

```text
Python 基础
    ↓
NumPy / Pandas
    ↓
Matplotlib 数据可视化
    ↓
Scikit-learn 机器学习
    ↓
模型训练 / 评估 / 调参
    ↓
PyTorch
    ↓
Tensor / Autograd
    ↓
神经网络 nn.Module
    ↓
MNIST
    ↓
CNN 卷积神经网络
    ↓
模型保存、加载与推理
```

## 主要学习内容

### Python

- Python 基础语法
- 函数
- 数据结构
- 面向对象编程
- 文件与 JSON
- 异常处理
- 模块化编程
- 列表推导式
- lambda / map / filter / reduce

### 数据分析

学习并使用：

- NumPy
- Pandas
- Matplotlib

完成了：

- 数组与矩阵操作
- DataFrame 数据处理
- 数据清洗
- merge / concat
- groupby
- pivot_table
- 数据可视化

### 机器学习

使用 Scikit-learn 学习：

- LinearRegression
- LogisticRegression
- DecisionTree
- RandomForest
- StandardScaler
- Pipeline
- train_test_split
- Cross Validation
- GridSearchCV

学习模型评价指标：

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix
- MSE
- R²

并完成 Titanic 生存预测项目。

### PyTorch

学习内容包括：

- Tensor
- NumPy 与 Tensor 转换
- Autograd 自动求导
- nn.Module
- Linear
- ReLU
- Loss Function
- Optimizer
- SGD
- Adam
- DataLoader
- 模型训练循环
- 模型保存与加载

## MNIST 深度学习项目

后期使用 MNIST 手写数字数据集完成神经网络训练。

### 全连接神经网络

模型结构：

```text
784
 ↓
128
 ↓
10
```

测试集准确率约：

```text
97.5%
```

### CNN 卷积神经网络

模型结构：

```text
1 × 28 × 28

Conv2d
1 → 16
 ↓
ReLU
 ↓
MaxPool
 ↓
Conv2d
16 → 32
 ↓
ReLU
 ↓
MaxPool
 ↓
Flatten
 ↓
Linear
1568 → 128
 ↓
ReLU
 ↓
Linear
128 → 10
```

训练 3 个 Epoch 后，MNIST 测试集准确率达到：

```text
98.88%
```

相比普通全连接神经网络进一步提高。

## 最终项目

Day 30 完成了 CNN 模型的完整使用流程：

```text
加载 MNIST 数据
        ↓
加载 CNN 模型
        ↓
单张图片预测
        ↓
批量预测
        ↓
随机图片预测
        ↓
Softmax
        ↓
预测概率与置信度
```

随机测试示例：

```text
真实标签：5
预测结果：5
预测置信度：99.99%
```

## 项目目录

主要代码位于：

```text
01_python/
```

其中按照学习进度划分为：

```text
day01_...
day02_...
...
day30_mnist_final/
```

每一天的目录中包含对应的代码和 README，用于记录当天的学习内容与实验结果。

## 使用技术

- Python
- NumPy
- Pandas
- Matplotlib
- Scikit-learn
- PyTorch
- Git
- GitHub
- VS Code

## 学习成果

通过这 30 天的学习，我已经初步完成了从传统 Python 编程到深度学习的完整入门过程，并能够：

- 使用 Python 进行基本程序开发
- 使用 Pandas / NumPy 处理数据
- 使用 Matplotlib 进行数据可视化
- 使用 Scikit-learn 建立机器学习模型
- 对模型进行训练、评估和调参
- 使用 PyTorch 构建神经网络
- 理解反向传播和梯度下降的基本原理
- 使用 CNN 完成图像分类
- 保存、加载并使用训练好的模型进行推理

## 下一阶段

接下来计划继续深入学习：

- PyTorch 深度学习
- CNN
- 模型优化
- GPU / CUDA
- 更完整的 AI 项目
- Transformer
- 大语言模型相关基础

---

30 天只是 AI 学习的起点。

持续学习，持续实践。