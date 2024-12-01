from datetime import datetime
import secrets

from sqlalchemy import exists

from . import db
from settings import (
    ALLOWED_CHARS_FOR_SHORT_LINK,
    MAX_LENGTH_FOR_CUSTOM_SHORT,
    MAX_LENGTH_FOR_ORIGINAL_LINK,
    ORIGINAL_LINK_FIELD,
    SHORT_LINK_LENGTH,
    SHORT_LINK_FIELD
)
from yacut.exceptions import ShortLinkAlreadyExists


class URLMap(db.Model):
    """Модель связывающая короткие и оригинальные ссылки."""

    id = db.Column(
        db.Integer,
        primary_key=True
    )
    original = db.Column(
        db.String(MAX_LENGTH_FOR_ORIGINAL_LINK),
        nullable=False
    )
    short = db.Column(
        db.String(MAX_LENGTH_FOR_CUSTOM_SHORT),
        unique=True,
        nullable=False
    )
    timestamp = db.Column(
        db.DateTime,
        index=True,
        default=datetime.utcnow
    )

    @staticmethod
    def get_link_object(short_id):
        return URLMap.query.filter_by(short=short_id).first()

    @staticmethod
    def check_link_exists(short_id):
        return db.session.query(
            exists().where(URLMap.short == short_id)
        ).scalar()

    @staticmethod
    def link_links(data):
        if not data.get(SHORT_LINK_FIELD):
            data[SHORT_LINK_FIELD] = URLMap.get_unique_short_id()
        return URLMap(
            original=data[ORIGINAL_LINK_FIELD],
            short=data[SHORT_LINK_FIELD]
        )

    @staticmethod
    def get_unique_short_id():
        while True:
            short_id = ''.join(
                secrets.choice(ALLOWED_CHARS_FOR_SHORT_LINK)
                for _ in range(SHORT_LINK_LENGTH)
            )
            if not URLMap.check_link_exists(short_id):
                return short_id

    @staticmethod
    def link_object_create(data=None):
        if (
            data.get(SHORT_LINK_FIELD) and
            URLMap.check_link_exists(data[SHORT_LINK_FIELD])
        ):
            raise ShortLinkAlreadyExists()

        new_link_obj = URLMap.link_links(data)
        db.session.add(new_link_obj)
        db.session.commit()
        return new_link_obj
