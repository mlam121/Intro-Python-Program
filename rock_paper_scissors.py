import random

test_input = input("Enable test mode? (yes/no): ").lower()

if test_input == "yes":
    test_mode = True
else:
    test_mode = False

user_choice = input("Enter rock, paper, or scissors: ").lower()


if test_mode:
    computer_choice = "rock"
else:
    computer_choice = random.choice(["rock", "paper", "scissors"])


if user_choice == computer_choice:
    result = "It's a tie!"

elif user_choice == "rock":
    if computer_choice == "scissors":
        result = "You win!"
    else:
        result = "You wins!"

elif user_choice == "paper":
    if computer_choice == "rock":
        result = "You win!"
    else:
        result = "Computer wins!"

elif user_choice == "scissors":
    if computer_choice == "paper":
        result = "You win!"
    else:
        result = "You lose!"

else:
    result = "Invalid input!"

print("Computer chose:", computer_choice)
print(result)