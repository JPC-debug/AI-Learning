import torch
import torch.nn as nn
from torch.utils.data import DataLoader
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
        '../day27_mnist_model/models/mnist_model.pth'
    )
)

confusion_matrix = torch.zeros(10, 10, dtype=torch.int32)

model.eval()

class_correct = [0] * 10
class_total = [0] * 10

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

correct = 0
total = 0
with torch.no_grad():
    for images,labels in test_loader:
        images = images.view(
            images.size(0),
            -1
        )

        outputs = model(images)
        predictions = torch.argmax(outputs, dim=1)

        for i in range(labels.size(0)):
            label = labels[i].item()
            prediction = predictions[i].item()
            class_total[label] += 1

            if prediction == label:
                class_correct[label] += 1

            confusion_matrix[label][prediction] += 1
                
        correct += (predictions == labels).sum().item()
        total += labels.size(0)

accuracy = correct / total
print('Overall Accuracy:', accuracy)

for digit in range(10):
    accuracy = (
        class_correct[digit] / class_total[digit]
    )

    print(
        f"数字{digit}的准确率：{accuracy}"
    )

print("混淆矩阵：")
print(confusion_matrix)

errors = []
for true_label in range(10):
    for pred_label in range(10):
        if true_label != pred_label:

            count = confusion_matrix[
                true_label,
                pred_label
            ].item()

            errors.append(
                (
                    count,
                    true_label,
                    pred_label
                )
            )

errors.sort(reverse=True)

print("最常见的错误组合：")
for count, true_label, pred_label in errors[:10]:
    print(
        f"真实标签: {true_label}, 预测标签: {pred_label}, 错误次数: {count}"
    )