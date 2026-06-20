from index import Book, Movie

book = Book(
    "Python Programming",
    "홍길동",
    2024,
    300,
    "IT"
)

movie = Movie(
    "Interstellar",
    "Christopher Nolan",
    2014,
    169,
    9.5
)

print(book.get_info())
print(book.reading_time())
print(book.recommend())

print(movie.get_info())
print(movie.is_long_movie())
print(movie.recommend())