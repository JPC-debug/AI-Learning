# with open('test.txt', 'w',encoding='utf-8') as file:

#     file.write('Jack 90')
#     file.write('\nRose 95')
# print('写入完成！')

# with open('test.txt', 'r', encoding='utf-8') as file:
#     content = file.read()

# print(content)

# import json

# students = [
#     {'name': 'Jack', 'score': 90},
#     {'name': 'Rose', 'score': 95}
# ]

# with open('students.json', 'w', encoding='utf-8') as file:
#     json.dump(students,file, indent=4)

# print('保存成功')

# with open('students.json', 'r', encoding='utf-8') as file:
#     loaded_students = json.load(file)

# print(loaded_students)
# print('第一个学生：', loaded_students[0]['name'])
# print('第一个学生成绩：', loaded_students[0]['score'])

# try:
#     num = int(input("请输入一个数字："))
#     result = 10 / num
#     print(result)

# except ValueError:
#     print("请输入正确的数字")

# except ZeroDivisionError:
#     print("除数不能为 0")

# import json
# try:
#     with open('students.json', 'r', encoding='utf-8')as file:
#         students = json.load(file)

# except FileNotFoundError:
#     students = []

# # print(students)

# students.append({
#     'name': 'Jack',
#     'score': 90
# })

# with open('students.json', 'w', encoding='utf-8') as file:
#     json.dump(students,file, indent = 4)

# print('保存成功！')

from student import Student
from student_manager import StudentManager

manager = StudentManager()

# student1 = Student('Jack', 90)
# student2 = Student('Rose', 95)

# manager.students.append(student1)
# manager.students.append(student2)

# manager.save_students()

# print('保存成功！')

# data = student1.to_dict()

# print('转换后的字典：',data )

# student2 = Student.from_dict(data)
# print('恢复后的姓名：', student2.name)
# print('恢复后的成绩：', student2.score)

manager.load_students()

for student in manager.students:
    print(student.name, student.score)