
class EmuError(Exception):
    """Base class for exceptions in this module."""
    def __init__(self, message: str) -> None:
        self.message = message

    def __str__(self) -> str:
        return colored(self.message, "red")


class MissingAllowedFieldError(EmuError):
    """Exception raised when a requested field is allowed, but not present in the object."""
    def __init__(self, field) -> None:
        super().__init__(f"Field '{field}; is allowed, but not present")


class MissingForbiddenFieldError(EmuError):
    """Exception raised when a requested field is not allowed."""
    def __init__(self, field) -> None:
        super().__init__(f"Field '{field}' was requested, but not allowed")