from abc import ABC, abstractclassmethod
from cerberus import Validator
from termcolor import colored
from emuobject.EmuExceptions import MissingAllowedFieldError, MissingForbiddenFieldError


class Emu(ABC):
    """
    Type-safe immutable objects in Python.

    This is a base class for creating immutable objects. It's designed to be type-safe and easy to use.

    There are no public attributes. Instead, you must use the get() method to retrieve the value of a field.

    Basic usage:

    >>> class Person(Emu):
    ...     @classmethod
    ...     def schema(cls):
    ...         # schema definition must be a valid cerberus schema
    ...         return {
    ...             "name": {"type": "string"},
    ...             "age": {"type": "integer", "min": 0},
    ...             "description": {"type": "string", "required": False},
    ...         }
    ...
    >>> ovid = Person({"name": "Ovid", "age": 42})
    >>> ovid.get("name")
    'Ovid'
    >>> ovid.get("age")
    42
    >>> ovid.get("description")
    Traceback (most recent call last):
        ...
    """

    def __init__(self, fields: dict) -> None:
        self._fields = fields
        self._validator = Validator(self.schema(), require_all=True)

        if not self._validator.validate(self._fields):
            raise TypeError("Invalid fields")

    @abstractclassmethod
    def schema(cls) -> dict:
        """
        This must be overridden in a subclass to return a dictionary of field names and their types.
        The syntax should match that of Cerberus.

        Args:
            None

        Returns:
            A dictionary of field names and their types in the form of a cerberus schema.
        """
        pass

    def definition(self, field) -> dict or None:
        """
        Returns the definition for a single field. Returns None if the field is not defined.

        Do not override this method.

        Args:
            field: The field name

        Returns:
            A dictionary of the field's definition, or None if the field is not allowed.
        """
        if field in self.schema():
            return self.schema()[field]
        return None

    def get(self, field: str):
        """
        Returns the value of the field, or raises an exception if the field is not allowed or not present.

        Do not override this method.

        Args:
            field: The field name you wish to retrieve.

        Returns:
            The value of the field, if it exists. Return type is determined by the schema.

        Raises:
            MissingAllowedFieldError: If the field is allowed but not present.
            MissingForbiddenFieldError: If the field is not allowed.
        """
        if not self.has(field):
            if self.allows(field):
                raise MissingAllowedFieldError(field)
            raise MissingForbiddenFieldError(field)
        return self._fields[field]

    @classmethod
    def allows(cls, field: str) -> bool:
        """
        Returns True if the field is allowed (e.g., it exists in the schema()), False otherwise.

        Do not override this method.

        Args:
            field: The field name you wish to check

        Returns:
            True if the field is allowed, False otherwise.
        """
        return field in cls.schema()

    def has(self, field: str) -> bool:
        """
        Returns True if the field is present in the object, False otherwise.

        Do not override this method.

        Args:
            field: The field name

        Returns:
            True if the field is present, False otherwise.
        """
        return field in self._fields
