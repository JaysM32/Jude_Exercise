class Person:
    def __init__(self,name,address):
        self.name = name
        self.adrress = address

    def getName(self):
        return self.name
    def getAddress(self):
        return self.adrress
    def setAddress(self, addr):
        self.adrress = addr

    def __str__(self):
        return f"Name: {self.name}. ({self.adrress})"

class Student(Person):
    def __init__(self, name, address):
        super().__init__(name, address)
        self.numCourses = 0
        self.courses = []
        self.grades = []

    def __str__(self):
        return super().__str__()+f"Num of courses : {self.numCourses}, courses: {self.courses}, grades: {self.grades}"

    def addCourseGrade(self, course, grade):
        self.courses.append(course)
        self.grades.append(grade)
        self.numCourses += 1

    def printGrades(self):
        for count in range(len(self.grades)):
            print(f"{count+1}. {self.courses[count]} : {self.grades[count]}")

    def getAverageGrades(self):
        count = 0
        total = 0
        for grades in self.grades:
            count += 1
            total = total + grades
        average = total / count
        return average

    def toString(self):
        return super().__str__()

class Teacher(Person):
    def __init__(self, name, address):
        super().__init__(name, address)
        self.numCourses = 0
        self.courses = []

    def __str__(self):
        return super().__str__()+f"Num of courses : {self.numCourses}, courses: {self.courses}"

    def addCourses(self, course):
        if course in self.courses:
            return False
        else:
            self.numCourses += 1
            self.courses.append(course)
            return True

    def removeCourse(self, course):
        if course not in self.courses:
            return False
        else:
            self.numCourses = self.numCourses - 1
            self.courses.remove(course)
            return True

    def toString(self):
        return super().__str__()



if __name__ == '__main__':
    student1 = Student("Bernard","Jakarta")
    teacher1 = Teacher("Jude", "Jakarta")
    student1.addCourseGrade("Maths", 70)
    student1.addCourseGrade("Physics", 60)
    student1.addCourseGrade("Biology", 75)
    student1.addCourseGrade("Chemistry", 50)
    print(student1.__str__())
    print(student1.getAverageGrades())
    teacher1.addCourses("Maths")
    teacher1.addCourses("Physics")
    teacher1.addCourses("Chemistry")
    print(teacher1.__str__())
    teacher1.removeCourse("Chemistry")


