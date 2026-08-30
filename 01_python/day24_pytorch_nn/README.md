# Day24 PyTorch Neural Network Basics

## 项目介绍

Day24 主要学习 PyTorch 中神经网络的基本结构，并完成第一个真正可以训练和预测的两层神经网络。

今天的核心内容包括：

nn.Module → Linear → 激活函数 → forward → Loss → Optimizer → 训练 → 新数据预测

---

## 项目结构

```text
day24_pytorch_nn
│
├── simple_network.py
└── README.md
```

---

## nn.Module

PyTorch 中的神经网络通常继承：

```python
nn.Module
```

例如：

```python
class SimpleNetwork(nn.Module):
    def __init__(self):
        super().__init__()
```

`nn.Module` 是 PyTorch 神经网络模型的基础类。

---

## Linear 层

首先创建一个简单线性层：

```python
self.linear = nn.Linear(2, 1)
```

表示：

```text
2 个输入特征
↓
1 个输出
```

本质计算：

```text
y = Wx + b
```

其中：

- W：权重
- b：偏置

通过打印 `weight` 和 `bias`，可以看到这些参数默认带有：

```text
requires_grad=True
```

因此可以通过反向传播自动更新。

---

## 两层神经网络

进一步创建：

```python
self.fc1 = nn.Linear(2, 4)
self.relu = nn.LeakyReLU()
self.fc2 = nn.Linear(4, 1)
```

网络结构：

```text
2 个输入
↓
Linear(2 → 4)
↓
LeakyReLU
↓
Linear(4 → 1)
↓
1 个输出
```

其中 4 表示隐藏层包含 4 个神经元。

数据 shape 变化：

```text
[1, 2]
→ [1, 4]
→ [1, 4]
→ [1, 1]
```

---

## forward

通过：

```python
def forward(self, x):
    x = self.fc1(x)
    x = self.relu(x)
    x = self.fc2(x)
    return x
```

定义数据在网络中的前向传播过程。

调用：

```python
model(x)
```

会自动执行 `forward()`。

---

## 模型参数

通过：

```python
model.named_parameters()
```

可以查看：

```text
fc1.weight
fc1.bias
fc2.weight
fc2.bias
```

本模型共有：

```text
17 个可学习参数
```

训练过程本质上就是不断调整这些参数。

---

## 训练数据

设置简单回归任务：

```text
[1, 2] → 3
[2, 3] → 5
[3, 4] → 7
[4, 5] → 9
```

目标规律：

```text
y = x1 + x2
```

---

## Loss 和 Optimizer

使用：

```python
loss_fn = nn.MSELoss()
```

计算预测值与真实值之间的均方误差。

优化器：

```python
optimizer = torch.optim.SGD(
    model.parameters(),
    lr=0.001
)
```

标准训练流程：

```python
y_pred = model(X)

loss = loss_fn(
    y_pred,
    y
)

optimizer.zero_grad()

loss.backward()

optimizer.step()
```

分别对应：

```text
前向预测
↓
计算损失
↓
清空旧梯度
↓
反向传播
↓
更新参数
```

---

## 训练过程

训练 500 轮后，Loss 从：

```text
约 50
```

逐渐下降到：

```text
约 0.26
```

说明模型正在不断学习目标规律。

训练过程中还遇到了两个问题：

### ReLU 卡住

部分随机初始化情况下，ReLU 可能导致神经元输出长期为 0，使 Loss 无法继续下降。

因此尝试：

```python
nn.LeakyReLU()
```

减少神经元失活问题。

### Loss 变成 NaN

当：

```text
lr = 0.01
```

时训练出现发散。

将学习率降低为：

```text
lr = 0.001
```

后训练恢复稳定。

这说明学习率会直接影响训练稳定性。

---

## 新数据预测

训练完成后输入：

```text
[5, 6]
```

理论结果：

```text
11
```

模型预测：

```text
10.8056
```

说明网络已经成功学习到接近：

```text
y = x1 + x2
```

的规律。

---

## 学习收获

通过 Day24 学习了：

1. nn.Module
2. nn.Linear
3. weight 和 bias
4. forward()
5. 多层神经网络结构
6. 隐藏层和神经元
7. LeakyReLU 激活函数
8. model.parameters()
9. MSELoss
10. SGD Optimizer
11. 完整训练循环
12. 学习率对训练的影响
13. Loss 卡住与 NaN 的基本排查
14. 使用训练后的模型预测新数据

Day24 完成了第一个真正可训练的 PyTorch 神经网络。

下一步 Day25 将继续系统学习 Loss Function、Optimizer 和完整神经网络训练流程。