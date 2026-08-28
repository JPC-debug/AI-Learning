import torch

a = torch.tensor(
    [1, 2, 3, 4]
)

# print(a)

matrix = torch.tensor(
    [
        [1, 2],
        [3, 4],
        [5, 6]
    ]
)

# print(matrix)

# print('shape:',matrix.shape)
# print('dtype:',matrix.dtype)

x = torch.tensor([1,2,3],dtype=torch.float32)
y = torch.tensor([4,5,6],dtype=torch.float32)

# print('加法：',x + y)
# print('减法', x-y)
# print('乘法：', x * y)
# print('除法：', x / y)

A = torch.tensor(
    [
        [1,2],
        [3,4]
    ],
    dtype=torch.float32
)

B = torch.tensor(
    [
        [5,6],
        [7,8]
    ],
    dtype=torch.float32
)

result = torch.matmul(A, B)
# print('矩阵乘法：',result)


import numpy as np

numpy_array = np.array([1,2,3])
tensor_from_numpy = torch.from_numpy(numpy_array)
# print('NumPy转Tensor:',tensor_from_numpy)

tensor_data = torch.tensor([4,5,6])
numpy_from_tensor = tensor_data.numpy()
# print('Tensor转NumPy:',numpy_from_tensor)

# print(
#     "CUDA 是否可用:",
#     torch.cuda.is_available()
# )

numpy_array = np.array(
    [1, 2, 3]
)

tensor_from_numpy = torch.from_numpy(
    numpy_array
)

# print(
#     "修改前:",
#     numpy_array,
#     tensor_from_numpy
# )

# numpy_array[0] = 100

# print(
#     "修改后:",
#     numpy_array,
#     tensor_from_numpy
# )

zeros = torch.zeros(2,3)
ones = torch.ones(2,3)
random_tensor = torch.rand(2,3)

# print(
#     "zeros:",
#     zeros
# )
# print(
#     "ones:",
#     ones
# )
# print(
#     "random:",
#     random_tensor
# )

X = torch.tensor([1,2,3,4,5,6])
print('原始shape:',X.shape)

X_reshaped = X.reshape(2,3)
print('reshape后：',X_reshaped)
print('新shape:',X_reshaped.shape)

device = torch.device(
    "cuda"
    if torch.cuda.is_available()
    else "cpu"
)

print(
    "当前设备:",
    device
)