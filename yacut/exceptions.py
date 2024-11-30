from settings import (
    API_ERROR_MESSAGE,
    ERROR_KEY,
)


class InvalidAPIUsage(Exception):
    """Класс исключения для некорректного использования API."""

    status_code = 400

    def __init__(self, message, status_code=None):
        super().__init__()
        self.message = message
        if status_code:
            self.status_code = status_code

    def to_dict(self):
        return {ERROR_KEY: self.message}


class ShortLinkAlreadyExists(InvalidAPIUsage):
    """
    Класс исключения вызывается при попытке создания объекта URLMap
    c уже существующей в бд короткой ссылкой.
    """

    status_code = 400

    def __init__(self, message=API_ERROR_MESSAGE['unique_field_err']):
        self.message = message

    def to_dict(self):
        return {ERROR_KEY: self.message}