from abc import ABC, abstractclassmethod
from termcolor import colored
from emuobject.EmuExceptions import MissingAllowedFieldError, MissingForbiddenFieldError

# Need to have definitions for the fields have required and optional fields

class Emu(ABC):
    def __init__(self, fields: dict) -> None:
        self._fields = fields

    @abstractclassmethod
    def definitions(cls) -> dict:
        """This should be overridden in a subclass to return a dictionary of field names and their types."""
        pass

    def get(self, field: str):
        """Returns the value of the field, or raises an exception if the field is not allowed or not present."""
        if not self.has(field):
            if self.allows(field):
                raise MissingAllowedFieldError(field)
            raise MissingForbiddenFieldError(field)
        return self._fields[field]

    def allows(self, field: str) -> bool:
        """Returns True if the field is allowed (e.g., it's defined in definitions method), False otherwise."""
        return field in self.definitions()

    def has(self, field: str) -> bool:
        """Returns True if the field is present in the object, False otherwise."""
        return field in self._fields
