"1- to define a list "
# l = []  # empty list ---> empty list ---> is considered to be falsy
# myl = list([])
#
# "2- list can hold different values from different datatypes "
# l = ["Ahmed", 2022, True, 3.14, "python", 4 + 6j, "python", "python"]
#
# '3- you can access elements of the list using index'
# print(l[3])
# l[3] = 'updated'
#
# "4- get the number of the elements in the list "
# # print(len(l))
#
#
# "5- count no of occurence of the element in the list"
# # print(l.count("python"))
#
# "6- get the index of the element from list"
# print(l.index('python'))  # get the first occurence of the element
#
# "7- append element to the list "
# l.append("new item")  # add the element to the end of the list
#
# "8- insert element at certain position"
# l.insert(4, "inserted value ")
#
# "9-pop element from the list --> remvoe element from the end of the list "
# popped_item= l.pop()
#
# '10- remove item from the list '
# l.remove("python")  # remove the first occurrence
#
# "11- pop item at index ? "
# item  =l.pop(5)

# "12- concat 2 list"
# courses1 = ["python", "databases", 'django']
# courses2 = ['git', "cloud", "python"]

## merge 2 lists in one list

# allcourses = courses1 + courses2
# print(allcourses)
# print(len(allcourses))
#
# "13- extend a list"
# courses1 = ["python", "databases", 'django']
# courses2 = ['git', "cloud", "python"]
# courses1.extend(courses2)
# print(courses1)
# print(courses2)
# courses1.remove("python")
# print(courses1)

"14- loop over the list using for in "

# courses1 = ["python", "databases", 'django']
#
# for item in courses1:
#     print(item)
#

"15- check existance of the element "
courses = ["python", "databases", 'django']
if "python" in courses:  # in operator search about value iterable
    print("found")
else:
    print("not found ")

"lists are mutable datatype ---> can be changed in the run time "

"16- sort for the list items ---> You must make sure the list items from the same type"
names = ["Ali", "Seif", 'Arwa', 'Ahmed', "Abdulrahman", "AbdElAleem", "Kareem"]
# print(names)
# # names.sort()  # sort items in the list ascending
# # print(names)
# # descendeing
# names.sort(reverse=True)
# print(names)
"16- reverse list elements"
courses  = ["python", 'Django', 'OOP', 'Flask', 2022, 14]
print(courses)
courses.reverse()
print(courses)

myl = [5,67,"Ali", ["test", "python"]]

"18- min and max with lists ---> list elements must be from the same type "
l = [4,5,6,88, 999, 1000]
print(min(l))
print(max(l))
print(sum(l))