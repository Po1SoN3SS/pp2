# Dictionary of movies
movies_dict = [
    {
        "name": "Usual Suspects",
        "imdb": 7.0,
        "category": "Thriller"
    },
    {
        "name": "Hitman",
        "imdb": 6.3,
        "category": "Action"
    },
    {
        "name": "Dark Knight",
        "imdb": 9.0,
        "category": "Adventure"
    },
    {
        "name": "The Help",
        "imdb": 8.0,
        "category": "Drama"
    },
    {
        "name": "The Choice",
        "imdb": 6.2,
        "category": "Romance"
    },
    {
        "name": "Colonia",
        "imdb": 7.4,
        "category": "Romance"
    },
    {
        "name": "Love",
        "imdb": 6.0,
        "category": "Romance"
    },
    {
        "name": "Bride Wars",
        "imdb": 5.4,
        "category": "Romance"
    },
    {
        "name": "AlphaJet",
        "imdb": 3.2,
        "category": "War"
    },
    {
        "name": "Ringing Crime",
        "imdb": 4.0,
        "category": "Crime"
    },
    {
        "name": "Joking muck",
        "imdb": 7.2,
        "category": "Comedy"
    },
    {
        "name": "What is the name",
        "imdb": 9.2,
        "category": "Suspense"
    },
    {
        "name": "Detective",
        "imdb": 7.0,
        "category": "Suspense"
    },
    {
        "name": "Exam",
        "imdb": 4.2,
        "category": "Thriller"
    },
    {
        "name": "We Two",
        "imdb": 7.2,
        "category": "Romance"
    }
]


# Write a function that takes a single movie and returns True if its IMDB score is above 5.5
def is_highly_rated(movie: dict) -> bool:
    return movie["imdb"] > 5.5


# Write a function that returns a sublist of movies with an IMDB score above 5.5.
def only_highly_rated(movies: dict) -> list:
    return [movie for movie in movies if is_highly_rated(movie)]


# Write a function that takes a category name and returns just those movies under that category.
def only_with_category(movies: dict, category: str) -> list:
    return [movie for movie in movies if movie["category"] == category]


# Write a function that takes a list of movies and computes the average IMDB score.
def average_imdb_score(movies: list) -> float:
    if len(movies) == 0:
        return 0
    total_score: float = sum(movie["imdb"] for movie in movies)
    return total_score / len(movies)


# Write a function that takes a category and computes the average IMDB score.
def average_category_score(movies: dict, category: str) -> float:
    movies_in_category: list = only_with_category(movies, category)
    return average_imdb_score(movies_in_category)