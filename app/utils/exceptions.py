class BaseAppException(Exception):
    def __init__(self, message, status_code=400):
        self.message = message
        self.status_code = status_code

class ValidationException(BaseAppException):
    def __init__(self, message="Invalid request"):
        super().__init__(message, 400)

class NotFoundException(BaseAppException):
    def __init__(self, message="Resource not found"):
        super().__init__(message, 404)

class DuplicateResourceException(BaseAppException):
    def __init__(self, message="Resource already exists"):
        super().__init__(message, 409)