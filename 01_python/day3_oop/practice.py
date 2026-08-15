class Student:
     def __init__(self,name,score):
         self.name = name
         self.score = score

     def show_info(self):
         print('姓名：', self.name)
         print('成绩：', self.score)

     def check_pass(self):
         if self.score >= 60 :
             print('及格')

         else:
             print('不及格')

     def update_score(self,new_score):
         if 0 <= new_score <= 100:
             self.score = new_score
             print('修改成功！')
         else:
             print('成绩必须在0到100之间')



# student1 = Student('Jack',90)
# student2 = Student('Rose',95)
# student3 = Student('Tom', 55)

# print(student1.name)
# print(student1.score)

# print(student2.name)
# print(student2.score)

# student1.update_score(200)
# student1.show_info()
# student1.check_pass()

# student3.show_info()
# student3.check_pass()

students = []
student1 = Student('Jack', 90)
student2 = Student('Rose', 95)
student3 = Student('Tom', 55)

students.append(student1)
students.append(student2)
students.append(student3)

def find_student(students,name):
    for student in students:
        if student.name == name:
            return student
    return None

result = find_student(students,'BobBob')

# if result:
#     result.show_info()
# else:
#     print('未找到该学生')

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self,student):
        self.students.append(student)

    def show_students(self):
        for student in self.students:
            student.show_info()

    def find_student(self,name):
        for student in self.students:
            if student.name == name:
                return student

        return None

    def remove_student(self,name):
        student = self.find_student(name)

        if student:
            self.students.remove(student)
            print('删除成功')

        else:
            print('未找到该学生')

    def update_student_score(self,name,new_score):
        student = self.find_student(name)

        if student:
            student.update_score(new_score)
        
        else:
            print('未找到该学生')


manager = StudentManager()
student1 = Student('Jack',90)
student2 = Student('Rose',95)
student3 = Student('Tom',55)

manager.add_student(student1)
manager.add_student(student2)
manager.add_student(student3)

manager.show_students()

# result = manager.find_student("Rose")

# if result:
#     result.show_info()
# else:
#     print('未找到该学生')

# manager.remove_student('Rose')
# manager.show_students()

# manager.update_student_score('Tom',100)
# manager.show_students()

manager.update_student_score("Jack", 98)
manager.update_student_score("Tom", 200)
manager.update_student_score("Bob", 80)

manager.remove_student("Rose")
manager.remove_student("Bob")

manager.show_students()