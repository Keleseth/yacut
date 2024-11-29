from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SubmitField,
    URLField
)
from wtforms.validators import (
    DataRequired,
    Length,
    Optional,
    Regexp,
    URL
)

from settings import (
    FRONT_ERROR_MESSAGE,
    MAX_LENGTH_FOR_CUSTOM_SHORT,
    MIN_LENGTH_FOR_CUSTOM_SHORT,
    PATTERN_FOR_CUSTOM_SHORT
)
from yacut.validators import form_unique_link_validator


class LinkKnitForm(FlaskForm):
    original_link = URLField(
        'Введите желаемую оригинальную ссылку',
        validators=[
            DataRequired(message=FRONT_ERROR_MESSAGE['missing_url']),
            URL(message=FRONT_ERROR_MESSAGE['invalid_url'])
        ]
    )
    custom_id = StringField(
        'Введите желаемую короткую ссылку',
        validators=[
            Length(
                MIN_LENGTH_FOR_CUSTOM_SHORT,
                MAX_LENGTH_FOR_CUSTOM_SHORT
            ),
            Regexp(
                PATTERN_FOR_CUSTOM_SHORT,
                message=FRONT_ERROR_MESSAGE['invalid_short_name']
            ),
            Optional(),
            form_unique_link_validator  # не уверен, стоило ли добавлять.
        ]
    )
    submit = SubmitField('Добавить')