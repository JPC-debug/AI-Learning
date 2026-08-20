# Day 11 - Matplotlib Data Visualization

## 学习内容

今天主要学习了 Python 数据可视化库 Matplotlib，并结合之前学习的 Pandas 完成了学生成绩数据可视化分析。

## 主要知识点

### 1. 折线图

使用 `plt.plot()` 绘制数据变化趋势。

学习了：

- `marker`
- `linestyle`
- `label`
- `legend()`
- `grid()`

### 2. 柱状图

使用 `plt.bar()` 比较不同类别的数据，例如不同学科的平均成绩。

### 3. 散点图

使用 `plt.scatter()` 分析两个变量之间的关系。

本项目中绘制了 Math 和 Python 成绩的散点图，并观察到两者整体呈正相关趋势。

### 4. 直方图

使用 `plt.hist()` 查看数据的分布情况，并通过 `bins` 控制数据分组数量。

### 5. Pandas + Matplotlib

使用 Pandas：

- `read_csv()`
- `mean()`
- `groupby()`
- `corr()`

进行数据处理和分析，再使用 Matplotlib 对结果进行可视化。

## 项目

完成学生成绩可视化分析，包括：

- 各科平均成绩柱状图
- Python 成绩分布直方图
- Math 与 Python 成绩散点图
- Math 与 Python 相关性分析

生成的图片保存到 `charts` 文件夹。

## 总结

通过 Day 11 的学习，掌握了基础的数据可视化方法，并将 NumPy、Pandas 和 Matplotlib 的知识进一步串联起来。

目前已经可以完成：

数据读取 → 数据分析 → 数据可视化 → 发现变量关系

这为后续机器学习的数据探索和模型分析打下了基础。