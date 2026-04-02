import random

word = input("Enter a word: ")
letters = list(word)
random.shuffle(letters)
scrambled = "".join(letters)

print(f"Original word: {word:>10}")
print(f"Scrambled word: {scrambled:>10}")