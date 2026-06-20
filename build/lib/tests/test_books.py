import pytest

from index import Book


def test_book_creation():
    book = Book("Python", "Kim", 2024, 300, "IT")

    assert book.title == "Python"
    assert book.creator == "Kim"
    assert book.year == 2024
    assert book.pages == 300
    assert book.genre == "IT"


def test_book_reading_time():
    book = Book("Python", "Kim", 2024, 300, "IT")

    assert book.reading_time() == 6.0


def test_invalid_year():
    with pytest.raises(ValueError):
        Book("Python", "Kim", -1, 300, "IT")