"""Example program that uses the conversion module."""

import conversion

speed_in_km = float(input("How fast were you driving? "))
speed_in_mi = conversion.km2mi(speed_in_km)
print("Woah, that's like", round(speed_in_mi), "mph!")

temp_in_c = float(input("What was the temperature? "))
temp_in_h = conversion.cel2fah(temp_in_c)
print("That's", round(temp_in_h), "degrees Fahrenheit!")

print(help(conversion))