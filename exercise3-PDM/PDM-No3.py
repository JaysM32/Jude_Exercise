AvoNum = 6.022*10**23

def numAtoms( grams, AtomW = 196.97):
    mass = grams/AtomW
    numAtoms = mass*AvoNum
    return numAtoms

carbon = 12.001
hydrogen = 1.008


print("substance selection = gold/carbon/hydrogen")
choice = input("choice = ")
grams1 = float(input("amount in grams = "))

if choice == "gold":
    print(numAtoms(grams1))
elif choice == "carbon":
    print(numAtoms(grams1, carbon))
elif choice == "hydrogen":
    print(numAtoms(grams1, hydrogen))