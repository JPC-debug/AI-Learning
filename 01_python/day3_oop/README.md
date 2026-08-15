# Day 3 - Python 面向对象编程 OOP

## 1. 今日学习内容

Day 3 主要学习了 Python 的面向对象编程（OOP），并将之前学习的列表、函数、循环等知识结合起来，完成了一个基于类和对象的学生管理系统。

主要内容：

- 类（Class）与对象（Object）
- `__init__` 初始化方法
- `self` 的作用
- 实例属性与实例方法
- 对象的创建和数据修改
- 使用列表保存多个对象
- `Student` 与 `StudentManager` 两个类之间的协作
- Python 多文件模块与 `import`
- `try / except` 异常处理
- `break` 与 `continue`

---

## 2. 类与对象

类可以理解为一种“模板”，对象则是根据这个模板创建出来的具体实例。

例如：

```python
student1 = Student("Jack", 90)
```

其中 `Student` 是类，`student1` 是一个具体的 Student 对象。

相比之前使用字典保存学生信息：

```python
student = {"name": "Jack", "score": 90}
```

面向对象可以把数据和操作这些数据的方法组织在一起，使程序结构更加清晰。

---

## 3. `__init__` 与 `self`

创建 Student 对象时：

```python
def __init__(self, name, score):
    self.name = name
    self.score = score
```

`__init__` 会在创建对象时自动执行，用来初始化对象的数据。

`self` 表示当前对象本身。

例如：

```python
student1 = Student("Jack", 90)
```

此时可以理解为：

```text
self → student1
self.name → "Jack"
self.score → 90
```

因此，不同 Student 对象可以保存各自独立的数据。

---

## 4. Student 类

`Student` 负责描述和管理一个学生自身的信息，主要包含：

- `name`：姓名
- `score`：成绩
- `show_info()`：显示学生信息
- `check_pass()`：判断是否及格
- `update_score()`：修改成绩

在修改成绩时增加了 `0～100` 的范围判断，防止对象出现不合理的成绩。

---

## 5. StudentManager 类

为了管理多个 Student 对象，又创建了 `StudentManager`。

它主要负责：

- 添加学生
- 查找学生
- 显示所有学生
- 修改学生成绩
- 删除学生

我的理解是：

> `Student` 负责一个学生自身的数据和行为，`StudentManager` 负责管理多个 `Student` 对象。

例如修改成绩时，`StudentManager` 先找到对应的学生，再调用该学生自己的 `update_score()` 方法完成修改。

---

## 6. 多文件模块

将最开始全部写在 `practice.py` 中的代码进行了拆分：

```text
day3_oop/
├── practice.py
├── student.py
├── student_manager.py
├── main.py
└── README.md
```

其中：

- `student.py`：保存 `Student` 类
- `student_manager.py`：保存 `StudentManager` 类
- `main.py`：程序入口和菜单
- `practice.py`：Day 3 学习过程中的练习代码

通过：

```python
from student import Student
from student_manager import StudentManager
```

可以在不同 Python 文件之间使用自己定义的类。

---

## 7. 异常处理

使用：

```python
try:
    score = float(input("请输入成绩："))
except ValueError:
    print("成绩必须是数字")
```

可以防止用户输入 `abc` 等内容时程序直接崩溃。

同时学习了：

- `break`：直接结束整个循环
- `continue`：结束当前这一轮，重新进入下一轮循环

---

## 8. 今天遇到的问题

### `return None` 位置错误

最开始把 `return None` 写在 `for` 循环内部，导致查找学生时只检查第一个对象。

正确思路是遍历所有学生，全部没有找到以后再 `return None`。

### 对象变量被覆盖

连续使用：

```python
student1 = Student(...)
```

会让 `student1` 不断指向新的对象，之前的数据被覆盖。因此不同学生应该使用不同变量，或者直接保存到列表中。

### 字符串与变量混淆

曾经写成：

```python
manager.find_student("name")
```

这里 `"name"` 是固定字符串，而：

```python
manager.find_student(name)
```

才是使用变量 `name` 中保存的数据。

### 成绩范围问题

最开始创建学生时可以输入 `200`，因为只有 `update_score()` 对成绩范围进行了检查。

这让我认识到：除了考虑程序能不能运行，还需要考虑数据是否合法，以及数据验证应该由程序中的哪一部分负责。

---

## 9. Day 3 总结

通过 Day 3，我初步理解了 Python 面向对象编程的基本思想。

Day 2 主要使用“字典 + 函数”处理数据，而 Day 3 开始使用“类 + 对象”组织程序，并进一步把程序拆分成多个 Python 文件。

目前已经能够使用 `class` 创建自己的类，理解 `self`、`__init__`、属性和方法，并能够让多个对象和多个类之间相互协作。

下一步继续在这些基础上学习更加实际的 Python 编程方式，为后续 NumPy、数据处理和 AI 相关学习打基础。