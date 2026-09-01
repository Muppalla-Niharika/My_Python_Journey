
'''
i = 1
while i <= 10:
    print(i)
    i = i + 1

i = 1
while i<=10:
    print("*"* i)
    i = i + 1


secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count  < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print('You Won!')
        break
else: 
    print("Sorry, You Failed")


#i didn't do the pblm !!!!
command = ""
while True:
    command = input("> ")
    if command.lower() == "start":
        print("Car Started...")
    elif command.lower() == "stop":
        print("Car Stopped...")
    elif command.lower() == "help":
        print("""
start - To start the car
stop  - To stop the car
quit  - To quit
        """)
    elif command.lower() == "quit":
        break
    else:
        print("Sorry, I don't understand that!")
'''


count = 1
while count <=10:
    print(count)
    count = count +1

number = int(input("Enter number: "))
count = 1
while count <=10:
    print(number , "x",count,"=",count*number)
    count = count + 1

number = int(input("Enter number: "))
while number != 0:
    number = int(input("Enter number: "))
print("Done")


total = 0
count = 1
while count <= 100:
    total = total + count
    count = count + 1
print(total)

password = input("enter password: ")
while password != "python123":
    password = input("enter password: ")
print("Welcome!")











































