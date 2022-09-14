"tuple is immutable datatupe... cannot be changed after creation "

# "1- to define a tuple "
# t = ()
# myt = tuple([])  #empty tuples
#
# "2- tuple can hold different values from different datatypes "
# t = ("Ahmed", 2022, True, 3.14, "python", 4 + 6j,
#      "python", "python")
#
# '3- you can access elements of the tuple using index'
# print(t[3])
# "4- get the number of the elements in the tuple "
# # print(len(t))
#
# "5- count no of occurence of the element in the tuple"
# # print(t.count("python"))
#
# "6- get the index of the element from tuple"
# print(t.index('python'))
#
#
# "7- concat 2 tuples"
# courses1 = ("python", "databases", 'django')
# courses2 = ('git', "cloud", "python")
#
# courses = courses1 + courses2
# print(courses, type(courses))
#
# "8- loop over the tuple"
# for i in courses:
#     print(f"item = {i}")
#
# "9- check existance of the element "
# if "python" in courses:  # in operator search about value iterable
#     print("found")
# else:
#     print("not found ")
#
#
# "10- min and max with lists ---> list elements must be from the same type "
# t = (4,5,6,88, 999, 1000)
# print(min(t))
# print(max(t))
# print(sum(t))


"11- create tuple of one item"
# tt = ("python")
# print(type(tt))
tt = (20,)
print(type(tt))

"12- coversion between list and tuple"

myt = ("Ahmed" , "Ali", "omar") # tuple
myt = list(myt)

l = ["iti", 3444,66,True, ["iti", "python"], False]
l = tuple(l)