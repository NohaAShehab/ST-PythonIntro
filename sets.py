""" sets is one of the built-in datatypes
    doesn't allow duplication in the values
    --> has no index
    --> items are unordered
"""
#
# "1- to define a set"
# s = {"Ahmed", "iti", "Cairo", 10}
# print(s)
# print(s)
#
# "2- get no of elements in the set "
# print(len(s))

"3- sets don't allow duplication ,,, "
s  = {"python","python", "iti", "Ahmed", 2022, "python"}
print(s)

"4- you can add value to the set "
s.add("myvalue")
# print(s)

"5- pop value from the set"
# popped_item  =s.pop()
# print(popped_item)
# print(s)

"6- remove certain value from the set"
# s.remove("iti")
# print(s)

"7- check item existence "
if 'iti' in s:
    print("found")
else:
    print("not found")

"8- loop over the set"
for i in s:
    print(i)

"convert set to tuple or list"

courses = ["python", "iti","python", "python", "django", "postgres"]
print(courses)
courses = set(courses)
print(courses)
courses.add("pythonnnnn")
# courses = list(courses)
print(courses)
