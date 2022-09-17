

"""
        dealing with files

        ----> read (( read file content ))

        ----> write ((open file for writing starting from the beginning of the file ))

        ---> append ((open file for writing starting from the end of the file ))
        ---------------------------------------------------------------------

        open(filename, mode for opening)
        mode ---> r , w , a

        --------------- operation
        -- read()
        --> write()
        -------------- Don't forget to close the file
        close()

"""
"""--------------- 1- read the file ----------------"""

# try:
#     fileobj = open("mycv.txt", "r")  ## this varaible holds the file information
# except Exception as e:
#     print(e)
# else:
#     print(fileobj)  # TextIOWrapper
#     # to read the content of the file
#     filedata = fileobj.read()  # read file content into one string
#     print(filedata)
#
#     fileobj.close()


######################################################
""" read file content line by line """

try:
    fileobj = open("mycv.txt", "r")  ## this varaible holds the file information
except Exception as e:
    print(e)
else:
    print(fileobj)  # TextIOWrapper
    # to read the content of the file
    filedata = fileobj.readlines()  # read file content into list each element represent line in the file
    print(filedata)

    fileobj.close()





















