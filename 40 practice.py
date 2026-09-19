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
'''
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


