# Day26 MNIST Handwritten Digit Classification

## 项目介绍

Day26 开始进入经典深度学习任务：MNIST 手写数字分类。

本项目使用 PyTorch 和 torchvision 加载 MNIST 数据集，并训练一个简单的全连接神经网络，对 0～9 的手写数字进行分类。

---

## 项目结构

```text
day26_mnist
│
├── mnist_basics.py
├── data
└── README.md
```

---

## MNIST 数据集

MNIST 是经典的手写数字数据集，包括：

```text
训练集：60000 张图片
测试集：10000 张图片
```

每张图片大小为：

```text
28 × 28
```

并且是灰度图，因此单张图片 shape 为：

```text
[1, 28, 28]
```

其中：

```text
1 = 灰度通道
28 = 高
28 = 宽
```

---

## 加载数据

使用：

```python
from torchvision import datasets
from torchvision.transforms import ToTensor
```

加载数据：

```python
train_data = datasets.MNIST(
    root="data",
    train=True,
    download=True,
    transform=ToTensor()
)

test_data = datasets.MNIST(
    root="data",
    train=False,
    download=True,
    transform=ToTensor()
)
```

`ToTensor()` 会把图片转换成 PyTorch Tensor。

---

## DataLoader

使用：

```python
from torch.utils.data import DataLoader
```

创建：

```python
train_loader = DataLoader(
    train_data,
    batch_size=64,
    shuffle=True
)

test_loader = DataLoader(
    test_data,
    batch_size=64,
    shuffle=False
)
```

其中：

```text
Dataset = 数据本身
DataLoader = 负责按批次取数据
```

`batch_size=64` 表示每次给模型 64 张图片。

因此一个 batch 的图片 shape 为：

```text
[64, 1, 28, 28]
```

标签 shape 为：

```text
[64]
```

---

## 图片展平

全连接神经网络不能直接处理二维图片，因此需要把：

```text
[64, 1, 28, 28]
```

转换成：

```text
[64, 784]
```

代码：

```python
images = images.view(
    images.size(0),
    -1
)
```

因为：

```text
1 × 28 × 28 = 784
```

即每张图片最终变成 784 个输入特征。

---

## 神经网络结构

创建：

```python
class MNISTNetwork(nn.Module):

    def __init__(self):
        super().__init__()

        self.fc1 = nn.Linear(784, 128)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):

        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)

        return x
```

网络结构：

```text
784 个输入
↓
Linear(784 → 128)
↓
ReLU
↓
Linear(128 → 10)
↓
10 个数字类别
```

10 个输出分别对应：

```text
0 1 2 3 4 5 6 7 8 9
```

---

## Loss 和 Optimizer

分类任务使用：

```python
loss_fn = nn.CrossEntropyLoss()
```

优化器使用：

```python
optimizer = torch.optim.Adam(
    model.parameters(),
    lr=0.001
)
```

---

## Epoch 和训练流程

训练 5 个 epoch。

一个 epoch 表示：

```text
模型完整看完一次全部训练数据
```

训练流程：

```text
DataLoader 取一个 batch
↓
图片展平
↓
前向传播
↓
计算 Loss
↓
清空梯度
↓
反向传播
↓
更新参数
```

训练过程中平均 Loss：

```text
Epoch 1：0.3444
Epoch 2：0.1610
Epoch 3：0.1124
Epoch 4：0.0857
Epoch 5：0.0670
```

Loss 持续下降，说明模型正在不断学习。

---

## 测试模型

测试阶段使用：

```python
model.eval()
```

并关闭梯度：

```python
with torch.no_grad():
```

模型输出 10 个类别分数，通过：

```python
torch.argmax(
    outputs,
    dim=1
)
```

得到最终预测数字。

测试集准确率：

```text
Test Accuracy: 0.975
```

即：

```text
97.5%
```

在 10000 张测试图片中，大约识别正确：

```text
9750 张
```

---

## 实际预测结果

前 10 个预测：

```text
tensor([7, 2, 1, 0, 4, 1, 4, 9, 5, 9])
```

真实标签：

```text
tensor([7, 2, 1, 0, 4, 1, 4, 9, 5, 9])
```

前 10 张图片全部预测正确。

---

## 学习收获

通过 Day26 学习了：

1. MNIST 数据集
2. torchvision.datasets
3. ToTensor
4. torch.utils.data
5. Dataset 与 DataLoader
6. batch_size
7. epoch
8. 图像 Tensor shape
9. 图片展平
10. 全连接神经网络
11. CrossEntropyLoss
12. Adam 优化器
13. 完整训练循环
14. 测试集 Accuracy
15. 查看具体预测结果

Day26 完成了第一个真正意义上的图像分类项目。

下一步将继续围绕 MNIST 深入学习模型评估、保存加载模型，并为后续 CNN 学习做准备。