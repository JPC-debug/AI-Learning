from student import Student

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