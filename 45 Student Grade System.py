students = {}


def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def add_student():
    name = input("Enter student name: ")

    if name in students:
        print("⚠️ Student already exists!")
        return

    try:
        python = float(input("Enter Python marks: "))
        dbms = float(input("Enter DBMS marks: "))
        dsa = float(input("Enter DSA marks: "))
        maths = float(input("Enter Maths marks: "))
        english = float(input("Enter English marks: "))

        marks = [python, dbms, dsa, maths, english]

        for mark in marks:
            if mark < 0 or mark > 100:
                print("⚠️ Marks must be between 0 and 100!")
                return

        students[name] = {
            "Python": python,
            "DBMS": dbms,
            "DSA": dsa,
            "Maths": maths,
            "English": english
        }

        print(f"✅ Student '{name}' added successfully!")

    except ValueError:
        print("⚠️ Please enter valid marks!")


def view_student():
    name = input("Enter student name: ")

    try:
        student = students[name]

        total = sum(student.values())
        average = total / len(student)
        grade = calculate_grade(average)

        print("\n================================")
        print(f"       STUDENT DETAILS")
        print("================================")
        print(f"Name: {name}")

        for subject, mark in student.items():
            print(f"{subject}: {mark}")

        print("--------------------------------")
        print(f"Total: {total}")
        print(f"Average: {average:.2f}")
        print(f"Grade: {grade}")
        print("================================")

    except KeyError:
        print("⚠️ Student not found!")


def view_all_students():
    if len(students) == 0:
        print("📋 No students available!")
        return

    print("\n================================")
    print("        ALL STUDENTS")
    print("================================")

    for name, student in students.items():
        total = sum(student.values())
        average = total / len(student)
        grade = calculate_grade(average)

        print(f"{name} → Average: {average:.2f} | Grade: {grade}")

    print("================================")


def search_student():
    name = input("Enter student name to search: ")

    if name in students:
        print(f"✅ Student '{name}' found!")
    else:
        print("❌ Student not found!")


def main():
    print("================================")
    print("    🎓 STUDENT GRADE SYSTEM")
    print("================================")

    while True:

        print("\n========== MENU ==========")
        print("1. Add Student")
        print("2. View Student")
        print("3. View All Students")
        print("4. Search Student")
        print("5. Exit")
        print("==========================")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                add_student()

            elif choice == 2:
                view_student()

            elif choice == 3:
                view_all_students()

            elif choice == 4:
                search_student()

            elif choice == 5:
                print("\n🎓 Thank you for using Student Grade System!")
                print("Goodbye! 👋")
                break

            else:
                print("⚠️ Invalid choice! Enter 1 to 5!")

        except ValueError:
            print("⚠️ Please enter a valid number!")


main()