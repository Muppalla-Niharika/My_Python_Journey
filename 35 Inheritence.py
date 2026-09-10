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
    def __init__(self,color,radius):
        super().__init__(color)
        self.radius = radius
    def area(self):
        print(f"Circlenarea = {3.14 * self.radius * self.radius}")
class Rectangle(Shape):
    def __init__(self,color,length,breadth):
        super().__init__(color)
        self.length = length
        self.breadth = breadth
    def area(self):
        print(f"Rectangle is = {self.length} * {self.breadth}")

circle = Circle("Yellow", 2.5)
rectangle = Rectangle("Blue", 8, 5)
circle.display()
circle.area()
rectangle.display()
rectangle.area()

#
class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"Hello! This is {self.name} and I'm {self.age} is years old")
class Student(Person):
    def __init__(self,name,age,marks):
        super().__init__(name,age)
        self.marks = marks
    def get_grade(self):
        print(f"Hello! This is {self.name} and I'm {self.age} is years old and also i got {self.marks}!")

std = Student("Niha", 19 , 98)
std.introduce()
std.get_grade()

'''
class Animal():
    def __init__(self,name,sound):
        self.name = name
        self.sound = sound
    def make_sound(self):
        print(f"{self.name} is {self.sound}ing")
class Dog(Animal):
    def display(self):
        print(f"{self.name} is {self.sound}ing")
class Cat(Animal):
    def display(self):
        print(f"{self.name} is {self.sound}ing")
class Bird(Animal):
    def display(self):
        print(f"{self.name} is {self.sound}ing")
dog = Dog("Bam" , "Bark")
cat = Cat("Lary" , "Meow")
bird = Bird("Crow", "Shout")
dog.display()
cat.display()
bird.display()
























































































