import time
def askforstring(message):
    userinput = input(message)
    if userinput.isalpha():
        return userinput

    print("------------ invalid input ----- ")
    return askforstring(message)

def askforemail(message):
    email = input(message)
    import re
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if (re.fullmatch(regex, email)):
        return email

    print("------- please enter valid email ----")
    return askforemail(message)


def generateid():
    id= round(time.time())
    return id