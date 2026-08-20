import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('students.csv')
df['average'] = df[
    ['python', 'math', 'english']
].mean(axis=1)

# print(df)

# plt.bar(df['name'], df['average'])
# plt.xlabel('Student')
# plt.ylabel('Average Score')
# plt.title('Student Average Scores')
# plt.show()

# subject_average = df[
#     ['python', 'math', 'english']
# ].mean(axis=0)

# print(subject_average)

# print(subject_average.index)
# print(subject_average.values)

# plt.bar(subject_average.index, subject_average.values)
# plt.xlabel('Subject')
# plt.ylabel('Average Score')
# plt.title('Subject Average Scores')
# plt.show()

fig, axes = plt.subplots(2,2, figsize=(12, 8))

axes[0,0].bar(df['name'], df['average'])
axes[0,0].set_xlabel('Student')
axes[0,0].set_ylabel('Average Score')
axes[0,0].set_title('Student Average Scores')


subject_average = df[
    ['python', 'math', 'english']
].mean(axis=0)
axes[0,1].bar(subject_average.index, subject_average.values)
axes[0,1].set_xlabel('Subject')
axes[0,1].set_ylabel('Average Score')
axes[0,1].set_title('Subject Average Scores')

axes[1,0].hist(df['python'], bins=3)
axes[1,0].set_xlabel('Score')
axes[1,0].set_ylabel('Frequency')
axes[1,0].set_title('Python Score Distribution')

axes[1,1].scatter(df['python'],df['math'])
axes[1,1].set_xlabel('Python Score')
axes[1,1].set_ylabel('Math Score')
axes[1,1].set_title('Python vs Math')

correlation = df['python'].corr(df['math'])
print('Correlation:', correlation)

plt.tight_layout()

plt.savefig(
    'student_analysis.png',
    dpi=300,
    bbox_inches='tight'
)

plt.show()