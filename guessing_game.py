import random

test_input = input("Enable test mode? ")

if test_input == "yes":
    test_mode = True
    secret_number = 50
    
else:
    test_mode = False
    secret_number = random.randint(1, 100)

attempts = 0
MAX_ATTEMPTS = 10

while attempts < MAX_ATTEMPTS:
    print("I am thinking of a number between 1 and 100.")
    user_guess = int(input("Enter your guess: "))
    attempts += 1

    if user_guess == secret_number:
        print(f"Correct! You guessed guessed it in {attempts} attempts.")
        break
    elif user_guess < secret_number:
        print("Too low!")  
    elif user_guess > secret_number:
        print("Too high!")

if user_guess != secret_number:
    print(f"The secret number was {secret_number}.")
    