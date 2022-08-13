def say_hello():
    print("Hello")


say_hello()


def say_name_2(name='Default'):
    print(f"Hello, {name}")


say_name_2('Luba')


def add_num(num1, num2):
    return num1 + num2


result = add_num(10, 20)
print(result)


def myfunc(a, b):
    print(a + b)
    return a + b


result_2 = myfunc(10, 21)


def sum_numbers(num1, num2):
    return num1 + num2


x = sum_numbers(10, 23)
y = sum_numbers('10', '20')
print(x)
print(y)

