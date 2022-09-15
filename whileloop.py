
"""
    we use the while loop to repeat the code multiple times according to condtition

"""

# count = 0
# while count < 5:
#     count +=1
#     print(count)

########## break , continue

# for i in range(10):
#     if i==5:
#         break  # if the condition statisfied =--> break the for loop
#     print(i)



# for i in range(10):
#     if i==5:
#         continue  # if the condition statisfied =--> break the for loop
#     print(i)
#


"""
    write a program to ask user to enter numbers ---> once he write exit  --> print sum of these numbers 
"""
# summ = 0
# inputnumbers = []
# while True:
#     num = input("please enter your num ... ")
#     if num =="exit":
#         break
#     if num.isdigit():
#         inputnumbers.append(int(num))
#         summ += int(num)
#
#     else:
#         print("--------------- please enter valid number or exit to stop ")
#
# print(f" you entered {inputnumbers} and sum of the entered numbers is {summ}")
""" ----- for else -------------"""

# for i in range(10):
#     if i==5:
#         continue
#     print(i)
# else:
#     print("----------- after the loop finished its iterations ---- ")


######################3 pass keyword
"""
    if(){}
    
"""
day = input("please enter day name ")
if day=="Monday":
    pass
else:
    print(day)







