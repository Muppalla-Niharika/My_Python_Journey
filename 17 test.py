
names = ['niha','priya','prerana','kalyani']
print(names[:])
print(names[1:-1])

#firsty we created list after asking user
names = []
for i in range(1,6):
    name = input("Enter Name: ")
    #we entered 5 names
    names.append(name)
    #we inserted them in list
for name in names:
    # so we need individual upper so use name to create upper each name separately
    print(name.upper())
#printing all names
print("names: ",names)

'''
#WRONG WE CAN USE MAX MIN SUM
mark = []
for i in range(1,6):
    marks = input("Enter marks: ")
    mark.append(marks)
    max = int(marks[0])
for marks in mark:
        if max > mark:
            max = mark
            print("Highest: ",max)
        low = mark[0]
for mark in marks:
        if mark < low:
            low = mark
            print("lowest: ",marks[0])
        total = marks
        sum = 0
        sum += total
        print("Sum: ",sum)
        Average = total / 5
        print("Average: ",Average)
'''

marks = []
for i in range(1, 6):
    mark = int(input("Enter mark: "))
    marks.append(mark)
print("Highest:", max(marks))
print("Lowest:", min(marks))
print("Sum:", sum(marks))
print("Average:", sum(marks) / len(marks))

numbers = [1,2,3,4,5,6,7,8,9,10]
for number in numbers:
    if number %2 !=0:
        continue
    if number %2 == 0:
        print(number)

name = input("Enter Name: ")
print("Original: ",name)
print("Reversed: ",name[::-1])
print("Uppercase: ",name.upper()) 
print("First 3 letters: ",name[0:3])
print(len(name))

subjects = ['Maths','Physics','Chemistry','Python','Html']
marks = [ 85,96,93,97,86]
for i in range(5):
    print("Subject",i+1,":",subjects[i],"- Marks: ",marks[i])



