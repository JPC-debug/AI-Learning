# Day23 PyTorch Autograd

## 项目介绍

Day23 主要学习 PyTorch 的自动求导机制 Autograd，以及神经网络训练中最核心的梯度下降流程。

今天的核心目标是理解：

前向计算 → 计算损失 → 反向传播 → 获取梯度 → 更新参数

这些步骤就是后续训练神经网络的基础。

---

## 项目结构

```text
day23_pytorch_autograd
│
├── autograd_basics.py
└── README.md
```

---

## requires_grad

创建 Tensor 时可以设置：

```python
x = torch.tensor(
    2.0,
    requires_grad=True
)
```

表示 PyTorch 需要追踪与该 Tensor 有关的计算过程，以便后续自动计算梯度。

例如：

```python
y = x ** 2
```

当：

```text
x = 2
```

得到：

```text
y = 4
```

---

## backward 和 grad

通过：

```python
y.backward()
```

进行反向传播。

然后通过：

```python
x.grad
```

查看梯度。

对于：

```text
y = x²
```

导数为：

```text
dy/dx = 2x
```

当 x=2 时：

```text
dy/dx = 4
```

PyTorch 自动得到：

```text
x.grad = 4
```

---

## 链式法则

进一步测试：

```text
y = 2x
z = y²
```

当：

```text
x = 3
```

得到：

```text
y = 6
z = 36
```

通过：

```python
z.backward()
```

PyTorch 自动根据链式法则计算：

```text
dz/dx = 24
```

这就是神经网络反向传播的基本原理。

---

## 梯度累加

PyTorch 默认会累加梯度。

例如连续两次进行反向传播：

```text
第一次：
x.grad = 4

第二次：
x.grad = 8
```

第二次并不是导数变成了 8，而是：

```text
4 + 4 = 8
```

因此每次训练前都需要清空旧梯度。

可以使用：

```python
x.grad.zero_()
```

真实神经网络训练中通常使用：

```python
optimizer.zero_grad()
```

---

## 梯度下降

通过一个简单例子让参数 w 自动接近目标值 3：

```python
loss = (w - 3) ** 2
```

初始：

```text
w = 0
```

学习率：

```python
learning_rate = 0.1
```

根据梯度更新：

```python
w -= learning_rate * w.grad
```

训练过程中：

```text
w:
0.60
1.08
1.46
1.77
2.02
...
2.68
```

逐渐接近目标值 3。

同时 loss：

```text
9.00
5.76
3.69
2.36
1.51
...
0.16
```

不断下降。

这说明梯度可以指导参数向减少损失的方向更新。

---

## Optimizer

PyTorch 提供优化器自动完成参数更新。

创建 SGD：

```python
optimizer = torch.optim.SGD(
    [w],
    lr=0.1
)
```

标准训练流程：

```python
optimizer.zero_grad()

loss.backward()

optimizer.step()
```

分别表示：

```text
zero_grad()
清空旧梯度

backward()
计算新梯度

step()
根据梯度更新参数
```

使用 Optimizer 后，参数更新结果和手动梯度下降基本一致。

---

## PyTorch训练核心流程

今天已经接触到后续神经网络训练最核心的代码结构：

```python
for epoch in range(...):

    y_pred = model(X)

    loss = loss_fn(
        y_pred,
        y
    )

    optimizer.zero_grad()

    loss.backward()

    optimizer.step()
```

无论以后模型有多少层、多少参数，训练过程的基本结构都不会发生太大变化。

---

## 学习收获

通过 Day23 学习了：

1. requires_grad=True
2. PyTorch 自动求导机制
3. backward()
4. Tensor 的 grad 属性
5. 链式法则
6. 梯度累加
7. 梯度清零
8. learning rate
9. 梯度下降
10. torch.no_grad()
11. SGD Optimizer
12. optimizer.zero_grad()
13. optimizer.step()

Day23 完成了神经网络训练原理的基础学习。