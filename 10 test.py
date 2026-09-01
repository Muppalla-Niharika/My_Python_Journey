
for numbers in range(1,21):
    if numbers == 13:
        break
    print(numbers)

#example 
for numbers in range(2,20,2):
    print(numbers)

for numbers in range(1,20,2):
     print(numbers)

for i in range(1,21):
    if i %2 != 0:
        continue
    print(i)

total = 0
for i in range(1,100):
    num = int(input("Enter number: "))
    if num <0:
        break
    total += num
print(total)

number = 5
for i in range(1,11):
    if i == 3:
        continue
    if i == 7:
        continue
    print(number,"x",i,"=",i*number)

total = 0
for i in range(1,6):
    marks = int(input("Enter marks: "))
    total += marks
print(total)
print(total/5)









