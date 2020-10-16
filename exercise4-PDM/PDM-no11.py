

def check(search):
    number = {}
    for x in search:
        number[x] = 0

    for i in search:
        number[i] += 1
    return number

if __name__ == '__main__':
    searchstring = input("input word: ")
    result = check(searchstring)
    print(result)