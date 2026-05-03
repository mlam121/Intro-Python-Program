# dictionary_practice.py
# Chapter 10 Guided Activity - Dictionary Practice

# Task 1: Creating Dictionaries
capitals = {
    "USA": "Washington, D.C.",
    "France": "Paris",
    "Japan": "Tokyo"
}

print("Task 1 Output:")
print(capitals)
print()  # blank line for readability


# Task 2: Dictionary Methods
capitals["Germany"] = "Berlin"

print("Task 2 Output:")
print(capitals)
print()


# Task 3: Iterating Over a Dictionary
print("Task 3 Output:")
for country, capital in capitals.items():
    print(f"The capital of {country} is {capital}.")
print()


# Task 4: Dictionary Nesting
library = {
    "Fantasy": {
        "Harry Potter": "J.K. Rowling"
    },
    "Sci-Fi": {
        "Dune": "Frank Herbert"
    }
}

print("Task 4 Output:")
print(library)