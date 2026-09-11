'''
try:
    num = int(input("Enter a number: "))
    result = 10/num
    print(result)
except ValueError:
    print("Something went wrong")
except ZeroDivisionError:
    print("Can't be divided by zero")
else:
    print(f"Result is {result}")
finally:
    print("Program Finished")
'''
#exception + file handling
try:
    with open("my_file.txt", "w") as file:
        file.write("Niharika")
    with open("my_file.txt","r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found! Please check the file name")
finally:
    print("file operation is completed")










































































