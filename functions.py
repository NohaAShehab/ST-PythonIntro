# def helloworld():
#     print("Hello world")
#
#
# helloworld()
#
# helloworld()
#
# helloworld()


#############################################
# def askfornumber():
#     while True:
#         num = input("please enter number ")
#         if num.isdigit():
#             num= int(num)
#             return num
#
#
# def calculator():
#     num1 = askfornumber()
#     num2 = askfornumber()
#     res = num1+num2
#     print(res)
#
# calculator()
##################################
# def askforname():
#     while True:
#         name = input("Please enter your name : ")
#         if name.isalpha():
#             print(name)
#             return name
#
#
# username = askforname()
#########################################33

# def getfullname():
#     firstname= input("please enter firstname ")
#     lastname = input("please enter lastname ")
#     fullname = f"{firstname} {lastname}"
#     print(fullname)
#     print("----------------------------------")
#     return   # return of the function None
#
# x= getfullname()
# print(x)
# getfullname()
# getfullname()

################################3
# def getfullname():
#     firstname= input("please enter firstname ")
#     lastname = input("please enter lastname ")
#     fullname = f"{firstname} {lastname}"
#     print(fullname)
#     print("----------------------------------")
#     return fullname  # return of the function None
#
# x= getfullname()
# print(x)
# getfullname()
# getfullname()


############################################3

# def saywelcome(name):
#     print(f"Welcome {name}")
#
# saywelcome("Ahmed")
#
# saywelcome("Ali")

#################################################################
def askfornum(message):
    while True:
        num = input(message)
        if num.isdigit():
            return int(num)
        print("----please enter valid value for it")


def askforoperation():
    while True:
        op = input("please enter operation +, -, *, /")
        if op in ["+","-","*","/"]:
            return op
        print("please enter valid operation ............")


def calculator():
    num1 = askfornum("please enter num1 ..... : ")
    num2  = askfornum("please enter num2 .... : ")
    op = askforoperation()
    print(num1, num2, op)


calculator()

















