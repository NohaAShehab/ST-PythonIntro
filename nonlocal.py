
"""

    you can create a function inside another function ====
"""

#
# def addnums(num1, num2):
#     res = num1 + num2
#
#     def printRes():
#         print("---- Hello from the inner function ")
#     printRes()
#
#     return res
#
# x = addnums(20, 20)


#####################################################33

#
# def addnums(num1, num2):
#     res = num1 + num2  # local variable for the function addnums --->
#     # accessable for reading anywhere in the function
#
#     def changeRes():
#         res = 100  # this is a local variable for the changeRes function
#         print(f"---- Hello from the inner function res = {res} ")
#     changeRes()
#
#     print(res)
#     # def printRes():
#     #     print(f"---- Hello from the inner function res = {res} ")
#     # printRes()
#
#     return res
#
# x = addnums(20, 20)



###############################################3



# def addnums(num1, num2):
#     res = num1 + num2  # local variable for the function addnums --->
#     # accessable for reading anywhere in the function
#
#     def changeRes():
#         nonlocal res
#         res = 100
#         print(f"---- Hello from the inner function res = {res} ")
#     changeRes()
#
#     print(res)
#
#     return res
#
# x = addnums(20, 20)
#####################################################3




def addnums(num1, num2):
    res = num1 + num2  # local variable for the function addnums --->
    # accessable for reading anywhere in the function

    def changeRes():
        nonlocal res
        res = 1000
        def test():
            nonlocal res
            res = 'iti'
            print("-------- test scope ")
        test()
    changeRes()

    print(res)

    return res

x = addnums(20, 20)













