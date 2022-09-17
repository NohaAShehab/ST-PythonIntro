""" open file for appending data
    if you try to open file with mode append ---
    if the file doesn't exist --> it will try to create it

    if the file exists
        ----> write ((open file for writing starting from the end of the file ))
        ---> keep the  old content

"""
try:
    fileobj = open("info.txt", "a")  ## this varaible holds the file information
except Exception as e:
    print(e)
else:
    print(fileobj)  # TextIOWrapper
    fileobj.write("Python is simple, you will enjoy it ----- \n")
    # fileobj.writelines(["Ahmed\n", "Ali\n", 'Omar\n', "Maraim\n"])
    fileobj.close()