# dictionary_practice.py
# Chapter 10 Guided Activity - Dictionary Practice

# Task 1
capitals = {
    "USA": "Washington, D.C.",
    "France": "Paris",
    "Japan": "Tokyo"
}
print(capitals)

# Task 2
capitals["Germany"] = "Berlin"
print(capitals)

# Task 3
for country, capital in capitals.items():
    print(f"The capital of {country} is {capital}")