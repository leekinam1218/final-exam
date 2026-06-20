"""
utils.py
"""

import csv


def save_to_csv(media_list, filename):
    """
    CSV 저장
    """

    with open(
        filename,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow(
            [
                "title",
                "creator",
                "year"
            ]
        )

        for media in media_list:
            writer.writerow(
                [
                    media.title,
                    media.creator,
                    media.year
                ]
            )


def search_media(
    media_list,
    keyword
):
    """
    제목 검색
    """

    return [
        media
        for media in media_list
        if keyword.lower()
        in media.title.lower()
    ]