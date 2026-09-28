questions = [
    {
        "question": "What is the capital of India?",
        "options": ["Mumbai", "New Delhi", "Chennai", "Kolkata"],
        "answer": "New Delhi"
    },
    {
        "question": "What does CPU stand for?",
        "options": [
            "Central Processing Unit",
            "Computer Processing Unit",
            "Central Program Unit",
            "Computer Program Utility"
        ],
        "answer": "Central Processing Unit"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Venus"],
        "answer": "Mars"
    },
    {
        "question": "How many continents are there in the world?",
        "options": ["5", "6", "7", "8"],
        "answer": "7"
    },
    {
        "question": "Which gas do plants mainly absorb during photosynthesis?",
        "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"],
        "answer": "Carbon Dioxide"
    },
    {
        "question": "Who developed the theory of relativity?",
        "options": [
            "Isaac Newton",
            "Albert Einstein",
            "Galileo Galilei",
            "Nikola Tesla"
        ],
        "answer": "Albert Einstein"
    },
    {
        "question": "Which data structure follows FIFO?",
        "options": ["Stack", "Queue", "Tree", "Graph"],
        "answer": "Queue"
    },
    {
        "question": "What does HTML stand for?",
        "options": [
            "HyperText Markup Language",
            "HighText Machine Language",
            "Hyper Transfer Markup Language",
            "Home Tool Markup Language"
        ],
        "answer": "HyperText Markup Language"
    },
    {
        "question": "Which is the largest ocean on Earth?",
        "options": [
            "Atlantic Ocean",
            "Indian Ocean",
            "Pacific Ocean",
            "Arctic Ocean"
        ],
        "answer": "Pacific Ocean"
    },
    {
        "question": "Which number is a prime number?",
        "options": ["9", "15", "21", "17"],
        "answer": "17"
    }
]


score = 0

print("================================")
print("        🧠 QUIZ GAME")
print("================================")
print("Answer all 10 questions!")
print("Enter the option number (1-4).")


for number, question in enumerate(questions, start=1):

    print(f"\nQuestion {number}: {question['question']}")

    for i, option in enumerate(question["options"], start=1):
        print(f"{i}. {option}")

    while True:
        try:
            answer = int(input("Enter your answer (1-4): "))

            if answer < 1 or answer > 4:
                print("⚠️ Please enter a number between 1 and 4!")
                continue

            break

        except ValueError:
            print("⚠️ Please enter a valid number!")


    selected_answer = question["options"][answer - 1]

    if selected_answer == question["answer"]:
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Wrong!")
        print(f"The correct answer is: {question['answer']}")


print("\n================================")
print("          🏆 QUIZ RESULT")
print("================================")
print(f"Your score: {score}/10")


if score == 10:
    print("🎉 Perfect score! Amazing!")
elif score >= 7:
    print("⭐ Great job!")
elif score >= 5:
    print("👍 Good effort!")
else:
    print("📚 Keep practicing!")

print("================================")