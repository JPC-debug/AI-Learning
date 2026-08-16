# Day 5 - Exception Handling and Modularization

## 1. 学习目标

Day 5 主要学习 Python 的**异常处理、主动抛出异常以及程序模块化**。

在 Day 4 中，学生管理系统已经能够通过 JSON 文件实现数据持久化。Day 5 在此基础上继续改进程序，使程序在遇到非法输入、文件不存在、JSON 文件损坏等情况时不会直接崩溃，同时对 `main.py` 进行函数拆分，使项目结构更加清晰。

---

## 2. 异常处理

Python 使用 `try / except` 捕获和处理程序运行过程中可能出现的异常。

基本结构：

```python
try:
    # 可能发生异常的代码
except ValueError:
    # 异常发生后的处理
```

例如：

```python
try:
    score = float(input("请输入成绩："))
except ValueError:
    print("成绩必须是数字")
```

当用户输入 `abc` 时，`float()` 会产生 `ValueError`，但程序不会直接崩溃，而是进入 `except`。

---

## 3. else 和 finally

完整的异常处理结构还可以包含：

```python
try:
    ...
except:
    ...
else:
    ...
finally:
    ...
```

其中：

- `try`：执行可能发生异常的代码
- `except`：捕获并处理异常
- `else`：没有发生异常时执行
- `finally`：无论是否发生异常都会执行

---

## 4. raise 主动抛出异常

除了 Python 自动产生异常，也可以使用 `raise` 主动产生异常。

例如学生成绩必须在 0～100 之间：

```python
if score < 0 or score > 100:
    raise ValueError("成绩必须在0到100之间")
```

在 `Student` 类中加入成绩校验后，无论从哪里创建或修改学生对象，都能够保证成绩数据合法。

例如：

```python
def update_score(self, new_score):
    if not 0 <= new_score <= 100:
        raise ValueError("成绩必须在0到100之间")

    self.score = new_score
```

---

## 5. 常见异常

本次学习和项目中使用了以下异常：

### ValueError

数据类型或数值不符合要求，例如：

```python
float("abc")
```

### ZeroDivisionError

除数为 0：

```python
10 / 0
```

### FileNotFoundError

尝试读取不存在的文件。

### json.JSONDecodeError

JSON 文件存在，但内容不是合法的 JSON 格式。

---

## 6. JSON 文件异常处理

读取 `students.json` 时加入异常处理：

```python
try:
    with open("students.json", "r", encoding="utf-8") as file:
        data = json.load(file)

except FileNotFoundError:
    self.students = []

except json.JSONDecodeError:
    print("数据文件格式错误，将使用空学生列表")
    self.students = []
```

这样即使数据文件不存在或者 JSON 内容损坏，程序也不会直接崩溃。

---

## 7. 异常传播

本次项目进一步理解了异常可以在不同函数和文件之间传播。

例如：

```text
main.py
    ↓
StudentManager
    ↓
Student.update_score()
    ↓
raise ValueError
    ↑
    ↑
main.py 中的 except 捕获
```

底层类负责发现数据问题并抛出异常，上层程序负责捕获异常并向用户显示合适的信息。

---

## 8. 模块化重构

原来的 `main.py` 将大量代码直接写在 `while True` 中。

Day 5 将不同功能拆分成独立函数：

```python
def add_student(manager):
    ...

def find_student(manager):
    ...

def update_student(manager):
    ...

def remove_student(manager):
    ...
```

主循环因此更加简洁：

```python
if choice == "1":
    add_student(manager)
elif choice == "2":
    find_student(manager)
elif choice == "3":
    manager.show_students()
elif choice == "4":
    update_student(manager)
elif choice == "5":
    remove_student(manager)
```

这样可以提高代码的可读性、可维护性和复用性。

---

## 9. main() 与程序入口

将程序主要运行逻辑封装到：

```python
def main():
    ...
```

并使用：

```python
if __name__ == "__main__":
    main()
```

它表示只有当当前文件被直接运行时才执行 `main()`。

如果 `main.py` 被其他 Python 文件导入，则不会自动启动学生管理系统。

---

## 10. 项目结构

```text
day5_exception_module/
│
├── README.md
├── main.py
├── practice.py
├── student.py
├── student_manager.py
└── students.json
```

各文件职责：

- `main.py`：程序入口及用户交互
- `student.py`：Student 类及学生数据校验
- `student_manager.py`：学生管理及 JSON 数据读写
- `practice.py`：异常处理练习
- `students.json`：保存学生数据
- `README.md`：记录 Day 5 学习内容

---

## 11. 今日总结

Day 5 在之前学生管理系统的基础上进一步提高了程序的健壮性。

通过 `try / except`，程序能够处理用户非法输入；通过 `raise`，类可以主动阻止非法数据进入系统；通过 `FileNotFoundError` 和 `JSONDecodeError`，程序能够处理数据文件异常。

同时，通过函数拆分和 `main()` 程序入口，将原本集中在主循环中的代码进行了模块化整理。

至此，学生管理系统已经从一个简单的 Python 练习逐渐发展为一个具有**面向对象、文件持久化、异常处理和模块化结构**的小型 Python 项目。