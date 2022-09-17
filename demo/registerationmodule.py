from inputsmodule import  askforstring , askforemail, generateid
from filehandler import createnewUser
def registerNewUser():
    print("register new user .... ")
    ## ask him about firstname ,  lastname, email
    firstname= askforstring("Please enter firstname: ")
    lastname = askforstring("Please enter lastname : ")
    email = askforemail('Please enter your email : ')
    id = generateid()
    print(id, firstname, lastname, email)
    """
        one line for each user
        id:firstname:lastname:email
    """
    userinfo =f"{id}:{firstname}:{lastname}:{email}\n"
    created = createnewUser(userinfo)
    if created:
        print("--- user added successfully ")
        return created




