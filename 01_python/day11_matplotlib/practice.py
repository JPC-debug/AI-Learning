# import matplotlib.pyplot as plt

# days = [1,2,3,4,5]
# scores = [60,68,75,82,90]

# plt.plot(
#     days, 
#     scores,
#     marker='o',
#     linestyle='--',
#     label='Score'
#     )

# plt.xlabel('Day')
# plt.ylabel('Score')
# plt.title('Learning Progress')

# plt.legend()
# plt.grid()
# plt.show()

# subjects = ['Math', 'English', 'Python', 'Physics']
# scores = [88, 82, 95, 76]

# plt.bar(subjects,scores)

# plt.xlabel('Subject')
# plt.ylabel('Score')
# plt.title('Subject Scores')

# plt.show()

# students = ["Jack", "Rose", "Tom", "Alice", "Bob"]

# scores = [85, 92, 78, 96, 88]

# plt.bar(students, scores)

# plt.xlabel('Student')
# plt.ylabel('Score')
# plt.title('Student Scores')

# plt.show()

# import matplotlib.pyplot as plt

# study_hours = [1, 2, 2, 3, 4, 5, 6, 7]
# scores = [55, 60, 65, 68, 75, 82, 88, 95]

# plt.scatter(study_hours,scores)

# plt.xlabel("Study Hours")
# plt.ylabel("Score")
# plt.title("Study Hours vs Score")

# plt.show()

# import matplotlib.pyplot as plt

# scores = [
#     56, 62, 67, 68, 71,
#     73, 75, 76, 78, 79,
#     81, 82, 83, 85, 86,
#     88, 90, 92, 94, 97
# ]

# plt.hist(scores, bins=10)

# plt.xlabel("Score")
# plt.ylabel("Frequency")
# plt.title("Score Distribution")

# plt.show()

import pandas as pd
import matplotlib.pyplot as plt

data = {
    "name": ["Jack", "Rose", "Tom", "Alice", "Bob", "Mike"],
    "class": ["A", "A", "B", "B", "C", "C"],
    "score": [85, 92, 78, 88, 95, 82]
}

df = pd.DataFrame(data)

print(df)

class_average = df.groupby('class')['score'].mean()

plt.bar(class_average.index,class_average.values)
plt.xlabel('Class')
plt.ylabel('Average Score')
plt.title('Average Score by Class')

plt.show()

