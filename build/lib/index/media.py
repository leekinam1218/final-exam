"""
media.py

부모 클래스 Media 정의
"""


class Media:
    """
    도서와 영화의 공통 정보를 관리하는 부모 클래스.

    :param title: 제목
    :param creator: 저자 또는 감독
    :param year: 출판/개봉 연도

    >>> media = Media("Python", "Kim", 2024)
    >>> media.title
    'Python'
    """

    def __init__(self, title, creator, year):
        self.title = title
        self.creator = creator
        self.year = year

        self._validate_year()

    def _validate_year(self):
        """
        연도 유효성 검사
        """
        if not isinstance(self.year, int):
            raise TypeError("Year must be integer")

        if self.year < 0:
            raise ValueError("Year cannot be negative")

    def get_info(self):
        """
        미디어 정보 반환

        :return: 문자열
        """
        return (
            f"Title: {self.title}, "
            f"Creator: {self.creator}, "
            f"Year: {self.year}"
        )

    def is_classic(self):
        """
        고전 작품 여부

        :return: bool
        """
        return self.year < 2000