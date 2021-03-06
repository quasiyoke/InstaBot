class APIError(Exception):
    def __init__(self, code):
        super(APIError, self).__init__(str(code))


class APIFailError(APIError):
    pass


class APIJSONError(Exception):
    pass


class APILimitError(Exception):
    pass


class APINotAllowedError(Exception):
    pass


class APINotFoundError(Exception):
    pass


class ConfigurationError(Exception):
    pass


class DBError(Exception):
    pass
