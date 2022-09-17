

"""

        calculator
        num1, num2 ----> divide by zero
        num2 ? ----> error ===> raise the exception

        num/num2 ===> zero division

"""

def divnums(num1, num2):
    if num2==0:
        raise Exception("sorry we cannot divid num1 by zero .....")
    print(f"num1 = {num1}, num2 = {num2}")
    res = num1/num2
    print(f"res = {res}")
    return res


r = divnums(10, 0)








