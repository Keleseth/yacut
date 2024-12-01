import os
import string


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    SECRET_KEY = os.getenv('SECRET_KEY')


JSON_POST_FIELDS = ['url', 'short_link']

# json ключ содержащий сообщения об ошибках
ERROR_KEY = 'message'

# Словарь содержащий текст ошибок для api-интерфейса
API_ERROR_MESSAGE = {
    'emty_body': 'Отсутствует тело запроса',
    'invalid_short_name': 'Указано недопустимое имя для короткой ссылки',
    'missing_required_field': '\"url\" является обязательным полем!',
    'unique_field_err': 'Предложенный вариант короткой ссылки уже существует.',
    'object_is_missing': 'Указанный id не найден',
}

# Словарь содержащий текст ошибок для веб-интерфейса
FRONT_ERROR_MESSAGE = {
    'invalid_short_name': 'Указано недопустимое имя для короткой ссылки',
    'invalid_url': 'Неверный формат длинной ссылки. Введие ссылку целиком.',
    'missing_url': 'Заполните поле длинной ссылки.'
}

# Допустимые символы для генерации короткой ссылки.
ALLOWED_CHARS_FOR_SHORT_LINK = string.ascii_letters + string.digits
# Регулярное выражение для валидации пользовательской короткой ссылки.
PATTERN_FOR_CUSTOM_SHORT = f'^[{ALLOWED_CHARS_FOR_SHORT_LINK}]*$'

# допустимая длина для длинной(оригинальной) ссылки
MAX_LENGTH_FOR_ORIGINAL_LINK = 2048

# Допустимая длина пользовательской короткой ссылки
MAX_LENGTH_FOR_CUSTOM_SHORT = 16
MIN_LENGTH_FOR_CUSTOM_SHORT = 0

# Длина генерируемой сервером короткой ссылки
SHORT_LINK_LENGTH = 6

# Наименования полей для сериализатора, модели и
# словаря data_for_model для views веб-интерфейса.
SHORT_LINK_FIELD = 'short'
ORIGINAL_LINK_FIELD = 'original'