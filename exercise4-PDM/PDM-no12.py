def changeform(word):
    if word[-1] == "y":
        new = word[:-1].split()
        new = new[0] + "ies"
    elif (word[-1] == "o" or "s" or "x" or "z"):
        new = word + "es"
    elif word[-2::] == "ch":
        new = word + "es"
    elif word[-2::] == "sh":
        new = word + "es"
    else:
        new = word + "s"

    return new

if __name__ == '__main__':
    changeword = input("input the verb to be changed = ")
    print("new form is ", changeform(changeword))
