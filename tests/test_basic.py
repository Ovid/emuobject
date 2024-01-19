import unittest
from emuobject.Emu import Emu
from emuobject.EmuExceptions import (
    MissingAllowedFieldError,
    MissingForbiddenFieldError,
    SchemaDefinitionError,
)


class Person(Emu):
    @classmethod
    def schema(cls):
        return {
            "name": {"type": "string"},
            "age": {"type": "integer", "min": 0},
            "description": {"type": "string", "required": False},
        }


class TestBasic(unittest.TestCase):
    ovid = Person({"name": "Ovid", "age": 42})

    def test_basic(self):
        self.assertEqual(self.ovid.get("name"), "Ovid")
        self.assertEqual(self.ovid.get("age"), 42)

    def test_allows(self):
        self.assertTrue(self.ovid.allows("name"))
        self.assertTrue(self.ovid.allows("age"))
        self.assertTrue(self.ovid.allows("description"))

        self.assertFalse(self.ovid.allows("address"))

    def test_has(self):
        self.assertTrue(self.ovid.has("name"))
        self.assertTrue(self.ovid.has("age"))

        self.assertFalse(self.ovid.has("description"))
        self.assertFalse(self.ovid.has("address"))

    def test_missing(self):
        with self.assertRaises(MissingAllowedFieldError):
            self.ovid.get("description")

        with self.assertRaises(MissingForbiddenFieldError):
            self.ovid.get("address")

    def test_init(self):
        with self.assertRaises(SchemaDefinitionError):
            Person({"name": "Ovid", "age": "42"})

        with self.assertRaises(SchemaDefinitionError):
            Person({"name": "Ovid", "age": -1})

        with self.assertRaises(SchemaDefinitionError):
            Person({"name": "Ovid", "age": 42, "address": "123 Main St"})


if __name__ == "__main__":
    unittest.main()
