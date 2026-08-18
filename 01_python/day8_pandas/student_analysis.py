import pandas as pd

students = {
    "name": ["Jack", "Rose", "Tom", "Alice", "Bob", "Lucy"],
    "math": [85, 90, 76, 95, 68, 88],
    "english": [78, 95, 82, 89, 75, 91],
    "python": [92, 88, 80, 96, 70, 94]
}

df = pd.DataFrame(students)
print(df)
print(df.shape)
print(df.columns)
print(df.dtypes)
df['average'] = (df['math'] + df['english'] + df['python']) / 3
df["average"] = df["average"].round(2)
print(df)

print(df[df["average"] >= 90])

print(f'数学平均分：{df['math'].mean().round(2)}')
print(f'英语平均分：{df['english'].mean().round(2)}')
print(f'Python平均分：{df['python'].mean().round(2)}')

print(df.loc[df["python"].idxmax()])

ranking = df.sort_values('average',ascending=False)
ranking = ranking.reset_index(drop=True)
ranking['rank'] = ranking.index + 1
print(ranking)

ranking.to_csv('student_ranking.csv', index=False)