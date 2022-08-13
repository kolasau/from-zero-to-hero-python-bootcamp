from random import shuffle

example = [1, 2, 3, 4, 5, 6, 7]
shuffle(example)
print(example)


def shuffle_list(mylist):
    shuffle(mylist)
    return mylist


result = shuffle_list(example)
print(result)

# where is 'O' ? game
mylist = [' ', 'O', ' ']
where_is_O = shuffle_list(mylist)
print(where_is_O)
