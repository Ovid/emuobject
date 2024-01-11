from abc import ABC, abstractclassmethod
from cerberus import Validator
from termcolor import colored
from emuobject.EmuExceptions import MissingAllowedFieldError, MissingForbiddenFieldError


class Emu(ABC):
    def __init__(self, fields: dict) -> None:
        """Creates an Emu object. The fields must be a dictionary. The schema method must be overridden in a subclass.
        :param fields: A dictionary of field names and their values."""
        self._fields = fields
        self._validator = Validator(self.schema(), require_all=True)
        if not self._validator.validate(self._fields):
            raise TypeError("Invalid fields")

    @abstractclassmethod
    def schema(cls) -> dict:
        """This should be overridden in a subclass to return a dictionary of field names and their types."""
        pass

    def definition(self, field) -> dict or None:
        """Returns the definition for a single field. Returns None if the field is not defined.:w
        :param key: The field name"""
        if field in self.schema():
            return self.schema()[field]
        return None

    def get(self, field: str):
        """Returns the value of the field, or raises an exception if the field is not allowed or not present.
        :param field: The field name"""
        if not self.has(field):
            if self.allows(field):
                raise MissingAllowedFieldError(field)
            raise MissingForbiddenFieldError(field)
        return self._fields[field]

    def allows(self, field: str) -> bool:
        """Returns True if the field is allowed (e.g., it's defined in the schema method), False otherwise.
        :param field: The field name"""
        return field in self.schema()

    def has(self, field: str) -> bool:
        """Returns True if the field is present in the object, False otherwise.
        :param field: The field name"""
        return field in self._fields
