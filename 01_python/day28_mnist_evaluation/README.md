# Day28 MNIST Model Evaluation

## 项目介绍

Day28 主要学习如何对 MNIST 分类模型进行更全面的评估。

除了整体 Accuracy，还进一步统计每个数字 0～9 的准确率、构建混淆矩阵，并自动找出最常见的错误分类组合。

---

## 项目结构

```text
day28_mnist_evaluation
│
├── evaluate.py
└── README.md
```

---

## 加载模型

先重新定义与 Day27 一致的网络结构：

```python
class MNISTNetwork(nn.Module):

    def __init__(self):
        super().__init__()

        self.fc1 = nn.Linear(784, 128)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):

        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)

        return x
```

然后加载已经训练好的参数：

```python
model = MNISTNetwork()

model.load_state_dict(
    torch.load(
        "../day27_mnist_model/models/mnist_model.pth"
    )
)

model.eval()
```

---

## 加载测试集

使用 Day26 已下载的 MNIST 测试数据：

```python
test_data = datasets.MNIST(
    root="../day26_mnist/data",
    train=False,
    download=True,
    transform=ToTensor()
)

test_loader = DataLoader(
    test_data,
    batch_size=64,
    shuffle=False
)
```

测试集共包含 10000 张图片。

---

## 整体准确率

测试时使用：

```python
with torch.no_grad():
```

关闭梯度计算。

每个 batch 的图片：

```text
[64, 1, 28, 28]
```

先展平为：

```text
[64, 784]
```

然后送入模型：

```python
outputs = model(images)
```

通过：

```python
predictions = torch.argmax(
    outputs,
    dim=1
)
```

得到最终预测类别。

整体准确率：

```text
Overall Accuracy: 0.9743
```

即：

```text
97.43%
```

---

## 每个数字的准确率

使用：

```python
class_correct = [0] * 10
class_total = [0] * 10
```

分别统计每个类别：

- 一共出现多少次
- 一共预测正确多少次

结果：

```text
数字0：98.37%
数字1：99.12%
数字2：95.74%
数字3：97.33%
数字4：97.15%
数字5：98.43%
数字6：97.81%
数字7：97.47%
数字8：96.00%
数字9：96.83%
```

其中：

```text
数字1准确率最高
数字2准确率最低
```

说明模型对不同类别的识别能力并不完全相同。

---

## 混淆矩阵

创建：

```python
confusion_matrix = torch.zeros(
    10,
    10,
    dtype=torch.int32
)
```

矩阵规则：

```text
行 = 真实标签
列 = 预测标签
```

例如：

```python
confusion_matrix[8][3]
```

表示：

```text
真实数字是8
但被预测成3
```

的数量。

在测试过程中：

```python
confusion_matrix[
    label,
    prediction
] += 1
```

不断累计每种预测情况。

混淆矩阵的对角线：

```text
[0,0]
[1,1]
[2,2]
...
[9,9]
```

表示预测正确的数量。

对角线数字越大，说明模型表现越好。

---

## 常见错误分析

通过遍历混淆矩阵中的非对角线元素，把所有错误整理成：

```text
(错误次数, 真实标签, 预测标签)
```

然后：

```python
errors.sort(
    reverse=True
)
```

按照错误次数从高到低排序。

最常见错误：

```text
8 → 3：15 次
4 → 9：15 次
3 → 5：15 次
2 → 8：9 次
2 → 3：9 次
9 → 7：8 次
7 → 1：8 次
9 → 4：7 次
9 → 3：7 次
7 → 2：6 次
```

可以发现部分形状相似的数字更容易发生混淆。

---

## 为什么不能只看 Accuracy

如果只看：

```text
Overall Accuracy = 97.43%
```

只能知道模型总体表现不错。

但进一步分析后可以发现：

```text
数字2识别能力相对较弱
8容易被识别成3
4容易被识别成9
3容易被识别成5
```

因此模型评估应该从整体结果继续深入到具体类别和具体错误。

---

## Day28 评估流程

```text
加载模型
↓
加载测试集
↓
整体 Accuracy
↓
每个类别 Accuracy
↓
混淆矩阵
↓
分析错误组合
```

---

## 学习收获

通过 Day28 学习了：

1. 整体 Accuracy
2. 每个类别 Accuracy
3. class_correct
4. class_total
5. 混淆矩阵
6. 真实标签与预测标签的对应关系
7. 分析错误分类
8. 自动统计最常见错误
9. 为什么不能只看整体准确率
10. 更完整的模型评估思路

Day28 完成了 MNIST 模型的深入评估和错误分析。

下一步将继续改进 MNIST 模型，并逐步进入 CNN 卷积神经网络。