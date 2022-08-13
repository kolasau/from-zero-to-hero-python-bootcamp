# immutability
name = 'Sam'
# name[0] = 'P'   ------- this is not possible
last_letters = name[1:]
print('P' + last_letters)
print(name)

x = 'Hello World'
x = x + ', it is beautiful outside!'
print(x)

letter = 'z'
print(letter * 10)

x = 'Hello World'
print(x.upper())
print(x.lower())
print(x.split('l'))

print('Hello World'[-3])
print('tinker'[1:4])