# Welcome message
print("Welcome to Chapter 1 practice!")

# Get user information
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("Enter your height in inches: ")
height = float(input())

# Print user info
print("Hello " + name + "! Next year you will be", age + 1, "years old.")
print(name, "is", height, "inches tall.")

# Simple arithmetic
years_to_100 = 100 - age
print("You will turn 100 in", years_to_100, "years.")

# String length
name_length = len(name)
print("Your name has", name_length, "letters.")

# Combine calculations
print("Next year, your age multiplied by 2 is", (age + 1) * 2)

