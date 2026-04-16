import random

test_input = input("Enable test mode? (yes/no): ").lower()

if test_input == "yes":
    test_mode = True
    secret_number = 50
else:
    test_mode = False
    secret_number = random.randint(1, 100)

attempts = 0
MAX_ATTEMPTS = 11

while attempts < MAX_ATTEMPTS:
    user_guess = int(input("Enter your guess (1-100): "))
    attempts += 1

    if user_guess == secret_number:
        print(f"Congratulations! You've guessed the number in {attempts} attempts!")
        break
    elif user_guess < secret_number:
        print("Too low! Try again.")  
    elif user_guess > secret_number:
        print("Too high! Try again.")

if attempts == MAX_ATTEMPTS and user_guess != secret_number:
    print(f"The secret number was {secret_number}.")
    