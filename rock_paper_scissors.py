import random

print("Welcome to Rock, Paper, Scissors!")
print("Do you want to run the test mode? (y/n)")
test_mode = input("Enter 'y' for test mode or 'n' to play normally: ").lower()

def test_mode():
    test_mode = input().lower()
    if user_input == 'y':
        user_choice = ['rock', 'paper', 'scissors']
        computer_choice = random.choice(user_choice)
        print(f"Computer choice (test mode): {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)
    if test_mode == 'n':
        user_choice = ['rock', 'paper', 'scissors']
        computer_choice = random.choice(user_choice)
        print(f"Computer choice: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)


def user_choice():
    choices = ['rock', 'paper', 'scissors']
    user_input = input("Enter your choice (rock, paper, scissors): ").lower()
    while user_input not in choices:
        print("Invalid choice. Please try again.")
        user_input = input("Enter your choice (rock, paper, scissors): ").lower()
    return user_input

def computer_choice(test_mode=False):
    choices = ['rock', 'paper', 'scissors']
    if test_mode:
        return 'rock'
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"