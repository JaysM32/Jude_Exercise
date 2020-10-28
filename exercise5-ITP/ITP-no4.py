def wordfrequencies(mylist):
    worddict = {}
    for word in mylist:
        worddict.setdefault(word, 0)
        worddict[word] += 1

    return worddict

if __name__ == '__main__':
    wordinput = input("input a list of words seperated with ',' >>>")
    wordlist = list(wordinput.split(","))
    print(wordfrequencies(wordlist))