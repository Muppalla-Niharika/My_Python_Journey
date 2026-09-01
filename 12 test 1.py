
for i in range(1,11):
    print(i)
#in for loop 
for i in range(10,0,-1):
    print(i)

#in while loop 1 to 10
count = 1
while count <=10:
    print(count)
    count += 1

#in while loop 10 to 1
count = 10
while count >=1:
    print(count)
    count -=1          


for i in range(1,20):
    if i == 3:
        continue
    if i == 6:
        continue
    if i == 9:
        continue
    if i == 12:
        continue
    if i == 15:
        continue
    if i == 18:
        continue
    print(i)

#OR
for i in range(1, 21):
    if i % 3 == 0:
        continue

    print(i)


total = 0
for i in range(1,100):
    num = int(input("Enter number: "))
    if num ==0:
        break
    total += num
print(total)

#individual fail
for i in range(1,6):
    marks = int(input("Enter marks "))
    if marks >= 35:
        print("Pass")
    else: 
        print("Fail")

total = 0
for i in range(1,6):
    marks = int(input("Enter marks"))
    total += marks
average = total/5
print(total)
print(average)
if average >= 35:
    print("Pass")
else:
    print("Fail")















