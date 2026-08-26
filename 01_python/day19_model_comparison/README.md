# Day19 Model Comparison

## 项目介绍

本项目主要学习如何在同一份数据上比较不同机器学习分类模型，并根据测试集准确率和交叉验证结果选择更合适的模型。

本次比较的模型包括：

- Logistic Regression
- Decision Tree
- Random Forest

核心流程：

数据读取 → 数据划分 → 多模型训练 → 测试集预测 → Accuracy比较 → Cross Validation → 自动选择最佳模型

---

## 项目结构

```text
day19_model_comparison
│
├── data
│   └── students.csv
│
├── model_comparison.py
│
└── README.md
```

---

## 使用模型

### Logistic Regression

逻辑回归适合处理较规则的分类问题。

本项目中使用：

```python
Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', LogisticRegression())
])
```

由于不同特征的数据范围不同，因此先通过 StandardScaler 进行标准化。

### Decision Tree

决策树通过不断进行条件判断完成分类，例如：

```text
学习时间 > 3？
出勤率 > 75？
作业成绩 > 80？
```

决策树通常不需要进行标准化。

### Random Forest

随机森林由多棵决策树组成，通过多个模型共同投票得到最终结果。

相比单棵决策树，随机森林通常更加稳定，也更不容易过拟合。

---

## 模型训练

三个模型使用相同的训练数据：

```python
model.fit(
    X_train,
    y_train
)
```

然后使用相同测试集进行预测：

```python
model.predict(
    X_test
)
```

通过：

```python
accuracy_score()
```

计算测试集准确率。

本次结果：

```text
Logistic Regression Accuracy: 1.0
Decision Tree Accuracy: 1.0
Random Forest Accuracy: 1.0
```

---

## 交叉验证

为了避免只依赖一次训练集和测试集划分，本项目进一步使用：

```python
cross_val_score()
```

进行 4 折交叉验证。

结果：

```text
Logistic Regression CV: [1. 1. 1. 1.]
Decision Tree CV: [1. 1. 1. 1.]
Random Forest CV: [1. 1. 1. 1.]
```

三个模型平均得分均为：

```text
1.0
```

由于当前数据集只有 8 条数据，而且不同类别之间差异明显，因此三个模型都可以较容易完成分类。

这些结果主要用于学习模型比较流程，不能说明模型在真实大型数据集上一定能达到相同效果。

---

## 自动选择最佳模型

使用字典保存不同模型的平均交叉验证分数：

```python
model_scores = {
    "Logistic Regression": float(logistic_scores.mean()),
    "Decision Tree": float(tree_scores.mean()),
    "Random Forest": float(forest_scores.mean())
}
```

然后通过：

```python
max(
    model_scores,
    key=model_scores.get
)
```

自动寻找最高得分模型。

本次三个模型得分相同，因此程序返回字典中第一个最高分模型：

```text
最佳模型: Logistic Regression
最佳平均得分: 1.0
```

这表示三个模型并列，而不是 Logistic Regression 一定优于其他两个模型。

---

## 学习收获

通过本项目掌握了：

1. Logistic Regression、Decision Tree、Random Forest 的基本区别
2. 不同模型对数据标准化的需求
3. 使用相同数据公平比较多个模型
4. 使用 Accuracy 评价分类效果
5. 使用 Cross Validation 提高评价可靠性
6. 使用字典保存多个模型得分
7. 自动选择最高得分模型

相比之前只训练单个模型，本项目进一步学习了实际机器学习项目中的模型比较与模型选择思想。