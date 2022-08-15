# c = 25
#
#
# def printer():
#     c = 50
#     return c
#
#
# print(c)
# print(printer())
#
# name = 'This is global string'
#
#
# def greet():
#     name = 'Sammy'
#
#     def hello():
#         print('Hello ' + name)
#
#     hello()
#
# y = greet()
# print(y)

x = 50


def func():
    global x
    print(f'X is {x}')

    x = 'NEW VALUE'
    print(f'Now x is {x}')


func()
print(x)