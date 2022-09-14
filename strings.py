
"<-----format string ----> "
#
# message = "Nice to meet you {0},{1}."
# # print(message.format("Ahmed", "I am happy to work without"))
# # print(message.format("Sara", "Python is easy"))
# "to ask the user to enter his name"
# username = input("please enter your name ")
# print(message.format(username, "python is easy"))
#
# print(message.format("test", username))

#### string
# message = "Nice to meet you {username}, {yourmessage}"
# stdname= input("please enter your name : ")
# msg  = input("please leave your message ")
# print(message.format(username=stdname, yourmessage=msg))
#####################################
"f- format string"

# username = input("please enter your name : ")
# password  = input("please enter your password : ")
# # print("You entered "+ username + password)
# myinput = f"you entered username= {username}, password = {password}"
# print(myinput)

##################33 strip string
"""
strip function remove the spaces from the beginning and the end of the string 
"""
# mymessge = "                  Hello, Nice to work with you all                     "
# print(len(mymessge))
#
# # print(mymessge.isalpha())  # false
#
# ############### strip
#
# mymessge = mymessge.strip()
# print(mymessge)
# print(len(mymessge))

#####################33
# msg = '$ this is my sencod day with Python                            $'
#
# print(msg.strip("n$ t"))
#
# for i in msg:
#     msg = msg.replace(" ","")
#
# print(msg)
#########################
sentence = "  @  Welcome to day02 python         @ "
# print(sentence.lstrip())

# sentence = sentence.lstrip()

sentence = sentence.rstrip(" @")









