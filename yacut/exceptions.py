from settings import ERROR_KEY


class InvalidAPIUsage(Exception):

    status_code = 400

    def __init__(self, message, status_code=None):
        super().__init__()
        self.message = message
        if status_code:
            self.status_code = status_code

    def to_dict(self):
        return {ERROR_KEY: self.message}