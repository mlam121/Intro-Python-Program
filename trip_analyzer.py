# Get driver info
trip_name = input("Enter your trip name: ")
miles_driven = float(input("Enter the miles driven: "))
gallons_used = float(input("Enter the gallons used: "))
gas_cost = float(input("Enter the cost per gallon: "))

#Calculatations
mpg = miles_driven / gallons_used
total = gallons_used * gas_cost
cost_per_mile = total / miles_driven

#Number of characters
length = len(trip_name)
first_letter = trip_name[0]
last_letter = trip_name[-1]
first_three = (trip_name[0], trip_name[1], trip_name[2])
reversed_name = trip_name[::-1]

#Trip Summary
print("-- Trip Summary --")
print(f"Trip Name: {trip_name}")
print(f"Miles Per Gallon: {mpg}")
print(f"Total Gas Cost: {total}")
print(f"Cost Per Mile: {cost_per_mile}")

# Trip Name Analysis
print("-- Trip Name --")
print(f"Total letters: {length}")
print(f"First letter: {first_letter}")
print(f"Last Letter: {last_letter}")
print(f"First three letters: {first_three}")
print(f"Reversed name: {reversed_name}")