def myfunc(x, y, z):
    if z == True:
        return x
    else:
        return y


x = myfunc('Hello', 'Goodbye', False)
print(x)