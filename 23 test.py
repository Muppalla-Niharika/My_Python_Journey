
#q5
friends = {
    "Niha":19,
    "Gopi":13,
    "Priya":14,
    "Kalyani":44,
    "Harshi":19
}
for key, value in friends.items():
    print(f"{key} is {value} years old!")

#q6
names = {}
for i in range(4):
    name = input("Enter item names: ")
    price = int(input("Enter prices: "))
    names[name] = price
total = 0
for key , value in names.items():
    total += value
print("Total Cost:" ,total)

#q7
subjects = {
    "Maths":96,
    "Science":82,
    "Physics":86,
    "Python":85,
    "English":93
}
for key , value in subjects.items():
    if value > 85:
        print(f"{key}:{value}")

#q8
subjects = {
    "Maths":96,
    "Science":82,
    "Physics":86
}
subjects.update ({
    "Python":85,
    "English":93,
    "Physics":89
})
removed = subjects.pop("Maths")
print(subjects)
print(removed)

#q9
details = {}
name = input("Enter Name: ")
age = int(input("Enter age: "))
city = input("Enter city: ")
college = input("Enter college: ")
goal = input("Enter goal: ")
details["Name"] = name
details["Age"] = age
details["City"] = city
details["College"] = college
details["Goal"] = goal
print("===== My Profile =====")
for key, value in details.items():
    print(f"{key}: {value}")
print("=====================")

#q10
#i gave up idk 
movies = {
    "bahubali_1" : 8.2,
    "bahubali2" : 8.1,
    "Oye" : 7.1,
    "Darling" : 7.4,
    "Seetha_raamam" : 8.5
}
for key , value in movies.items():
    if value >=8.0:
        print(f"{key}:{value}")
print(movies)
 
        
    














































































































































































































































