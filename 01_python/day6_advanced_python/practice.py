# scores = [45, 78, 92, 56, 88, 30, 67]

# result1 = [score1 for score1 in scores if score1 >= 60]

# print(result1)

# result2 = [round(score2 * 1.1,1) for score2 in scores]

# print(result2)

# scores = {
#     'Jack': 85,
#     'Rose': 92,
#     'Tom': 55,
#     'Bob': 48,
#     'Alice': 76
# }

# passed = {
#     name : score
#     for name, score in scores.items()
#     if score >= 60
# }

# print(passed)

# numbers = [1, 2, 2, 3, 4, 4, 5, 5, 5]

# result = {number **2 for number in numbers}

# print(result)

# languages = ['Python', 'C++', 'Java', 'Go']

# for index, language in enumerate(languages, start=1):
#     print(index, language)

# names = ['Jack', 'Rose', 'Tom', 'Alice']
# scores = [85, 92, 76, 88]

# for name, score in zip(names, scores):
#     print(name,'的成绩是', score)

# result = {
#     name : score
#     for name, score in zip(names, scores)
# }
# print(result)

# students = [
#     {"name": "Jack", "score": 85},
#     {"name": "Rose", "score": 92},
#     {"name": "Tom", "score": 76},
#     {"name": "Alice", "score": 88},
#     {"name": "Bob", "score": 59}
# ]

# ranking = sorted(
#     students,
#     key = lambda student : student['score'],
#     reverse= True
# )

# print(ranking)

# for index, student in enumerate(ranking, start=1):
#     print('第', index, '名', student['name'], ', 成绩', student['score'])

scores = [45, 78, 92, 56, 88, 30, 67]

result = list(map(lambda score: round(score * 1.1,1), scores))
print(result)

result1 = list(filter(lambda score: score >= 60, scores))
print(result1)

result2 = list(map(lambda score: round(score * 1.1, 1),result1))
print(result2)