def convert(list):
    number = []
    for i in list:
        number.append(len(i))
    return number


words = list(input("Enter words: ").split(","))
print(convert(words))