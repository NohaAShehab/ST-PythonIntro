"""

    Word guessing game (hangman)
○
A list of words will be hardcoded in your program, out of
which the interpreter will
○choose 1 random word.
○The user first must input their names
○
Ask the user to guess any alphabet. If the random word
contains that alphabet, it
○will be shown as the output(with correct placement)
○Else the program will ask you to guess another alphabet.
○Give 7 turns maximum to guess the complete word.

 ----->  laptop

"""


def get_indices_of_char(word, char):
    indices = []
    if word.count(char) > 0:
        char_index = 0
        for c in word:
            if c == char:
                indices.append(char_index)
            char_index += 1

    return indices


def hangman():
    words = {"iti", "python", 'django', 'laptop'}
    chosen_word = words.pop()
    no_of_chars = len(chosen_word)
    username = input('please enter your name : ')
    print(f"---- Hello {username} ---------- ")
    print(f"---- You have seven trials , try to guess the word consists of {no_of_chars} chars ")
    guesse_word = []
    for i in range(no_of_chars):
        guesse_word.append("-")
    print(guesse_word)

    for i in range(7):
        inputchar = input(f" try: {i + 1} , please enter char ")
        char_indcies = get_indices_of_char(chosen_word, inputchar)
        for i in char_indcies:
            guesse_word[i] = inputchar

        print(guesse_word)
        if guesse_word.count("-") == 0:
            print("---- Congratulations you Won")
            break

    else:
        print("--- you lost the game -----")


hangman()

####
