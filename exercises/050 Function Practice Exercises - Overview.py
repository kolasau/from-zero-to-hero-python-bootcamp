def myfunc(a, b):
    if a and b % 2 == 0:
        return min(a, b)
    else:
        return max(a, b)


x = myfunc(2, 4)
print(x)


def two_word_string(text):
    wordlist = text.lower().split()
    return wordlist[0][0] == wordlist[1][0]


y = two_word_string('lana Lakka')
print(y)
z = two_word_string('Kega kaga')
print(z)


def makes_twenty(a, b):
    return a + b == 20 or a == 20 or b == 20


r = makes_twenty(20, 10)
g = makes_twenty(12, 8)
h = makes_twenty(2, 32)
print(r, g, h)