
#q1
numbers = []
for i in range(1,6):
    number = int(input("Enter names: "))
    numbers.append(number)
    average = sum(numbers)/len(numbers)
print("Sum: ",sum(numbers))
print("Average: ",average)
print("Highest: ",max(numbers))
print("Lowest: ",min(numbers))

#q2
numbers = [i for i in range(1,11)]
odd_numbers = [number for number in numbers if number %2 != 0]
print(odd_numbers)

#q3
students = [
    ["Niharika",96,98,98],
    ["Priya",85,96,78],
    ["Kayani",85,96,86]
]
total1 = students[0][1]+students[0][2]+students[0][3]
average1 = total1/3
total2 = students[1][1]+students[1][2]+students[1][3]
average2 = total2/3
total3 = students[2][1]+students[2][2]+students[2][3]
average3 = total3/3
print(students[0][0],"- Total: ",total1," - Average ",average1)
print(students[1][0],"- Total: ",total2," - Average ",average2)
print(students[2][0],"- Total: ",total3," - Average ",average3)

#q4
names = []
for i in range(1,6):
    name = input("Enter names: ")
    names.append(name)

names.sort()
print(names)
upper_names = [ name.upper() for name in names]
print(upper_names)
print(names)

#q5
numbers = [i for i in range(1,21)]
for number in numbers:
    if number %3 ==0:
        print(number)
#q6
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for item in row:
        print(item, end=" ")
    print()
#q7
sentence = " I Love Python "
words = sentence.split()
for word in words:
    print(word)

#q8
marks = [80,75,90,85,70]
new_marks = [new_marks +5  for new_marks in marks]
print(new_marks)

#q9
numbers = [5,-3,8,-1,9,-7,2,-4]
positive_numbers = [i for i in numbers if i >= 0 ]
print(positive_numbers)
negative_numbers = [i for i in numbers if i<0]
print(negative_numbers)

#q10
friends = [
    ["Niha",19,"Nellore"],
    ["Priya",13,"Tada"],
    ["Kayani",44,"Chennai"]
]
print(f'Friend 1: {friends[0][0] } | Age: {friends[0][1]} | City: {friends[0][2]}')
print(f'Friend 2: {friends[1][0] } | Age: {friends[1][1]} | City: {friends[1][2]}')
print(f'Friend 3: {friends[2][0] } | Age: {friends[2][1]} | City: {friends[2][2]}')














































































































