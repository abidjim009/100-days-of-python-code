# Quiz questions list
questions = [
    ["Which language was used to create Facebook?", "Python", "French", "JavaScript", "Php", "None", 4],
    ["Which company developed the Windows OS?", "Apple", "Microsoft", "Google", "IBM", "None", 2],
    ["Which of these is a Python framework?", "React", "Laravel", "Django", "Spring", "None", 3],
    ["Which planet is known as the Red Planet?", "Earth", "Mars", "Jupiter", "Saturn", "None", 2],
    ["What does CPU stand for?", "Central Process Unit", "Control Process Unit", "Central Processing Unit", "Central Performance Unit", "None", 3],
    ["Who is known as the father of computers?", "Bill Gates", "Charles Babbage", "Steve Jobs", "Alan Turing", "None", 2],
    ["What does HTTP stand for?", "HyperText Transfer Protocol", "HyperText Transmission Process", "High Text Transfer Protocol", "Hyper Transfer Text Protocol", "None", 1],
    ["Which is the largest ocean?", "Atlantic", "Pacific", "Indian", "Arctic", "None", 2],
    ["What is the square root of 64?", "6", "7", "8", "9", "None", 3],
    ["Which is the longest river in the world?", "Amazon", "Nile", "Yangtze", "Mississippi", "None", 2]
]

# Prize levels
levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]

# Map letter options to indices
option_map = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

money = 0

print("Welcome to the Quiz Game!\n")

for i in range(len(questions)):
    question = questions[i]
    print(f"\nQuestion {i+1} for Rs. {levels[i]}")
    print(f"a. {question[1]}          b. {question[2]}")
    print(f"c. {question[3]}          d. {question[4]}")

    # Take input
    reply = input("Enter your answer (a, b, c, d) or 0 to quit:\n").strip().lower()

    if reply == '0':
        money = levels[i - 1] if i > 0 else 0
        print("You chose to quit.")
        break

    if reply in option_map:
        selected_option = option_map[reply]
        if selected_option == question[-1]:
            print(f"Correct! You have won Rs. {levels[i]}")
            # Set safe levels
            if i == 4:
                money = 10000
            elif i == 9:
                money = 320000
            elif i == 14:
                money = 10000000
        else:
            print("Wrong answer!")
            break
    else:
        print("Invalid input. Please choose from a, b, c, d or 0.")
        break

print(f"\nYour take-home money is Rs. {money}")
