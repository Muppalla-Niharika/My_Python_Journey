
student = { 
    "name" : "Niharika",
    "age" : 18,
    "City": "Nellore",
    "CGPA":8.59
}
student["college"] = "Kalsalingam University"
student["age"] = 19
del student["age"]
print("name" in student)
print("City" in student)

#looping in dictionaries
for key ,value in student.items():
    print(f"{key}:{value}")

    
print(student)

print(student.keys())
print(student.values())
print(student.items())
print(len(student))

phone = input("Phone: ")
digits_mapping = {
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four",
    "5":"Five",
    "6":"Six",
    "7":"Seven",
    "8":"Eight",
    "9":"Nine",
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!" ) + " "
print(output)

'''


'''
#questions 
#q5
student = {
    "Name":"Niharika",
    "Age":18,
    "City":"Nellore",
    "College":"KARE",
    "Goal": "15 LPA" 
}
for key in student:
    print(student[key])

#q6
marks = {
    "Maths":85,
    "Python":90,
    "English":78,
    "Science":92,
    "Social":88
}
for key , values in marks.items():
    print(f"{key}:{values}")

#q7
marks = {
    "Maths":85,
    "Python":90,
    "English":78,
    "Science":92,
    "Social":88
}
marks["CSS"] = 99
marks["HTML"] = 92
marks["Social"] = 81
del marks["English"]
print(marks.items())

#q8
students = {
    "Niharika": 85,
    "Priya": 72,
    "Sravani": 91
}
for key, value in students.items():
    if value >= 80:
        print(f"{key}:{value}")

#q9
marks = {}
for i in range(3):
    subject = input("Enter Subject names: ")
    mark = int(input("Enter marks: "))
    marks[subject] = mark
for key,value in marks.items():
    print(f"{key}:{value}")

#q10
fav_movie = {
    "Name":"Oye",
    "Hero":"Siddarth",
    "Heroine":"Baby",
    "Year":2007,
    "Rating":9.6
}
print("========== Movie Details ==========")
print("")
for key , value in fav_movie.items():
    print(f"{key}:{value}")
print("")
print("===================================")


















































































































































































