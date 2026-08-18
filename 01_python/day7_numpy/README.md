# Day 7 - NumPy 基础与学生成绩数据分析

## 学习目标

Day 7 开始正式进入 Python 数据科学与 AI 常用工具的学习。本日主要学习 NumPy，理解 ndarray 数组、二维数据、向量化计算、布尔索引以及常见统计操作，并通过学生成绩分析项目进行综合练习。

## 一、NumPy 基础

NumPy 是 Python 中常用的数值计算库，在数据分析、机器学习和深度学习中都会大量使用。

通常使用：

```python
import numpy as np
```

创建 NumPy 数组：

```python
scores = np.array([85, 92, 78, 96, 88])
```

常用属性：

```python
scores.size
scores.ndim
scores.shape
```

其中：

- `size` 表示数组中的元素总数
- `ndim` 表示数组的维度
- `shape` 表示每一个维度的大小

## 二、数组索引与切片

一维数组的索引和 Python 列表类似：

```python
scores[0]
scores[-1]
scores[0:3]
```

二维数组可以使用：

```python
scores[行, 列]
```

例如：

```python
scores[0, 1]
```

表示第 0 行、第 1 列的数据。

二维数组切片：

```python
scores[0, :]
scores[:, 2]
scores[0:2, 1:3]
```

其中 `:` 表示该维度上的全部数据。

## 三、向量化运算

NumPy 可以直接对整个数组进行数学运算：

```python
scores + 5
scores - 10
scores * 2
scores / 2
```

也可以对两个形状相同的数组进行逐元素计算。

这种直接对整个数组进行运算的方式称为向量化操作，相比逐个使用 `for` 循环处理数据更加简洁，也是 NumPy 的重要特点。

## 四、布尔索引

可以直接对数组中的所有元素进行条件判断：

```python
scores > 90
```

得到由 `True` 和 `False` 组成的布尔数组。

再利用布尔数组筛选数据：

```python
scores[scores > 90]
```

多个条件可以使用：

```python
scores[(scores >= 80) & (scores <= 90)]
```

布尔索引是后续数据清洗和数据筛选的重要基础。

## 五、统计计算

NumPy 提供了很多常见的统计方法：

```python
scores.sum()
scores.mean()
scores.max()
scores.min()
scores.argmax()
scores.argmin()
```

其中：

- `max()` 返回最大值
- `argmax()` 返回最大值所在的索引
- `min()` 返回最小值
- `argmin()` 返回最小值所在的索引

## 六、axis 的理解

对于二维数组：

```python
scores.mean(axis=1)
```

表示按行计算，每一行得到一个结果。

在学生成绩项目中，它可以计算每个学生的平均成绩。

```python
scores.mean(axis=0)
```

表示按列计算，每一列得到一个结果，可以用来计算每门课程的平均成绩。

同样：

```python
scores.max(axis=0)
scores.argmax(axis=0)
```

可以得到每一门课程的最高分以及最高分所在学生的索引。

## 七、学生成绩分析项目

项目使用一个二维 NumPy 数组保存 5 名学生的数学、英语和 Python 成绩。

主要实现：

- 查看学生和课程信息
- 查看完整成绩矩阵
- 获取指定学生或指定课程的数据
- 计算每个学生的平均成绩
- 计算每门课程的平均成绩
- 找出平均成绩最高的学生
- 找出每门课程的最高分及对应学生
- 处理并列最高平均分
- 使用布尔索引筛选平均分大于等于 90 的优秀学生

通过本项目，将 Python 中的 `for`、`zip()`、f-string 与 NumPy 数组操作结合起来，完成了一个简单的数据分析程序。

## 总结

Day 7 是从 Python 基础编程向数据分析和 AI 学习过渡的重要一步。

本日重点掌握了：

- ndarray
- shape 与 ndim
- 数组索引与切片
- 二维数组
- 向量化运算
- 布尔索引
- NumPy 统计函数
- `axis=0` 与 `axis=1`
- 基础数据分析思路

下一阶段将继续学习 Pandas 等数据处理工具，为之后的数据分析、机器学习和 AI 学习打基础。