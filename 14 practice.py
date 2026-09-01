
for i in range(1, 6):
    print(f"Number is {i} and its square is {i*i}")

name = input("Enter Name: ")
for i in range(len(name)):
    print("Position",i,":",name[i])

count = 1
while count <=5:
    print("*" * count)
    count += 1

for i in range(1,6):
    name = (input("Enter name: "))
    print(name.upper())

word = input("Enter name: ")
print("Word: ",word)
print("Uppercase:",word.upper())
print("Lowercase:",word.lower())
print("Lenght:",len(word))

count = 0
for num in range (1,51):
    if num %3 == 0 and num %5 == 0:
        print(num)

word = input("Enter name: ")
for i in range(1,len(word)+1):
    print(word[:i])






    

    