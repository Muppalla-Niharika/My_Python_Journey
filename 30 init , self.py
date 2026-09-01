
class Student:
    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks
student1 = Student("niha", 19,99 )
student2 = Student("jyo",20,95)
print(student1.name,student1.age,student1.marks)
print(student2.name,student2.age,student2.marks)

class Phone:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price
phone1 = Phone("Samsung S24 FE" , 143 , 40000)
phone2 = Phone("Samsung S24 FE" , 132 , 32000)
phone3 = Phone("Iphone 17 pro max" ,123, 140000)
print(phone1.brand,phone1.model,phone1.price)
print(phone2.brand,phone2.model,phone2.price)
print(phone3.brand,phone3.model,phone3.price)

class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
bankaccount1 = BankAccount("Niha",240000)
bankaccount2 = BankAccount("jyo",120000)
print(bankaccount1.owner,bankaccount1.balance)
print(bankaccount2.owner,bankaccount2.balance)

class Movie:
    def __init__(self,title,hero,rating):
        self.title = title
        self.hero = hero
        self.rating = rating
movie1 = Movie("Oye","Siddarth",9.8)
movie2 = Movie("manasara","ravi",7.86)
movie3 = Movie("jyo","ram",7)
print(movie1.title,movie1.hero,movie1.rating)
print(movie2.title,movie2.hero,movie2.rating)
print(movie3.title,movie3.hero,movie3.rating)

class Person:
    def __init__(self,name,age,city):
        self.name = name
        self.age =age
        self.city = city

name1 = input("Enter name: ")
age1 = int(input("enter age: "))
city1 = input("Enter city: ")
name2 = input("Enter name: ")
age2 = int(input("enter age: "))
city2 = input("Enter city: ")
person1 = Person(name1,age1,city1)
person2 = Person(name2,age2,city2)
print(person1.name,person1.age,person1.city)
print(person2.name,person2.age,person2.city)

class Dream:
    def __init__(self,name,goal_salary,target_year):
        self.name = name
        self.goal_salary = goal_salary
        self.target_year = target_year
dream = Dream("Niharika", "15 LPA", 2028)
print(f"Name: {dream.name}, Goal Salary: {dream.goal_salary}, Target Year: {dream.target_year}")


































