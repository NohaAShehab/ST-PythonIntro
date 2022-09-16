
# reason

"""
    any variable defined in the python file --- > this variable is accessible anywhere in the script
    --> accessible for read  <--- even inside a function

"""
# coursename = 'python'  # this variable has global scope ---->
#
#
# def sayhello():
#     print("------------------------------------------------------")
#     print(f"value of the coursename = {coursename}")
#     print("Hello world")
#     print("------------------------------------------------------")
#
#
#
#
# print(coursename)
#
# sayhello()
#############################################################################################
# """
#     variable defined in a function ---> can be accessed only inside the function
#     with scope ---> local scope
# """
# track = 'open source '  #### global scope
#
# def modifytrack():
#     print("-------------------------function started ------------------------------------")
#     track = 'system development'  # create new local variable for the function
#     print(f"from the function track = {track}")
#     print("-------------------------------------------------------------\n")
#
#
# modifytrack()
#
# print(track)
# print("--------------------------")


#############################################################################33
""" make function that changes the global variable"""

name = 'noha'

def changeglobalname():
    global name ###please don't create new variable name ---> and use the global one
    name = 'Noha shehab'
    print(f"---- {name}---------")


print(f" before calling the function name = {name}")
changeglobalname()

print(f"=========== {name}============")












