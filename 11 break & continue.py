
for item in range(1,20):
    if item == 13:
        break
    print(item)

for item in range(1,20):
    if item %2 !=0:
        continue
    print(item)

#CAN'T YOU DO THIS IDIOT !!!!! LEARN THIS
total = 0
for i in range(1,100):
    num = int(input("Enter Number: "))
    if num <0:
        break
    total += num
print(total)


number =5
count = 1
for count in range(1,11):
    if count==3:
        continue
    if count==7:
        continue
    print(number,"X",count,"=",number*count)

total = 0
for i in range(1,6):
    marks = int(input("Enter marks: "))
    total +=marks
print("Total: ",total)
print("Average: ",total/5)










































































