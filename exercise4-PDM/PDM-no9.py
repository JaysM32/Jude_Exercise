def longest(list, x):
    number = []
    for i in list:
        if len(i) > x:
            number.append(i)
        else:
            pass
    return number

if __name__ == '__main__':
    words = list(input("Input a list of words: ").split(","))
    searchval = int(input("search words longer than: "))
    print("words longer than ",searchval, "are", longest(words, searchval))