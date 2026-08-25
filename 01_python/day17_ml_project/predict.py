import joblib
import pandas as pd


# 加载模型

model = joblib.load(
    "models/student_model.pkl"
)


print("模型加载成功！")

# 新学生数据

new_student = pd.DataFrame(
    [
        {
            "study_hours": 6,
            "attendance": 90,
            "homework": 95
        }
    ]
)
# 预测类别

result = model.predict(
    new_student
)


print(
    "预测结果:",
    result
)

# 预测概率

probability = model.predict_proba(
    new_student
)


print(
    "预测概率:",
    probability
)