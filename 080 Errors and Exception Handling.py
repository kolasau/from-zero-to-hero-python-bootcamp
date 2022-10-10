# def add(n1, n2):
#     print(n1 + n2)
#
#
# add(20, 30)
#
# number1 = 10
# number2 = input("Please provide a number: ")

# try:
#     f = open('testfile', 'w')
#     f.write("Write a test line")
# except:
#     print("all other exceptions")
# # except TypeError:
# #     print("There was a TypeError")
# # except OSError:
# #     print("Hey you have an OS Error")
# finally:
#     print("I always run")


def ask_for_int():
    while True:
        try:
            result = int(input("Please provide number: "))
        except:
            print("Whoops! That's not a number :(")
            continue
        else:
            print("Yes thank you!")
            break
        finally:
            print("Always run")


ask_for_int()
