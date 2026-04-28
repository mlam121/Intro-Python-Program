movies = {}

def add_movie(title, year, genre, rating):
    movies[title] = [year, genre, rating]
    print(f"Movie '{title}' added successfully.")

def display_movies():
    if not movies:
        print("No movies in the library.")
    else:
        print("\nTitle                         Year    Genre           Rating")
        print("---------------------------------------------------------------")
        for title, details in movies.items():
            print(f"{title:<18} {details[0]:<6} {details[1]:<12} {details[2]}")
        print()

def remove_movie(title):
    if title in movies:
        del movies[title]
        print(f"Movie '{title}' removed.")
    else:
        print("Movie not found.")

def update_rating(title, new_rating):
    if title in movies:
        movies[title][2] = new_rating
        print(f"Rating for '{title}' updated.")
    else:
        print("Movie not found.")

def sort_movies():
   sorted_movies = dict(sorted(movies.items()))
   print("Movies sorted by title.")

   if not sorted_movies:
       print("No movies in the library.")
   else:
       print("\nTitle                         Year    Genre           Rating")
       print("--------------------------------------")
       for title, details in sorted_movies.items():
           print(f"{title:<18} {details[0]:<6} {details[1]:<12} {details[2]}")
       print()

def main():
    print("Welcome to the Movie Library Manager!")

    choice = 1

    while choice >= 1 and choice <= 6:
        print("\n1. Add Movie")
        print("2. View Movies")
        print("3. Remove Movie")
        print("4. Update Rating")
        print("5. Sort Movies")
        print("6. Quit")

        try:
            choice = int(input("Enter your choice (1-6): "))
        except ValueError:
             print("Invalid choice. Please enter a number 1 through 6.")
             continue

        if choice == 1:
            title = input("Enter movie title: ").title()
            year = int(input("Enter release year: "))
            genre = input("Enter genre: ").title()
            rating = int(input("Enter rating (1-10): "))

            add_movie(title, year, genre, rating)

        elif choice == 2:
            display_movies()

        elif choice == 3:
            title = input("Enter the movie title to remove: ").title()
            remove_movie(title)

        elif choice == 4:
            title = input("Enter movie title: ").title()
            new_rating = int(input("Enter new rating (1-10): "))
            update_rating(title, new_rating)

        elif choice == 5:
            sort_movies()

        elif choice == 6:
            print("Exiting program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()