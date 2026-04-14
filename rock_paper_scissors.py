import random

print("Welcome to Rock, Paper, Scissors!")

user_choice = ["rock", "paper", "scissors"]
computer_choice = random.choice(user_choice)

test_mode = input("Do you want to play in test mode? (y/n): ").lower() == 'y'
if test_mode: 'y'
computer_choice = 'rock'

if test_mode: 'n'
computer_choice = random.choice(user_choice)

print("Enter rock, paper, or scissors: ", user_choice)
print("Computer chose: ", computer_choice)

