for i in range(0, 11, 2):
    print(i)
print('_________________________________________')
print(list(range(0, 11, 2)))

index_count = 0

for letter in 'abcde':
    print('At index {} the letter is {}'.format(index_count, letter))
    index_count += 1

word = 'abcde'
index_count = 0
for letter in word:
    print(word[index_count])
    index_count += 1

for item in enumerate(word):
    print(item)

print('______________')

mylist1 = [1, 2, 3]
mylist2 = ['a', 'b', 'c']
zip(mylist1, mylist2)

for item in zip(mylist1, mylist2):
    print(item)

d = {'mykey': 123, 'mysecodkey': 456}
p = 123 in d.values()
print(p)

from random import shuffle, randint
mylist3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
shuffle(mylist3)
print(mylist3)

p = randint(0, 100)
print(p)