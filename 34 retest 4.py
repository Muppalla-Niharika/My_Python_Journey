

#write a code to know the max number in a list of numbers
numbers = [10,28,35,42,8,62,94,28,98]
max = numbers[0]
for num in numbers:
    if num > max:
        max = num
print(max)

#using max()
numbers = [10,28,35,42,8,62,94,28,98,99]
maximum = max(numbers)
print(maximum) #don't print abov code and this same time 


#create list of 5 marks and print , first mark, last mark, highest, lowest
marks = [85,99,84,88,86]
print(marks[0])
print(marks[4])
print(max(marks))
print(min(marks))

#append - inserting the elements into list at the end only
number = []
for i in range(21):
    number.append(i)
print(number)

numbers = []
for i in range(1,20):
    numbers.append(i)
print(numbers)

#append,insert,pop,remove,clear,sort,reverse,count,index
names = ["Niharika", "Gopi","Gopi" ,"Priya", "Kalyani"]
names.append("Rayudu")
names.insert(2,"Harika")
names.remove("Niharika")
names.pop()
print(names.count("Gopi"))
print(names.index("Kalyani"))
names.reverse()
print(names)

#tuple
names = ("Niha","Gopi","Jyothi")
print(names[0])
print(names[-1])
print(len(names))


#set - unordered elemenets where duplicates are removed automatically
names = ["Niharika", "Gopi","Gopi" ,"Priya", "Kalyani"]
names.append("Rayudu")
names.remove("Priya")
print("Priya" in names) #checking wether priya is there or not in the existing list
print("Niharika" in names)
print(names)

#conveert a list into set with duplicates on
names = ["Niharika", "Gopi","Gopi" ,"Priya", "Kalyani"]
print(set(names))

 
#2D list - making lot of lists in one variable
marks =[
    [85,96,92],
    [86,83,94],
    [58,62,74]]
print(marks[0][0])
print(marks[0])


marks =[
    [85,96,92],
    [86,83,94],
    [58,62,74]]
for row in marks: #each row becomes a row like row = [85,96,92] like this every row
    for mark in row: #from each row take every mark individually
        print(mark, end =" ") #end is used to tell to python print it as it is don't got to next line
    print()

#list comprehension
numbers = [i for i in range(1,100)]
print(numbers)


names = ["Niharika", "Gopi","Gopi" ,"Priya", "Kalyani"]
print(set(names))
upper_names = [name.upper() for name in names]
print(upper_names)


#sentence splitting
sentence = "Niharika is a 3RD year Student"
words = sentence.split()
print(sentence)
print(words) #same line but each becomes one one variable

sentence = "Niharika is a 3RD year Student"
words = sentence.split()
for word in words:
    print(word) #prints in diff line

#dictionaries
student = {
    "Name": "Niharika",
    "Age": 18,
    "Course":"CSE-AIML"
}
student["College"] = "Kalasalingam"
student["Age"] = 19
del student["Course"]
print("Course" in student)
print(student)

for key in student:
    print(key)
for key in student:
    print(student[key])
for key,value in student.items():
    print(f"{key}:{value}")
print(student.keys())
print(student.values())
print(student.items())
print(len(student))
removed = student.pop("Age")
print(removed)


#q9
list = [3, 1, 4, 1, 5]
list.sort()
print(list)

lst = [1, 2, 3]
lst.extend([4,5])
print(lst)

lst = [i**2 for i in range(11)]
print(lst)

list = [
[0,0,0],
[0,0,0],
[0,0,0]]
print(list)

d = {"name": "Niha", "age": 20}
print(d.get("City", "Not Found"))

d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
d1.update(d2)
print(d1)

a = {1,2,3}
b = {2,3,4}
print(a|b)
print(a&b)
























































































