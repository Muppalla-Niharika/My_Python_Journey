"""
class Animal:
    def eat(self):
        print("Eating...")

class Dog(Animal):
    def sound(self):
        print("barking...")

dog = Dog()
dog.eat()
dog.sound()
"""
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"Hi! My name is {self.name} and I am {self.age} years old.")
class Student(Person):
    def study(self,course):
        self.course = course
        print(f"{self.name} is studying {self.course}.")
std1 = Student("Niharika",19,"CSE AIML")
std2 = Student("Jyo",20,"ECE")
std1.introduce()
std2.study()
print(std1.name, std1.age, std1.course)
print(std2.name, std2.age, std2.course)
