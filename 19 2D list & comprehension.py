
marks = [
    [85, 90, 78],
    [92, 88, 95],
    [70, 75, 80]
]

for row in marks:
    for mark in row:
        print(mark, end=" ")
    print()

num = [i for i in range(1,100)]
print(num)

students = [
    ["Niharika", 85, 90],
    ["Priya", 92, 88],
    ["Sravani", 78, 95]
]
average1 = (students[0][1] + students[0][2]) / 2
average2 = (students[1][1] + students[1][2]) / 2
average3 = (students[2][1] + students[2][2]) / 2
print(students[0][0]," - Average: ",average1)
print(students[1][0]," - Average: ",average2)
print(students[2][0]," - Average: ",average3)

tables = [
    [2, 4, 6, 8, 10],
    [3, 6, 9, 12, 15],
    [5, 10, 15, 20, 25]
]
print(tables[0])
print(tables[1])
print(tables[2])

numbers = [i for i in range(1,11)]
squares = [i**2 for i in range(1,11)]
even_numbers = [i for i in range(1,21) if i %2 == 0]
print(numbers)
print(squares)
print(even_numbers)

names = ["niharika", "priya", "sravani", "divya"]
upper_names = [name.upper() for name in names]
print(upper_names)

numbers = [12, 67, 34, 89, 45, 91, 23, 78]
greater_numbers = [number for number in numbers if number > 50]
print(greater_numbers)

schedule = [
    ["Monday", "Python"],
    ["Tuesday", "HTML"],
    ["Wednesday", "Python"],
    ["Thursday", "HTML"],
    ["Friday", "Python"]
]
print(schedule[0][0],"->",schedule[0][1])
print(schedule[1][0],"->",schedule[1][1])
print(schedule[2][0],"->",schedule[2][1])
print(schedule[3][0],"->",schedule[3][1])
print(schedule[4][0],"->",schedule[4][1])

























