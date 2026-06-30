question = [
    ["What is 5x6?",
     "30",
     "56",
     "65",
     "53",
     "A"],
    ["What is capital of India?",
     "mumbai",
     "delhi",
     "kolkata",
     "bombay",
     "B"],
    ["Python is a?",
     "programming language",
     "snake",
     "both",
     "none",
     "A"]
]
prize = [1000, 2000, 3000]
money = 0
if input("Do you want to play KBC? (yes/no): ").lower() == "yes":
    for i in range(len(question)):
        print(f"Question {i+1}: {question[i][0]}")
        print(f"A: {question[i][1]}")
        print(f"B: {question[i][2]}")
        print(f"C: {question[i][3]}")
        print(f"D: {question[i][4]}")
        answer = input("Enter your answer (A/B/C/D): ").upper()
        if answer == question[i][5]:
            money += prize[i]
            print(f"Correct! You have won Rs. {money}.")
        else:
            print("Incorrect answer. Game over.")
            break
else:
    print("Thank you for visiting KBC!")