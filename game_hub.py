import random

running =input("Would you like to play?: ")

while running == True:
    game_menu = input("1. Play Rock, Paper, Scissors", 
                      "2. Play Guessing Game", 
                      "3. Quit")
    game_choice = input("Enter your game choice (1,2,3): ")

#Rock, Paper, Scissors
    if user_choice == 1:
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
    
# Guessing Game
    elif user_choice == 2:
        test_input = input("Enable test mode? ")

        if test_input == "yes":
            test_mode = True
            secret_number = 50
            
        else:
            test_mode = False
            secret_number = random.randint(1, 100)

        attempts = 0
        MAX_ATTEMPTS = 10

        print("I am thinking of a number between 1 and 100.")

        while attempts < MAX_ATTEMPTS:
            
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
            
    else:
        game_choice == quit
        break
