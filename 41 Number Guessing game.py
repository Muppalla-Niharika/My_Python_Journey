import random
print("Welcome to Number Guessing Game!")
print("Choose difficulty:")
print("1 — Easy (1 to 50)")
print("2 — Medium (1 to 100)")
print("3 — Hard (1 to 200)")
level = input("Enter 1, 2 or 3: ")
if level == "1":
    secret_number = random.randint(1, 50)
    max_num = 50
elif level == "2":
    secret_number = random.randint(1, 100)
    max_num = 100
else:
    secret_number = random.randint(1, 200)
    max_num = 200
guess = 0
attempts = 0
print(f"I am thinking of a number between 1 and {max_num}!")
while guess != secret_number:
    try:
        guess = int(input(f"Guess the number between 1 and {max_num}: "))
        attempts += 1
        if guess == secret_number:
            print(f"Correct! You got it in {attempts} attempts!")
        elif guess > secret_number:
            print("Too High! Try Again !")
        else:
            print("Too Low!! Try Again !")
    except ValueError:
        print("Please Enter a valid number! ")