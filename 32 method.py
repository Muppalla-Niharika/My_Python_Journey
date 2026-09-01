
class Circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14*self.radius*self.radius
    def perimeter(self):
        return 2*3.14*self.radius
    def is_big(self):
        if self.radius >10:
            return True
        else:
            return False
r1 = Circle(3)
r2 = Circle(7)
print(r1.area())
print(r1.perimeter())
print(r1.is_big())
print(r2.area())
print(r2.perimeter())
print(r2.is_big())
 

class Student:
    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks
    def introduce(self):
        print(f"Hi! I am {self.name} and I am {self.age} years old.")
    def get_grade(self):
        if self.marks >=90:
            return "A"
        elif self.marks >=75 and self.marks <=90:
            return "B"
        elif self.marks >=60 and self.marks <=75:
            return "C"
        elif self.marks >=35 and self.marks <=60:
            return "D"
        else:
            return "F"
    def is_passed(self):
        if self.marks>=35:
            return True
        else:
            return False
std1 = Student("Niha",19,89)
print(std1.name,std1.age,std1.marks,std1.is_passed())


#IMPORTANT
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"₹{amount} deposited successfully!")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully!")
        else:
            print("Insufficient balance!")

    def show_balance(self):
        print(f"Owner: {self.owner}")
        print(f"Current Balance: ₹{self.balance}")


account1 = BankAccount("Niharika", 5000)

account1.deposit(2000)
account1.withdraw(3000)
account1.withdraw(10000)
account1.show_balance()


class Phone:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price
    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"model: {self.model}")
        print(f"price: {self.price}")
    def is_affordable(self):
        if self.price <= 20000:
            return True
        else:
            return False
    def discount_price(self):
        discount = self.price * 10/100
        return self.price - discount
phone1 = Phone("Samsung","Galaxy S24 FE",40000)
phone2 = Phone("Iphone","10",10000)
print(phone1.model,phone1.price,phone1.brand,phone1.discount_price(),phone1.is_affordable())
print(phone2.model,phone2.price,phone2.brand,phone2.discount_price(),phone2.is_affordable())


class Employee:
    def __init__(self,name,role,salary):
        self.name = name
        self.role = role
        self.salary = salary
    def introduce(self):
        print(f"Hi! I am {self.name} and I work as a {self.role}")
    def annual_salary(self):
        return self.salary*12
    def got_raise(self,percent):
        self.percent = percent
        raise_amount = self.salary * percent / 100
        return self.salary + raise_amount
name1 = input("Enter employee 1 name: ")
role1 = input("Enter employee 1 role: ")
salary1 = float(input("Enter employee 1 salary: "))
name2 = input("Enter employee 2 name: ")
role2 = input("Enter employee 2 role: ")
salary2 = float(input("Enter employee 2 salary: "))
emp1 = Employee(name1, role1, salary1)
emp2 = Employee(name2, role2, salary2)
emp1.introduce()
print("Annual Salary:", emp1.annual_salary())
print("Salary after 10% raise:", emp1.got_raise(10))
emp2.introduce()
print("Annual Salary:", emp2.annual_salary())
print("Salary after 15% raise:", emp2.got_raise(15))

class FullStackDeveloper:
    def __init__(self,name,frontend,backend,experience):
        self.name = name
        self.frontend = frontend
        self.backend = backend
        self.experience = experience
    def introduce(self):
        print(f"Hi! I am {self.name}.")
        print(f"Frontend: {self.frontend}")
        print(f"Backend: {self.backend}")
        print(f"Experience: {self.experience} years")
    def is_experienced(self):
        if self.experience >= 3:
            return True
        else:
            return False
    def learn(self,skill):
        self.skill = skill
        print(f"{self.name} is learning {self.skill}.")
dev1 = FullStackDeveloper("Niharika", "React", "Python", 2)
dev2 = FullStackDeveloper("Rahul", "HTML/CSS", "Java", 5)
dev1.introduce()
print(dev1.is_experienced())
dev1.learn("Docker")

dev2.introduce()
print(dev2.is_experienced())
dev2.learn("AWS")



























