import secrets

from settings import (
    ALLOWED_CHARS_FOR_SHORT_LINK,
    SHORT_LINK_LENGTH
)
from yacut.models import URLMap


def get_unique_short_id():
    while True:
        short_id = ''.join(
            secrets.choice(ALLOWED_CHARS_FOR_SHORT_LINK)
            for _ in range(SHORT_LINK_LENGTH)
        )
        if not URLMap.query.filter_by(short=short_id).first():
            return short_id


def link_links(model, original, short):
    if not short:
        short = get_unique_short_id()
    return model(
        original=original,
        short=short
    ), short
