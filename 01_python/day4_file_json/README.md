# Python AI Learning - Day 4

## 学习主题

Day 4 主要学习 Python 的文件操作、JSON 数据处理和异常处理，并在 Day 3 面向对象学生管理系统的基础上，实现数据持久化。

---

## 1. 文件读写

学习使用 `open()` 打开文件，并了解常见的文件模式：

- `r`：读取文件
- `w`：写入文件，会覆盖原来的内容
- `a`：追加内容

例如：

```python
file = open("test.txt", "w", encoding="utf-8")
file.write("Hello Python")
file.close()
```

实际开发中，更推荐使用 `with open()`：

```python
with open("test.txt", "w", encoding="utf-8") as file:
    file.write("Hello Python")
```

使用 `with open()` 后，文件使用结束时会自动关闭，不需要手动调用 `close()`。

读取文件：

```python
with open("test.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(content)
```

---

## 2. JSON 数据处理

JSON 是一种常见的数据存储和交换格式。

Python 自带 `json` 模块：

```python
import json
```

### 保存 JSON

使用：

```python
json.dump()
```

可以把 Python 数据写入 JSON 文件。

例如：

```python
students = [
    {"name": "Jack", "score": 90},
    {"name": "Rose", "score": 95}
]

with open("students.json", "w", encoding="utf-8") as file:
    json.dump(students, file, indent=4)
```

其中：

```python
indent=4
```

可以让生成的 JSON 文件更加整齐、方便阅读。

### 读取 JSON

使用：

```python
json.load()
```

可以读取 JSON 文件：

```python
with open("students.json", "r", encoding="utf-8") as file:
    students = json.load(file)
```

因此可以简单记住：

```text
json.dump() → 保存

json.load() → 读取
```

---

## 3. 异常处理

学习使用：

```python
try:
    ...
except:
    ...
```

处理程序运行过程中可能出现的错误。

例如：

```python
try:
    num = int(input("请输入一个数字："))
    result = 10 / num
    print(result)

except ValueError:
    print("请输入正确的数字")

except ZeroDivisionError:
    print("除数不能为 0")
```

通过异常处理，可以避免用户输入错误时程序直接崩溃。

---

## 4. FileNotFoundError

在读取文件时，如果文件不存在：

```python
with open("students.json", "r", encoding="utf-8") as file:
    students = json.load(file)
```

Python 会产生：

```text
FileNotFoundError
```

因此可以使用：

```python
try:
    with open("students.json", "r", encoding="utf-8") as file:
        students = json.load(file)

except FileNotFoundError:
    students = []
```

如果第一次运行程序时还不存在 `students.json`，就使用空列表作为初始数据。

---

## 5. Student 对象与字典转换

Day 3 中学生信息使用 `Student` 对象保存。

例如：

```python
student = Student("Jack", 90)
```

但是 JSON 不能直接保存自定义的 `Student` 对象。

因此需要先把 Student 对象转换成字典。

### to_dict()

在 `Student` 类中增加：

```python
def to_dict(self):
    result = {
        "name": self.name,
        "score": self.score
    }

    return result
```

实现：

```text
Student 对象
    ↓
to_dict()
    ↓
Python 字典
```

例如：

```text
Student("Jack", 90)

↓

{"name": "Jack", "score": 90}
```

---

## 6. from_dict()

读取 JSON 后得到的是 Python 字典。

为了重新创建 Student 对象，使用：

```python
@classmethod
def from_dict(cls, data):
    return cls(data["name"], data["score"])
```

这里使用了：

```python
@classmethod
```

普通实例方法中的：

```python
self
```

代表某一个具体对象。

而类方法中的：

```python
cls
```

代表这个类本身。

因此：

```python
cls(data["name"], data["score"])
```

在这里相当于：

```python
Student(data["name"], data["score"])
```

最终实现：

```text
Python 字典
    ↓
Student.from_dict()
    ↓
Student 对象
```

---

## 7. 保存学生数据

在 `StudentManager` 中增加：

```python
save_students()
```

首先遍历：

```python
self.students
```

把每个 Student 对象转换成字典：

```python
data = []

for student in self.students:
    data.append(student.to_dict())
```

然后保存到 JSON：

```python
with open("students.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4)
```

完整的数据流：

```text
Student 对象
    ↓
to_dict()
    ↓
Python 字典
    ↓
json.dump()
    ↓
students.json
```

---

## 8. 加载学生数据

在 `StudentManager` 中增加：

```python
load_students()
```

读取 JSON：

```python
with open("students.json", "r", encoding="utf-8") as file:
    data = json.load(file)
```

然后把每个字典重新转换成 Student 对象：

```python
self.students = []

for student_data in data:
    student = Student.from_dict(student_data)
    self.students.append(student)
```

同时使用：

```python
except FileNotFoundError:
    self.students = []
```

处理第一次运行时文件不存在的问题。

完整的数据流：

```text
students.json
    ↓
json.load()
    ↓
Python 字典
    ↓
Student.from_dict()
    ↓
Student 对象
```

---

## 9. 数据持久化

最终，Day 3 的学生管理系统从：

```text
程序启动
↓
添加学生
↓
数据只存在内存
↓
程序关闭
↓
数据消失
```

升级成：

```text
程序启动
↓
load_students()
↓
读取 students.json
↓
恢复 Student 对象
↓
添加 / 修改 / 删除学生
↓
save_students()
↓
保存 students.json
↓
程序关闭
↓
再次启动
↓
数据仍然存在
```

同时，在添加、修改和删除学生后立即保存数据，降低程序异常关闭导致数据丢失的风险。

---

## Day 4 总结

通过 Day 4 的学习，我第一次实现了一个具有数据持久化能力的 Python 项目。

本次学习掌握了：

- Python 文件读取和写入
- `open()`
- `with open()`
- `r`、`w`、`a` 文件模式
- JSON 数据格式
- `json.dump()`
- `json.load()`
- `try / except`
- `ValueError`
- `ZeroDivisionError`
- `FileNotFoundError`
- `@classmethod`
- `self` 和 `cls` 的基本区别
- Student 对象与字典之间的转换
- `to_dict()`
- `from_dict()`
- `save_students()`
- `load_students()`
- 数据持久化的基本思想

Day 4 在 Day 3 面向对象项目的基础上进一步加入了文件存储能力，使学生管理系统的数据能够跨程序运行保存，也为后续的数据处理、API、数据库以及 AI 项目学习打下基础。