import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor

class CNNNetwork(nn.Module):
    def __init__(self):
        super().__init__()

        self.conv1 = nn.Conv2d(
            in_channels = 1,
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
        self.fc2 = nn.Linear(128,10)

    def forward(self, x):
        x = self.conv1(x)
        x = self.relu(x)
        x = self.pool(x)

        x = self.conv2(x)
        x = self.relu(x)
        x = self.pool(x)

        x = x.view(x.size(0),-1)

        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)

        return x



model = CNNNetwork()

model.load_state_dict(
    torch.load(
        '../day29_mnist_cnn/models/mnist_cnn.pth'
    )
)

model.eval()

print('CNN模型加载成功！')

test_data = datasets.MNIST(
    root='../day26_mnist/data',
    train=False,
    download=True,
    transform=ToTensor()
)

test_loader = DataLoader(
    test_data,
    batch_size=1,
    shuffle=False
)

image, label = test_data[0]
print('图片shape:', image.shape)
print('真实标签:', label)

with torch.no_grad():
    output = model(image.unsqueeze(0))
    prediction = torch.argmax(
        output,
        dim=1
    )

print('预测结果：',prediction.item())

correct = 0

with torch.no_grad():
    for i in range(10):
        image, label = test_data[i]

        output = model(image.unsqueeze(0))
        prediction = torch.argmax(output, dim=1).item()

        print(f"第{i + 1}张：真实={label},预测={prediction}")

        if prediction == label:
            correct += 1

print(f"\n前10张图片预测正确率：{correct / 10:.2%}")


import random

index = random.randint(0, len(test_data) - 1)
image, label = test_data[index]
with torch.no_grad():
    output = model(image.unsqueeze(0))
    probabilities = torch.softmax(output, dim=1)
    prediction = torch.argmax(probabilities, dim=1).item()
    confidence = probabilities[0][prediction].item()

print("\n随机预测结果：")
print("图片编号：", index)
print("真实标签：", label)
print("预测结果：", prediction)
print(f"预测置信度：{confidence:.2%}")