"""
movie.py
ai 활용명시
-함수
"""

from .media import Media


class Movie(Media):
    """
    영화 클래스
    """

    def __init__(
        self,
        title,
        creator,
        year,
        runtime,
        rating
    ):
        super().__init__(
            title,
            creator,
            year
        )

        self.runtime = runtime
        self.rating = rating

    def get_info(self):
        """
        영화 정보 반환
        """
        return (
            f"{super().get_info()}, "
            f"Runtime: {self.runtime}, "
            f"Rating: {self.rating}"
        )

    def is_long_movie(self):
        """
        장편 영화 여부

        :return: bool
        """
        return self.runtime >= 120

    def recommend(self):
        """
        추천 여부 반환
        """
        return self.rating >= 8.0