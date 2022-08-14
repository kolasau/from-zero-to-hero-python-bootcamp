def old_macdonald(name):
    name1 = name[0]
    name2 = name[1:3]
    name3 = name[3]
    name4 = name[4:]
    return name1.upper() + name2 + name3.upper() + name4


x = old_macdonald('macdonald')
print(x)


def old_macdonald2(name):
    first_half = name[:3]
    second_half = name[3:]
    return first_half.capitalize() + second_half.capitalize()


y = old_macdonald2('macdonald')
print(y)


def master_yoda(text):
    yoda = text.split()
    yoda.reverse()
    return ' '.join(yoda)


k = master_yoda('I am home')
print(k)
p = master_yoda('We are ready')
print(p)


def almost_there(n):
    return (abs(100-n) <= 10) or (abs(200-n) <= 10)


x = almost_there(90)
y = almost_there(104)
z = almost_there(150)
p = almost_there(209)
print(x, y, z, p)


print(abs(100-2))