# print("day1 python start!")
# def hello():
#     print("hello world")

# hello()
# def introduce(name):
#     print("my name is" , name)

# introduce("Peter paker")

# def add(a,b):
#     result = a + b
#     return result

# x = add(3,5)
# print(x)

# def introduce2(name, age=18):
#     print("My name is",name,"and I am",age, "years old.")

# introduce2("John")
# introduce2("Alice",22)
# def students(name, age, score):
#     print(name, age, score)

# students("Jhon", 18, 90)
# students(age=20, name="Peter", score=88)
# def add(*numbers):
#     print(numbers)

# add(1,2,3,4,5)
# def add(*numbers):
#     total = 0
#     for number in numbers:
#         total += number
#     return total
# #如果写add(1,2,3,4,5),不会输出结果，因为没有print()函数来显示返回值。需要使用print()函数来输出add()函数的返回值。
# print(add(1,2,3,4,5))
#*number相当于一个元组，**kwargs相当于一个字典

# def add(**kwargs):
#     print(kwargs)
# add(name="Peter", age=22, score=100)

# def square(x):
#     return x * x
# print(square(5))
# square = lambda x : x * x
# print(square(10))
names = ["jack", "rose", "tom"]
for number, name in enumerate(names,start=1):
    print(number, name)