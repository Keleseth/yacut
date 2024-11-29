from datetime import datetime
import secrets

from flask import url_for

from . import db
from settings import (
    ALLOWED_CHARS_FOR_SHORT_LINK,
    JSON_POST_FIELDS,
    SHORT_LINK_LENGTH
)


class URLMap(db.Model):
    """Модель связывающая короткие и оригинальные ссылки."""

    id = db.Column(
        db.Integer,
        primary_key=True
    )
    original = db.Column(
        db.String(2048),
        nullable=False
    )
    short = db.Column(
        db.String(16),
        unique=True,
        nullable=False
    )
    timestamp = db.Column(
        db.DateTime,
        index=True,
        default=datetime.utcnow
    )

    def to_dict(self):
        return dict(
            url=self.original,
            short_link=url_for(
                'redirect_to_original', short_id=self.short, _external=True
            )
        )

    def from_dict(self, data):
        for field in JSON_POST_FIELDS:
            if field in data:
                setattr(self, field, data[field])

    def link_links(self, model, original, short):
        if not short:
            short = self.get_unique_short_id()
        return model(
            original=original,
            short=short
        ), short

    def get_unique_short_id(self):
        while True:
            short_id = ''.join(
                secrets.choice(ALLOWED_CHARS_FOR_SHORT_LINK)
                for _ in range(SHORT_LINK_LENGTH)
            )
            if not URLMap.query.filter_by(short=short_id).first():
                return short_id