def convert(list):
    number = []
    for i in list:
        number.append(len(i))
    return number

if __name__ == '__main__':
    words = list(input("Enter words: ").split(","))
    print(convert(words))