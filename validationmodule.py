
# print("------------------- this is the validation module --------------------")
def askforInt(message):
    while True:
        num = input(message)
        if num.isdigit():
            return int(num)



# num = askforInt("please enter year : ")
# print(num)


def cleanstr(yourstring):
    yourstring = yourstring.strip("\n ")
    return yourstring


def sayHello(username):
    print(f"Hello {username}")


def sayWelcome(username, message="Nice to meet you"):
    print(f"welcome {username}... {message}..")
    return


def sumnumm(num1, num2):
    summ = num1 + num2
    print(f" sum of {num1} + {num2}= {summ}")
    return summ




def fullname(fname, lname):
    return f"{fname} {lname}."

