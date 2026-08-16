from student import Student
from student_manager import StudentManager

def add_student(manager):
    name = input('请输入学生姓名：')

    try:
        score = float(input('请输入学生成绩：'))

    except ValueError:
        print('添加失败：成绩必须是数字')
        return

    try:
        student = Student(name, score)

    except ValueError as e:
        print('添加失败', e)
        return

    manager.add_student(student)
    manager.save_students()

    print('添加成功！')

def find_student(manager):
    name = input('请输入要查找的学生姓名：')
    result = manager.find_student(name)

    if result:
        result.show_info()
    else:
        print('未找到该学生')

def update_student(manager):
    name = input('请输入要修改成绩的学生姓名：')

    try:
        new_score = float(input('请输入新成绩：'))

    except ValueError:
        print('修改失败：成绩必须是数字')
        return

    try:
        manager.update_student_score(name, new_score)

    except ValueError as e:
        print('修改失败：', e)
        return

    manager.save_students()

def remove_student(manager):
    name = input('请输入要删除成绩的学生姓名:')
    manager.remove_student(name)
    manager.save_students()
def main():
    manager = StudentManager()
    manager.load_students()

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
            add_student(manager)

        elif choice == '0':
            manager.save_students()
            print('数据已保存')
            print('退出系统')
            break

        elif choice == '2':
            find_student(manager)

        elif choice == '3':
            manager.show_students()

        elif choice == '4':
            update_student(manager)

        elif choice == '5':
            remove_student(manager)

if __name__=='__main__':
    main()