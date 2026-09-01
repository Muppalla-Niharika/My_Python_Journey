
num = [i for i in range(1,100)]
print(num)

numbers = []
for i in range(5):
    num = int(input("Enter numbers: "))
    numbers.append(num)
print(numbers)
total = sum(numbers)
print(total)
average = total/ len(numbers)
print(average)
highest = max(numbers)
print(highest)
lowest = min(numbers)
print(lowest)

#q15
marks = {
    "maths": 76,
    "Physics": 86,
    "Chemistry": 96,
    "Html" : 99,
    "css": 86
}
for key, value in marks.items():
    if value >= 80:
        print(f"{key}:{value}")

#q16
def check_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 35:
        return "D"
    else:
        return"F"
grade1 = check_grade(98)
grade2 = check_grade(19)
print(grade1)
print(grade2)

numbers = [12, 67, 34, 89, 45, 91, 23, 78]
new_numbers = [numbers for numbers in numbers if numbers >= 50]
print(new_numbers)

students = [
    ["Niharika", 90, 80],
    ["Priya", 70, 60],
    ["Rahul", 85, 95]
]
for student in students:
    average = (student[1]+student[2])/2
    print(f"{student[0]}: Average is {average}")

def shopping_discount(amount,member_type="regular"):
    if member_type == "premium":
        discount = amount*0.20 
        final_amount = amount - discount 
    else:
        discount = amount*0.10
        final_amount = amount - discount

    return final_amount
print(shopping_discount(5000, "premium"))
print(shopping_discount(10000))

names = {}
for name in range(3):
    name = input("Enter name: ")
    age = int(input("Enter your age: "))
    names[name] = age
    oldest = (max(names.values()))
for key,value in names.items():
    if value == oldest:
        print(f"Oldest is : {key} is the {oldest}!")

#list and loops


























