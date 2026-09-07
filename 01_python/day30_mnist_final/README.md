# Day 30 - MNIST 最终项目总结

## 今日目标

完成 30 天 Python + 机器学习 + PyTorch 学习计划的最终收尾。

本次主要练习：

- 加载已经训练好的 CNN 模型
- 单张图片预测
- 批量预测
- 统计预测正确率
- 随机抽取测试图片
- 使用 Softmax 计算预测概率
- 输出模型预测置信度

---

## 项目结构

```text
day30_mnist_final/
│
├── final_predict.py
└── README.md
```

CNN 模型直接使用 Day 29 训练并保存的模型：

```text
../day29_mnist_cnn/models/mnist_cnn.pth
```

MNIST 测试数据继续复用 Day 26 的数据：

```text
../day26_mnist/data
```

---

## CNN 模型结构

模型主要包含：

```text
输入图片：1 × 28 × 28

Conv2d
1 → 16

ReLU

MaxPool
28 × 28 → 14 × 14

Conv2d
16 → 32

ReLU

MaxPool
14 × 14 → 7 × 7

Flatten
32 × 7 × 7 = 1568

Linear
1568 → 128

ReLU

Linear
128 → 10
```

最终输出 10 个分数，分别对应数字：

```text
0 1 2 3 4 5 6 7 8 9
```

---

## 模型加载

使用：

```python
model.load_state_dict(torch.load(...))
model.eval()
```

加载 Day 29 保存的 CNN 参数，并切换到推理模式。

---

## 单张图片预测

测试第一张图片：

```text
图片shape: torch.Size([1, 28, 28])

真实标签: 7

预测结果: 7
```

预测正确。

---

## 批量预测

预测 MNIST 测试集前 10 张图片：

```text
真实=7  预测=7
真实=2  预测=2
真实=1  预测=1
真实=0  预测=0
真实=4  预测=4
真实=1  预测=1
真实=4  预测=4
真实=9  预测=9
真实=5  预测=5
真实=9  预测=9
```

结果：

```text
前10张图片预测正确率：100.00%
```

---

## Softmax 与置信度

神经网络最后输出的是 logits，而不是直接的概率。

使用：

```python
probabilities = torch.softmax(output, dim=1)
```

可以把模型输出转换成概率。

随机预测结果：

```text
图片编号：779

真实标签：5

预测结果：5

预测置信度：99.99%
```

需要注意：

> 高置信度并不代表预测一定正确，模型也可能非常自信地预测错误。

---

## 今日总结

Day 30 完成了一个完整的深度学习模型使用流程：

```text
数据加载
↓
CNN 模型
↓
模型训练
↓
模型保存
↓
模型加载
↓
模型推理
↓
批量预测
↓
Softmax 概率
↓
预测置信度
```

经过 30 天学习，目前已经接触并实践了：

```text
Python
NumPy
Pandas
Matplotlib
Scikit-learn
机器学习
模型评估
模型调参
PyTorch
Tensor
Autograd
nn.Module
Loss
Optimizer
MNIST
CNN
模型训练
模型保存与加载
模型推理
```

30 天 Python + AI 基础学习计划完成。