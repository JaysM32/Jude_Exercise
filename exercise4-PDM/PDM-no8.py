def longest(list):
    number = []
    for i in list:
        number.append(len(i))
    return max(number)


words = list(input("Enter a list of long words: ").split(","))
print("Longest word length is ", longest(words))