'''
try:
    num = int(input("Enter a number: "))
    result = 10/num
    print(result)
except ValueError:
    print("Something went wrong")
except ZeroDivisionError:
    print("Can't be divided by zero")
else:
    print(f"Result is {result}")
finally:
    print("Program Finished")

#exception + file handling
try:
    with open("my_file.txt", "w") as file:
        file.write("Niharika")
    with open("my_file.txt","r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found! Please check the file name")
finally:
    print("file operation is completed")


try:
    num = int(input("Enter a Number: "))
    result = 10/num
    print(result)
except ValueError:
    print("Give a valid number")
except ZeroDivisionError:
    print("The num Can't be Zero")
else:
    print(f"Result is {result}")
finally:
    print("Program is completed!")


try:
    with open("data.txt","r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not Found!")
else:
    print(content)
finally:
    print("File program is completed")

    
try:
    fruits = ["apple", "banana", "mango", "orange"]
    index = int(input("Enter the index: "))
    print(fruits[index])
except IndexError:
    print("Something went Wrong in The Index! Check Again")
finally:
    print("Completed!")


try:
    student = {
    "name": "Niharika",
    "age": 19,
    "city": "Nellore"
}
    key = (input("Enter Key: "))
    print(student[key])
except KeyError:
    print("Please check the Key Range Again And Try Again1")
else:
    print(f"Key is found: {key}")
finally:
    print("completed!")

#oops + exception handling
#do Again You did lot of mistakes!
class Calculator:

    def divide(self, a, b):
        try:
            result = a / b
            print(f"Result = {result}")
        except ZeroDivisionError:
            print("Can't divide by zero")

    def convert_to_int(self, value):
        try:
            number = int(value)
            print(f"Integer = {number}")
        except ValueError:
            print("Please enter a valid number")


calc = Calculator()

calc.divide(10, 2)
calc.divide(10, 0)

calc.convert_to_int("25")
calc.convert_to_int("hello")

try:
    num = " "
    
    while num != 1:
        num = int(input("Enter a num: "))
except ValueError:
    print("Give a valid num!")
else:
    print("Successfull")
finally:
    print("completed!")

'''
#Write a program that keeps asking the user for a number until they enter a valid number, using:
#while loop , try, except ValueError
#Once they enter a valid number, print it and stop the loop.
while True: #while being true 
    try:
        num = int(input("Enter a num: "))
        print(f"Valid number: {num}")
        break #breaking the true statement 

    except ValueError:
        print("Give a valid num!")

print("Completed!")


































































