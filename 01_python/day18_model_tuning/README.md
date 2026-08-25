# Day18 Model Tuning

## 项目介绍

本项目是在 Day17 机器学习项目工程化基础上的进一步优化。

之前项目已经完成：

数据读取 → 特征处理 → 模型训练 → 模型评估 → 模型保存 → 模型预测

本项目进一步学习如何通过**超参数调优（Hyperparameter Tuning）**提升模型性能。

主要学习内容：

- 超参数概念
- GridSearchCV自动调参
- Pipeline参数搜索
- 最佳模型选择与保存

---

## 项目结构

```
day18_model_tuning

│
├── data
│   └── students.csv              # 学生成绩数据
│
├── model_tuning.py               # 模型调参与训练程序
│
├── best_student_model.pkl        # 调优后的最佳模型
│
└── README.md
```

---

## 项目流程

### 1. 数据读取

使用 Pandas 读取学生成绩数据：

```python
pd.read_csv()
```

数据包含：

- study_hours：学习时间
- attendance：出勤率
- homework：作业成绩
- pass：是否通过

其中：

- X：模型输入特征
- y：预测目标

---

## 2. 数据划分

使用：

```python
train_test_split()
```

将数据划分为：

- 训练集
- 测试集

训练集用于模型学习，测试集用于评价最终效果。

---

## 3. Pipeline模型构建

使用 Pipeline 将数据标准化和分类模型结合：

```python
Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', LogisticRegression())
])
```

模型流程：

原始数据

↓

StandardScaler标准化

↓

Logistic Regression分类预测

使用Pipeline可以保证训练和预测阶段的数据处理方式保持一致。

---

## 4. 超参数调优

模型中的参数会影响最终效果。

例如 Logistic Regression 中：

```python
C
```

控制模型正则化强度。

本项目使用 GridSearchCV 自动搜索最佳参数：

```python
GridSearchCV()
```

设置搜索范围：

```python
classifier__C:
[
0.01,
0.1,
1,
10,
100
]
```

由于模型使用Pipeline，因此参数名称格式为：

```
步骤名称__参数名称
```

例如：

```
classifier__C
```

表示：

Pipeline中的classifier模型的C参数。

---

## 5. 交叉验证

GridSearchCV内部使用交叉验证评价不同参数效果。

本项目使用：

```python
cv=4
```

原因：

数据集较小，每个类别样本数量有限。

通过多次训练和验证，寻找更加可靠的参数组合。

---

## 6. 最佳模型选择

通过：

```python
grid_search.best_params_
```

获得最佳参数：

```
{'classifier__C': 1}
```

通过：

```python
grid_search.best_estimator_
```

获取最佳模型。

---

## 7. 模型评估

使用最佳模型预测测试集：

```python
predict()
```

并通过：

```python
accuracy_score()
```

计算准确率。

实验结果：

```
最佳参数:
{'classifier__C': 1}

最佳交叉验证分数:
1.0

测试集准确率:
1.0
```

---

## 8. 模型保存

使用 joblib 保存调优后的模型：

```python
joblib.dump()
```

保存文件：

```
best_student_model.pkl
```

后续可以直接加载该模型进行预测，无需重新训练。

---

## 使用技术

- Python
- Pandas
- Scikit-learn
- Logistic Regression
- Pipeline
- StandardScaler
- GridSearchCV
- Cross Validation
- Joblib

---

## 学习收获

通过本项目，掌握了机器学习模型优化的基本流程：

1. 理解超参数与模型参数区别
2. 使用GridSearchCV自动搜索最佳参数
3. 掌握Pipeline中的参数访问方式
4. 使用交叉验证评价模型
5. 获取最佳模型并保存

相比之前只能训练模型，本项目进一步学习了模型优化和模型选择方法，更接近真实机器学习项目开发流程。

下一步将学习不同机器学习算法之间的比较，例如 Logistic Regression、Decision Tree 和 Random Forest。
