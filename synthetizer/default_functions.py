""" Basic Functions in a Linter """

"""
    A word is a string with this alphabet:
        [a-ZA-Z_0-9]
"""

def is_a_lower_char(c):
    """
        Receives a char and return true if the char is a lower char
    """

    return ord(c) >= 97 and ord(c) <= 122


def is_an_upper_char(c):
    """
        Receives a char and return true if the char is a upper char
    """

    return ord(c) >= 65 and ord(c) <= 90


def is_an_underscore(c):
    """
        Receives a char and return true if the char is an underscore
    """

    return c == '_'


def all_upper(word):
    """
        Receives a word and returns the same word but with all its characters in Upper
    """

    return word.upper()


def all_lower(word):
    """
        Receives a word and returns the same word but with all its characters in Lower
    """

    return word.lower()

def first_upper(word):
    """
        Receives a word and returns the same word but with its first character in Upper
    """

    return word[0].upper() + word[1:]

def first_lower(word):
    """
        Receives a word and returns the same word but with its first character in Lower
    """

    return word[0].lower() + word[1:]

def to_upper_case(word):
    """
        Receives a word and returns the same word but in Upper case
    """

    new_word = ""
    
    i = 0
    while i < (len(word)):
        if is_an_underscore(word[i]):
            while i < len(word) and is_an_underscore(word[i]):
                i += 1
            if i == len(word):
                break
            new_word += word[i].upper()
        else:
            new_word += word[i]
        i += 1

    return new_word

def to_underscore_case(word):
    """
        Receives a word and returns the same word but in undescore case
    """

    new_word = ""
    
    i = 0
    while i < (len(word)):
        if is_an_upper_char(word[i]):
            new_word += '_'
            new_word += word[i].lower()
        else:
            new_word += word[i]
        i += 1

    return new_word

def remove_underscores(word):
    """
        Receives a word and returns the same word but without underscores
    """

    word_size = len(word)
    new_word = ""
    for i in range(word_size):
        if not is_an_underscore(word[i]):
            new_word += word[i]

    return new_word

def insert_first_underscore(word):
    """
        Receives a word and returns the same word with an initial underscore.
    """

    return "_" + word

def insert_last_underscore(word):
    """
        Receives a word and returns the same word with an ending underscore.
    """

    return word + "_"
