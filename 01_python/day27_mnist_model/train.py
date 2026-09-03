import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor

class MNISTNetwork(nn.Module):
    def __init__(self):
        super().__init__()

        self.fc1 = nn.Linear(28 * 28, 128)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):

        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x

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

model = MNISTNetwork()

loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(
    model.parameters(),
    lr=0.001
)

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
        'loss:',
        average_loss
    )

torch.save(
    model.state_dict(),
    'models/mnist_model.pth'
)

print('模型保存成功')