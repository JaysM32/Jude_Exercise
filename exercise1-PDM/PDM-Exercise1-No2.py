ClassScore = []
total = 0

print("----Welcome to the ClassScore Average Calculator!----")
print("Please input the Scores of the Students in the class.")
print("type 'done' when finished inputting the scores.")
print("--------------------------------------------")
while True:
    scoreinput = input("Score of Student = ")
    if (scoreinput == "done"):
        break
    else:
        ClassScore.append(float(scoreinput))
        print("Added!")

for i in range(len(ClassScore)):
    total += ClassScore[i]

average = total / len(ClassScore)

print("--------------------------------------------")
print("Student scores: ")
for j in range(len(ClassScore)):
    print(ClassScore[j])
print("Total score of all students =", total)
print("Total num of students =", len(ClassScore))
print("Average score among students =", average)