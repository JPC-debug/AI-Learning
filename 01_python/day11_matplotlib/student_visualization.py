import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('students.csv')

print("=== Student Data ===")
print(df)

Math_average = df['math'].mean()
English_average = df['english'].mean()
Python_average = df['python'].mean()

subject_average = [Math_average, English_average, Python_average]

subjects = ["Math", "English", "Python"]

plt.bar(subjects, subject_average)

plt.xlabel('Subject')
plt.ylabel('Average Score')
plt.title('Average Score by Subject')
plt.savefig("charts/subject_average.png")
plt.show()

score = df['python']
plt.hist(score, bins=5)
plt.xlabel('Python Score')
plt.ylabel('Frequency')
plt.title('Python Score Distribution')

plt.savefig("charts/python_distribution.png")
plt.show()

x_data = df['math']
y_data = df['python']

plt.scatter(x_data, y_data)
plt.xlabel('Math Score')
plt.ylabel('Python Score')
plt.title('Math vs Python Score')

plt.grid()

plt.savefig('charts/math_python_scatter.png')
plt.show()

correlation = df['math'].corr(df['python'])
print('Math and Python correlation:', correlation)