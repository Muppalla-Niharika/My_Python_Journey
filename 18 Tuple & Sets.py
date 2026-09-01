
days = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
print("First day: ",days[0])
print("Last day: ",days[-1])
print("Total days: ",len(days))

months = ("January","February","March","April","May","June","July","August","September","October","November","December")
print("First month: ",months[0])
print("Last month: ",months[-1])
print("Total months: ",len(months))

numbers = {1, 2, 3, 2, 4, 1, 5, 3, 6}
print(numbers)

fruits = {"apple","banana","mango","Orange","Kiwi"}
fruits.add("grapes")
fruits.remove("banana")
print("apple" in fruits)
print(fruits)

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))
num5 = int(input("Enter number 5: "))
numbers = (num1, num2, num3, num4, num5)

print("Your numbers: ",numbers)
print("First: ",numbers[0])
print("Last: ",numbers[-1])
print("Total count: ",len(numbers))


names = ["Niharika", "Priya", "Niharika", "Sravani", "Priya"]
print(set(names))

movies = ("Oye", "RRR", "Pushpa", "KGF", "Bahubali")

for i in range(len(movies)):
    print(i + 1, ".", movies[i])



















































