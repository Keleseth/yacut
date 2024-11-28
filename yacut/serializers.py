from flask import request
from marshmallow import (
    fields,
    post_load,
    Schema,
    validate,
    validates,
)

from settings import API_ERROR_MESSAGE
from yacut.exceptions import InvalidAPIUsage
from yacut.utils import get_unique_short_id
from yacut.validators import api_unique_link_validator


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
                max=16,
                error=API_ERROR_MESSAGE['invalid_short_name']
            ),
            validate.Regexp(
                '^[A-Za-z0-9]*$',
                error=API_ERROR_MESSAGE['invalid_short_name']
            )
        ]
    )

    @validates('short')
    def validate_short_is_unique(self, value):
        api_unique_link_validator(value)

    @post_load
    def if_not_short_generate(self, data, **kwargs):
        if not data.get('short'):
            data['short'] = get_unique_short_id()
        return data

    short_link = fields.Method("get_short_link")

    def get_short_link(self, obj):
        return f"{request.host_url}{obj.short}"

    def handle_error(self, error, data, **kwargs):
        first_error_message = next(iter(error.messages.values()))[0]
        raise InvalidAPIUsage(first_error_message)