# class inherit / parent class

class Animal:
    def eat(self):
        print("The animal is eating")

class Cow(Animal):
    def eat(self):
        print("The cow is eating")

# object
cow1=Animal()
cow1.eat()

cow2=Cow()
cow2.eat()