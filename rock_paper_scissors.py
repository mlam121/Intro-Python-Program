import random

print("Welcome to Rock, Paper, Scissors!")

user_choice = ["rock", "paper", "scissors"]
computer_choice = random.choice(user_choice)

test_mode = input("Do you want to play in test mode? (y/n): ").lower() == 'y'
if test_mode:
    print("Test mode enabled. Computer will always choose rock.")
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    computer_choice = 'rock'
    print(f"Computer choice: rock")

if not test_mode:
    user_choice = input("Enter rock, paper, or scissors: ").lower()
    print(f"Computer choice: {computer_choice}")
    result = (f"Computer choice: {computer_choice}")

if user_choice == computer_choice:
    result = ("It's a tie!")

elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "paper" and computer_choice == "rock") or \
     (user_choice == "scissors" and computer_choice == "paper"):
    result = ("You win!")
else:
    result = ("Computer wins!")
