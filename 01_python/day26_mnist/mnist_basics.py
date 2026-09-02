import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor

train_data = datasets.MNIST(
    root='data',
    train=True,
    download=True,
    transform=ToTensor()
)

test_data = datasets.MNIST(
    root='data',
    train=False,
    download=True,
    transform=ToTensor()
)

# print('训练集数量：', len(train_data))
# print('测试集数量：', len(test_data))

# image, label = train_data[0]

# print('图片shape：',image.shape)
# print('标签：', label)

train_loader = DataLoader(
    train_data,
    batch_size=64,
    shuffle=True
)

test_loader = DataLoader(
    test_data,
    batch_size=64,
    shuffle=False
)

images, labels = next(iter(train_loader))

print('一个batch图片shape:', images.shape)
print('一个batch标签shape：', labels.shape)

print('前十个标签：', labels[:10])

images = images.view(images.size(0),-1)
print('展开后的shape:', images.shape)

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


model = MNISTNetwork()
print(model)

loss_fn = nn.CrossEntropyLoss()

optimizer = torch.optim.Adam(
    model.parameters(),
    lr=0.001
)


model.train()
for epoch in range(5):
    model.train()
    total_loss = 0
    for images, labels in train_loader:

        images = images.view(images.size(0),-1)

        outputs = model(images)

        loss = loss_fn(outputs, labels)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        total_loss += loss.item()

    average_loss = total_loss / len(train_loader)

    print(
        'epoch:',
        epoch + 1,
        'average loss:',
        average_loss
    )

model.eval()

correct = 0
total = 0

with torch.no_grad():
    for images, labels in test_loader:
        images = images.view(images.size(0),-1)
        outputs = model(images)
        predictions = torch.argmax(outputs,dim=1)
        correct += (predictions ==labels).sum().item()
        total += labels.size(0)

accuracy = correct / total

print('Test Accuracy:',accuracy)

model.eval()

with torch.no_grad():
    images,labels = next(iter(test_loader))

    images = images.view(images.size(0),-1)
    outputs = model(images)
    predictions = torch.argmax(outputs,dim=1)

    print('前十个预测：', predictions[:10])
    print('前十个真实标签：', labels[:10])