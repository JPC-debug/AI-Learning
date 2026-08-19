# Day 10 - Pandas Advanced Data Analysis

## 学习目标

Day 10 主要学习 Pandas 中的数据合并、数据拼接、分组统计、聚合分析以及数据透视表。

在前面学习 Pandas 基础数据分析和数据清洗的基础上，本次进一步学习如何处理多张数据表，并通过学生成绩综合分析项目，将 `merge()`、`concat()`、`groupby()`、`agg()` 和 `pivot_table()` 等方法组合起来使用。

---

## 1. DataFrame 合并：merge()

`pd.merge()` 可以根据共同字段将两个 DataFrame 关联起来。

例如学生基本信息和学生成绩分别存储在不同的数据表中，可以通过 `student_id` 进行关联：

```python
student_scores = pd.merge(
    students,
    scores,
    on='student_id'
)
```

本次学习了四种常见的合并方式：

- `inner`：只保留两张表中都存在的数据
- `left`：保留左表中的全部数据
- `right`：保留右表中的全部数据
- `outer`：保留两张表中的全部数据

例如：

```python
inner_result = pd.merge(
    students,
    scores,
    on='student_id',
    how='inner'
)

left_result = pd.merge(
    students,
    scores,
    on='student_id',
    how='left'
)
```

如果某一条数据无法在另一张表中找到对应记录，合并后的相关字段可能出现 `NaN`。

可以简单理解为：

```text
inner → 两边都有
left  → 左边全要
right → 右边全要
outer → 两边全要
```

---

## 2. DataFrame 拼接：concat()

`pd.concat()` 可以将多个结构相似的 DataFrame 拼接在一起。

例如将两个班级的学生成绩合并：

```python
all_students = pd.concat(
    [class1, class2],
    ignore_index=True
)
```

其中：

```python
ignore_index=True
```

表示忽略原来的索引，并在拼接完成以后重新生成从 `0` 开始的连续索引。

`merge()` 和 `concat()` 的主要区别：

```text
merge  → 根据共同字段建立对应关系
concat → 直接将多个 DataFrame 拼接起来
```

例如：

```text
学生信息表 + 成绩表 → merge()

一班学生 + 二班学生 → concat()
```

---

## 3. 分组统计：groupby()

`groupby()` 可以按照指定字段对数据进行分组，然后分别对每一组进行统计。

例如计算每个班级的平均成绩：

```python
class_average = df.groupby('class')['score'].mean()
```

可以按照下面的顺序理解：

```text
df
 ↓
按照 class 分组
 ↓
选择 score
 ↓
计算 mean
```

也就是：

```python
df.groupby('class')['score'].mean()
```

常见的统计方法包括：

```python
mean()   # 平均值
max()    # 最大值
min()    # 最小值
sum()    # 总和
count()  # 数量
```

例如：

```python
class_average = df.groupby('class')['score'].mean()
class_max = df.groupby('class')['score'].max()
class_min = df.groupby('class')['score'].min()
class_count = df.groupby('class')['score'].count()
```

当遇到类似下面的问题时，可以优先考虑 `groupby()`：

```text
每个班级的平均成绩
每个城市的平均工资
每个商品的销售额
每个用户的消费金额
每个月的订单数量
```

---

## 4. 聚合统计：agg()

如果需要对同一个分组同时进行多个统计操作，可以使用 `agg()`。

例如：

```python
class_statistics = df.groupby('class')['score'].agg(
    average_score='mean',
    highest_score='max',
    lowest_score='min',
    score_count='count'
)
```

这样一次 `groupby()` 就可以同时计算：

- 平均成绩
- 最高成绩
- 最低成绩
- 成绩记录数量

相比重复写：

```python
mean()
max()
min()
count()
```

使用 `agg()` 可以让代码更加简洁，也更加适合进行综合数据统计。

其中：

```python
average_score='mean'
```

表示：

```text
average_score → 新统计列的名称
mean          → 使用的统计方法
```

---

## 5. 数据透视表：pivot_table()

`pivot_table()` 可以按照多个维度对数据进行交叉统计。

例如：

```python
score_pivot = pd.pivot_table(
    df,
    values='score',
    index='class',
    columns='subject',
    aggfunc='mean'
)
```

其中：

```text
values='score'
→ 要统计的数据

index='class'
→ 行代表班级

columns='subject'
→ 列代表科目

aggfunc='mean'
→ 使用平均值进行统计
```

