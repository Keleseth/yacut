from wtforms.validators import ValidationError as WTFValidationError
from marshmallow import ValidationError as MMValidationError

from yacut.models import URLMap


def form_unique_link_validator(form, field):
    if URLMap.query.filter_by(short=field.data).first():
        raise WTFValidationError(
            'Предложенный вариант короткой ссылки уже существует.'
        )


def api_unique_link_validator(value):
    if URLMap.query.filter_by(short=value).first():
        raise MMValidationError(
            'Предложенный вариант короткой ссылки уже существует.'
        )