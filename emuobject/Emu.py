from abc import ABC, abstractclassmethod
from termcolor import colored

# Need to have definitions for the fields have required and optional fields


class EmuError(Exception):
    def __init__(self, message: str) -> None:
        self.message = message

    def __str__(self) -> str:
        return colored(self.message, 'red')

class MissingAllowedFieldError(EmuError):
    def __init__(self, field) -> None:
        super().__init__(f"Field '{field}; is allowed, but not present")

class MissingForbiddenFieldError(EmuError):
    def __init__(self, field) -> None:
        super().__init__(f"Field '{field}' was requested, but not allowed")

class Emu(ABC):
    def __init__(self, fields: dict) -> None:
        self._fields = fields

    @abstractclassmethod
    def _definitions(cls) -> dict:
        pass

    def get(self, field: str):
        if not self.has(field):
            if self.allows(field):
                raise MissingAllowedFieldError(field)
            raise MissingForbiddenFieldError(field)
        return self._fields[field]
    
    def allows(self, field: str) -> bool:
        return field in self._definitions()
    
    def has(self, field) -> bool:
        return field in self._fields
