# Day 8 - Pandas 数据处理基础

## 学习目标

Day 8 主要学习 Pandas 的基础使用，并完成一个学生成绩数据分析项目。在 Day 7 NumPy 数值计算的基础上，进一步学习如何使用 Python 处理二维表格数据。

## 1. DataFrame 基础

导入 Pandas：

    import pandas as pd

使用字典创建 DataFrame：

    df = pd.DataFrame(data)

DataFrame 可以理解为一张二维表格，其中：

- DataFrame：整张表
- columns：列名
- index：行索引
- Series：单独的一列数据

常用的数据查看方法：

    df.head()       # 查看前几行
    df.tail()       # 查看最后几行
    df.shape        # 查看行数和列数
    df.columns      # 查看列名
    df.dtypes       # 查看各列数据类型

## 2. 数据选择

选择单列：

    df["score"]

返回 Series。

选择多列：

    df[["name", "score"]]

返回 DataFrame。

按照标签选择：

    df.loc[1, "score"]

按照位置选择：

    df.iloc[1, 2]

简单记忆：

- loc：按照标签
- iloc：按照位置

## 3. 条件筛选

筛选成绩大于 80 的学生：

    df[df["score"] > 80]

多个条件：

    df[(df["age"] >= 20) & (df["score"] >= 90)]

其中：

- & 表示“并且”
- | 表示“或者”

还可以结合 loc 筛选指定行和列：

    df.loc[df["score"] > 80, ["name", "score"]]

## 4. 数据统计

常用统计方法：

    df["score"].mean()      # 平均值
    df["score"].max()       # 最大值
    df["score"].min()       # 最小值
    df["score"].sum()       # 求和
    df["score"].idxmax()    # 最大值所在索引

结合 loc 可以找到最高分对应的完整数据：

    df.loc[df["score"].idxmax()]

## 5. 新增计算列

Pandas 可以直接对整列进行运算，不需要手动使用 for 循环。

例如计算学生平均成绩：

    df["average"] = (df["math"] + df["english"] + df["python"]) / 3

保留两位小数：

    df["average"] = df["average"].round(2)

## 6. 排序与排名

按照平均成绩从高到低排序：

    ranking = df.sort_values("average", ascending=False)

重新设置索引：

    ranking = ranking.reset_index(drop=True)

增加排名：

    ranking["rank"] = ranking.index + 1

## 7. CSV 文件保存

将分析结果保存为 CSV：

    ranking.to_csv("student_ranking.csv", index=False)

index=False 表示不将 DataFrame 的索引写入 CSV 文件。

## 综合项目

本次完成了学生成绩数据分析程序 student_analysis.py，实现：

1. 创建学生成绩 DataFrame
2. 计算每个学生的平均成绩
3. 筛选平均分大于等于 90 的学生
4. 计算数学、英语和 Python 平均分
5. 找出 Python 最高分学生
6. 按平均成绩进行排名
7. 将排行榜保存为 student_ranking.csv

## 项目结构

    day8_pandas/
    ├── practice.py
    ├── student_analysis.py
    ├── student_ranking.csv
    └── README.md

## Day 8 总结

通过 Day 8 的学习，我掌握了 Pandas 中 DataFrame 和 Series 的基本使用，能够进行数据查看、行列选择、条件筛选、统计计算、新增列、排序和 CSV 文件保存。

Day 7 的 NumPy 更侧重数组和数值计算，而 Pandas 更适合处理结构化表格数据。经过本次学习，已经能够完成简单的数据分析流程：

    创建数据 → 查看数据 → 筛选数据 → 统计计算 → 排序 → 保存结果

这些知识将为后续的数据清洗、数据可视化以及机器学习的数据预处理打下基础。