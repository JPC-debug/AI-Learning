import numpy as np

numbers = np.array([85,92,78,96,88])
# print(numbers)
# print(type(numbers))
# print(numbers.size)
# print(numbers.ndim)

# print(numbers[0])
# print(numbers[-1])
# print(numbers[0:3])
# print(numbers[1:4])

# scores = np.array([
#     [85, 90, 92],
#     [78, 88, 95],
#     [92, 76, 89]
# ])

# print(scores)
# print(scores.ndim)
# print(scores.shape)
# print(scores[0,1])
# print(scores[1,2])
# print(scores[2,0])

# print(scores[0, :])
# print(scores[1, :])
# print(scores[:,0])
# print(scores[:,2])
# print(scores[0:2,1:3])

# numbers1 = numbers + 5
# numbers2 = numbers - 10
# numbers3 = numbers * 2
# numbers4 = numbers / 2

# bonus = np.array([1, 2, 3, 4, 5])

# numbers5 = numbers + bonus
# print(numbers1)
# print(numbers2)
# print(numbers3)
# print(numbers4)
# print(numbers5)
# print(numbers > 90)

# print(numbers[numbers > 90])
# print(numbers[numbers < 85])
# print(numbers[numbers >= 85])
# print(numbers[(numbers >= 80) & (numbers <= 90)])

print(numbers.sum())
print(numbers.mean())
print(numbers.max())
print(numbers.min())
print(numbers.argmax())
print(numbers.argmin())

names = np.array(["Jack", "Rose", "Tom", "Bob", "Alice"])
print(names[numbers.argmax()])
print(names[numbers.argmin()])