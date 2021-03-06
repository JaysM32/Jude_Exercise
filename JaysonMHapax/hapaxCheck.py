import re

def wordfrequencies(mylist):
    worddict = {}
    wordlist = []
    for word in mylist:
        worddict.setdefault(word, 0)
        worddict[word] += 1
    for word in worddict:
        if worddict[word] == 1:
            wordlist.append(word)

    return wordlist

def nonreadelim(text):
    new1 = ""
    for letter in text:
        if letter == "-":
            letter = letter.replace("-", " ")
        elif letter == '"':
            letter = letter.replace('"', " ")
        elif letter == ",":
            letter = letter.replace(",", " ")
        elif letter == ".":
            letter = letter.replace(".", " ")
        elif letter == "!":
            letter = letter.replace("!", " ")
        elif letter == "?":
            letter = letter.replace("?", " ")
        new1 = new1 + letter

    return new1

def straightcheck(chosefile):
    hapaxes = []
    list_of_words = re.findall('\w+', chosefile.read().lower())
    freqs = {key: 0 for key in list_of_words}
    for word in list_of_words:
        freqs[word] += 1
    for word in freqs:
        if freqs[word] == 1:
            hapaxes.append(word)

    return hapaxes



if __name__ == '__main__':
    file = open("Little_Helpers.txt", "r")
    checked = straightcheck(file)
    print (checked)
    file.seek(0)
    checked2 = nonreadelim(file.read().lower())
    checked3 = wordfrequencies(checked2.split())
    print (checked3)
