# Day 12 - Matplotlib Advanced

今天学习了 Matplotlib 的进阶用法，并把之前学习的 Pandas 数据处理和 Matplotlib 数据可视化结合起来，完成了一个学生成绩分析小项目。

## 1. 多子图 subplots

使用：

```python
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
```

可以在同一个 Figure 中创建多个子图。

其中：

- `fig` 表示整张画布
- `axes` 表示各个子图
- `axes[0, 0]` 表示左上角
- `axes[0, 1]` 表示右上角
- `axes[1, 0]` 表示左下角
- `axes[1, 1]` 表示右下角

常用的 Axes 方法包括：

```python
set_title()
set_xlabel()
set_ylabel()
legend()
grid()
set_xlim()
set_ylim()
```

## 2. Figure 与 Axes

`fig.suptitle()` 用于设置整个 Figure 的总标题：

```python
fig.suptitle("Matplotlib Multiple Charts")
```

而：

```python
axes[0, 0].set_title("Line Chart")
```

只用于设置某一个子图的标题。

## 3. Pandas 与 Matplotlib 联动

使用 Pandas 读取学生成绩数据：

```python
df = pd.read_csv("students.csv")
```

计算每个学生三门课程的平均成绩：

```python
df["average"] = df[
    ["python", "math", "english"]
].mean(axis=1)
```

其中：

- `axis=1`：按行计算，每个学生计算一次平均值
- `axis=0`：按列计算，每门课程计算一次平均值

计算每门课程的平均成绩：

```python
subject_average = df[
    ["python", "math", "english"]
].mean(axis=0)
```

## 4. Pandas Series

计算课程平均成绩后得到的是一个 Series。

例如：

```python
subject_average.index
```

得到：

```text
python
math
english
```

可作为图表的 X 轴。

而：

```python
subject_average.values
```

得到各门课程对应的平均成绩，可以作为 Y 轴。

## 5. 常见图表

### 柱状图

适合比较不同类别之间的数据大小：

```python
axes[0, 0].bar(df["name"], df["average"])
```

例如比较不同学生的平均成绩。

### 直方图

用于观察连续数值的分布：

```python
axes[1, 0].hist(df["python"], bins=3)
```

`bins` 表示把数据范围划分成多少个区间。

- `bins` 越大，区间越窄
- `bins` 越小，区间越宽

### 散点图

用于观察两个数值变量之间的关系：

```python
axes[1, 1].scatter(
    df["python"],
    df["math"]
)
```

通过散点图可以观察两个变量是否存在正相关、负相关或较弱的关系。

## 6. 相关系数

使用：

```python
correlation = df["python"].corr(df["math"])
```

计算 Python 成绩和数学成绩之间的相关系数。

本次结果约为：

```text
0.565
```

说明两者存在一定程度的正相关。

相关系数通常位于：

```text
-1 ~ 1
```

其中：

- 越接近 `1`，正相关越明显
- 越接近 `-1`，负相关越明显
- 越接近 `0`，线性相关越弱

需要注意：

**相关并不代表因果。**

## 7. 保存图表

使用：

```python
plt.savefig(
    "student_analysis.png",
    dpi=300,
    bbox_inches="tight"
)
```

可以把绘制好的图表保存成图片。

其中：

- `dpi=300`：提高图片清晰度
- `bbox_inches="tight"`：减少图片周围多余空白

## 8. 综合项目

本次完成了一个 2×2 的学生成绩分析 Dashboard，包括：

1. 学生平均成绩柱状图
2. 科目平均成绩柱状图
3. Python 成绩分布直方图
4. Python 与 Math 成绩散点图

最终完成了：

**CSV → Pandas 数据处理 → 数据统计 → Matplotlib 可视化 → 图片保存**

这也是一个基本的数据分析工作流程。