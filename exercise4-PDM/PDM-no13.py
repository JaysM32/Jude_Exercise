def changeform(word):

    newword = ""
    consonant = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y",
                     "z"]
    vowel = ["a", "e", "i", "o", "u"]
    if word == "be":
        newword = word + "ing"
    elif word[-2::] == "ee":
        newword = word + "ing"
    elif word[-2::] == "ie":
        newword = word[:-2].split()
        newword = newword[0] + "ying"
    elif word[-1] == "e":
        newword = word[:-1].split()
        newword = newword[0] + "ing"
    elif word[-1] in consonant:
        if word[:-2] in consonant:
            if word[-2:-1] in vowel:
                newword = word + str(word[-1]) + "ing"
    else:
        newword = newword + "ing"
    return newword


changeword = input(" input verb to be changed = ")
print(changeform(changeword))