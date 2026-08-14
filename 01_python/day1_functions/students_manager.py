students = []
def add_student(students, name, score):
    student = {
        "name" :name,
        "score" : score
    }
    students.append(student)


# add_student(students,"jack",90)
# add_student(students,"rose",95)

# print(students)

def find_student(students,name):
     for student in students:
         if student["name"] == name:
            return student
     return"未找到该学生"
        
# name = input("请输入要查找的学生姓名：")
# result = find_student(students,name)
# print(result)

def show_students(students):
    if not students:
        print("没有学生信息")
        return
    for stu in students:
        print("姓名：", stu["name"], "成绩：", stu["score"])

# show_students(students)

def calculate_average(students):
    if not students:
        print("没有学生信息，无法计算平均成绩")
        return
    total = 0
    for student in students:
        total += student['score']
    average = total / len(students)
    return average

# result = calculate_average(students)
# print("平均成绩为：", result)

def get_ranking(students):
    if not students:
        print("没有学生信息，无法计算排名")
        return
    ranking = sorted(students, key=lambda student : student['score'], reverse=True)
    return ranking

# for rank, student in enumerate(get_ranking(students), start=1):
#     print(rank, student['name'],'成绩:', student['score'])

while True:
    print('学生管理系统')
    print('1. 添加学生')
    print('2. 查找学生')
    print('3. 显示所有学生')
    print('4. 计算平均成绩')
    print('5. 排名')
    print('0. 退出')
    choice = input('请输入操作编号：')

    if choice == '1':
        name = input('请输入学生姓名：')
        score = float(input('请输入学生成绩：'))
        add_student(students, name, score)
        print("学生信息已添加!")
    elif choice == '2':
        name = input('请输入要查找的学生姓名：')
        result = find_student(students, name)
        print(result)
    elif choice == '3':
        show_students(students)
    elif choice == '4':
        result = calculate_average(students)

        if result is not None:
            print("平均成绩为：", result)
    elif choice == '5':
        ranking = get_ranking(students)

        if ranking is not None:
            print("学生排名：")
            for rank, student in enumerate(ranking, start=1):
                print(rank, student['name'], '成绩:', student['score'])
    elif choice == '0':
        print("退出系统")
        break
    else:
        print("无效的操作编号，请重新输入")