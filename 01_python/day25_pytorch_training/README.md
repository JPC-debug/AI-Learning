# Day25 PyTorch Training Basics

## 项目介绍

Day25 主要学习 PyTorch 中神经网络训练的完整流程，并重点理解：

- Loss Function
- Optimizer
- model.train()
- model.eval()
- torch.no_grad()
- 分类预测
- Accuracy
- SGD 与 Adam 的区别

今天完成了一个简单的二分类神经网络训练任务。

---

## 项目结构

```text
day25_pytorch_training
│
├── training_basics.py
└── README.md
```

---

## 数据集

准备 6 个二维样本：

```python
X = torch.tensor(
    [
        [1.0, 1.0],
        [1.5, 1.2],
        [2.0, 1.8],
        [4.0, 4.0],
        [4.5, 4.2],
        [5.0, 4.8]
    ]
)

y = torch.tensor(
    [
        0,
        0,
        0,
        1,
        1,
        1
    ]
)
```

前 3 个样本属于类别 0，后 3 个样本属于类别 1。

---

## 分类网络

定义两层神经网络：

```python
class Classifier(nn.Module):

    def __init__(self):
        super().__init__()

        self.fc1 = nn.Linear(2, 4)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(4, 2)

    def forward(self, x):

        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)

        return x
```

网络结构：

```text
2 个输入特征
↓
Linear(2 → 4)
↓
ReLU
↓
Linear(4 → 2)
↓
2 个类别分数
```

最后输出 2 个值，分别代表类别 0 和类别 1 的分数。

---

## CrossEntropyLoss

分类任务使用：

```python
loss_fn = nn.CrossEntropyLoss()
```

它适合多分类任务。

模型直接输出类别分数，不需要手动添加 Softmax。

真实标签使用：

```text
0
1
```

这样的类别编号。

---

## 标准训练流程

PyTorch 的训练循环：

```python
for epoch in range(200):

    model.train()

    outputs = model(X)

    loss = loss_fn(
        outputs,
        y
    )

    optimizer.zero_grad()

    loss.backward()

    optimizer.step()
```

完整流程：

```text
model.train()
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

其中：

```python
optimizer.zero_grad()
```

用于清空上一轮梯度。

```python
loss.backward()
```

计算梯度。

```python
optimizer.step()
```

根据梯度更新模型参数。

---

## 模型评估

训练完成后进入评估模式：

```python
model.eval()
```

预测时使用：

```python
with torch.no_grad():
```

避免构建反向传播计算图，提高推理效率。

分类结果通过：

```python
predictions = torch.argmax(
    outputs,
    dim=1
)
```

得到。

例如：

```text
[2.1, 0.4] → 类别 0

[0.3, 3.2] → 类别 1
```

---

## Accuracy

使用：

```python
correct = (
    predictions == y
).sum().item()

total = y.size(0)

accuracy = correct / total
```

最终预测：

```text
tensor([0, 0, 0, 1, 1, 1])
```

真实标签：

```text
tensor([0, 0, 0, 1, 1, 1])
```

因此：

```text
Accuracy = 1.0
```

准确率达到 100%。

---

## SGD

首先使用：

```python
optimizer = optim.SGD(
    model.parameters(),
    lr=0.01
)
```

SGD 训练稳定，但下降速度相对较慢。

训练 1000 轮后，Loss 从约：

```text
0.63
```

下降到：

```text
0.12
```

最终准确率达到：

```text
1.0
```

---

## Adam

随后使用：

```python
optimizer = optim.Adam(
    model.parameters(),
    lr=0.01
)
```

仅训练 200 轮，Loss 从：

```text
0.56
```

下降到：

```text
0.036
```

最终：

```text
Accuracy = 1.0
```

在本次实验中，Adam 比 SGD 收敛更快。

但不同任务和网络中效果可能不同，不能简单认为 Adam 一定优于 SGD。

---

## train 和 eval

训练阶段：

```python
model.train()
```

测试阶段：

```python
model.eval()
```

以后使用 Dropout、BatchNorm 等网络层时，这两个模式会更加重要。

标准流程可以总结为：

```text
训练：
model.train()
→ forward
→ loss
→ zero_grad
→ backward
→ step

测试：
model.eval()
→ no_grad()
→ forward
→ argmax
→ accuracy
```

---

## 学习收获

通过 Day25 学习了：

1. MSELoss 与 CrossEntropyLoss 的区别
2. 分类任务标签格式
3. 分类网络输出方式
4. 标准 PyTorch 训练循环
5. model.train()
6. model.eval()
7. torch.no_grad()
8. torch.argmax()
9. Accuracy 计算
10. SGD 优化器
11. Adam 优化器
12. 不同优化器对训练速度的影响

Day25 完成了 PyTorch 神经网络从训练到评估的完整流程。

下一步将进入更接近真实深度学习任务的内容，为 MNIST 图像分类做准备。