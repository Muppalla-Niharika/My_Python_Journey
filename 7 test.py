
name = input("Enter name: ")
print("Welcome " + name + "!")

input = "python"
print(input.upper())

num = int(input("Enter number: "))
if num >0:
    print("Positive Number")
else:
    print("Not Positive")

marks = int(input("Enter marks: "))
if marks >= 90:
    print("Excellent")
elif 90 > marks >= 75:
    print("Good")
elif 75 > marks >=35:
    print("Pass")
else:
    print("Fail")

username = input("Enter name: ")
if username == "admin":
    password = input("enter password: ")
    if password == "1234":
        print("Login Successful")
    else:
        print("Wrong Password")
else:
    print("User not found")

word = input("Enter a word: ")
if len(word) > 5:
    print(word.upper())
else:
    print(word.lower())

word = input("Enter a word: ")
if len(word) == 5:
    print("Perfect")
elif len(word) > 5:
    print(word.upper())
else:
    print(word.lower())




















