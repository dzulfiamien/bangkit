import re

def print_hello():
    print("hello")

def filter_only_word(word):
    if re.match("^[a-z]{2,}$", word):
        return word
    else:
        return None