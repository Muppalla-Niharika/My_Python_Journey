'''#lambda
double = lambda x: x ** 2
print(double(3))

add = lambda a,b : a +b 
print(add(9,12))

#map()
numbers = [1, 2, 3, 4, 5]
result = map(lambda x: x*2 , numbers)
print(list(result))

#filter()
numbers = [1, 2, 3, 4, 5, 6]
result = filter(lambda x: x%2 == 0,numbers)
print(list(result))

#sorted
numbers = [5, 2, 8, 1, 3]
result = sorted(numbers)
print(result)
students = [
    ("Niharika", 85),
    ("Anu", 95),
    ("Rahul", 75)
]
result1 = sorted(students, key=lambda x: x[1])
result2 = sorted(students, key=lambda x: x[1], reverse=True)
print(result1)
print(result2)

#min
numbers = [50, 20, 80, 10, 40]
print(min(numbers))
'''
students = [
    ("Niharika", 85),
    ("Anu", 95),
    ("Rahul", 75)
]
result = min(students, key=lambda x: x[1])
print(result)
#max
students = [
    ("Niharika", 85),
    ("Anu", 95),
    ("Rahul", 75)
]
result = max(students, key=lambda x: x[1])
print(result)


square = lambda x: x * x
print(square(5))

add = lambda a, b: a + b
print(add(10, 20))

numbers = [1, 2, 3, 4, 5]
result = map(lambda x: x * 2, numbers)
print(list(result))

numbers = [1, 2, 3, 4, 5, 6]
result = filter(lambda x: x % 2 == 0, numbers)
print(list(result))

students = [
    ("Niharika", 85),
    ("Anu", 95),
    ("Rahul", 75)
]

result = sorted(students, key=lambda x: x[1])

print(result)


