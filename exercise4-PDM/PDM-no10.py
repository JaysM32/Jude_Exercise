import string


def check(text):
    for i in string.ascii_lowercase:
        if i not in text.lower():
            return False
    return True


searchtext = input("Enter sentence to check if it is a pangram: ")
print("sentence is pangram: ", check(searchtext))