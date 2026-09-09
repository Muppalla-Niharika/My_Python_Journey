
class Car:
    def __init__(self,name,price):
        self.name = name
        self.price = price
        print(f"This Special {name} is Around {price}")
my_car = Car("BMW",5800000)


class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def show(self):
        print(f"{self.brand} can go {self.speed} km/h")

my_car = Car("BMW", 200)
my_car.show()   # BMW can go 200 km/h


#inheritance
class Animal:
    def sound(self):
        print("Sound")
class Dog(Animal):
    def sound(self):
        print("Bark")
class Cat(Animal):
    def sound(self):
        print("Meow")
d = Dog()
d.sound()
c = Cat()
c.sound()

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def display(self):
        print(f"{self.name} got these many {self.marks} Marks!")
Std = Student("Niha",96)
Std.display()

class Shape:
    def area(self):
        print("Area not defined")

class Square(Shape):
    def area(self):
        print("Area = side * side")

sq = Square()
sq.area()





























































































































