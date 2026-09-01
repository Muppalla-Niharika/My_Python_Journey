#q1
def check_password(password):
    password_length = len(password)
    if password_length >=8:
        return "Strong"
    else:
        return "Weak"
print(check_password("Niharika@"))
print(check_password("Gopi12"))

#q2
def temperature_status(temperature):
    if temperature >38:
        return "Fever"
    elif 36 <= temperature <=38:
        return "Normal"
    else:
        return "Low"
print(temperature_status(37))

#q3
def simple_interest(principal,rate,time):
    interest = (principal*rate*time)/100
    return interest
print(simple_interest(15000,5,2))

#q4
def leap_year_check(year):
    if year %4==0:
        return True
    else:
        return False
print(leap_year_check(2024))
print(leap_year_check(1997))
print(leap_year_check(2007))
print(leap_year_check(2025))

#q5
def max_of_three(x,y,z):
    if x>=y and x>=z:
        return x
    elif y>=x and y>=z:
        return y
    else:
        return z
print(max_of_three(10,25,15))
print(max_of_three(66,38,78))
print(max_of_three(33,18,96))

#q6
def ticket_price(age):
    if 0 <= age < 5:
        return 0
    elif 5 <= age <=12:
        return 50
    elif 13 <= age <=60:
        return 100
    else:
        return 70
print(ticket_price(2))
print(ticket_price(5))
print(ticket_price(7))
print(ticket_price(14))
print(ticket_price(60))
print(ticket_price(73))

#q7
def calculate_emi(loan_amount,months=12):
    emi = loan_amount/months
    return emi
print(calculate_emi(50000))
print(calculate_emi(153000,6))

#q8
def vowel_or_consonant(letter): 
    if letter in "aeiou":
        return "Vowel"
    else:
        return "Consonent"
print(vowel_or_consonant("k"))
print(vowel_or_consonant("a"))

#q9
def shopping_bill(amount):
    if amount > 5000:
        discount = amount*20/100
    elif 2000 >= amount <= 5000:
        discount = amount*10/100
    else:
        discount =0
    final_amount = amount - discount
    return final_amount
print(shopping_bill(1890))
print(shopping_bill(2200))
print(shopping_bill(9600))

#q10
def internship_eligibility(cgpa, backlogs):
    if cgpa >= 7.0 and backlogs == 0:
        return "Eligible", "You can apply for top companies!"
    elif cgpa >= 6.0 and backlogs == 0:
        return "Eligible", "You can apply for mid companies!"
    else:
        return "Not Eligible", "Clear backlogs and improve CGPA first!"
status, message = internship_eligibility(8.5, 0)
print("Status:", status)
print("Message:", message)




















