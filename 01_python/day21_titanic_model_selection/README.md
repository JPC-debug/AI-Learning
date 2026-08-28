# Day21 Titanic Model Selection

## 项目介绍

本项目是在 Day20 Titanic 生存预测项目基础上的进一步优化。

Day20 已经完成：

数据清洗 → 类别编码 → Logistic Regression → 模型评估 → 交叉验证 → 特征分析

Day21 主要学习如何比较多个模型、选择更稳定的模型，并使用 GridSearchCV 进行参数调优。

完整流程：

Titanic 数据 → 数据处理 → 三模型训练 → Accuracy 比较 → Cross Validation → Random Forest 调参 → 保存最佳模型

---

## 项目结构

```text
day21_titanic_model_selection
│
├── data
│   └── titanic.csv
│
├── models
│   └── best_titanic_model.pkl
│
├── model_selection.py
│
└── README.md
```

---

## 数据处理

读取 Titanic 数据：

```python
pd.read_csv()
```

处理缺失值：

- Age 使用中位数填充
- Embarked 使用众数填充

类别特征：

```text
Sex
Embarked
```

通过：

```python
pd.get_dummies()
```

转换为模型可以使用的数值特征。

训练集和测试集按照 80% / 20% 划分，并使用：

```python
stratify=y
```

保持生还和未生还类别比例基本一致。

---

## 模型比较

本项目比较三个分类模型：

### Logistic Regression

使用：

```python
Pipeline([
    ("scaler", StandardScaler()),
    ("classifier", LogisticRegression(max_iter=1000))
])
```

测试集准确率：

```text
80.45%
```

### Decision Tree

```python
DecisionTreeClassifier()
```

测试集准确率：

```text
82.12%
```

### Random Forest

```python
RandomForestClassifier()
```

测试集准确率：

```text
81.56%
```

单次测试集中 Decision Tree 得分最高，但单次划分不能完全反映模型稳定性。

---

## 5折交叉验证

使用：

```python
cross_val_score()
```

比较三个模型的平均表现。

结果：

```text
Logistic Regression Mean:
78.57%

Decision Tree Mean:
78.12%

Random Forest Mean:
81.37%
```

Random Forest 的平均准确率最高，同时整体表现更加稳定，因此选择 Random Forest 作为后续调优模型。

---

## GridSearchCV 参数调优

设置 Random Forest 参数搜索范围：

```text
n_estimators:
50 / 100 / 200

max_depth:
None / 5 / 10

min_samples_split:
2 / 5 / 10
```

使用：

```python
GridSearchCV()
```

自动尝试不同参数组合。

最佳参数：

```text
max_depth = None
min_samples_split = 10
n_estimators = 50
```

最佳交叉验证分数：

```text
82.87%
```

相比默认 Random Forest 的：

```text
81.37%
```

交叉验证平均准确率有所提升。

---

## 最终测试

通过：

```python
grid_search.best_estimator_
```

获得最佳模型，并在测试集上进行预测。

结果：

```text
调优后测试集准确率:
81.01%
```

虽然略低于默认 Random Forest 在单次测试集上的 81.56%，但调优模型的交叉验证平均表现更好。

这说明机器学习模型不能只根据某一次测试集结果进行选择，更应该关注多次交叉验证后的整体稳定性。

---

## 模型保存

使用：

```python
joblib.dump()
```

保存最佳模型：

```text
models/best_titanic_model.pkl
```

后续可以直接加载该模型进行预测，无需重新训练。

---

## 学习收获

通过本项目掌握了：

1. Logistic Regression、Decision Tree、Random Forest 模型比较
2. 使用相同数据和评价指标公平比较模型
3. 使用 5 折交叉验证评价模型稳定性
4. 根据交叉验证结果选择候选模型
5. 使用 GridSearchCV 自动调参
6. 理解 n_estimators、max_depth、min_samples_split
7. 使用 best_estimator_ 获取最佳模型
8. 使用 Joblib 保存训练后的模型

Day20 和 Day21 共同完成了一个较完整的 Titanic 机器学习分类项目，为后续进入 PyTorch 和深度学习阶段做好准备。