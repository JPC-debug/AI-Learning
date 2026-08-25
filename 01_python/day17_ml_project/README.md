# Day17 Machine Learning Project Engineering

## 项目介绍

本项目是在前面机器学习学习基础上的工程化实践，对学生成绩分类预测项目进行了完整升级。

项目实现了一个完整的机器学习流程：

数据读取 → 特征处理 → 模型训练 → 模型评估 → 模型保存 → 模型加载 → 新数据预测

通过本项目，学习如何将之前单文件形式的机器学习实验代码，转变为更加接近真实项目开发的结构。

---

## 项目结构

day17_ml_project

```
day17_ml_project
│
├── data
│   └── students.csv              # 学生成绩数据
│
├── models
│   └── student_model.pkl         # 保存的训练模型
│
├── train.py                      # 模型训练程序
│
├── predict.py                    # 模型预测程序
│
└── README.md
```

---

## 项目流程

### 1. 数据读取

使用 Pandas 读取 CSV 数据：

```python
pd.read_csv()
```

数据包含：

- study_hours：学习时间
- attendance：出勤率
- homework：作业成绩
- pass：是否通过

其中：

- X：输入特征
- y：预测目标

模型通过学习学生的学习情况，预测最终是否通过。

---

### 2. 数据划分

使用 Scikit-learn：

```python
train_test_split()
```

将数据划分为：

- 训练集（Training Set）
- 测试集（Testing Set）

训练集用于模型学习规律，测试集用于评价模型效果。

---

### 3. Pipeline模型

项目使用 Pipeline 将数据标准化和分类模型结合：

```python
Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', LogisticRegression())
])
```

完整流程：

原始数据

↓

StandardScaler标准化

↓

Logistic Regression分类预测


使用 Pipeline 的优势：

- 保证训练和预测过程的数据处理一致
- 避免手动处理标准化步骤
- 方便整体保存模型

---

### 4. 模型训练

使用：

```python
model.fit()
```

让模型学习训练数据中的规律。

训练完成后，模型可以根据：

- 学习时间
- 出勤率
- 作业成绩

预测学生是否通过。

---

### 5. 模型评估

使用：

```python
accuracy_score()
```

计算模型准确率。

同时使用：

```python
cross_val_score()
```

进行交叉验证，提高模型评价的可靠性。

由于本项目数据量较小，每个类别样本数量有限，因此设置：

```python
cv=4
```

避免交叉验证时出现样本数量不足的问题。

---

### 6. 模型保存

训练完成后，使用 joblib 保存整个 Pipeline：

```python
joblib.dump()
```

保存文件：

```
models/student_model.pkl
```

保存内容包括：

- StandardScaler参数
- Logistic Regression模型参数

之后无需重新训练，可以直接加载模型进行预测。

---

### 7. 模型预测

predict.py 中：

首先加载模型：

```python
joblib.load()
```

然后输入新的学生数据：

学习时间：
6

出勤率：
90

作业成绩：
95


使用：

```python
model.predict()
```

预测分类结果。

使用：

```python
model.predict_proba()
```

查看预测概率。


示例结果：

```
预测结果:
[1]

预测概率:
[[0.032 0.968]]
```

表示：

- 不通过概率约 3.2%
- 通过概率约 96.8%

---

## 使用技术

- Python
- Pandas
- Scikit-learn
- Logistic Regression
- Pipeline
- StandardScaler
- Cross Validation
- Joblib

---

## 学习收获

通过本项目，掌握了机器学习项目的完整开发流程：

1. 数据读取与处理
2. 特征和标签划分
3. 模型训练
4. 模型评估
5. 交叉验证
6. 模型保存
7. 模型加载
8. 新数据预测

相比之前的机器学习练习，本项目进一步学习了工程化思想：

将模型训练和模型预测分离，使代码结构更加清晰，也更加接近实际 AI 项目的开发方式。

下一步将继续学习模型优化、参数调优以及更加复杂的机器学习算法。