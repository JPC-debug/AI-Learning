import joblib

model = joblib.load('student_model.pkl')
print('模型加载成功！')

new_student = [
    [
        6,
        90,
        95
    ]
]


result = model.predict(
    new_student
)


print("预测结果:")
print(result)