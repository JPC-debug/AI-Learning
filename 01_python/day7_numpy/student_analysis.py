import numpy as np

names = np.array(["Jack", "Rose", "Tom", "Bob", "Alice"])

subjects = np.array(["数学", "英语", "Python"])

scores = np.array([
    [85, 90, 92],
    [78, 88, 95],
    [92, 76, 89],
    [96, 85, 91],
    [88, 94, 90]
])

print('学生：')
print(names)

print('科目：')
print(subjects)

print('成绩：')
print(scores)

print('成绩表形状：',scores.shape)
print('成绩表维度：',scores.ndim)

print(scores[0,:])
print(scores[:,2])
print(scores[4,1])

student_averages = scores.mean(axis = 1)
print(student_averages)

subject_averages = scores.mean(axis = 0)
print(subject_averages)

for name, average in zip(names,student_averages):
    print(f"{name} 平均分：{average}")

for subject, average in zip(subjects,subject_averages):
    print(f'{subject} 平均分：{average}')

best_average = student_averages.max()

print(f'最高平均分：{best_average}')
print(f'最高平均分学生：{names[student_averages == best_average]}')

high_scores = scores.max(axis=0)
high_index = scores.argmax(axis=0)

print(f'数学最高分：{high_scores[0]}，学生：{names[high_index[0]]}')
print(f'英语最高分：{high_scores[1]}，学生：{names[high_index[1]]}')
print(f'Python最高分：{high_scores[2]}，学生：{names[high_index[2]]}')

print(f'优秀学生：{names[student_averages >= 90]}')
print(f'优秀学生平均分：{student_averages[student_averages >= 90]}')