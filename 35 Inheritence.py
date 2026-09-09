'''
class Animal:
    def __init__(self,name,sound):
        self.name = name
        self.sound = sound
    def eat(self):
        print(f"{self.name} is Eating!")
    def make_sound(self):
        print(f"{self.name} is {self.sound}")
class Dog(Animal):
    def catch(self):
        print(f"{self.name} is {self.sound}ing and catching a ball!")
dog = Dog("Bam" , "Bark")
dog.eat()
dog.make_sound()
dog.catch()

#Super
class Animal:
    def __init__(self,name,sound):
        self.name = name
        self.sound = sound
class Dog(Animal):
    def __init__(self,name,sound,breed):
        super(). __init__(name,sound)
        self.breed = breed
    def info(self):
        print(f"{self.name} is a {self.breed}")
dog = Dog("Bittu", "Bark", "Golden Retriver")
dog.info()
print(dog.name)
print(dog.sound)
print(dog.breed)
'''
#Create a parent class Shape with:
#a property color
#a method display() that prints the color
#Then create child classes Circle and Rectangle that inherit from Shape and add their own properties and methods.

class Shape:
    def __init__(self,color):
        self.color = color
    def display(self):
        print(f"Shape color is {self.color}")
class Circle(Shape):
    def __init__(self,color):
        self.color = color
        print(f"Circle is {self.color}")
class Rectangle(Shape):
    def __init__(self,color):
        self.color = color
        print(f"Circle is {self.color}")

print(Circle)
print(Rectangle)

    























































































