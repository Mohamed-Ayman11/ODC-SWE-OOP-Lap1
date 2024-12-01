
#Base Class
class Animal:
    def __init__(self, name):
        self.name = name

    def Eat(self):
        print("Animal Is Eating...")

    def Sleep(self):
        print("Animal Is Sleeping...")

#Derived Classes
class Dog(Animal):
    def __init__(self, name):
        self.name = name

    def Eat(self):
        print("Dog Is Eating...")

    def Sleep(self):
        print("Dog Is Sleeping...")

    def Barking(self):
        print("Dog Is Barking...")

class Cat(Animal):
    def __init__(self, name):
        self.name = name

    def Eat(self):
        print("Cat Is Eating...")

    def Sleep(self):
        print("Cat Is Sleeping...")

    def Meowing(self):
        print("Cat Is Meowing...")

#Created An Instance From Animal(Base) Class
animal1 = Animal("Animal")
animal1.Eat()
animal1.Sleep()

print("--------------------------------------")


#Created An Instance From Dog(Derived) class
#Eat And Sleep Function Behaves differently in the Derived Classes (Polymorphism)
dog1 = Dog("REX")
dog1.Eat()
dog1.Sleep()
dog1.Barking()

print("--------------------------------------")

#Created An Instance From Cat(Derived) class
#Eat And Sleep Function Behaves differently in the Derived Classes (Polymorphism)
cat1 = Cat("Sanfor")
cat1.Eat()
cat1.Sleep()
cat1.Meowing()