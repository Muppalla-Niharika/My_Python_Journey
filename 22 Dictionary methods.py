'''
student = {
    "name": "Niharika",
    "age": 18,
    "CGPA":8.61
}
student.update({
    "CGPA":8.59,
    "age":19,
    "College":"KARE"

})
print(student.items())
print(student.get("CGPA"))
print(student.get("phone"))
print(student.get("phone","Not available"))

student = {
    "name": "Niharika",
    "city": "Nellore",
    "age" : 19
}

removed = student.pop("city")
del student["age"]
student.clear()
print(student)

student = {
    "name": "Niharika",
    "age": 18
}

student_copy = student.copy()

student_copy["age"] = 25

print(student)
print(student_copy)
'''

#q6
student = {
    "name": "Niharika",
    "age": 18,
    "CGPA":8.61
}
print(student.get("name"))
print(student.get("phone","Not Available"))

#q7
subjects = {
    "Maths":95,
    "HTML":93,
    "CSS":99
}
subjects.update({
    "Science":96,
    "DM":98,
    "CSS":96
})
print(subjects)

#q8
subjects = {
    "Maths":95,
    "HTML":93,
    "CSS":99,
    "Science":96,
    "DM":98
}
remove = subjects.pop("DM")
print(remove)
print(subjects)

#q9
subjects = {
    "Maths":95,
    "HTML":93,
    "CSS":99,
    "Science":96,
    "DM":98
}
subjects_copy = subjects.copy()
subjects_copy["CSS"] = 96
print(subjects)
print(subjects_copy)

#q10 
#LOT'S OF TROUBLE I DID EVERYTHING ON MY OWN
#I COPIED IT FROM GPT BECOZ IDK HOW TO PRINT FRIEND 1 TO 3 IN LOOP
names = {}
for i in range(3):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    names[name] = age
    friend_no = 1
for name, age in names.items():
    print(f"friend {friend_no}: {name} is {age} years old")
    friend_no +=1

#q11
products = {
    "Book": 100,
    "Pen": 20,
    "Bag": 500,
    "Bottle": 150,
    "Mouse": 300
}
total = 0
for key,value in products.items():
    total += value
print("Total: " ,total)


#q12
#i gava up on average
subjects = {}

for i in range(4):
    subject = input("Enter subject: ")
    mark = int(input("Enter marks: "))
    subjects[subject] = mark

total = sum(subjects.values())
average = total / len(subjects)
highest_subject = max(subjects, key=subjects.get)
print("Total marks:", total)
print("Average:", average)
print("Highest subject:", highest_subject, "with", subjects[highest_subject])

















