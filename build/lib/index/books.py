"""
book.py

AI 활용 내역:
- ChatGPT를 활용하여 클래스 구조와 docstring 작성 예시를 참고함.
- 생성된 코드는 직접 수정 및 검토 후 사용함.

"""

from .media import Media


class Book(Media):
    """
    도서 클래스

    :param pages: 페이지 수
    :param genre: 장르
    
    """

    def __init__(
        self,
        title,
        creator,
        year,
        pages,
        genre
    ):
        super().__init__(
            title,
            creator,
            year
        )

        self.pages = pages
        self.genre = genre

    def get_info(self):
        """
        책 정보 반환
        """
        return (
            f"{super().get_info()}, "
            f"Pages: {self.pages}, "
            f"Genre: {self.genre}"
        )

    def reading_time(self):
        """
        예상 독서 시간 계산

        :return: 시간
        """
        return round(self.pages / 50, 1)

    def recommend(self):
        """
        추천 문구 반환
        """
        return f"{self.genre} 장르 추천 도서"
    