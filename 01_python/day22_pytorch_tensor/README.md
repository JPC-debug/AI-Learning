# Day22 PyTorch Tensor Basics

## 项目介绍

本项目正式开始进入 PyTorch 学习阶段。

Day22 主要学习 PyTorch 最基础、最核心的数据结构：

Tensor

可以把 Tensor 暂时理解为：

PyTorch 版本的 NumPy ndarray。

但相比 NumPy，Tensor 还可以支持：

- GPU 计算
- 自动求导
- 神经网络训练

---

## 项目结构

```text
day22_pytorch_tensor
│
├── tensor_basics.py
└── README.md
```

---

## PyTorch 环境

首先导入：

```python
import torch
```

并查看版本：

```python
print(torch.__version__)
```

当前使用的是 CPU 版本 PyTorch。

通过：

```python
torch.cuda.is_available()
```

可以判断 CUDA GPU 是否可用。

---

## Tensor 创建

创建一维 Tensor：

```python
a = torch.tensor(
    [1, 2, 3, 4]
)
```

创建二维 Tensor：

```python
matrix = torch.tensor(
    [
        [1, 2],
        [3, 4],
        [5, 6]
    ]
)
```

通过：

```python
matrix.shape
```

查看形状。

例如：

```text
torch.Size([3, 2])
```

表示 3 行 2 列。

通过：

```python
matrix.dtype
```

查看数据类型。

---

## Tensor 基本运算

Tensor 支持：

```python
x + y
x - y
x * y
x / y
```

其中：

```python
x * y
```

表示对应位置元素相乘。

例如：

```text
[1, 2, 3]
*
[4, 5, 6]

=

[4, 10, 18]
```

---

## 矩阵乘法

矩阵乘法可以使用：

```python
torch.matmul(A, B)
```

或者：

```python
A @ B
```

例如：

```text
A =
[[1, 2],
 [3, 4]]

B =
[[5, 6],
 [7, 8]]
```

得到：

```text
[[19, 22],
 [43, 50]]
```

矩阵乘法是后续神经网络计算的重要基础。

---

## NumPy 与 Tensor 转换

NumPy 转 Tensor：

```python
torch.from_numpy()
```

Tensor 转 NumPy：

```python
tensor.numpy()
```

需要注意：

```python
torch.from_numpy()
```

创建的 Tensor 通常会和原 NumPy 数组共享内存。

因此修改其中一个，另一个也可能发生变化。

如果希望独立复制，可以使用：

```python
torch.from_numpy(array).clone()
```

---

## 常用 Tensor 创建方法

全 0 Tensor：

```python
torch.zeros()
```

全 1 Tensor：

```python
torch.ones()
```

随机 Tensor：

```python
torch.rand()
```

例如：

```python
torch.rand(2, 3)
```

创建一个 2 行 3 列、数值位于 0 到 1 之间的随机 Tensor。

---

## reshape

使用：

```python
reshape()
```

可以改变 Tensor 的形状。

例如：

```text
[1, 2, 3, 4, 5, 6]
```

从：

```text
shape = [6]
```

转换为：

```text
[[1, 2, 3],
 [4, 5, 6]]

shape = [2, 3]
```

需要注意：

reshape 前后的元素总数量必须保持一致。

---

## Device

通过：

```python
device = torch.device(
    "cuda"
    if torch.cuda.is_available()
    else "cpu"
)
```

自动选择计算设备。

当前环境输出：

```text
cpu
```

以后可以通过：

```python
tensor.to(device)
model.to(device)
```

将数据和模型移动到对应计算设备。

---

## 学习收获

通过 Day22 学习了：

1. PyTorch Tensor 的基本概念
2. Tensor 的创建、shape 和 dtype
3. Tensor 加减乘除
4. 矩阵乘法
5. NumPy 和 Tensor 相互转换
6. NumPy 与 Tensor 的共享内存
7. zeros、ones、rand
8. reshape
9. CPU / GPU device

Day22 完成了 PyTorch 基础准备。