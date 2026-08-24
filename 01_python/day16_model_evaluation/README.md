# Day16 - Machine Learning Model Evaluation

## 项目介绍

本项目是在 Day15 分类模型基础上的进一步完善。

Day15 学习了使用 Logistic Regression 完成学生是否通过考试的二分类预测。

Day16 主要学习机器学习模型评估方法，以及如何判断一个分类模型是否真正有效。

本项目完整实现：

- 数据集划分（train_test_split）
- Logistic Regression 分类模型训练
- 模型预测
- Accuracy 准确率
- Confusion Matrix 混淆矩阵
- Precision 精确率
- Recall 召回率
- F1-score
- Classification Report
- Cross Validation 交叉验证
- 使用 joblib 保存和加载模型

完成了一个完整的机器学习分类流程。

---

# 项目结构

```
day16_model_evaluation

│
├── student_evaluation.py      # 模型训练、预测、评估
│
├── predict_student.py         # 加载模型并预测新数据
│
├── student_model.pkl          # 保存的训练模型
│
└── README.md
```

---

# 一、项目目标

根据学生的学习情况预测学生是否能够通过考试。

输入特征：

- study_hours：学习时间
- attendance：出勤率
- homework：作业完成情况

输出：

- 0：不通过
- 1：通过


机器学习流程：

```
学生数据
    ↓
特征提取
    ↓
Logistic Regression模型
    ↓
预测结果
    ↓
模型评估
    ↓
保存模型
```

---

# 二、数据准备

使用 Pandas 创建学生数据：

```python
data = {
    "study_hours": [],
    "attendance": [],
    "homework": [],
    "pass": []
}
```

其中：

X：

表示输入特征：

```
study_hours
attendance
homework
```

y：

表示预测目标：

```
pass
```

---

# 三、训练集与测试集划分

使用：

```python
train_test_split()
```

将数据划分为训练集和测试集。


代码：

```python
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)
```


参数说明：

- test_size=0.25

表示25%的数据用于测试。

- random_state=42

固定随机划分结果，保证每次运行一致。

---

# 四、Logistic Regression分类模型

创建模型：

```python
model = LogisticRegression()
```

训练：

```python
model.fit(
    X_train,
    y_train
)
```


预测：

```python
y_pred = model.predict(X_test)
```

---

# 五、模型评估

## 1. Accuracy

准确率：

```python
accuracy_score()
```

表示：

> 所有预测结果中，预测正确的比例。


公式：

```
Accuracy =
正确预测数量 / 总数量
```

---

## 2. Confusion Matrix

混淆矩阵：

```python
confusion_matrix()
```


用于观察模型预测正确和错误的位置。


结构：

```
              预测0       预测1

实际0          TN          FP

实际1          FN          TP
```


含义：

- TP（True Positive）

真正例，预测为正，实际也是正。


- TN（True Negative）

真负例，预测为负，实际也是负。


- FP（False Positive）

假正例，预测为正，但是实际为负。


- FN（False Negative）

假负例，预测为负，但是实际为正。

---

# 六、Precision、Recall、F1-score

## Precision（精确率）

表示：

> 模型预测为正类的数据中，有多少是真正的正类。


公式：

```
Precision = TP / (TP + FP)
```


---

## Recall（召回率）

表示：

> 所有真实正类中，有多少被模型成功找到。


公式：

```
Recall = TP / (TP + FN)
```


---

## F1-score

综合 Precision 和 Recall：

```
F1 =
2 × Precision × Recall /
(Precision + Recall)
```


---

# 七、Classification Report

使用：

```python
classification_report()
```

可以一次输出：

- precision
- recall
- f1-score
- support


示例：

```
              precision    recall    f1-score

0             1.00        1.00      1.00

1             1.00        1.00      1.00
```


其中：

0 和 1 代表分类标签。

本项目：

```
0 = 不通过

1 = 通过
```

support表示测试集中该类别的数据数量。

---

# 八、交叉验证 Cross Validation

单次训练测试可能受到数据划分影响。

例如：

一次测试：

```
Accuracy = 100%
```

不一定代表模型真实能力。


因此使用：

```python
cross_val_score()
```

进行交叉验证。


本项目使用：

```python
cv=5
```

即5折交叉验证。


流程：

```
数据

↓

划分5份

↓

训练5次

↓

计算平均结果
```


代码：

```python
scores = cross_val_score(
    model,
    X,
    y,
    cv=5
)
```


最后：

```python
scores.mean()
```

得到平均准确率。

---

# 九、模型保存与加载

## 保存模型

使用：

```python
joblib
```

保存训练好的模型。


代码：

```python
joblib.dump(
    model,
    "student_model.pkl"
)
```


生成：

```
student_model.pkl
```

---

## 加载模型

使用：

```python
joblib.load()
```


代码：

```python
model = joblib.load(
    "student_model.pkl"
)
```


加载后可以直接预测新的学生数据。


---

# 十、项目运行结果

示例：

```
预测结果:
[1 0 0]


真实结果:
[1 0 0]


Accuracy:
1.0


Confusion Matrix:

[[2 0]
 [0 1]]
```


Classification Report：

```
              precision    recall    f1-score

0             1.00        1.00      1.00

1             1.00        1.00      1.00
```


---

# 十一、学习总结

通过 Day16 学习，完成了机器学习分类模型从训练到保存的完整流程。


完整流程：

```
数据准备

↓

训练模型

↓

预测结果

↓

模型评估

↓

交叉验证

↓

保存模型
```


掌握知识：

- train_test_split
- Logistic Regression
- Accuracy
- Confusion Matrix
- TP / TN / FP / FN
- Precision
- Recall
- F1-score
- Classification Report
- Cross Validation
- joblib模型保存


Day16 完成了机器学习分类项目的工程化基础流程。

下一阶段将进入真实数据集项目，学习如何处理更加接近实际应用的机器学习任务。