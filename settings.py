import os
import string


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    SECRET_KEY = os.getenv('SECRET_KEY')


SHORT_LINK_LENGTH = 6

JSON_POST_FIELDS = ['url', 'short_link']

ERROR_KEY = 'message'

API_ERROR_MESSAGE = {
    'emty_body': 'Отсутствует тело запроса',
    'invalid_short_name': 'Указано недопустимое имя для короткой ссылки',
    'missing_required_field': '\"url\" является обязательным полем!',
    'unique_field_err': 'Предложенный вариант короткой ссылки уже существует.',
    'object_is_missing': 'Указанный id не найден',
}

FRONT_ERROR_MESSAGE = {
    'invalid_url': 'Неверный формат длинной ссылки. Введие ссылку целиком.',
    'missing_url': 'Заполните поле длинной ссылки.'
}

ALLOWED_CHARS_FOR_SHORT_LINK = string.ascii_letters + string.digits