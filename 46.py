class Car:
    def __init__(self,year=20, make=45, model=675):
        self.year = year
        self.make = make
        self.model = model

    def age(self):
        print(2021 - self.year)    

car = Car(2000)
car.age()
     