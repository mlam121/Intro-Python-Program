import random

def get_computer_choice(test_mode=False):
    if test_mode:
        return "rock"
    return random.choice(["rock", "paper", "scissors"])


def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    
    if (user == "rock" and computer == "scissors") or \
       (user == "paper" and computer == "rock") or \
       (user == "scissors" and computer == "paper"):
        return "You win!"
    
    return "Computer wins!"


def play_game():
    # Ask if test mode should be on
    test_input = input("Enable test mode? (yes/no): ").lower()
    test_mode = test_input == "yes"

    user_choice = input("Enter rock, paper, or scissors: ").lower()
    
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice!")
        return

    computer_choice = get_computer_choice(test_mode)

    print(f"Computer chose: {computer_choice}")
    print(determine_winner(user_choice, computer_choice))


play_game()