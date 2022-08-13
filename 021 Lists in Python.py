my_list = [1 , 2, 3]
print(len(my_list))
print(my_list[0])
another_list = [4, 5, 6]

new_list = my_list + another_list
print(new_list)
print(my_list)
new_list[5] = 'six'
print(new_list)
new_list.append('hello')
print(new_list)
new_list.pop()
print(new_list)
popped_item = new_list.pop(0)
print(popped_item)
print(new_list)

new_list = ['a', 'for ', 'wer', 'po', 'af']
numlist = [1, 23, 545, 1231, 912, 2]
print(new_list.sort())
print(new_list)
print(numlist.reverse())
print(numlist)
print('-------------------')
e = [[[1, 'thank you', 23.109824], [1243, 'sdoif', 9.123]], [['hi', 5555, 1.1], [456, 7777, 0.2342343242]]]
print(e[1][1][1])
