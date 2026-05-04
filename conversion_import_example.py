"""Example program that uses the conversion module."""

import conversion

speed_in_km = float(input("How fast were you driving? "))
speed_in_mi = conversion.km2mi(speed_in_km)
print("Woah, that's like", round(speed_in_mi), "mph!")

temp_in_c = float(input("What was the temperature? "))
temp_in_f = conversion.cel2fah(temp_in_c)
print("That's", round(temp_in_f), "degrees Fahrenheit!")

# Weight conversions
kg = float(input("Enter weight in kilograms: "))
lb = conversion.kg2lb(kg)
print(kg, "kilograms is", round(lb, 2), "pounds")

pounds = float(input("Enter weight in pounds: "))
kg_result = conversion.lb2kg(pounds)
print(pounds, "pounds is", round(kg_result, 2), "kilograms")

# Length conversions
cm = float(input("Enter length in centimeters: "))
inches = conversion.cm2in(cm)
print(cm, "centimeters is", round(inches, 2), "inches")

inch_value = float(input("Enter length in inches: "))
cm_result = conversion.in2cm(inch_value)
print(inch_value, "inches is", round(cm_result, 2), "centimeters")

# Volume conversions
liters = float(input("Enter volume in liters: "))
gallons = conversion.l2gal(liters)
print(liters, "liters is", round(gallons, 2), "gallons")

gallon_value = float(input("Enter volume in gallons: "))
liters_result = conversion.gal2l(gallon_value)
print(gallon_value, "gallons is", round(liters_result, 2), "liters")

print(help(conversion))