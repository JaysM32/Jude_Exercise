
def checker(lastletter, list):
    for index, item in enumerate(list):
        if item.startswith(lastletter):
            return index
    return False


def namegame(chosenfile):
    givenlist = chosenfile.split()
    longerlist , currentlist = [], []

    for name in givenlist:
        current = name
        currentlist.append(current)

        checklist = givenlist
        checklist.pop(checklist.index(current))

        checkindex = checker(current[-1],checklist)

        while checkindex is not False:
            current = checklist[checkindex]
            currentlist.append(current)
            checklist.pop(checkindex)
            checkindex = checker(current[-1], checklist)

        if len(currentlist)>len(longerlist):
            longerlist = currentlist

        currentlist = []

    return longerlist


if __name__ == '__main__':
    file = open("pokemon.txt", "r")
    fileRead = file.read()
    print(namegame(fileRead))
