# Day27 MNIST Model Save and Load

## 项目介绍

Day27 主要学习 PyTorch 模型的保存、加载和独立预测。

在 Day26 中已经完成 MNIST 手写数字分类模型训练，Day27 进一步把训练好的模型参数保存到本地，并在新的 `predict.py` 中重新加载模型，实现无需重新训练即可直接预测。

---

## 项目结构

```text
day27_mnist_model
│
├── train.py
├── predict.py
├── models
│   └── mnist_model.pth
└── README.md
```

---

## 神经网络结构

模型继续使用：

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

---

## 加载训练数据

继续复用 Day26 已下载的 MNIST 数据：

```python
train_data = datasets.MNIST(
    root="../day26_mnist/data",
    train=True,
    download=True,
    transform=ToTensor()
)
```

这里：

```text
train_data
```

表示数据本身。

随后通过：

```python
train_loader = DataLoader(
    train_data,
    batch_size=64,
    shuffle=True
)
```

把数据按每批 64 张的方式送入模型。

---

## Loss 和 Optimizer

使用：

```python
loss_fn = nn.CrossEntropyLoss()
```

作为分类损失函数。

优化器：

```python
optimizer = torch.optim.Adam(
    model.parameters(),
    lr=0.001
)
```

训练流程：

```text
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

核心代码：

```python
outputs = model(images)

loss = loss_fn(
    outputs,
    labels
)

optimizer.zero_grad()
loss.backward()
optimizer.step()
```

---

## 保存模型

训练完成后使用：

```python
torch.save(
    model.state_dict(),
    "models/mnist_model.pth"
)
```

其中：

```python
model.state_dict()
```

保存的是模型训练得到的参数，例如：

```text
fc1.weight
fc1.bias
fc2.weight
fc2.bias
```

保存后的文件：

```text
models/mnist_model.pth
```

---

## 为什么保存 state_dict

`state_dict` 只保存模型参数，不保存完整模型结构。

因此加载时需要先重新创建同样结构的模型。

这种方式更灵活，也是 PyTorch 中常见的模型保存方式。

---

## 加载模型

在 `predict.py` 中首先重新创建模型：

```python
model = MNISTNetwork()
```

然后读取参数：

```python
model.load_state_dict(
    torch.load(
        "models/mnist_model.pth"
    )
)
```

整个过程：

```text
MNISTNetwork()
↓
重新创建模型结构
↓
torch.load()
↓
读取保存的参数
↓
load_state_dict()
↓
把参数装入模型
```

随后：

```python
model.eval()
```

进入评估模式。

---

## 单张图片预测

从测试集中取一张图片：

```python
image, label = test_data[0]
```

原始 shape：

```text
[1, 28, 28]
```

展平：

```python
image = image.view(
    1,
    -1
)
```

变成：

```text
[1, 784]
```

然后预测：

```python
with torch.no_grad():

    output = model(image)

    prediction = torch.argmax(
        output,
        dim=1
    )
```

预测结果：

```text
预测：7
真实：7
```

说明加载后的模型可以直接使用，无需重新训练。

---

## 批量预测

进一步预测测试集前 10 张图片。

首先取出图片：

```python
images = []
labels = []

for i in range(10):

    image, label = test_data[i]

    images.append(image)
    labels.append(label)
```

使用：

```python
images = torch.stack(images)
```

把 10 个：

```text
[1, 28, 28]
```

合并成：

```text
[10, 1, 28, 28]
```

随后展平为：

```text
[10, 784]
```

预测结果：

```text
tensor([7, 2, 1, 0, 4, 1, 4, 9, 6, 9])
```

真实标签：

```text
tensor([7, 2, 1, 0, 4, 1, 4, 9, 5, 9])
```

前 10 张中预测正确 9 张。

其中一张真实数字 5 被预测成 6。

这说明模型具有较高准确率，但仍然可能对部分相似手写数字产生误判。

---

## 学习收获

通过 Day27 学习了：

1. torch.save()
2. torch.load()
3. model.state_dict()
4. load_state_dict()
5. 保存模型参数
6. 加载模型参数
7. model.eval()
8. 独立预测
9. 单张图片预测
10. 批量图片预测
11. torch.stack()
12. 模型预测错误样本分析

Day27 完成了 PyTorch 模型从训练、保存到重新加载和独立预测的完整流程。

下一步将继续深入 MNIST 模型评估和优化，并为后续 CNN 学习做准备。