# Day 6 - Python 进阶语法与数据处理

## 学习目标

Day 6 主要学习 Python 中常见的进阶语法，并开始练习使用多个 Python 工具组合处理数据，为后续学习 NumPy、Pandas 和机器学习中的数据处理打基础。

本日重点包括：

- 列表推导式
- 字典推导式
- 集合推导式
- `enumerate()`
- `zip()`
- `lambda` 匿名函数
- `sorted()` 自定义排序
- `map()`
- `filter()`
- 综合数据处理

---

## 1. 推导式

列表推导式可以用更加简洁的方式生成新的列表。

```python
numbers = [1, 2, 3, 4, 5]

result = [number ** 2 for number in numbers]
```

还可以加入条件：

```python
result = [number for number in numbers if number % 2 == 0]
```

字典推导式：

```python
result = {name: score for name, score in zip(names, scores)}
```

集合推导式：

```python
result = {number ** 2 for number in numbers}
```

集合会自动去除重复元素。

---

## 2. enumerate()

`enumerate()` 可以在遍历数据的同时获得编号。

```python
for index, name in enumerate(names, start=1):
    print(index, name)
```

使用 `start=1` 可以让编号直接从 1 开始。

---

## 3. zip()

`zip()` 可以把多个可迭代对象中对应位置的数据组合起来。

```python
names = ["Jack", "Rose", "Tom"]
scores = [85, 92, 76]

for name, score in zip(names, scores):
    print(name, score)
```

它非常适合处理具有对应关系的数据。

---

## 4. lambda 与 sorted()

`lambda` 可以创建简单的匿名函数。

```python
lambda x: x * 2
```

结合 `sorted()` 可以指定排序依据：

```python
ranking = sorted(
    students.items(),
    key=lambda item: item[1],
    reverse=True
)
```

其中 `item[1]` 表示按照成绩排序，`reverse=True` 表示从高到低排列。

---

## 5. map() 与 filter()

`map()` 主要用于对一批数据进行转换：

```python
result = list(map(lambda x: x * 2, numbers))
```

`filter()` 主要用于按照条件筛选数据：

```python
result = list(
    filter(lambda x: x >= 60, scores)
)
```

可以简单理解为：

- `map()`：改变数据
- `filter()`：筛选数据

---

## 6. 综合项目：学生成绩数据分析器

本日完成了一个学生成绩数据分析程序。

原始数据由学生姓名列表和成绩列表组成，通过 `zip()` 和字典推导式将两个列表转换为学生成绩字典。

程序实现了：

- 生成学生成绩数据
- 筛选及格学生
- 按成绩从高到低排名
- 显示学生名次
- 计算平均成绩
- 获取最高成绩
- 获取最低成绩

在项目中综合使用了：

```text
zip()
→ 字典推导式
→ filter()
→ lambda
→ sorted()
→ enumerate()
→ 数据统计
```

通过这个项目，开始从单独学习 Python 语法转向使用多个工具组合完成数据处理任务。

---

## Day 6 总结

Day 6 的重点不是单纯记忆新的函数，而是理解 Python 中的数据处理方式。

例如：

```text
原始数据
   ↓
组合
   ↓
筛选
   ↓
转换
   ↓
排序
   ↓
统计
   ↓
输出结果
```

这种“数据处理流水线”的思想会在后续 NumPy、Pandas、数据分析和机器学习中继续出现。

Day 6 完成后，已经能够使用 Python 的常见进阶语法对简单数据进行组合、筛选、转换、排序和统计，为下一阶段的数据科学工具学习做好准备。