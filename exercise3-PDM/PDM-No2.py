def calcweightonplanet(weight, gravity = 23.1):
    mass = weight / 9.8
    weight1 = mass * gravity
    return weight1

x = calcweightonplanet(120,9.8)
y = calcweightonplanet(120)
z = calcweightonplanet(120,23.1)

print(x)
print(y)
print(z)