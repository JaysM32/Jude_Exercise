def ROT13(sentence):
    key = {'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f': 's', 'g': 't', 'h': 'u', 'i': 'v', 'j': 'w', 'k': 'x',
           'l': 'y', 'm': 'z', 'n': 'a', 'o': 'b', 'p': 'c', 'q': 'd', 'r': 'e', 's': 'f', 't': 'g', 'u': 'h', 'v': 'i',
           'w': 'j', 'x': 'k', 'y': 'l', 'z': 'm', 'A': 'N', 'B': 'O', 'C': 'P', 'D': 'Q', 'E': 'R', 'F': 'S', 'G': 'T',
           'H': 'U', 'I': 'V', 'J': 'W', 'K': 'X', 'L': 'Y', 'M': 'Z', 'N': 'A', 'O': 'B', 'P': 'C', 'Q': 'D', 'R': 'E',
           'S': 'F', 'T': 'G', 'U': 'H', 'V': 'I', 'W': 'J', 'X': 'K', 'Y': 'L', 'Z': 'M'}
    changed = ""
    for letter1 in sentence:
        if letter1 == " ":
            changed += " "
        elif letter1 == "?":
            changed += "?"
        elif letter1 == "!":
            changed += "!"
        else:
            for checker in key:
                if letter1 == checker:
                    changed = changed + key[letter1]


    return changed

if __name__ == '__main__':
    text = 'Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!'
    decoded = ROT13(text)
    encode = ROT13(decoded)
    print ("text = ", text)
    print ("decode = ", decoded)
    print ("recode = ", encode)