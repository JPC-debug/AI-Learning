# Day29 MNIST CNN

## 项目介绍

Day29 开始学习 CNN（卷积神经网络），并使用 CNN 完成 MNIST 手写数字分类。

相比 Day26 的全连接网络，CNN 不需要一开始就把图片展平成 784 个数字，而是先保留图片的二维结构，通过卷积层提取局部特征，再通过池化层压缩特征，最后接全连接层完成分类。

---

## 项目结构

```text
day29_mnist_cnn
│
├── cnn_basics.py
├── models
│   └── mnist_cnn.pth
└── README.md
```

---

## CNN 网络结构

```python
class CNNNetwork(nn.Module):

    def __init__(self):
        super().__init__()

        self.conv1 = nn.Conv2d(
            in_channels=1,
            out_channels=16,
            kernel_size=3,
            padding=1
        )

        self.relu = nn.ReLU()
        self.pool = nn.MaxPool2d(kernel_size=2)

        self.conv2 = nn.Conv2d(
            in_channels=16,
            out_channels=32,
            kernel_size=3,
            padding=1
        )

        self.fc1 = nn.Linear(
            32 * 7 * 7,
            128
        )

        self.fc2 = nn.Linear(
            128,
            10
        )

    def forward(self, x):

        x = self.conv1(x)
        x = self.relu(x)
        x = self.pool(x)

        x = self.conv2(x)
        x = self.relu(x)
        x = self.pool(x)

        x = x.view(
            x.size(0),
            -1
        )

        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)

        return x
```

---

## Conv2d

第一层卷积：

```python
nn.Conv2d(
    in_channels=1,
    out_channels=16,
    kernel_size=3,
    padding=1
)
```

其中：

```text
in_channels=1
→ MNIST 是灰度图

out_channels=16
→ 学习 16 种不同特征

kernel_size=3
→ 使用 3×3 卷积核扫描图片

padding=1
→ 保持图片长宽不变
```

输入：

```text
[64, 1, 28, 28]
```

卷积后：

```text
[64, 16, 28, 28]
```

---

## 卷积核

卷积核可以理解成一个小窗口，在图片上不断移动。

例如 3×3 卷积核：

```text
图片局部区域
↓
与卷积核对应位置相乘
↓
结果相加
↓
生成新的特征值
```

不同卷积核可以学习不同特征，例如边缘、线条和局部形状。

---

## MaxPool

使用：

```python
nn.MaxPool2d(
    kernel_size=2
)
```

将每个 2×2 区域压缩成一个最大值。

因此：

```text
28 × 28
↓
14 × 14
```

第二次池化：

```text
14 × 14
↓
7 × 7
```

池化可以减少数据量，同时保留较明显的特征。

---

## Shape 变化

完整数据流：

```text
输入
[64, 1, 28, 28]

↓ Conv2d 1 → 16

[64, 16, 28, 28]

↓ MaxPool

[64, 16, 14, 14]

↓ Conv2d 16 → 32

[64, 32, 14, 14]

↓ MaxPool

[64, 32, 7, 7]

↓ Flatten

[64, 1568]

↓ Linear

[64, 128]

↓ Linear

[64, 10]
```

其中：

```text
32 × 7 × 7 = 1568
```

---

## CNN 与全连接网络的区别

Day26 全连接网络：

```text
[1,28,28]
↓
直接展平
↓
784
↓
Linear
```

这样会破坏图片原本的二维空间结构。

CNN：

```text
图片
↓
卷积
↓
提取局部特征
↓
池化
↓
提取更复杂特征
↓
最后再展平
```

因此更适合图像任务。

---

## Loss 和 Optimizer

使用：

```python
loss_fn = nn.CrossEntropyLoss()
```

优化器：

```python
optimizer = torch.optim.Adam(
    model.parameters(),
    lr=0.001
)
```

---

## 训练结果

训练 3 个 epoch：

```text
Epoch 1 Average Loss:
0.2327

Epoch 2 Average Loss:
0.0629

Epoch 3 Average Loss:
0.0429
```

Loss 持续下降，说明 CNN 正在不断学习。

---

## 测试结果

测试集准确率：

```text
Test Accuracy: 0.9888
```

即：

```text
98.88%
```

Day26 的全连接网络准确率约为：

```text
97.5%
```

CNN 提升约：

```text
1.38 个百分点
```

在 10000 张测试图片中：

```text
全连接网络大约错误：250 张

CNN 大约错误：112 张
```

CNN 的错误数量明显更少。

---

## 保存 CNN 模型

训练完成后：

```python
torch.save(
    model.state_dict(),
    "models/mnist_cnn.pth"
)
```

保存后的文件：

```text
models/mnist_cnn.pth
```

其中包含：

```text
conv1.weight
conv1.bias
conv2.weight
conv2.bias
fc1.weight
fc1.bias
fc2.weight
fc2.bias
```

等训练后的模型参数。

---

## 学习收获

通过 Day29 学习了：

1. CNN 基本概念
2. nn.Conv2d
3. in_channels
4. out_channels
5. kernel_size
6. padding
7. 卷积核
8. 特征图
9. nn.MaxPool2d
10. CNN 中图片 shape 的变化
11. 两层卷积网络
12. Flatten
13. CNN 训练流程
14. CNN 与全连接网络的区别
15. CNN 测试准确率
16. 保存 CNN 模型

Day29 完成了第一个真正的 CNN 图像分类模型。

下一步 Day30 将对整个 30 天学习计划进行总结，并完成最终的 MNIST CNN 模型加载、预测和项目收尾。