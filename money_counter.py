print("Enter the number of quarters, dimes, nickels, and pennies.")

Quarters = int(input("Enter the number of quarters: "))
Dimes = int(input("Enter the number of dimes: "))
Nickels = int(input("Enter the number of nickels: "))
Pennies = int(input("Enter the numner of pennies: "))

total = (quarters * .25) + (dimes * .10) + (nickels * .05) + (pennies * .01)

print("You have: " total)
