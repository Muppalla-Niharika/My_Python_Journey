'''#Functions
def greet(name): 
    print(f"{name} Hello Welcome")
greet('Niharika')
greet('Jyo')
#Default parameter must come after a nrml parameter if we have more than 1
def course(course_name = "CSE"):
    print(f"Your Course is {course_name}")
course()
course("EEE")
def sum(a,b):
    return a+b
result  = sum(9,2)
print(result)

#print
def add(a,b):
    print(a+b) #print , function never sent the value back so it never stored
x = add(2,3) #we called 2,3 to add 
print(x) #None becox x stored nothing

def add(a,b):
    return a+b #function sent the value back to x
x = add(9,14) #x stored the ans
print(x) # x has 23 

#File Handling
file = open("My_file.txt","w")
file.write("Hi Niharika")
file.write("\n I am Learning Python")
file.close()
file = open("My_file.txt","r")
file.close()
file = open("My_file.txt","a")
file.write("\n I Thought of learning frontend")
file.write("\n I'll Next learn backend")
file.close()
file = open("My_file.txt","r")
content = file.read()
print(content)
file.close()


#forgot to close and write
with open("My_file.txt","w") as file:
    file.write("I'm In 3rd year")
with open("My_file.txt","r") as file:
    context = file.read()
    print(context) 
#forgot to close and want to read every line
with open("My_file.txt","r") as file:
    for line in file:
        print(line)
'''
#6
def add(a,b):
    return a+b
result = add(3,4)
print(result)
#7
def greet(name="Guest"):
    print(f"Hello, {name}")
greet()
greet("Niha")
#8
with open("test.txt","w") as file:
    file.write("Hello Niha")
#9
with open("test.txt","w") as file:
    file.write("Hello Niha")
with open("test.txt","r") as file:
    content = file.read()
    print(content)
#10
def is_even(n):
    if n %2 == 0:
        return True
    else:
        return False
print(is_even(7))
print(is_even(8))






























































































