names = ["Jack", "Rose", "Tom", "Alice", "Bob", "Mike"]

scores = [85, 92, 56, 88, 45, 76]
print("===== 学生成绩分析 =====")

print("\n所有学生：")
students = {
    name : score
    for name, score in zip(names,scores)
}

print(students)

print("\n及格学生：")
result = list(filter(
    lambda item: item[1] >= 60,
    students.items()
    ))
print(result)

passed_students = dict(result)
print(passed_students)

ranking = sorted(
    students.items(),
    key= lambda item: item[1],
    reverse= True
)
print("\n成绩排名：")
for index, student in enumerate(ranking, start=1):
    print(f"第{index}名：{student[0]},{student[1]}分")

average = round(sum(scores) / len(scores), 2)
highest = max(scores)
lowest = min(scores)


print("\n统计信息：")
print("平均成绩：", average)
print("最高成绩：", highest)
print("最低成绩：", lowest)