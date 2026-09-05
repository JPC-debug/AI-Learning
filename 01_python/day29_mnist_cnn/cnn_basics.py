import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor

train_data = datasets.MNIST(
    root='../day26_mnist/data',
    train=True,
    download=True,
    transform=ToTensor()
)

train_loader = DataLoader(
    train_data,
    batch_size=64,
    shuffle=True
)

class CNNNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(
            in_channels=1,
            out_channels=16,
            kernel_size=3,
            padding=1
        )

        self.relu = nn.ReLU()
        self.pool = nn.MaxPool2d(kernel_size=2)

        self.conv2 = nn.Conv2d(
            in_channels=16,
            out_channels=32,
            kernel_size=3,
            padding=1
        )

        self.fc1 = nn.Linear(32*7*7,128)
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        # print('输入shape:',x.shape)

        x = self.conv1(x)
        # print('卷积后shape:',x.shape)
        x = self.relu(x)
        x = self.pool(x)
        # print('池化后shape:',x.shape)

        x = self.conv2(x)
        # print('第二次卷积后shape:', x.shape)
        x = self.relu(x)
        x = self.pool(x)
        # print('第二次池化后shape:', x.shape)

        x = x.view(x.size(0), -1)
        # print('展平后shape:', x.shape)

        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)

        # print('最终输出shape:',x.shape)

        return x

model = CNNNetwork()

# images, labels = next(
#     iter(train_loader)
# )

# output = model(images)

loss_fn = nn.CrossEntropyLoss()

optimizer = torch.optim.Adam(
    model.parameters(),
    lr=0.001
)

for epoch in range(3):
    model.train()
    total_loss = 0
    for images, labels in train_loader:

        outputs = model(images)

        loss = loss_fn(
            outputs,
            labels
        )

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        total_loss += loss.item()

    average_loss = (
        total_loss /
        len(train_loader)
    )

    # print(
    #     'epoch:',
    #     epoch + 1,
    #     'average loss:',
    #     average_loss
    # )


test_data = datasets.MNIST(
    root='../day26_mnist/data',
    train=False,
    download=True,
    transform=ToTensor()
)

test_loader = DataLoader(
    test_data,
    batch_size=64,
    shuffle=False
)

model.eval()

correct = 0
total = 0

with torch.no_grad():
    for images, labels in test_loader:
        outputs = model(images)
        predictions = torch.argmax(outputs,dim=1)

        correct += (predictions == labels).sum().item()

        total += labels.size(0)

accuracy = correct / total

print('Test Accuracy:',accuracy)

torch.save(
    model.state_dict(),
    'models/mnist_cnn.pth'
)

print('CNN模型保存成功！')