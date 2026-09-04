"""
#user needs to use 2 num and do hypothesis
num1 = float(input("Enter Num1: "))
num2 = float(input("Enter Num2: "))
num3 = ((num1**2 + num2**2)**0.5)
print(num3)

a= int(100)
a = (a+50)
print(a)
b= 9
b= float(b)
print(b)
c = str(2026)
print(c)

#while loop
password = ""
while password != "Niharika@07":
    password = input("Enter the Password: ")
print("Login Successful")


count = 1
while count <=5:
    print("*"*count)
    count += 1


number = ""
while number != 0:
    number = int(input("Enter Number: "))
print("Done!")

#for loop
for item in "python":
    print(item)
for item in "Niharika":
    print(item)

for names in ["Niharika", "Priya", "gopi", "kalyani"]:
    if names == "gopi":
        break
    print(names)

#continue 
for i in range(1,50):
    if i == 25:
        continue
    elif i ==30:
        break
    print(i)

for items in range(1,25,2):
    print(items)

#string slicing
course = "Python"
print(course[-5: ]) #ython 
print(course[0: ]) #python
print(course[-1:-7]) #empty string
print(course[0:3]) #Pyt

#f string
name = "Niharika"
print(f"Bonjour! {name} ! Welcome to paris")

a = 2/4
print(a)
b = 2//4
print(b)
""" 
#lower upper case
name = "NIHA"
print(name.lower())
#strip
name = "      Harshi "
print(f"Hi {name.strip()}")


















































