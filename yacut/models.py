from datetime import datetime

from flask import url_for

from . import db
from settings import JSON_POST_FIELDS


class URLMap(db.Model):
    """Модель связывающая короткие и оригинальные ссылки."""

    id = db.Column(
        db.Integer,
        primary_key=True
    )
    original = db.Column(
        db.Text,
        nullable=False
    )
    short = db.Column(
        db.String,
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