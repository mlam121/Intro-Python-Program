print("Money Counter")

Quarters = int(input("Enter the number of quarters: "))
Dimes = int(input("Enter the number of dimes: "))
Nickels = int(input("Enter the number of nickels: "))
Pennies = int(input("Enter the number of pennies: "))


total = (Quarters * 0.25) + (Dimes * 0.10) + (Nickels * 0.05) + (Pennies * 0.01)

# Round total
total = round(total, 2)

# Format as a string with exactly 2 decimal places
total_str = "{:.2f}".format(total)

# Print
print("You have: $" + total_str)
