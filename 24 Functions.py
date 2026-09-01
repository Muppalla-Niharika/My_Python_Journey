'''
def greet(name):
    print(f"Hello {name}! , Nice to meet you !")
greet("Gopi Priya")

def add_numbers(a, b):
    return a +b
result = add_numbers(8,9)
print(result)

def add_print(a, b):
    return(a + b)
x = add_print(5, 10)
print(x)

#nested function where outer uses return
def outer(a,b):
    def inner(c,d):
        print(c+d)
    inner(9,12)
    return a+b
result = outer(6,3)
print(result)

#nested function where inner uses return
def outer(a, b):
    def inner(c, d):
        return c + d
    result = inner(9,12)
    print(result)
outer(6,3)
'''

#q5
def greet_user(name):
    print(f"Hello {name}! Have a great day!")
greet_user("Niharika")
greet_user("priya")
greet_user("gopi")


#q6
def add(a,b):
    return (a+b)
result = add(6,4)
print(result)


#q7
def is_even(a):
    if a %2 ==0:
        return(True)
    else:
        return(False)
result = is_even(4)
print(result)

#or 
def is_even(a):
    return a%2 ==0
print(is_even(3))
print(is_even(8))


#q8
#i didn't called it before chatgpt scolded me so bad that i did afterwards
def calculate_area(l,b):
    return l*b
length = int(input("Enter length: "))
breadth = int(input("Enter breadth: "))
area= calculate_area(length,breadth)
print("Area:",area)

#q9
#i entered the vaue 963 just to make gpt more angry and guess wt i did so here is the code if someone enters > 100 or < 0
def grade(marks):
    if marks < 0 or marks > 100:
        return "Error"
    elif marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 35:
        return "D"
    else:
        return "F"
marks = int(input("Enter marks: "))
result = grade(marks)
print("Grade:", result)


#q10
# i left my soul at CALL , it's literally exhausted me!
def bio(name , age , goal):
    print(f"Hi! My name is {name}.")
    print(f"I am {age} years old.")
    print(f"My goal is {goal} LPA!")
bio("Niharika",19,15)










































