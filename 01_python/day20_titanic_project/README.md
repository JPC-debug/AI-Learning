# Day20 Titanic Machine Learning Project

## 项目介绍

本项目使用经典 Titanic 乘客数据集，完成一次较完整的机器学习分类实践。

目标是根据乘客的个人信息预测其是否生还，并进一步分析模型效果和重要特征。

完整流程：

数据读取 → 缺失值处理 → 类别编码 → 特征选择 → 模型训练 → 模型评估 → 交叉验证 → 特征解释

---

## 项目结构

```text
day20_titanic_project
│
├── data
│   └── titanic.csv
│
├── titanic_analysis.py
│
└── README.md
```

---

## 数据集

Titanic 数据集共有：

- 891 条乘客记录
- 12 个原始字段

预测目标：

```text
Survived
0 = 未生还
1 = 生还
```

主要使用特征：

- Pclass：舱位等级
- Sex：性别
- Age：年龄
- SibSp：同行兄弟姐妹/配偶数量
- Parch：同行父母/子女数量
- Fare：票价
- Embarked：登船港口

---

## 缺失值处理

通过：

```python
df.isnull().sum()
```

发现主要缺失字段：

```text
Age       177
Cabin     687
Embarked    2
```

Age 使用中位数填充：

```python
df["Age"] = df["Age"].fillna(
    df["Age"].median()
)
```

Embarked 使用众数填充：

```python
df["Embarked"] = df["Embarked"].fillna(
    df["Embarked"].mode()[0]
)
```

Cabin 缺失过多，本次暂时不作为训练特征。

---

## 类别特征编码

Sex 和 Embarked 为字符串，不能直接输入模型，因此使用：

```python
pd.get_dummies()
```

转换后生成：

```text
Sex_male
Embarked_Q
Embarked_S
```

并使用：

```python
drop_first=True
```

避免产生重复信息。

---

## 模型训练

使用：

```python
Pipeline([
    ("scaler", StandardScaler()),
    ("classifier", LogisticRegression(max_iter=1000))
])
```

将数据标准化和 Logistic Regression 分类模型结合。

训练集和测试集按照：

```text
80% / 20%
```

划分，并使用：

```python
stratify=y
```

保持生还与未生还类别比例基本一致。

---

## 模型结果

测试集准确率：

```text
Accuracy: 0.8045
```

约为：

```text
80.45%
```

混淆矩阵：

```text
[[98 12]
 [23 46]]
```

其中：

- 98：正确预测未生还
- 12：错误预测为生还
- 23：实际生还但预测未生还
- 46：正确预测生还

生还类别的 Recall 约为：

```text
0.67
```

说明模型对生还乘客的识别能力仍有提升空间。

---

## 交叉验证

使用 5 折交叉验证：

```python
cross_val_score(
    model,
    X,
    y,
    cv=5
)
```

结果：

```text
[0.7709, 0.7865, 0.7809, 0.7697, 0.8202]
```

平均准确率：

```text
78.57%
```

说明模型整体准确率大约稳定在 79% 左右。

---

## 特征影响分析

通过 Logistic Regression 的系数分析各特征影响。

影响较大的特征：

```text
Sex_male   -1.2696
Pclass     -0.9287
Age        -0.5029
```

其中：

- Sex_male 为较大的负值，说明男性对应的预测生还概率更低
- Pclass 为负值，舱位数字越大，预测生还概率越低
- Age 为负值，年龄增加时预测生还概率下降
- Fare 为正值，票价较高时预测生还概率略有增加

---

## 学习收获

通过本项目掌握了：

1. 真实数据集读取与基本探索
2. 缺失值分析和填充
3. 类别特征编码
4. 特征选择
5. Logistic Regression 模型训练
6. Accuracy、混淆矩阵和分类报告
7. 5 折交叉验证
8. Logistic Regression 特征系数解释

相比之前的小型学生数据，本项目首次使用接近真实规模的数据完成完整机器学习分类流程，为后续模型比较和参数调优做好准备。