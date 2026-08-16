# try:
#     number1 = int(input('请输入第一个数字：'))
#     number2 = int(input('请输入第二个数字：'))
#     result = number1 / number2

# except ValueError:
#     print('输入错误，请输入整数')

# except ZeroDivisionError:
#     print('第二个数字不能为零')

# else:
#     print('输入成功！')
#     print('结果是：', result)

# finally:
#     print('程序执行结束')

# try:
#     score = float(input('请输入学生成绩：'))

#     if score < 0 or score > 100:
#         raise ValueError('成绩必须在0到100之间')
# except ValueError as e:
#     print('输入错误：', e)

# else:
#     print('学生成绩：', score)

# try:
#     age = float(input('请输入年龄：'))
# except ValueError:
#     print('输入错误，请输入数字')


# else:
#     try:
#         if age < 0 or age > 150:
#             raise ValueError('年龄必须在0到150之间')
#     except ValueError as e:
#         print('输入错误：', e)
#     else:
#         print('年龄为：', age)
# try:
#     with open('test.txt', 'r', encoding='utf-8') as file:
#         content = file.read()
# except FileNotFoundError:
#     print('文件不存在')

# else:
#     print(content)

# import json

# try:
#     with open('test.json', 'r', encoding='utf-8') as file:
#         data = json.load(file)

# except FileNotFoundError:
#     print('数据文件不存在')
    
# except json.JSONDecodeError:
#     print('JSON 文件格式错误')

# else:
#     print(data)

from student import Student

student1 = Student('Jack', 200)
print(student1.name, student1.score)