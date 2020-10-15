def translate(text):
    complete = ""
    for i in range(len(text)):
        if text[i] == "a":
            complete = complete + "a"
        elif text[i] == "i":
            complete = complete + "i"
        elif text[i] == "u":
            complete = complete + "u"
        elif text[i] == "e":
            complete = complete + "e"
        elif text[i] == "o":
            complete = complete + "o"
        elif text[i] == " ":
            complete = complete + " "
        else:
            complete = complete + text[i] + "o" + text[i]
    return complete

input1 = input("input text = ")
print("---------------------------")
print("translated text : ", translate(input1))