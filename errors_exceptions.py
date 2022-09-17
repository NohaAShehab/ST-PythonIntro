"""
                                        Errors

        Syntax errors                 runtime errors  (Exception)          logical error



sytnax ---> you didn't the syntax standard  ----> The application will not run ?

logical error -===> error in your logic

exception ---> unexpected action cause the script to stop execution...
"""

print("---------- hello world -----------------")

print("--------Python-------------------")

def sumnum(num1, num2):
       print("this function is to get the summation of 2 number")
       return num1*num2

#
print(sumnum(2,2))
print(sumnum(4,5))

#
# print(name)
#
# print("----------------------------------------")

# def divnums(num1, num2):
#        return num1/num2
#
# r = divnums(10,0)
# print(r)


##########################
# def divnums(num1, num2):
#        return num1/num2
# try:
#        r = divnums(10, 0)
# except:
#        print("There a problem with division operation ... ")

########################3



# def divnums(num1, num2):
#        return num1/num2
# try:
#        r = divnums(10, 0)
# except Exception as e:
#        print(f"There a problem with division operation ... {e}")

###############################################

def divnums(num1, num2):
       return num1/num2
try:
       r = divnums(10,0)
except Exception as e:
       print(f"There a problem with division operation ... {e}")

finally:
       print("--------------------- end the of danger ----------------------")













