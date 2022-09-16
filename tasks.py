

"""Write a function that takes a string and prints the
longest alphabetical ordered substring occurred For example, if
the string is 'abdulrahman' then the output is: Longest substring in
alphabetical order is: abdu"""

"""
    abdfjkmsr
    hjklo
    iu
"""

def logestsubstr():
    inputstr = input("please enter string ... ")
    longest_str = ""
    substrings = []
    for char in inputstr:
        # the beginning of the program
        if len(longest_str) == 0:
            longest_str = char
        else:
            if char > longest_str[-1]:
                longest_str +=char
            else:
                substrings.append(longest_str)
                longest_str = char

    else:
        print(longest_str)
        substrings.append(longest_str)
        print(substrings)

    longest = ""
    for word in substrings:
        if len(word)> len(longest):
            longest =word


    print(f"the longest word is {longest}")
logestsubstr()






