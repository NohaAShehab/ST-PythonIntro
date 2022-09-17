""" open file for writing
    if you try to open file with mode writing ---
    if the file doesn't exist --> it will try to create it

    if the file exists
        ----> write ((open file for writing starting from the beginning of the file ))
        ---> the old content in the file will be removed

"""
try:
    fileobj = open("info.txt", "w")  ## this varaible holds the file information
except Exception as e:
    print(e)
else:
    print(fileobj)  # TextIOWrapper
    # text = input("please enter message ")
    # fileobj.write(f"{text}\n")
    # fileobj.write("Python is simple \n")
    #
    # fileobj.write("=---------------------------\n")
    fileobj.writelines(["Ahmed\n", "Ali\n", 'Omar\n', "Maraim\n"])
    fileobj.close()