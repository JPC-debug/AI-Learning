import torch
import torch.nn as nn

class SimpleNetwork(nn.Module):
    def __init__(self):
        super().__init__()

        self.linear = nn.Linear(
            2,
            1
        )

    def forward(self, x):
        return self.linear(x)

model = SimpleNetwork()
print(model)

x = torch.tensor(
    [
        [1.0, 2.0]
    ]
)
output = model(x)
print('输入：',x)
print('输出：',output)

print('weight:',model.linear.weight)
print('bias:',model.linear.bias)

manual_output = (
    model.linear.weight[0][0] * x[0][0]
    +
    model.linear.weight[0][1] * x[0][1]
    +
    model.linear.bias[0]
)

print(
    "模型输出:",
    model(x)
)

print(
    "手动计算:",
    manual_output
)


class TwoLayerNetwork(nn.Module):
    def __init__(self):
        super().__init__()

        self.fc1 = nn.Linear(2,4)

        self.relu = nn.LeakyReLU()

        self.fc2 = nn.Linear(4,1)

    def forward(self, x):

        #print('输入shape：',x.shape)
        x = self.fc1(x)
        #print('fc1后shape:',x.shape)
        x = self.relu(x)
        #print('ReLU后shape:',x.shape)
        x = self.fc2(x)
        #print('fc2后shape：',x.shape)
        return x 

model2 = TwoLayerNetwork()
print(model2)

x = torch.tensor(
    [
        [1.0, 2.0]
    ]
)
output = model2(x)
print('最终输出：',output)

for name, param in model2.named_parameters():
    print(name, param.shape)

total_params = sum(
    p.numel()
    for p in model2.parameters()
)
print('总参数数量：',total_params)

X = torch.tensor(
    [
        [1.0, 2.0],
        [2.0, 3.0],
        [3.0, 4.0],
        [4.0, 5.0]
    ]
)

y = torch.tensor(
    [
        [3.0],
        [5.0],
        [7.0],
        [9.0]
    ]
)

loss_fn = nn.MSELoss()

optimizer = torch.optim.SGD(
    model2.parameters(),
    lr=0.001
)

for epoch in range(500):
    y_pred = model2(X)
    loss = loss_fn(y_pred,y)

    optimizer.zero_grad()

    loss.backward()

    optimizer.step()

    if epoch % 50 == 0:
        print(
            'epoch:',
            epoch,
            'loss:',
            loss.item()
        )


test_x = torch.tensor(
    [
        [5.0, 6.0]
    ]
)

with torch.no_grad():
    prediction = model2(test_x)

print(
    "新数据预测:",
    prediction
)