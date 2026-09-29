'''
count = 1
while count <= 5:
    if count == 3:
        count += 1
        continue
    print(count)
    count += 1


for i in range(1, 6):
    if i == 4:
        break
    print(i * i)


marks = 75
if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 60:
    print("C")
else:
    print("F")

numbers = [i * 2 for i in range(1, 6)]
print(numbers)

evens = [i for i in range(1, 21) if i % 2 == 0]
print(len(evens))

name = input("Enter your Name: ")
age = int(input("enter your age: "))
city = input("Enter your City: ")
print(f"My name is {name}, I am {age} years old and I live in {city}.")

num = int(input("Enter a Num: "))
if num > 0:
    print("Positive")
elif num <0:
    print("Negative")
else:
    print("zero")

i = 1
num = int(input("Enter a Num: "))
while i <=10:
    result = num * i
    print(f"{num} x {i} = {result}")
    i+=1

i = 0
for i in range(1,51):
    if i % 3 ==0 and i % 5 ==0:
        print(i)

name = input("Enter your Name: ")
print(f"Original:{name}")
print(f"Uppercase:{name.upper()}")
print(f"Lowercase:{name.lower()}")
print(f"Length:{len(name)}")
print(f"Reversed:{name[::-1]}")
print(f"First 3 letters:{name[0:3]}")
print(f"Last 3 letters:{name[-3:]}")

password = ""
attempt =0
while password != "python123":
    password = input("Enter the Password: ")
    attempt += 1
    if password == "python123":
        print(f"Welcome! you got it in {attempt} attempts")
        break
    else:
        print("Wrong password!")

numbers = []
for i in range(5):
    num = int(input("Enter a num: "))
    numbers.append(num)
    average = sum(numbers)/len(numbers)
    print(f"Sum:{sum(numbers)}")
    print(f"Average:{average}")
    print(f"Highest:{max(numbers)}")
    print(f"Lowest:{min(numbers)}")
'''
square_num = [i**2 for i in range(1,11)]
print(square_num)
odd_num = [i for i in range(1,21)if i%2 !=0]
print(odd_num)
import math
names = ["niharika", "priya", "sravani"]
uppercase_names = map()



