最终可以得到类似：

```text
subject  Math  Python
class
A        ...    ...
B        ...    ...
```

这样可以非常直观地比较不同班级、不同科目的平均成绩。

可以通过四个问题理解 `pivot_table()`：

```text
1. 我要统计什么？
   → values

2. 谁放在左边？
   → index

3. 谁放在上面？
   → columns

4. 怎么进行统计？
   → aggfunc
```

---

## 6. 综合项目：学生成绩分析

本次综合项目使用两张原始数据表：

```text
students.csv
→ 学生基本信息

scores.csv
→ 学生各科成绩
```

首先使用：

```python
pd.read_csv()
```

读取数据：

```python
students = pd.read_csv('students.csv')
scores = pd.read_csv('scores.csv')
```

然后通过共同字段：

```text
student_id
```

合并两张表：

```python
student_scores = pd.merge(
    students,
    scores,
    on='student_id'
)
```

得到完整的数据结构：

```text
student_id
name
class
subject
score
```

一个学生可以对应多条成绩记录，例如：

```text
Jack → Math
Jack → Python
```

因此合并以后，一个学生可能出现多行，这属于正常的数据关系，并不是重复数据。

---

## 7. 班级整体成绩统计

通过：

```python
class_statistics = df.groupby('class')['score'].agg(
    average_score='mean',
    highest_score='max',
    lowest_score='min',
    score_count='count'
)
```

统计每个班级的：

```text
average_score → 平均成绩
highest_score → 最高成绩
lowest_score  → 最低成绩
score_count   → 成绩记录数量
```

---

## 8. 学生平均成绩统计

通过：

```python
student_average = df.groupby('name')['score'].mean()
```

计算每个学生所有课程的平均成绩。

这里进一步练习了：

```text
groupby
+
mean
```

的组合使用。

---

## 9. 班级 × 科目平均成绩

通过数据透视表：

```python
score_pivot = pd.pivot_table(
    df,
    values='score',
    index='class',
    columns='subject',
    aggfunc='mean'
)
```

分析：

```text
A班 Math 平均成绩
A班 Python 平均成绩
B班 Math 平均成绩
B班 Python 平均成绩
```

相比普通分组结果，数据透视表更加适合展示多个维度之间的关系。

---

## 10. 导出分析结果

完成分析以后，使用 `to_csv()` 将结果保存：

```python
class_statistics.to_csv(
    'class_statistics.csv'
)

student_average.to_csv(
    'student_average.csv',
    header=['average_score']
)

score_pivot.to_csv(
    'score_pivot.csv'
)
```

最终生成三个分析结果文件：

```text
class_statistics.csv
student_average.csv
score_pivot.csv
```

这样就完成了从原始数据到分析结果文件的完整流程。

---

## 项目文件结构

```text
day10_pandas_advanced/
│
├── README.md
├── practice.py
├── student_analysis.py
├── students.csv
├── scores.csv
├── class_statistics.csv
├── student_average.csv
└── score_pivot.csv
```

---

## Day 10 核心知识总结

今天主要掌握了以下 Pandas 技能：

```text
pd.merge()
    ↓
多张数据表关联

pd.concat()
    ↓
多个 DataFrame 拼接

groupby()
    ↓
按照指定字段分组

agg()
    ↓
一次完成多个统计

pivot_table()
    ↓
多维度交叉统计

to_csv()
    ↓
保存分析结果
```

完整的数据分析流程为：

```text
原始 CSV
    ↓
read_csv()
    ↓
读取数据
    ↓
merge()
    ↓
合并多张数据表
    ↓
groupby() / agg()
    ↓
分组和聚合统计
    ↓
pivot_table()
    ↓
多维度分析
    ↓
to_csv()
    ↓
导出分析结果
```

## 学习总结

通过 Day 10 的学习，我进一步掌握了 Pandas 中多表数据处理和进阶数据分析的方法。

相比之前主要针对单张 DataFrame 进行分析和清洗，今天开始处理多张存在关联关系的数据表，并能够通过共同字段将数据合并起来。

同时，通过 `groupby()`、`agg()` 和 `pivot_table()`，可以从不同角度对数据进行统计和分析。

目前已经能够完成一个基本的数据处理流程：

**数据读取 → 数据合并 → 分组统计 → 聚合分析 → 数据透视 → 结果导出**

这些知识是后续机器学习中进行数据预处理、探索性数据分析和特征处理的重要基础。