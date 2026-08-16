class Student:
    def __init__(self,name,score):
        if score < 0 or score > 100:
            raise ValueError('成绩必须在0到100之间')
         
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
        if new_score < 0 or new_score >100:

            raise ValueError('成绩必须在0到100之间')

        self.score = new_score
        print('修改成功！')

    def to_dict(self):
        result = {
             'name': self.name,
             'score': self.score
        }
        return result
    @classmethod
    def from_dict(cls,data):
        return cls(data['name'], data['score'])