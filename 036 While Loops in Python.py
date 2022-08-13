x = 50
while x < 5:
    print(f'The current value of x is {x}')
    x += 1
else:
    print('X is not LESS then FIVE')

#  BREAK CONTINUE, PASS
x = [1, 2, 3]

for i in x:
    pass

#  for example, I don't want to print 'a' letter
mystring = 'Sammy'

for letter in mystring:
    if letter == 'a':
        continue
    print(letter)
print('BREAKBREAKBREAKBREAKBREAKBREAKBREAKBREAKBREAK')
for letter in mystring:
    if letter == 'a':
        break
    print(letter)

x = 0
while x < 5:
    if x == 2:
        break
    print(x)
    x += 1
