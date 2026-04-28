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