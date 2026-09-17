'''
try:
    num = int(input("Enter a num: "))
    result = 10/num
    print(result)
except ValueError:
    print(f"Enter the value correctly!")
except ZeroDivisionError:
    print(f"It can't be divided with Zero!")
else:
    print(f"result : {result}")
finally:
    print(f"Program is Successfuly completed!")

#without raise 
class BankAccount:
    def __init__(self,owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
    def withdraw(self,amount):
        if amount < 0:
            print("withdraw ammount cannot be negative!")
        else:
            self.balance -= amount
    def show_balance(self):
        print(f"The balance of your acc is : {self.balance}")
    
account = BankAccount("Niharika Muppalla", 99000)
account.deposit(5000)
account.withdraw(500)
account.withdraw(-200)
account.show_balance()

#with raise 
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        try:
            if amount < 0:
                raise ValueError("Withdrawal amount cannot be negative")
            self.balance -= amount
        except ValueError as e:
            print(e)

    def show_balance(self):
        print(f"Balance: {self.balance}")


account = BankAccount("Niharika", 5000)

account.deposit(1000)
account.withdraw(500)
account.withdraw(-200)
account.show_balance()

import random
try:
    
    number = random.randint(1,50)
    guess_num = int(input("Enter num: "))
    if guess_num < number:
        print("Higher")
    elif guess_num > number:
        print("Lower")
    else:
            print("Correct")
except ValueError:
    print("Enter the Number correctly!")
else:
    print(f"Result is : {guess_num}")
finally:
    print("Program completed")


class Vehicle:
    def __init__(self,brand,speed):
        self.brand = brand
        self.speed = speed
        print(f"the brand name is {brand} and it goes with the speed of {speed}")
class Car(Vehicle):
    def __init__(self,brand,speed):
        super().__init__(brand,speed)
    def move(self):
        print("Car is moving")
class Bike(Vehicle):
    def __init__(self,brand,speed):
        super().__init__(brand,speed)
    def move(self):
        print("Bike is moving")

try:
    car = Car("Volkswagen",200)
    bike = Bike("Royal Enfield",180)
    car.move()
    bike.move()
except:
    print("something went wrong")
finally:
    print("Completed")            


import math
try:
    num = float(input("Enter a num: "))
    if num < 0:
        print("Cannot find square root of negative number!")
    else:
        print(f"sqrt is : {math.sqrt(num)}")
except ValueError:
    print("Invalid input")
finally:
    print("completed")
'''
#copied chat gpt ans
class StudentDatabase:
    def __init__(self):
        self.students = {}

    def add_student(self, name, marks):
        self.students[name] = marks

    def get_marks(self, name):
        try:
            return self.students[name]
        except KeyError:
            print("Student not found!")

    def get_grade(self, name):
        try:
            marks = self.students[name]

            if marks >= 90:
                return "A"
            elif marks >= 75:
                return "B"
            elif marks >= 60:
                return "C"
            elif marks >= 50:
                return "D"
            else:
                return "F"

        except KeyError:
            print("Student not found!")


db = StudentDatabase()

db.add_student("Niharika", 95)
db.add_student("Rahul", 82)
db.add_student("Anu", 68)

print("Niharika marks:", db.get_marks("Niharika"))
print("Niharika grade:", db.get_grade("Niharika"))

print("Rahul marks:", db.get_marks("Rahul"))
print("Rahul grade:", db.get_grade("Rahul"))

print("Anu marks:", db.get_marks("Anu"))
print("Anu grade:", db.get_grade("Anu"))

print("Missing student marks:", db.get_marks("Priya"))
print("Missing student grade:", db.get_grade("Priya"))












































































