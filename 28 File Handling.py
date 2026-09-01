"""
file = open("my_file.txt", "w")
file.write("Hello Niharika")
file.write("\n you are learning python ?")
file.close()

file = open("mine_file.txt", "w")
file.write("Hi Kalyani!")
file.close()

file = open("my_file.txt", "a")
file.write("\n Do You love coding? ")
file.close()
with open("mine_file.txt", "a") as file:
    file.write("i love your cooking")

with open("my_file.txt", "r") as file:
    for line in file:
        print(line)

with open("test.txt", "w") as f:
    f.write("Line 1\n")
    f.write("Line 2\n")

with open("test.txt", "r") as f:
    content = f.read()
    print(content)
"""

file = open("my_info.txt", "w")
file.write("Niharika")
file.write("\n 19")
file.write("\n to achieve 15 LPA job")
file.close()
file = open("my_info.txt" , "r")
content = file.read()
print(content)

with open("movies.txt" ,"w") as file:
    file.write("Oye")
    file.write("\nbahubali")
    file.write("\nbahubali 2")
    file.write("\nseetha ramam")
    file.write("\nshyam singa roy")
with open("movies.txt" , "r") as file:
    content = file.read()
    print(content)

file = open("greeting.txt", "w")
file.write("hello!")
file.close()
file = open("greeting.txt", "a")
file.write("\nHow are you?")
file.close()
file = open("greeting.txt", "r")
content = file.read()
print(content)

file = open("notes.txt" , "w")
for i in range(3):
    text = input("text: ")
    file.write(text)
    file.write("\n")
file.close()
 
file = open("notes.txt" , "r")
content = file.read()
print(content)
file.close()


count = 1

with open("notes.txt", "r") as file:
    for line in file:
        print(f"Line {count}: {line.strip()}")
        count = count + 1 #idk about line.strip gpt told me this

diary_entry = input("Today's Diary Entry: ")
with open("diary.txt", "a") as file:
    file.write(diary_entry)
    file.write("\n")
with open("diary.txt", "r") as file:
    content = file.read()
    print(content)
    #gpt gave me becoz i'm bad for this question

    


























































































