# scores = [78, 92, 85, 66, 95, 88]
# print(scores[0])
# print(scores[-1])
# print(scores[0:3])
# print(scores[1:4])
# scores[3] = 70
# scores.append(100)
# print(scores)

# high_scores = []

# for score in scores:
#     if score >= 85:
#         high_scores.append(score)

# print(high_scores)

# new_scores = []

# for score in scores:
#     score += 5
#     new_scores.append(score)

# print(new_scores)

# new_scores = [score + 5 for score in scores]
# print(new_scores)
# high_scores = [score for score in scores if score >= 85]
# print(high_scores)

# result = []
# for score in scores:
#     if score >= 85:
#         result.append(score + 5)
# print(result)

# result = [score +5 for score in scores if score >=85]
# print(result)

# student ={
#     'name' :'Jack',
#     'age' : 20,
#     'score' :90
#     }

# # print(student['name'])
# student['score'] = 95
# student['major'] = 'Computer Science'

# print(student)
# print(student['gender'])
# print(student.get('gender'))
# print(student.get('gender', 'Not specified'))

# print(student.keys())
# print(student.values())
# print(student.items())

# for key, value in student.items():
#     print(f"{key}: {value}")

# students = {
#     'Jack': 90,
#     'Rose': 85,
#     'Tom': 78,
#     'Alice': 88
# }

# for name, score in students.items():
#     if score >=85:
#         print(f"{name}:{score}")

# position = (120,30)
# print(position[0])
# print(position[1])
# print(position)

# # position[0] = 100
# x, y = position
# print(x)
# print(y)

# courses = [
#     'Python',
#     'AI',
#     'Python',
#     'Math',
#     'AI',
#     'English'
# ]
# unique_courses = set(courses)
# print(unique_courses)
# unique_courses.add('Physics')
# unique_courses.add('Python')
# print(unique_courses)

# student_a = {'python','AI','Math'}
# student_b = {'python','English','Math'}
# print(student_a & student_b)  # Intersection
# print(student_a | student_b)  # Union

students = [
    {
        'name': 'Jack',
        'score': 90,
        'skills': ['Python', 'C++']
    },
    {
        'name': 'Rose',
        'score': 95,
        'skills': ['Python', 'AI']
    },
    {
        'name': 'Tom',
        'score': 78,
        'skills': ['Java', 'C++']
    }
]

# print(students[0]['name'])
# print(students[1]['score'])
# print(students[2]['skills'])
# print(students[1]['skills'][1])

for student in students:
    print(f"{student['name']} :{student['score']}")

for student in students:
    if 'Python' in student['skills']:
        print(student['name'])
