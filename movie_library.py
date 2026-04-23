movies = {}

movies["Inception"] = [2010, "Sci-Fi", 9]

def add_movie(title, year, genre, rating):
    movies[title] = [year, genre, rating]
    print(f"Movie {title} added successfully.")

def display_movies():
    if not movies:
        print("No movies in the library.")
    else:
        print("Title\t\tYear\tGenre\tRating")
        for title, details in movies.items():
            print(f"{title}\t\t{details[0]}\t{details[1]}\t{details[2]}")

def remove_movie(title):
    if title in movies:
        del movies[title]
        print(f"Movie {title} removed.")
    else:
        print("Movie not found.")

def update_rating(title, new_rating):
    if title in movies:
        movies[title][2] = new_rating
        print(f"Rating for {title} updated.")
    else:
        print("Movie not found.")

def sort_movies():
    choice = input("Sort by title or rating? ").lower()

    if choice == "title":
        sorted_movies = sorted(movies.items())

    elif choice == "rating":
        sorted_movies = sorted(movies.items(), key=lambda item: item[1][2], reverse=True)

    else:
        print("Invalid sort option.")
        return
    
    for title, details in sorted_movies:
        print(f"{title}\t{details[0]}\t{details[1]}\t{details[2]}")

while choice == 1 or choice == 2 or choice == 3 or choice == 4 or choice == 5 or choice == 6:
    print("Welcome to the Movie Library Manager!")
    choice = 1
    print("1. Add Movie")
    print("2. View Movies")
    print("3. Remove Movie")
    print("4. Update Rating")
    print("5. Sort Movies")
    print("6. Quit")
    choice = input("Enter your choice (1-6): ")

    if choice not in ["1", "2", "3", "4", "5", "6"]:
        print(f"Invalid choice. Please enter a number between 1 and 6.")
        continue

    if choice == "1":
        title = input("Enter movie title: ").title()
        year = int(input("Enter release year: "))
        genre = input("Enter genre: ").title()
        rating = int(input("Enter rating (1-10): "))
        print(f"Movie '{title}' added successfully")
        add_movie(title, year, genre, rating)
        
    elif choice == "2":
        display_movies()

    elif choice == "3":
        remove_title = input("Enter movie title to remove: ").title()
        remove_movie(remove_title)

    elif choice == "4":
        title = input("Enter movie title: ").title()
        new_rating = float(input("Enter new rating: "))
        update_rating(title, new_rating)

    elif choice == "5":
        sort_movies()

    elif choice == "6":
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 6.")



