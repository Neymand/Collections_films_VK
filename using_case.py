import main

if __name__ == "__main__":
    # Создаем коллекцию фильмов
    collection = main.MovieCollection()

    # Добавляем фильмы в коллекцию
    collection.add_movie(main.Movie("Inception", 2010, "Science Fiction"))
    collection.add_movie(main.Movie("The Matrix", 1999, "Science Fiction"))
    collection.add_movie(main.Movie("Avengers: Endgame", 2019, "Action"))

    # Выводим все фильмы в коллекции
    print("Все фильмы в коллекции:")
    for movie in collection.get_movie_collection():
        print(movie)

    # Поиск фильмов по году
    movies_2010 = collection.search_movies_year(2010)
    print("\nФильмы, выпущенные в 2010 году:")
    for movie in movies_2010:
        print(movie)

    # Поиск фильмов по жанру
    sci_fi_movies = collection.search_movies_genre("Science Fiction")
    print("\nФильмы жанра Science Fiction:")
    for movie in sci_fi_movies:
        print(movie)

    # Удаление фильма
    collection.remove_movie("The Matrix")

    # Опять выводим все фильмы в коллекции после удаления
    print("\nФильмы в коллекции после удаления:")
    for movie in collection.get_movie_collection():
        print(movie)

    # Итерация по коллекции
    print("\nИтерация по коллекции фильмов:")
    for movie in collection:
        print(movie)
