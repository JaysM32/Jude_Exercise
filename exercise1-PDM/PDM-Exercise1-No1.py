import math
import time

pie = math.pi

print("-----------------------------------------")
print("welcome to the radians/degree calculator!")
print("select whether you wish to convert :")
print("1. degrees to radians")
print("2. radians to degrees")
print("-----------------------------------------")
print("input the number to continue")
select = int(input("selection = "))

if (select == 1):
    print("-----------------------------------------")
    degrees = eval(input("input Degrees = "))
    radians = degrees * pie / 180
    print("Calculating....")
    time.sleep(1)
    print("Degrees =", degrees)
    print("Radians =", radians)
elif (select == 2):
    print("-----------------------------------------")
    radians = eval (input("input Radians = "))
    degrees = radians * 180 / pie
    print("Calculating....")
    time.sleep(1)
    print("Radians =", radians)
    print("Degrees =", degrees)

