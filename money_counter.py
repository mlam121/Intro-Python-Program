print("Money Counter")
print("Enter the number of quarters, dimes, nickels, and pennies.")

Quarters = int(input("Enter the number of quarters: "))
Dimes = int(input("Enter the number of dimes: "))
Nickels = int(input("Enter the number of nickels: "))
Pennies = int(input("Enter the numner of pennies: "))

total = (Quarters * .25) + (Dimes * .10) + (Nickels * .05) + (Pennies * .01)

# Round total
total = round(total, 2)

# Format as a string with exactly 2 decimal places
total_str = "{:.2f}".format(total)

# Print
print("You have: $" + total_str)
