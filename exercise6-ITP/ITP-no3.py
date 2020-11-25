import re

def sentenceSplit (chosenfile):
    readfile = chosenfile.read()
    split = re.split(r'(?<=[^A-Z].[.?]) +(?=[A-Z])', readfile)
    return split


if __name__ == '__main__':
    file = open("sentsplit.txt", "r")
    sentenceList = sentenceSplit(file)
    for sentence in sentenceList:
        print(sentence)
