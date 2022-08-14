def myfunc(*args):
    a = []
    for item in args:
        if item % 2 == 0:
            a.append(item)
    return a


x = myfunc(5, 6, 7, 8)
print(x)
