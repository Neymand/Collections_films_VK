from typing import Dict, List, Iterator, Optional

class Movie:

    def __init__(self, title: str, year: int, genre: str):
        self.title = title
        self.year = year
        self.genre = genre

    def __repr__(self) -> str:
        return f"Movie(title='{self.title}', year={self.year}, genre='{self.genre}')"

class MovieCollection:

    def __init__(self):
        self.movies: Dict[str, Movie] = {}

    def add_movie(self, movie: Movie) -> None:
        self.movies[movie.title] = movie
        print(f"Добавлен фильм: {movie.title}")

    def get_movie_collection(self) -> List[str]:
        """Возвращает список описаний фильмов в коллекции"""
        if not self.movies:
            return ["Коллекция фильмов пуста."]
        return [repr(movie) for movie in self.movies.values()]

    def remove_movie(self, title: str) -> None:
        if title in self.movies:
            removed_movie = self.movies.pop(title)
            print(f"Фильм удалён: {removed_movie.title}")
        else:
            print(f"Фильм под названием '{title}' не найден")

    def search_movies_by_attribute(self, attribute: str, value) -> List:
        """Универсальный метод для поиска фильмов по заданному атрибуту."""
        return [movie for movie in self.movies.values() if getattr(movie, attribute) == value]

    def search_movies_year(self, year: int) -> List:
        return self.search_movies_by_attribute('year', year)

    def search_movies_genre(self, genre: str) -> List:
        return self.search_movies_by_attribute('genre', genre)

    def search_movies_title(self, title: str) -> List:
        return self.search_movies_by_attribute('title', title)

    def __iter__(self) -> Iterator[Movie]:
        return iter(self.movies.values())





