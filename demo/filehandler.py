

def createnewUser(userinfo):
    try:
        filobj = open("users.txt","a")
    except Exception as e:
        print("------- error while opening the file -----")
        return False
    else:
        filobj.write(userinfo)
        return True


def getallusers():
    try:
        filobj = open("users.txt","r")
    except Exception as e:
        print("------- error while opening the file -----")
        return False
    else:
        userinfo = filobj.readlines()
        return userinfo