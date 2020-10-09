class1 =[]
group1 =[]

print("Welcome to the Class divider / Class Groupmaker!")
print("Please input the number of student in the class!")
print("when finished / no more classes remain,")
print("type 'done' to continue to the next phase.")
print("------------------------------------------------")
while True:
    classinput = input("Number of Student in class = ")
    if (classinput == "done"):
        break
    else:
        class1.append(float(classinput))
        print("Added!")

print("------------------------------------------------")
print("Determine number of groups!")
for i in range(len(class1)):
    print("Class", i+1, "=")
    groupinput = input()
    group1.append(int(groupinput))

print("------------------------------------------------")
for j in range(len(class1)):
    GrupStu, StuLeft = divmod(class1[j], group1[j])
    print("Num. of Student per group in Class", j+1, "=",  GrupStu)
    print("Num. of Student left =", StuLeft)
    print("------")