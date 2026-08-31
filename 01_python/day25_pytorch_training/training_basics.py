import torch
import torch.nn as nn
import torch.optim as optim

X = torch.tensor(
    [
        [1.0, 1.0],
        [1.5, 1.2],
        [2.0, 1.8],
        [4.0, 4.0],
        [4.5, 4.2],
        [5.0, 4.8]
    ]
)

y = torch.tensor(
    [
        0,0,0,1,1,1
    ]
)

class Classifier(nn.Module):
    def __init__(self):
        super().__init__()

        self.fc1 = nn.Linear(2, 4)

        self.relu = nn.ReLU()

        self.fc2 = nn.Linear(4,2)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)

        return x

model = Classifier()

loss_fn = nn.CrossEntropyLoss()

# optimizer = optim.SGD(
optimizer = optim.Adam(
    model.parameters(),
    lr=0.01
)

# for epoch in range(1000):
for epoch in range(200):
    model.train()
    outputs = model(X)
    loss = loss_fn(outputs,y)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    # if epoch % 100 == 0:
    if epoch % 20 == 0:
        print(
            'epoch:',
            epoch,
            'loss:',
            loss.item()
        )

model.eval()

with torch.no_grad():
    outputs = model(X)

    predictions = torch.argmax(
        outputs,
        dim=1
    )

print('预测结果：')
print(predictions)
print('真实结果：')
print(y)

correct = (predictions == y).sum().item()

total = y.size(0)

accuracy = correct / total
print('Accuracy:',accuracy)