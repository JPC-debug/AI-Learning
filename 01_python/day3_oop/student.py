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