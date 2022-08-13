# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#  example 1
# for i in list1:
#     print(i)
# #  example 2
# for i in list1:
#     print('Hello')
# example 3
# for i in list1:
#     #  Check for odd numbers
#     if i % 2 != 0:
#         print(f"Odd number: {i}")
#     else:
#         print(f"Even number: {i}")
#
# #  makes a list sum
# list_sum = 0
# for i in list1:
#     list_sum = list_sum + i
#     print(list_sum)
# print(f"Result: {list_sum}")

#  tup
tup = (1, 2, 3)
for item in tup:
    print(item)
print('_______________________________________________________')
#  tuple unpacking 1
mylist = [(1, 2), (3, 4), (5, 6), (7, 8)]
for a, b in mylist:
    print(b)

print('_______________________________________________________')

#  tuple unpacking 2
mylist = [(1, 2, 3), (5, 6, 7), (8, 9, 10)]
for a, b, c in mylist:
    print(c)

print('_______________________________________________________')

d = {'k1': 1, 'k2': 2, 'k3': 3, 'k4': 4}
for item in d.items():
    print(item)
for item in d.values():
    print(item)
for key, value in d:
    print(key)
    print(value)