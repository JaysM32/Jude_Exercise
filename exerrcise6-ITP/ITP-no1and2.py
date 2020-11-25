import re, string

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
        if letter in string.punctuation:
            letter.replace(letter," ")
        new1 = new1 + letter

    return new1

def straightcheck(chosenfile):
    hapaxes = []
    list_of_words = re.findall('\w+', chosenfile.read().lower())
    freqs = {key: 0 for key in list_of_words}
    for word in list_of_words:
        freqs[word] += 1
    for word in freqs:
        if freqs[word] == 1:
            hapaxes.append(word)

    return hapaxes

def getAvg (chosenfile):
    totalLen = 0
    wordCount = 0
    listWords = nonreadelim(chosenfile)
    sortWords = listWords.split()
    for word in sortWords :
        totalLen = totalLen + len(word)
        wordCount = wordCount + 1
    avgLen = totalLen / wordCount

    return avgLen

if __name__ == '__main__':
    file = open("Little_Helpers.txt", "r")
    checked = straightcheck(file)
    print(checked)
    file.seek(0)
    checked2 = nonreadelim(file.read().lower())
    checked2.split()
    checked3 = wordfrequencies(checked2.split())
    checked4 = getAvg(checked2)
    print(checked3)
    print(checked4)