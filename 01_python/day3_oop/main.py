from student import Student
from student_manager import StudentManager

manager = StudentManager()

while True:
    print("\n学生管理系统")
    print("1. 添加学生")
    print("2. 查找学生")
    print("3. 显示所有学生")
    print("4. 修改成绩")
    print("5. 删除学生")
    print("0. 退出")

    choice = input("请输入操作编号：")

    if choice == '1':
        name = input('请输入学生姓名：')
        try:
            score = float(input('请输入学生成绩：'))

        except ValueError:
            print('成绩必须是数字')
            continue

        if score < 0 or score > 100:
            print('成绩必须在0到100之间')
            continue

        student = Student(name,score)
        manager.add_student(student)

        print('添加成功！')

    elif choice == '0':
        print('退出系统')
        break

    elif choice == '2':
        name = input('请输入要查找的学生姓名：')
        result = manager.find_student(name)

        if result:
            result.show_info()
        else:
            print('未找到该学生')

    elif choice == '3':
        manager.show_students()

    elif choice == '4':
        name = input('请输入要修改成绩的学生姓名：')
        try:
            new_score = float(input('请输入新成绩：'))
        except ValueError:
            print('成绩必须是数字')
            continue

        manager.update_student_score(name,new_score)

    elif choice == '5':
        name = input('请输入要删除成绩的学生姓名')
        manager.remove_student(name)