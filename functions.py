
# def sumnum(num1, num2):
#     res = num1 + num2
#     return  res
#
#
# m = sumnum(5,6)
# print(m)
#
# n = sumnum(5)

# ############# python support default arguments
# def sumnum(num1=10, num2=10):
#     print(f"num1={num1}, num2={num2}")
#     res = num1 + num2
#     return  res
#
#
# m = sumnum(5,6)
# print(m)
# print("--------------------------")
# n = sumnum(88)
# print(n)
# print("--------------------------")
# s = sumnum()
# print(s)

# ##########################################3


# def greeting(message="Hello world", name=""):
#     print(f"{message}, Nice to meet you {name}")
#
#
# greeting()
#
# greeting(message='How are you, ')
#
# greeting('How are you', "Ahmed")
#
# #
# l = [4, 5, 67, 8, 9999, 1, 3]
# l.sort(reverse=True)
# print(l)
#
# print('noha', end="$")
# print("shehab")

##############################################
# ## function accept variable number of arguments -

# print()
#
# print("name")
#
# print("iti", 'python', 'test')


# def getWords(*args):  # * zero or parameter
#     print(type(args))
#     print(args)
#     print("-----------------------")
#
#
# getWords()
# getWords("iti", "Ahmed", "ali")
#
# getWords("noha")
# getWords("omar", "Mariam", "Arwa", "test", 88, 888, True)

################################33
""" write a function that allow the user to enter any number of digits and print their multiplication"""

#
# def mulnums(*nums):
#     print(nums)
#     mul=1
#     for n in nums:
#         mul *=n
#     print(f"mul of {nums} = {mul}")
#     print('--------------------------')
#
# mulnums(1)
# mulnums(4,56,6)
# mulnums(7,89,7)
#
###################################################################

temp = "I love {programminglang},I study at {uni}, {year} "
print(temp.format(programminglang='python', uni='MUST', year=2022))

""" 
    I need to create a function that accepts unknow number keyword args
"""


def introduceYourself(** kwargs):  # {
    print(kwargs)
    print("------------------------------")

introduceYourself()
introduceYourself(name='noha') # {'name':'noha'}
introduceYourself(fname='noha', lname='shahab') # {'fname':'noha'}
introduceYourself(lastname='Ahmed')
introduceYourself(username='user' ,faculty='engineering', lives_in='cairo')



def test(*args):
    print(args)


test()
test(34 ,5 ,56)
test("iti", "test")
