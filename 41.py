class Skilledge:

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course


    def students(self, str):
        print("Welcome! " + str)

mytutor = Skilledge("Vasu", 26, "FSD")
mytutor.students("Alien")      
print(mytutor.name)
print(mytutor.age)
print(mytutor.course)
