class Skilledge:

    info = "The Best Online Classes"

    def students(self, str):
        print("Welcome! " + str)

mytutor = Skilledge()
mytutor.students("Alien")
mytutor.name = "pranbir"        
mytutor.age = 29
print(mytutor.name)
print(mytutor.age)

Skilledge.info = "You are in the Best Classes"
print(Skilledge.info)