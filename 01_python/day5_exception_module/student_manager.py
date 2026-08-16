from student import Student
import json 

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

    def save_students(self):
        data = []

        for student in self.students:
            data.append(student.to_dict())

        with open('students.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)

    def load_students(self):
        try:
            with open('students.json', 'r', encoding='utf-8') as file:
                data = json.load(file)

            self.students = []

            for student_data in data:
                student = Student.from_dict(student_data)
                self.students.append(student)

        except FileNotFoundError:
            print('数据文件不存在，将创建新的学生列表')
            self.students = []

        except json.JSONDecodeError:
            print('数据文件格式错误，将使用空学生列表')
            self.students = []
               