my_nums = [1, 2, 3, 4, 5]


def square(num):
    return num**2


for item in map(square, my_nums):
    print(item)


print(map(square, my_nums))


def splicer(mystring):
    if len(mystring) % 2 == 0:
        return 'EVEN'
    else:
        return mystring[0]


names = ['Andy', 'Eve', 'Sally']
print(list(map(splicer, names)))