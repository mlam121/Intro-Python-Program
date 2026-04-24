import random

# Start by asking the user
start_input = input("Would you like to play? (yes/no): ").lower()
running = True

while running:
    print("\nGame Menu:")
    print("1. Play Rock, Paper, Scissors")
    print("2. Play Guessing Game")
    print("3. Quit")

    game_choice = input("Enter your game choice (1, 2, or 3): ")

# Rock, Paper, Scissors
    if game_choice == "1":
        test_input = input("Enable test mode? (yes/no): ").lower()
        test_mode = test_input == "yes"

        user_choice = input("Enter rock, paper, or scissors: ").lower()

        if test_mode:
            computer_choice = "rock"
        else:
            computer_choice = random.choice(["rock", "paper", "scissors"])

        if user_choice == computer_choice:
            result = "It's a tie!"
        elif user_choice == "rock":
            result = "You win!" if computer_choice == "scissors" else "You lose!"
        elif user_choice == "paper":
            result = "You win!" if computer_choice == "rock" else "You lose!"
        elif user_choice == "scissors":
            result = "You win!" if computer_choice == "paper" else "You lose!"
        else:
            result = "Invalid choice. Try again."

        print("Computer chose:", computer_choice)
        print(result)

# Guessing Game
    elif game_choice == "2":
        test_input = input("Enable test mode? (yes/no): ").lower()

        if test_input == "yes":
            secret_number = 50
        else:
            secret_number = random.randint(1, 100)

        attempts = 0
        MAX_ATTEMPTS = 10

        print("I am thinking of a number between 1 and 100.")

        while attempts < MAX_ATTEMPTS:
            try:
                user_guess = int(input("Enter your guess: "))
                attempts += 1

                if user_guess == secret_number:
                    print(f"Correct! You guessed it in {attempts} attempts.")
                    break
                elif user_guess < secret_number:
                    print("Too low!")
                else:
                    print("Too high!")
            except ValueError:
                print("Please enter a valid number.")

        if attempts == MAX_ATTEMPTS and user_guess != secret_number:
            print(f"The secret number was {secret_number}.")

    # Quit
    elif game_choice == "3":
        print("Goodbye!")
        running = False 

    else:
        print("Invalid choice. Try again.")
