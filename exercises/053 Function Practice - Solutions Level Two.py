def has_33(nums):
    for i in range(0, len(nums) - 1):
        if nums[i:i + 2] == [3, 3]:  # if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False


x1 = has_33([1, 3, 3])
x2 = has_33([1, 3, 1, 3])
x3 = has_33([3, 1, 3])
print(x1, x2, x3)


def paper_doll(text):
    result = ''
    for char in text:
        result += char * 3
    return result


x1 = paper_doll('Mississippi')
x2 = paper_doll(('Hello'))
print(x1, x2)


def blackjack(a, b, c):
    if sum([a, b, c]) <= 21:
        return sum([a, b, c])
    elif 11 in [a, b, c] and sum([a, b, c]) > 21:
        return sum([a, b, c]) - 10
    elif sum([a, b, c]) > 21:
        return 'BUST'


x1 = blackjack(5, 6, 11)
x2 = blackjack(9, 9, 9)
x3 = blackjack(9, 9, 11)
print(x1, x2, x3)


def summer_69(arr):
    total = 0
    add = True

    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total


x1 = summer_69([1, 3, 5])
x2 = summer_69([4, 5, 6, 7, 8, 9])
x3 = summer_69([5, 6, 7, 8, 9, 12])
print(x1, x2, x3)
