feet = eval(input("input feet:"))
inches = eval(input("input inches:"))

totalinches = inches + ( feet * 12)
boardlength = totalinches*2.54*0.88

print("the approximate board length for a person with a height of", feet, "feet and", inches, "inches is ", boardlength, "cm")