# def myfunc(a, b):
#     #  returns 5 % of the sum of a and b
#     return sum((a, b)) * 0.05
#
#
# x = myfunc(40, 60)
# print(x)


def myfunc(*args):
    return sum(args) * 0.05


x = myfunc(12, 10, 8)
print(x)


def myfunc2(**kwargs):
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')


myfunc2(fruit='apple', veggie='lettuce')


def myfunc3(*args, **kwargs):
    print(args)
    print(kwargs)
    print('I would like {} {}'.format(args[0], kwargs['food']))


myfunc3(10, 20, 30, fruit='orange', food='eggs', animal='dog')
