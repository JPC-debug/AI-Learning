# Day 14 - Machine Learning Pipeline

## 一、学习目标

本日学习机器学习项目的完整流程。

在 Day13 完成线性回归基础之后，进一步学习如何将真实数据应用到机器学习模型中，包括：

- CSV 数据读取
- 特征（Feature）与标签（Label）划分
- 训练集与测试集划分
- 特征标准化
- 多元线性回归
- 模型评价指标
- Pipeline 工程化流程


---

# 二、项目流程

一个完整的机器学习流程：

```
原始数据
    ↓
数据读取
    ↓
特征选择
    ↓
训练集/测试集划分
    ↓
数据预处理
    ↓
模型训练
    ↓
预测
    ↓
模型评价
```


本项目实现：

```
students.csv

↓

Pandas读取数据

↓

选择特征 X

↓

选择标签 y

↓

StandardScaler标准化

↓

LinearRegression训练

↓

预测成绩

↓

MSE、R²评价
```


---

# 三、数据说明

项目使用学生学习情况数据：

|字段|说明|
|-|-|
|name|学生姓名|
|study_hours|学习时间|
|attendance|出勤率|
|homework|作业完成率|
|score|最终成绩|


模型输入：

```
X = study_hours + attendance + homework
```


模型预测目标：

```
y = score
```


机器学习本质：

```
X → y
```


---

# 四、特征标准化 StandardScaler

不同特征的数据范围可能不同。

例如：

```
学习时间：
1~10

出勤率：
80~100
```


如果直接输入模型，不同尺度可能影响模型学习。


StandardScaler 会将数据转换到相近范围，使模型更容易学习。


标准化公式：

```
z = (x - mean) / standard deviation
```


训练数据：

使用：

```python
fit_transform()
```


测试数据：

使用：

```python
transform()
```


原因：

测试数据应该模拟未知数据，不能提前利用测试集信息。


---

# 五、多元线性回归

本项目使用：

```python
LinearRegression
```


相比 Day13 的单变量线性回归：

```
学习时间 → 成绩
```


本日：

```
学习时间
出勤率
作业完成率

↓

成绩
```


模型学习多个因素与成绩之间的关系。


---

# 六、模型评价


## 1. MSE

Mean Squared Error（均方误差）

表示：

预测值与真实值之间误差的平方平均。


特点：

- 越小越好
- 对较大的预测误差更加敏感


本次实验结果：

```
MSE:
11.987
```


---

## 2. R²

R²（决定系数）

表示模型对数据变化的解释能力。


本次结果：

```
R2:
0.9009
```


说明：

模型能够解释约90%的成绩变化。


---

# 七、Pipeline

传统写法：

```
StandardScaler

↓

LinearRegression
```


需要分别处理。


Pipeline 可以将多个步骤组合：

```python
Pipeline(
[
    ("scaler", StandardScaler()),
    ("model", LinearRegression())
]
)
```


优势：

- 简化代码结构
- 避免数据泄露
- 保证训练和预测流程一致
- 更接近实际机器学习工程


---

# 八、特征选择实验


## 实验1：只使用学习时间

特征：

```
study_hours
```


结果：

```
MSE:
10.784

R2:
0.9108
```


---

## 实验2：使用出勤率和作业完成率

特征：

```
attendance
homework
```


结果：

```
MSE:
13.280

R2:
0.8902
```


实验结论：

更多特征不一定带来更好的模型效果。

有效特征比特征数量更加重要。


---

# 九、项目文件结构

```
day14_ml_pipeline

├── students.csv

├── student_prediction.py

├── pipeline_demo.py

└── README.md
```


---

# 十、总结

Day14 完成了从简单模型调用到完整机器学习流程的过渡。

掌握：

- 使用 Pandas 读取机器学习数据
- Feature 和 Label 的概念
- 训练集和测试集划分
- StandardScaler 标准化
- 多元线性回归
- MSE 与 R²评价指标
- Pipeline 工程化流程


目前已经能够完成基础机器学习项目：

```
数据

↓

处理

↓

训练

↓

预测

↓

评价
```


下一阶段将继续学习：

- 多元线性回归深入
- 特征相关性分析
- 特征选择方法
- 更多机器学习模型
```