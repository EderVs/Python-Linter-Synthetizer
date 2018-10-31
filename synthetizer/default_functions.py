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

