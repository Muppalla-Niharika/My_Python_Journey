'''
class Laptop:
    def __init__(self,brand,ram,price):
        self.brand = brand
        self.ram = ram
        self.price = price
laptop1 = Laptop("HP","16 ram", 80000)
laptop2 = Laptop("lenovo","16 ram", 46000)
laptop3 = Laptop("HP","8 ram", 50000)
print(laptop1.brand, laptop1.ram, laptop1.price)
print(laptop2.brand, laptop2.ram, laptop2.price)
print(laptop3.brand, laptop3.ram, laptop3.price)

class College:
    def __init__(self,name,location,ranking):
        self.name = name
        self.location = location
        self.ranking = ranking
college1 = College("Kare","madurai", 5)
college2 = College("avit","chennai",6)
print(college1.name,college1.location,college1.ranking)
print(college2.name,college2.location,college2.ranking)

class Book:
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
book1 = Book("Anandham","rama raju",200)
book2 = Book("how alone you are","steven",489)
book3 = Book("overthinking","catheline",386)
print(book1.title,book1.author,book1.pages)
print(book2.title,book2.author,book2.pages)
print(book3.title,book3.author,book3.pages)

class Employee:
    def __init__(self,name,role,salary):
        self.name = name
        self.role = role
        self.salary = salary
employee1 = Employee("Niha","Full stock developer","15 lpa")
employee2 = Employee("jyo","web developer","9 lpa")
print(employee1.name,employee1.role,employee1.salary)
print(employee2.name,employee2.role,employee2.salary)

class Student:
    def __init__(self,name,age,cgpa):
        self.name = name
        self.age = age
        self.cgpa = cgpa
name1 = input("enter name: ")
age1 = int(input("Enter age: "))
cgpa1 = float(input("Enter cgpa: "))
name2 = input("enter name: ")
age2 = int(input("Enter age: "))
cgpa2 = float(input("Enter cgpa: "))
name3 = input("enter name: ")
age3 = int(input("Enter age: "))
cgpa3 = float(input("Enter cgpa: "))
student1 = Student(name1,age1,cgpa1)
student2 = Student(name2,age2,cgpa2)
student3 = Student(name3,age3,cgpa3)
print(student1.name,student1.age,student1.cgpa)
print(student2.name,student2.age,student2.cgpa)
print(student3.name,student3.age,student3.cgpa)
'''
class MyProfile:
    def __init__(self,name,age,college,city,goal):
        self.name = name
        self.age = age
        self.college = college
        self.city = city
        self.goal = goal
person1 = MyProfile("Niharika",19,"Kalasalingam University","Nellore","15 LPA")
print("========== My Profile ==========")
print(f"Name: {person1.name}")
print(f"Age: {person1.age}")
print(f"College: {person1.college}")
print(f"City: {person1.city}")
print(f"Goal: {person1.goal}")
print("================================")

















