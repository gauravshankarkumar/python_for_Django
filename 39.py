class Skilledge:

    info = "The Best Online Classes"

    def students(self):
        print("Welcome")

mytutor = Skilledge()
mytutor.students()
mytutor.name = "pranbir"        
mytutor.age = 29
print(mytutor.name)
print(mytutor.age)

Skilledge.info = "You are in the Best Classes"
print(Skilledge.info)