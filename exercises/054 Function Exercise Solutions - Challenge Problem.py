def spy_game(nums):

    code = [0, 0, 7, 'x']

    for num in nums:
        if num == code[0]:
            code.pop(0)
    return len(code) == 1


x1 = spy_game([1, 2, 4, 0, 0, 7, 5])
x2 = spy_game([1 ,0 ,2 ,4 ,0 ,5 ,7])
x3 = spy_game([1 ,7 ,2 ,0 ,4 ,5 ,0])
print(x1, x2, x3)


def count_primes(num):
    #  Check for 0 or 1
    if num < 2:
        return 0
    #  2 or greater

    #  Store prime numbers
    primes = [2]
    #  Counter going up to the input num
    x = 3
    #  x is going through every number up to input num
    while x <= num:
        #  Check if x is prime
        for y in range(3,x,2):
            if x % y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)


x = count_primes(100)
print(x)

