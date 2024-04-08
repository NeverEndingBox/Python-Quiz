
questions = [ 
    {   #1
        "question": "How many time zones are ther in Russia?",
        "options": ["A: 1", "B: 7", "C: 11", "D: 13"],
        "answer": "C"
    },
   {    #2
        "question": "What's the national flower of Japan?", 
        "options": ["A:Tsubaki", "B:Cherry Blossom", "C:Morning glory", "D:Kochia"],
        "answer": "B"
    },
    {    #3
        "question": "How many stripes are ther on the US flag?", 
        "options": ["A:10", "B:13", "C:18", "D:22"],
        "answer": "B"
    },
    {    #4
        "question": "What country has the most islands in the world?", 
        "options": ["A:The united kingdom", "B:New zealand", "C:Greece", "D:Sweden"],
        "answer": "D"
    },
    {    #5
        "question": "What is the smallest country in the world?", 
        "options": ["A:The Vatican", "B:Luxembourg", "C:Andorra", "D:San Marino"],
        "answer": "A"
    },
    {    #6
        "question": "What is the name of the longest river in the world?", 
        "options": ["A:Amazon River", "B:Yenisei", "C:Nile", "D:Yellow River"],
        "answer": "C"
    },
    {    #7
        "question": "Which of the following empires had no written language?", 
        "options": ["A:Incan", "B:Aztec", "C:Egyptian", "D:Roman"],
        "answer": "A"
    },
    {    #8
        "question": "What is the capital city of Canada?", 
        "options": ["A:Toronto", "B:Vancouver", "C:Ottawa", "D:Moncton"],
        "answer": "C"
    },
    {    #9
        "question": "What country has the highest population?", 
        "options": ["A:The United States", "B:China", "C:India", "D:Russia"],
        "answer": "B"
    },
    {    #10
        "question": "In which continent is the Yuma desert?", 
        "options": ["A:Africa", "B:South America", "C:Asia", "D:North America"],
        "answer": "D"
    },
]

# This function will define the quiz code on launch
def run_quiz(questions):
    score = 0  # Initialize score to 0 and create a variable "score" to store the value of correct answers

    # Loop through all the questions. This will follow all the questions above until finished
    for question in questions:
        print("\n" + question["question"])  # Print the question
        for option in question["options"]:
            print(option)  # Print all the answer options

        # Get the user's answer
        user_answer = input("Enter your answer (A, B, C, or D): ").strip().upper()

        # Check if the user's answer is correct
        if user_answer == question["answer"]:
            print("Correct!")
            score += 1  # Increment score if correct
        else:
            print("Wrong answer.")

    # Print the final score from the stored variable
    print(f"\nYou got {score} out of {len(questions)} questions correct!")

    # Run the quiz
    run_quiz(questions)