import secrets

from settings import (
    ALLOWED_CHARS_FOR_SHORT_LINK,
    SHORT_LINK_LENGTH
)
from yacut.models import URLMap


def get_unique_short_id():
    """Генерирует уникальный относительный путь для короткой ссылки."""
    while True:
        short_id = ''.join(
            secrets.choice(ALLOWED_CHARS_FOR_SHORT_LINK)
            for _ in range(SHORT_LINK_LENGTH)
        )
        if not URLMap.get_link_object(short_id):
            return short_id
