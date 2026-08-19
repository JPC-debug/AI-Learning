import pandas as pd

students = pd.read_csv('students.csv')
scores = pd.read_csv('scores.csv')
print("学生信息：")
print(students)

print("\n成绩信息：")
print(scores)

student_scores = pd.merge(students,scores, on='student_id')

print("\n完整学生成绩数据：")
print(student_scores)

df = student_scores
class_statistics = df.groupby('class')['score'].agg(
    average_score = 'mean',
    highest_score = 'max',
    lowest_score = 'min',
    score_count = 'count'
)


student_average = df.groupby('name')['score'].mean()


score_pivot = pd.pivot_table(
    df,
    values='score',
    index='class',
    columns='subject',
    aggfunc='mean'
)

print("\n班级整体成绩统计：")
print(class_statistics)

print("\n每个学生平均成绩：")
print(student_average)

print("\n班级 × 科目平均成绩：")
print(score_pivot)

class_statistics.to_csv('class_statistics.csv')

student_average.to_csv(
    'student_average.csv',
    header=['average_score']
)

score_pivot.to_csv('score_pivot.csv')

print("\n分析结果已成功保存！")