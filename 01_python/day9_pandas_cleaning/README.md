# Day 9 - Pandas 数据清洗

## 学习目标

本次学习主要练习使用 Pandas 对真实数据中常见的“脏数据”进行清洗，包括缺失值、重复值、错误类型、字符串格式问题和异常值，并完成一个学生数据清洗项目。

## 主要知识点

### 1. 缺失值处理

使用：

```python
df.isnull().sum()
```

检查每一列的缺失值数量。

使用：

```python
df.dropna()
```

删除包含缺失值的数据。

使用：

```python
df['score'] = df['score'].fillna(df['score'].mean())
```

用平均值填充缺失数据。

---

### 2. 重复数据处理

使用：

```python
df.duplicated()
```

判断重复记录。

使用：

```python
df.drop_duplicates()
```

删除重复数据。

还可以使用：

```python
df.duplicated(subset=['name'])
```

根据指定列判断重复。

---

### 3. 数据类型转换

使用：

```python
df['age'] = df['age'].astype(int)
```

转换数据类型。

对于包含 `unknown`、`error` 等非法字符串的数据，可以使用：

```python
df['age'] = pd.to_numeric(df['age'], errors='coerce')
```

无法转换的数据会变成 `NaN`，之后再进行缺失值处理。

---

### 4. 字符串数据清洗

使用：

```python
df['name'] = df['name'].str.strip().str.lower()
```

删除字符串两端空格并统一大小写。

常用方法包括：

```python
.str.strip()
.str.lower()
.str.upper()
.str.replace()
```

---

### 5. 分类数据统计

使用：

```python
df['city'].value_counts()
```

统计一列中每个不同值出现的次数。

---

### 6. 异常值处理

通过条件筛选发现异常数据，例如：

```python
df.loc[(df['age'] <= 0) | (df['age'] >= 100), 'age'] = np.nan
```

也可以使用：

```python
df.loc[~df['score'].between(0, 100), 'score'] = np.nan
```

将异常数据转换为 `NaN`，再使用平均值等方式进行填充。

---

## 综合项目

本次完成了学生数据清洗项目。

原始数据文件：

```text
students_dirty.csv
```

数据中包含：

- 缺失值
- 重复数据
- `unknown` 和 `error` 等非法字符串
- 多余空格
- 大小写不统一
- 年龄异常值
- 成绩异常值

使用 Pandas 完成以下流程：

```text
读取 CSV
↓
检查数据
↓
清洗字符串
↓
转换数据类型
↓
删除重复数据
↓
处理异常值
↓
处理缺失值
↓
成绩分析
↓
导出干净 CSV
```

最终生成：

```text
students_cleaned.csv
```

同时完成平均成绩、最高成绩、最低成绩和成绩排名分析。

## 本次收获

通过 Day 9 的学习，我开始理解真实数据通常不能直接用于数据分析或机器学习。

在进行 AI 和机器学习之前，需要先检查并处理数据质量问题。

相比单独记住 Pandas 函数，更重要的是建立完整的数据清洗思路：

```text
发现问题 → 判断问题类型 → 清洗数据 → 再次检查 → 分析与导出
```

这也是后续机器学习数据预处理的重要基础。