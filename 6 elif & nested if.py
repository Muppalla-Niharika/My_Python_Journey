'''
#q5
marks = int(input("Enter marks: "))
if marks >= 90:
    print("Grade A - Execellent! ")
elif 90 > marks >= 75:
    print("Grade B — Very Good!")
elif 75 > marks >= 60:
    print("Grade C — Good!")
elif 60 > marks >= 35:
    print("Grade D — Pass!")
else:
    print("Grade F — Fail!")

#q6
age = int(input("Enter Age: "))
if  0 <= age <=12:
    print("You are a child!")
elif 13 <= age <= 17:
    print("You are a teenager!")
elif 18 <= age <= 60:
    print("You are an adult!")
else:
    print("You are a senior citizen!")

#q7
number = int(input("Enter number: "))
if number > 0:
    print("Your number is Positive!")
elif number < 0:
    print("Your number is Negative!")
else:
    print("Your number is Zero!")

#q8
name = input("Enter name: ")
marks = int(input("Enter marks: "))
if name == "Niharika":
    if marks >= 35:
        print("Well done Niharika! You passed!")
    else:
        print("Don't worry Niharika! Try again!")
else:
    print("Hello " + name + "! Give your marks to see result!")


#q9
income = int(input("Enter income: "))
if income > 50000:
    print("High income!")
elif 50000 > income > 25000:
    print("Middle income!")
elif 25000 > income > 10000:
    print("Low income!")
else:
    print("Very low income!")

'''
#q10
cgpa = float(input("Enter cgpa: "))
backlogs = int(input("Enter Backlogs: "))
if cgpa >= 8.0 and backlogs ==0:
    print("Excellent profile! You will get a great job!")
elif 8.0 > cgpa >= 6.0 and backlogs == 0:
    print("Good profile! Keep improving!")
elif 8.0 > cgpa >= 6.0 and backlogs > 0:
    print("Clear your backlogs first!")
else:
    print("Focus on your studies first!")

















































































































