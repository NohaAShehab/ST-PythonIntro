"""

    registration system for students

    ====>  create system --> information
        student --> id
            name , email

    menu:
        register or list all students

"""



from registerationmodule import registerNewUser
from displayusers import displayallusers
def mainmenu():
    choice = input("please enter r for register, l for listing all users , e for exit")
    if choice=="l":
        displayallusers()
        return mainmenu()
    elif choice =="r":
        added =registerNewUser()
        return mainmenu()
    elif choice=='e':
        print("-------- bye ------------")
    else:
        print("-------------- Invalid choice ---------------- ")
        return mainmenu()


mainmenu()