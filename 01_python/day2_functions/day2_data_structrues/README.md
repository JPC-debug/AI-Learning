# Day 2 - Python 数据结构与通讯录项目

## 1. 今日学习内容

Day 2 主要学习 Python 常用数据结构，并通过通讯录项目进行综合练习。

### List 列表

```python
scores = [78, 92, 85, 66, 95, 88]
```

掌握了：

- 索引：`scores[0]`、`scores[-1]`
- 切片：`scores[0:3]`
- 修改元素：`scores[3] = 70`
- 添加元素：`scores.append(100)`
- 使用 `for` 遍历列表

还学习了列表推导式：

```python
high_scores = [score for score in scores if score >= 85]
new_scores = [score + 5 for score in scores]
```

---

### Dictionary 字典

```python
student = {
    'name': 'Jack',
    'age': 20,
    'score': 90
}
```

掌握了字典的查询、修改和添加：

```python
student['name']
student['score'] = 95
student['major'] = 'Computer Science'
```

以及：

```python
student.get('gender', 'Not specified')
```

相比直接使用 `student['gender']`，`get()` 在 key 不存在时不会产生 `KeyError`。

还学习了：

```python
student.keys()
student.values()
student.items()
```

其中 `.items()` 可以同时遍历 key 和 value：

```python
for name, score in students.items():
    print(name, score)
```

---

### Tuple 和 Set

元组：

```python
position = (120, 30)
x, y = position
```

元组与列表类似，但创建后不能直接修改。

集合：

```python
courses = {'Python', 'AI', 'Math'}
```

集合中的元素不会重复，并学习了交集和并集：

```python
student_a & student_b
student_a | student_b
```

---

## 2. 嵌套数据结构

学习了列表、字典之间的组合，例如：

```python
students = [
    {
        'name': 'Jack',
        'score': 90,
        'skills': ['Python', 'C++']
    }
]
```

可以逐层访问：

```python
students[0]['name']
students[0]['skills'][0]
```

这让我开始理解真实程序中的数据通常不是单独的列表或字典，而是多种数据结构组合使用。

---

# 3. 综合项目：通讯录管理系统

使用字典保存联系人：

```python
contacts = {
    'Jack': {
        'phone': '123456789',
        'email': 'jack@example.com'
    }
}
```

最终实现了：

- 添加联系人
- 查找联系人
- 删除联系人
- 修改联系人
- 显示所有联系人
- 退出程序

对应函数：

```python
add_contact()
find_contact()
delete_contact()
update_contact()
show_contacts()
```

使用：

```python
while True:
```

让通讯录持续运行，并通过：

```python
choice = input('请输入操作编号：')
```

配合 `if / elif` 判断用户选择。

输入 `0` 时：

```python
break
```

结束程序。

---

## 4. 项目中学到的重要细节

### `input()` 与 `None`

直接按 Enter 时：

```python
input()
```

得到的是空字符串：

```python
''
```

而不是 `None`。

因此修改联系人时使用：

```python
if phone == '':
    phone = None
```

再通过：

```python
if phone is not None:
    contacts[name]['phone'] = phone
```

实现“不输入就不修改”。

### `=` 和 `==`

```python
email = None
```

表示赋值。

```python
email == None
```

表示比较。

### `return` 和 `print`

```python
return
```

负责把结果返回并结束函数。

```python
print()
```

负责把内容显示到终端。

两者作用不同。

### 程序逻辑优化

修改联系人时，最开始是先输入新手机号和邮箱，再判断联系人是否存在。

后来改成：

```text
输入姓名
  ↓
判断联系人是否存在
  ↓
不存在 → 直接提示
存在 → 再输入新信息
```

这让我意识到程序不仅要“能运行”，还应该考虑用户实际使用时是否合理。

---

# 5. Day 2 总结

今天最大的收获不是单独记住 List、Dictionary、Tuple、Set 的语法，而是开始理解：

> **数据结构负责组织数据，函数负责处理数据，条件判断和循环负责控制程序运行。**

通讯录项目第一次把多个知识点真正组合了起来：

```text
数据结构
   +
函数
   +
if / elif
   +
while
   +
input
   ↓
完整的小程序
```

下一步继续学习 Python，并逐渐从“会写语法”向“能够独立设计程序”过渡。

**Day 2 Completed ✅**