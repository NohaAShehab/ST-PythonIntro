
# info = ["noha", "python", "cairo"]
#
# print(info[0])
"""

    dictionary ::: items ---> key:value pair ---> 
    no index but key ---> 

"""
"1- to define a dictionary"
# myinfo = {}
# mydic = dict([])
#
# """ 2- dictionary items ---> key:value pair ---> key should be string
#     no index but key
#     you can access the element using the key
#     ==> comma seperated key-value pair
# """
# myinfo = {
#     "name" :"Ahmed",
#     "track" : "python",
#     "year": 2022
# }
# "2- access the dictionary elements using the keys ...."
# print(myinfo["name"])
#
# "3- update the dictionary element "
# myinfo["name"] = "Ali"
# print(myinfo)
#
# "4- add new key-value pair to the dictionary "
# myinfo["city"] = "Cairo"
# print(myinfo)
#
# "5- get number of key-value pairs in the dictionary "
# print(len(myinfo))
#
# "5- pop element from the dictionary "
#
# # popped_item=myinfo.pop("city")
# # print(popped_item)
# # print(myinfo)
#
# "6- delete item from the dictionary "
# del myinfo["track"]

"7- get the keys of the dictionary"
mydict = {
    "name":"Ahmed",
    "track":"python",
    "year":2022,
    "courses": ["python", "django"],
    "active": True
}

# keys = mydict.keys()  # this will return with the dict_keys?
# print(keys)  # object dict_keys
# # print(keys[1])
# for k in keys:
#     print(k)
# ## you can cast the dict_keys to a list
# keys = list(keys)
# print(keys[1])

"7- get the values of the dictionary"

vals = mydict.values()
# print(vals) # dict_values
# for v in vals:
#     print(v)

## cast it to the list
vals = list(vals)
# print(vals)

#####################

"8- get the items of the dictionary "

# items = mydict.items()
# print(items)  # dict_items
# items = list(items)
# print(items)

"9- loop over the dictionary "

# for i in mydict:
#     print(i)  # i will represent the keys

# print(mydict)
# print(mydict["name"])
# for i in mydict:
#     print(f" key: {i},|||||||| value {mydict[i]}")  # i will represent the keys
#
# print("----------------")

# #################### print the dictionary info --> keys, values..
# for i in mydict.items():
#     print(i)
# for k , v in mydict.items():
#     print(k)

"10- update the dictionary ....."

basic_info = {
    "name":"noha",
    "address": "cairo"
}

add_info ={
    "email":'nshehab@iti.gov.eg',
    "faculty":"Engineering",
    'name':"Ahmed"
}
basic_info.update(add_info)
print(basic_info)

"11- check existance "

# if "Ahmed" in basic_info:  # if item in dict --> search about this value in the dict_keys
#     print("found")
# else:
#     print("not found")


if "Ahmed" in basic_info.values():  # if item in dict --> search about this value in the dict_keys
    print("found")
else:
    print("not found")



".... clear the dictionary ...."

mydict.clear()  # remove the content of the dictionary
print(mydict)

