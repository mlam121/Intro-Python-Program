import random

test_mode = input("Do you want to run in test mode? (yes/no): ")
user_choice = input(["rock", "paper", "scissors"])
computer_choice = random.choice(["rock", "paper", "scissors"])

def test_mode():
    print("Running in test mode...")
    user_choice = "rock"
    computer_choice = "scissors"
    print(f"User choice: {user_choice}")
    print(f"Computer choice: {computer_choice}")
    determine_winner(user_choice, computer_choice)




