'''
def analyze_list(numbers):
    total = sum(numbers)
    average = total/len(numbers)
    highest = max(numbers)
    lowest = min(numbers)
    return total,average,highest,lowest
numbers = [10,40,50,92,40,58]
result = analyze_list(numbers)
print("Total: ",result[0])
print("Average:", result[1])
print("Highest:", result[2])
print("Lowest:", result[3])


class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book added: {book}")

    def remove_book(self, book):
        try:
            self.books.remove(book)
            print(f"Book removed: {book}")
        except ValueError:
            print("Book not found!")

    def show_books(self):
        print("Books in library:")
        for book in self.books:
            print(book)

    def search_book(self, book):
        return book in self.books


library = Library()

library.add_book("Ram")
library.add_book("Kurukshetra")
library.add_book("Ramayana")
library.add_book("The Lonely Love")

library.show_books()

print("Is Ramayana available?", library.search_book("Ramayana"))
print("Is Harry Potter available?", library.search_book("Harry Potter"))

library.remove_book("Ram")
library.remove_book("Harry Potter")

library.show_books()

students = [
    ("Niharika", 85),
    ("Priya", 30),
    ("Sravani", 91),
    ("Divya", 20),
    ("Rahul", 67)
]
result = filter(lambda x: x[1] >= 35, students)
print(list(result))

try:
    with open("students.txt","w") as file:
        for i in range(3):
            names = input("Enter your name: ")
            file.write(names + "\n")
    with open("students.txt","r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found!")

def calculate_salary(salary):
    salary_tax = salary * 0.8
    return salary_tax
salary = int(input("Enter your salary: "))
sal = calculate_salary(salary)
print(sal)

salaries = [15000, 25000, 40000, 60000, 100000]
result = map(lambda x: x * 0.8 , salaries)
print(list(result))

import random
class Animal:
    def __init__(self):
        print(f"Animal Created")
class Dog(Animal):
    def __init__(self):
        super().__init__()
        dog_actions = ["fetching", "barking", "running"]
        action1 = random.choice(dog_actions)
        print(action1)
class Cat(Animal):
    def __init__(self):
        super().__init__()
        cat_actions = ["purring", "sleeping", "climbing"]
        action2 = random.choice(cat_actions)
        print(action2)
dog = Dog()
cat = Cat()


def process_data():
    numbers = [-5, 2, -3, 4, 6, -1]
    if not numbers:
        raise ValueError("List is empty")
    result1 = filter(lambda x: x >0 , numbers)
    result2 = map(lambda x: x **2 , result1)
    return(list(result2))
try:
    result = process_data()
    print(result)
except ValueError:
    print("List is empty")

students = [
    ("Niharika", 85),
    ("Priya", 72),
    ("Sravani", 95),
    ("Divya", 60)
]
result = sorted(students , key = lambda x: x[1],reverse = True)
print(result)
'''

def analyze_numbers(numbers):
    result1 = max(numbers, key=lambda x: x)
    result2 = min(numbers, key=lambda x: x)
    return result1, result2
numbers = [10, 25, 4, 80, 15, 60]
result = analyze_numbers(numbers)
print(f"Highest:",result[0])
print(f"Lowest:",result[1])





























































































































