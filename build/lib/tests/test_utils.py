from index import Book
from index.utils import search_media


def test_search_media_found():
    book1 = Book("Python", "Kim", 2024, 300, "IT")
    book2 = Book("Java", "Lee", 2023, 250, "IT")

    result = search_media(
        [book1, book2],
        "Python"
    )

    assert len(result) == 1


def test_search_media_not_found():
    book1 = Book("Python", "Kim", 2024, 300, "IT")

    result = search_media(
        [book1],
        "C++"
    )

    assert len(result) == 0