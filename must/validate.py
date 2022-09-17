

def askforstr():
    while True:
        mystr= input("please enter valid string .. .")
        if mystr.isalpha():
            return mystr

        print("----- please choose valid string ---- ")