myset = set()
myset.add(1)
print(myset)
myset.add(2)
print(myset)
myset.add(2)  # let's add 2 again and see what's going on
print(myset)  # it means that sets can hold only unique objects

mylist = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4]
q = set(mylist)
print(q)

print(set('Mississippi'))