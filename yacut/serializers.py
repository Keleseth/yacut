from flask import request
from marshmallow import (
    fields,
    Schema,
    validate,
)

from settings import (
    API_ERROR_MESSAGE,
    MAX_LENGTH_FOR_CUSTOM_SHORT,
    MIN_LENGTH_FOR_CUSTOM_SHORT,
    PATTERN_FOR_CUSTOM_SHORT
)
from yacut.exceptions import InvalidAPIUsage


class GetOriginalURLSchema(Schema):
    """
    Сериализатор для GET запросов, возвращающий 1 поле объекта:
    оригинальную ссылку.
    """

    original = fields.Url(
        data_key='url',
        required=True,
        error_messages={
            'required': API_ERROR_MESSAGE['missing_required_field'],
            'invalid': 'Неверный формат поля. Введите ссылку.'
        }
    )


class URLMapSChema(GetOriginalURLSchema):
    """
    Сериализатор для модели URLMap. Работает с GET и POST запросами.

    Выполняет валидации:
    оригинальной ссылки на формат и наличие,
    короткой ссылки на формат, длину и уникальность в базе данных.
    Если в json отсутствует короткая ссылка, или ключ короткой ссылки пуст,
    генерирует для поля short значение через функцию "if_not_short_generate".
    """

    short = fields.String(
        data_key='custom_id',
        load_only=True,
        required=False,
        validate=[
            validate.Length(
                min=MIN_LENGTH_FOR_CUSTOM_SHORT,
                max=MAX_LENGTH_FOR_CUSTOM_SHORT,
                error=API_ERROR_MESSAGE['invalid_short_name']
            ),
            validate.Regexp(
                PATTERN_FOR_CUSTOM_SHORT,
                error=API_ERROR_MESSAGE['invalid_short_name']
            )
        ]
    )

    short_link = fields.Method("get_short_link")

    def get_short_link(self, obj):
        return f"{request.host_url}{obj.short}"

    def handle_error(self, error, data, **kwargs):
        first_error_message = next(iter(error.messages.values()))[0]
        raise InvalidAPIUsage(first_error_message)
