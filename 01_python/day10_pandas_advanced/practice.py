import pandas as pd

# students = pd.DataFrame({
#     'student_id': [1,2,3,4,5],
#     'name': ['Jack', 'Rose', 'Tom', 'Lucy', 'Bob']
# })

# scores = pd.DataFrame({
#     'student_id':[1,2,3,4,6],
#     'score':[88,95,76,91,100]
# })

# result = pd.merge(students,scores, on='student_id')

# print(result)

# inner_result = pd.merge(students, scores, on='student_id', how='inner')
# left_result = pd.merge(students, scores, on='student_id', how='left')
# right_result = pd.merge(students, scores, on='student_id', how='right')
# outer_result = pd.merge(students, scores, on='student_id', how='outer')

# print("inner 合并：")
# print(inner_result)

# print("\nleft 合并：")
# print(left_result)

# print("\nright 合并：")
# print(right_result)

# print("\nouter 合并：")
# print(outer_result)

# class1 = pd.DataFrame({
#     'name': ['Jack', 'Rose', 'Tom'],
#     'score': [88,95,76]
# })

# class2 = pd.DataFrame({
#     'name': ['Lucy', 'Bob', 'Mike'],
#     'score': [91,83,87]
# })

# all_students = pd.concat([class1,class2],ignore_index=True)
# print(all_students)

# students_data = pd.DataFrame({
#     'name': ['Jack', 'Rose', 'Tom', 'Lucy', 'Bob', 'Mike'],
#     'class': ['A', 'A', 'B', 'B', 'A', 'B'],
#     'score': [88, 95, 76, 91, 83, 87]
# })

# df = students_data
# class_average = df.groupby('class')['score'].mean()
# class_max = df.groupby('class')['score'].max()
# class_min = df.groupby('class')['score'].min()
# class_count = df.groupby('class')['score'].count()

# print("\n每班平均成绩：")
# print(class_average)

# print("\n每班最高成绩：")
# print(class_max)

# print("\n每班最低成绩：")
# print(class_min)

# print("\n每班学生人数：")
# print(class_count)

# class_stats = df.groupby('class')['score'].agg(
#     average_score = 'mean',
#     highest_score = 'max',
#     lowest_score = 'min',
#     student_count = 'count'
# )

# print("\n班级成绩统计：")
# print(class_stats)

scores_data = pd.DataFrame({
    'name': [
        'Jack', 'Jack',
        'Rose', 'Rose',
        'Tom', 'Tom',
        'Lucy', 'Lucy'
    ],
    'class': [
        'A', 'A',
        'A', 'A',
        'B', 'B',
        'B', 'B'
    ],
    'subject': [
        'Math', 'Python',
        'Math', 'Python',
        'Math', 'Python',
        'Math', 'Python'
    ],
    'score': [
        88, 92,
        95, 90,
        76, 85,
        91, 94
    ]
})
df = scores_data

score_pivot = pd.pivot_table(
    df,
    values='score',
    index='class',
    columns='subject',
    aggfunc='mean'
)

print("\n班级 × 科目平均成绩：")
print(score_pivot)