
from  filehandler import getallusers
def displayallusers():
    print("------------- Users list -------------------")
    users = getallusers()
    for user in users:
        print(user)
