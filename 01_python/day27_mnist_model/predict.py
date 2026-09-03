import torch
import torch.nn as nn
from torchvision import datasets
from torchvision.transforms import ToTensor

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
model.load_state_dict(
    torch.load(
        'models/mnist_model.pth'
    )
)

model.eval()
print('模型加载成功')

test_data = datasets.MNIST(
    root='../day26_mnist/data',
    train=False,
    download=True,
    transform=ToTensor()
)

image, label = test_data[0]
print('原始图片shape:', image.shape)
print('真实标签：',label)

image = image.view(1, -1)

with torch.no_grad():
    output = model(image)
    prediction = torch.argmax(output, dim=1)
    print('预测结果：',prediction.item())
    print('真实结果：',label)

images = []
labels = []

for i in range(10):
    image, label = test_data[i]

    images.append(image)
    labels.append(label)

images = torch.stack(images)
print(images.shape)

images = images.view(images.size(0), -1)

with torch.no_grad():
    outputs = model(images)
    predictions = torch.argmax(outputs, dim=1)

print("前10个预测：")
print(predictions)

print("前10个真实标签：")
print(torch.tensor(labels))