import random
secret_number = random.randint(1,100)
guess = 0 #guess attempts 
attempts = 0
while guess != secret_number:
    try:
        guess = int(input("Guess the number: "))
        attempts +=1
        if guess == secret_number:
            print(f"Correct! You got it in {attempts} attempts!")
        elif guess > secret_number:
            print("Too High! Try Again !")
        else:
            print("Too Low!! Try Again !")
    except ValueError:
        print("Please Enter a valid number! ")