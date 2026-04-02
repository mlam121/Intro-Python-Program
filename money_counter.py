print("Money Counter")

quarters = int(input("Enter the number of quarters: "))
dimes = int(input("Enter the number of dimes: "))
nickels = int(input("Enter the number of nickels: "))
pennies = int(input("Enter the number of pennies: "))


total = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)

# Round total
total = round(total, 2)

# Format as a string with exactly 2 decimal places
total_str = "{:.2f}".format(total)

# Print
print("You have: $" + total_str)
