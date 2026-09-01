'''
# CORRECT!
def greet(name, greeting):
    print(f"{greeting}, {name}!")
greet("Niha",greeting="Hello!")
greet("Priya")

def calculte(a,b,c):
    mul_add =  a*b+c
    add_mul = a+b*c
    add_add = a+b+c
    mul_mul = a*b*c
    return mul_add,add_mul,add_add,mul_mul
result1, result2, result3, result4 = calculte(5,3,6)
print(result1)
print(result2)
print(result3)
print(result4)

def check_vote(age, vote_id):
    if age >=18 and vote_id == "Yes":
        return"You are eligible to Vote!"
    elif age>=18 and vote_id == "No":
        return"You have no voter id!"
    elif age<18 and vote_id == "Yes":
        return"You have fake id! Come for investigation"
    else:
        return"You are too young to vote!!"
print(check_vote(20,"Yes"))
print(check_vote(25,"No"))
print(check_vote(15,"No"))
print(check_vote(14,"Yes"))
'''

#q5
def order_coffee(coffe_type,size="Medium"):
    print(f"You ordered a {size} {coffe_type}!")
order_coffee("Cappuccino")
order_coffee("Latte","Large")

#q6
def rectangle_info(length ,breadth):
    return length * breadth, 2*(length + breadth)
x,y = rectangle_info(6,9)
print(x)
print(y)


#q7
def student_details(name, marks, attendance):
    if marks>=35 and attendance>=75:
        return "Pass"
    else:
        return "Fail"
print(student_details("Niharika",98,79))
print(student_details("Sasha",98,74))

#q8
def calculate_discount(price,discount_percent=10):
    discount = price * discount_percent /100
    final_price = price - discount
    return final_price
print(calculate_discount(12000))
print(calculate_discount(12000,50))

#q9
def bmi_category(weight,height):
    height = height/100
    BMI = weight/(height*height)
    if BMI < 18.5:
        return "Underweight"
    elif 18.5 <= BMI <24.9:
        return "Normal"
    else:
        return "Overweight"
print(bmi_category(95,162))


#q10
#i got it wrong so gpt gave ans 
def future_self(name,current_age,goal_salary):
    message = f"Hi {name}! Hope You are doing good and alive, See {goal_salary} LPA job! we made it! "
    future_age = current_age + 4
    return message,future_age
msg,age = future_self("Niharika",19,15)
print("Message: ",msg)
print("Age after 4 years: ",age)











