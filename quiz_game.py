# animal_quiz.py
# Chapter Project - Animal Quiz Program

import random


# Task 1: Creating the Question Bank (List of Dictionaries)
questions = [
    {
        "question": "What is the largest land animal?",
        "answer": "elephant",
        "type": "string"
    },
    {
        "question": "How many legs does a spider have?",
        "answer": 8,
        "type": "number"
    },
    {
        "question": "What animal is known as the King of the Jungle?",
        "answer": "lion",
        "type": "string"
    },
    {
        "question": "How many hearts does an octopus have?",
        "answer": 3,
        "type": "number"
    },
    {
        "question": "What is the fastest land animal?",
        "answer": "cheetah",
        "type": "string"
    }
]

print("Task 1 Output:")
print("Question bank created with", len(questions), "questions.")
print()


# Task 2: Function to Ask One Question (with 3 attempts)
def ask_question(q):
    attempts = 0

    while attempts < 3:
        user_answer = input(q["question"] + " ")

        # Handle number answers
        if q["type"] == "number":
            try:
                user_answer = int(user_answer)
            except:
                print("Please enter a number.")
                attempts += 1
                continue

        # Handle string answers (case-insensitive)
        if q["type"] == "string":
            user_answer = user_answer.lower()

        # Check answer
        if user_answer == q["answer"]:
            print("Correct!\n")
            return 1
        else:
            print("Incorrect.")
            attempts += 1
            print("Attempts left:", 3 - attempts)

    print("Out of attempts! Correct answer was:", q["answer"], "\n")
    return 0


# Task 3: Function to Run the Quiz
def run_quiz():
    score = 0

    print("Task 3 Output:")
    print("Welcome to the Animal Quiz!\n")

    random.shuffle(questions)

    for q in questions:
        score += ask_question(q)

    print("Quiz finished!")
    print("Final Score:", score, "/", len(questions))
    print()


# Task 4: Running the Program
print("Task 4 Output:")
run_quiz()