# Day15 Classification Model - Logistic Regression

## 项目介绍

本项目是 Python AI 学习计划 Day15 的机器学习分类项目。

在 Day14 学习回归模型（Linear Regression）的基础上，本次学习进入机器学习中的另一个重要方向：

**分类问题（Classification）**

本项目通过学生学习情况数据，训练一个机器学习模型，用于预测学生是否能够通过考试。

输入学生的：

- 学习时间（study_hours）
- 出勤率（attendance）
- 作业完成度（homework）

模型输出：

- 0：不通过
- 1：通过

通过这个项目，掌握了从数据处理到模型训练、预测和评估的完整分类模型流程。

---

# 项目结构

```
day15_classification
│
├── students.csv
├── student_classifier.py
└── README.md
```

---

# 一、数据介绍

数据文件：

```
students.csv
```

包含学生学习情况：

|字段|说明|
|-|-|
|name|学生姓名|
|study_hours|学习时间|
|attendance|出勤率|
|homework|作业完成度|
|pass|是否通过考试|

其中：

```
0 = 不通过
1 = 通过
```

---

# 二、机器学习流程

本项目完整流程：

```
读取数据
    ↓
划分特征 X 和 标签 y
    ↓
训练集 / 测试集划分
    ↓
数据标准化
    ↓
Logistic Regression模型训练
    ↓
模型预测
    ↓
准确率评价
    ↓
新数据预测
```

---

# 三、核心知识点

## 1. 分类问题 Classification

与之前 Day14 的回归问题不同：

### 回归问题

预测连续数值：

例如：

```
预测学生成绩：

85.6分
```

使用：

```
LinearRegression
```

---

### 分类问题

预测类别：

例如：

```
是否通过考试：

0 / 1
```

使用：

```
LogisticRegression
```

---

# 四、Logistic Regression

虽然名字中包含 Regression：

但是 Logistic Regression 主要用于分类任务。

它通过计算样本属于不同类别的概率，完成分类。

例如：

输入：

```
学习时间：5小时
出勤率：90%
作业：95%
```

模型输出：

```
通过概率：95.2%
不通过概率：4.8%
```

最终判断：

```
通过
```

---

# 五、Pipeline

本项目继续使用 Day14 学习的 Pipeline 方法。

代码：

```python
Pipeline([
    ("scaler", StandardScaler()),
    ("classifier", LogisticRegression())
])
```

作用：

将数据处理和模型组合在一起。

流程：

```
原始数据
    ↓
StandardScaler标准化
    ↓
LogisticRegression分类
    ↓
预测结果
```

这样可以减少手动处理步骤，提高代码规范性。

---

# 六、数据标准化 StandardScaler

不同特征的数据范围不同：

例如：

```
study_hours:
0-10

attendance:
0-100

homework:
0-100
```

如果直接训练模型，可能导致某些特征影响过大。

StandardScaler 会将数据转换到相近范围：

```
均值≈0
标准差≈1
```

使模型能够更加合理地学习数据规律。

---

# 七、模型训练

使用：

```python
model.fit(
    X_train,
    y_train
)
```

让模型学习：

```
学习情况
    ↓
是否通过
```

之间的关系。

---

# 八、模型预测

## predict()

用于预测最终类别：

例如：

```python
model.predict(new_student)
```

输出：

```
[1]
```

表示：

```
预测通过
```

---

## predict_proba()

用于查看预测概率：

例如：

```
[[0.04828227 0.95171773]]
```

表示：

```
不通过概率：
4.8%

通过概率：
95.2%
```

相比直接输出类别，概率结果能够体现模型的判断信心。

---

# 九、模型评价

分类任务使用：

```python
accuracy_score()
```

计算准确率：

```
正确预测数量 / 总预测数量
```

本项目测试结果：

```
Accuracy:

1.0
```

表示测试数据预测全部正确。

---

# 十、运行结果

运行：

```bash
python student_classifier.py
```

结果：

```
预测结果:
[0 0]

真实结果:
[0 0]

Accuracy:
1.0

新学生预测:
[1]

预测概率:
[[0.04828227 0.95171773]]
```

模型成功预测：

一个学习情况较好的学生：

```
通过考试
```

并给出：

```
95.2%的通过概率
```

---

# 十一、学习总结

通过 Day15 学习：

掌握了机器学习分类任务的完整流程：

- 理解分类问题和回归问题区别
- 学习 Logistic Regression 分类算法
- 掌握 Pipeline 在机器学习中的应用
- 复习 StandardScaler 数据标准化
- 学习 Accuracy 分类评价指标
- 学习 predict() 和 predict_proba() 区别
- 完成第一个分类预测项目

目前已经能够独立完成：

```
数据读取
→ 数据处理
→ 模型训练
→ 模型评价
→ 新数据预测
```

这是进入更复杂机器学习模型的重要基础。

---

# 下一步学习方向

Day16 将继续学习更强大的机器学习模型：

- Decision Tree（决策树）
- Random Forest（随机森林）

进一步理解：

- 模型如何自动学习规则
- 集成学习思想
- 不同模型之间的差异