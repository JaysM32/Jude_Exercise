def calcnewheight(Cwidth, Cheight, Nwidth):
    ratio = Cwidth/Cheight
    newheight = Nwidth/ratio

    return newheight

width1 = float(input("input current photo width = "))
height1 = float(input("input current photo height = "))
width2 =float(input("input desired photo width = "))
print("New photo height with desired width = ", calcnewheight(width1, height1, width2))