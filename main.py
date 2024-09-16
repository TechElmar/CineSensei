import requests
import random

# Replace 'your_api_key_here' with your TMDb API key
API_KEY = '2c70d1ad4b2b76126ecf89e8b8ed34e6'
BASE_URL = 'https://api.themoviedb.org/3'

# Genre dictionary
GENRES = {
    28: 'Action',
    12: 'Adventure',
    16: 'Animation',
    35: 'Comedy',
    80: 'Crime',
    99: 'Documentary',
    18: 'Drama',
    10751: 'Family',
    14: 'Fantasy',
    36: 'History',
    27: 'Horror',
    10402: 'Music',
    9648: 'Mystery',
    10749: 'Romance',
    878: 'Science Fiction',
    10770: 'TV Movie',
    53: 'Thriller',
    10752: 'War',
    37: 'Western'
}


def get_movies_by_genre(genre_id):
    url = f"{BASE_URL}/discover/movie?api_key={API_KEY}&with_genres={genre_id}&sort_by=popularity.desc"
    response = requests.get(url)
    print(f"Request URL: {url}")  # Debugging
    print(f"Response Status Code: {response.status_code}")  # Debugging
    return response.json()


def print_recommendations(data):
    print("\nRecommended Movies by Genre:")
    if 'results' not in data or not data['results']:
        print("No results found.")
        return

    # Filter movies to only include those with a sufficient number of votes
    filtered_movies = [item for item in data['results'] if
                       item['vote_count'] > 50]  # Adjust vote count threshold as needed

    if not filtered_movies:
        print("No movies with sufficient votes found.")
        return

    for item in filtered_movies:
        # Convert vote average to percentage
        rating_percentage = item['vote_average'] * 10
        print(f"- {item['title']} (Rating: {rating_percentage:.0f}%)")


def get_genre_choice():
    print("Please choose a genre from the following list:")
    for id, genre in GENRES.items():
        print(f"{id}: {genre}")
    choice = input("\nEnter the number corresponding to your preferred genre:\n").strip()
    try:
        genre_id = int(choice)
        return GENRES.get(genre_id, None), genre_id
    except ValueError:
        return None, None


def main():
    print("Welcome to the CineSensei Movie Recommendation System!")

    # Get user preferences
    genre_name, genre_id = get_genre_choice()

    if genre_id:
        # Get movies for the selected genre
        movies_data = get_movies_by_genre(genre_id)

        if movies_data:
            print_recommendations(movies_data)

            # Prompt user for random recommendation
            if 'results' in movies_data and movies_data['results']:
                user_choice = input(
                    "\nCan't decide? Let us pick a movie for you! (yes/no)\n").strip().lower()
                if user_choice == 'yes':
                    filtered_movies = [item for item in movies_data['results'] if
                                       item['vote_count'] > 50]  # Adjust vote count threshold as needed
                    if filtered_movies:
                        random_movie = random.choice(filtered_movies)
                        # Convert vote average to percentage
                        rating_percentage = random_movie['vote_average'] * 10
                        print(f"\nRandomly Selected Movie: {random_movie['title']} (Rating: {rating_percentage:.0f}%)")
                    else:
                        print("No movies with sufficient votes available for a random recommendation.")
                else:
                    print("Feel free to review the list and pick a movie yourself!")
            else:
                print("No movies available for the selected genre.")
        else:
            print("Failed to retrieve movie data.")
    else:
        print("Invalid genre choice. Please select a valid genre.")


if __name__ == "__main__":
    main()
