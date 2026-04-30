# list_practice.py
# Chapter 10 Guided Activity - List Practice

# Task 1
colors = ["red", "green", "blue", "yellow"]
print(colors)

# Task 2
colors.append("purple")

# Task 3
for color in colors:
    print("Color:", color)

# Task 4
user_input = input("Enter a color: ")
if user_input in colors:
        print("Correct guess!")
else:
        print("Try again.")

# Task 5
points = [[2, 3], [5, 6], [8, 9]]
print(points)

# Task 6
print(points[0])
print(points[1])

# Task 7
for point in points:
    for i in range(len(point)):
        point[i] = point[i] * 2

print(points)

# Task 8
squares = [x**2 for x in range(1, 11)]
print(squares)

# Task 9
colors.sort()
print(colors)

#color list


