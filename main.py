from typing import Dict, List, Iterator, Optional

class Movie:

    def __init__(self, title: str, year: int, genre: str):
        self.title = title
        self.year = year
        self.genre = genre

class MovieCollection:

    def __init__(self):
        self.movies: Dict[str, Movie] = {}

    def add_movie(self, movie: Movie):
        self.movies[movie.title] = movie
        print(f"Добавлен фильм: {movie.title}")

    def remove_movie(self, title: str):
        if title in self.movies:
            removed_movie = self.movies.pop(title)
            print(f"Фильм удалён: {removed_movie.title}")
        else:
            print(f"Фильм под названием '{title}' не найден")

    def search_movies(self):
        pass

    def add_movie_collection(self):
        pass

    def remove_movie_from_collection(self):
        pass

# if __name__ == "__main__":
#     main_collection = MovieCollection()
#
#     # Добавляем фильмы
#     main_collection.add_movie(Movie(title="pulp fiction", year=1994, genre="Action"))
#     main_collection.add_movie(Movie(title="Matrix", year=1999, genre="Action"))
#     main_collection.add_movie(Movie(title="Interstellar", year=2014, genre="Action"))
#
#     main_collection.remove_movie("Matrix")