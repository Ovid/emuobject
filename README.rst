"""
The EmuObject Project
"""
'''
Type safe immutable objects for Python
'''

========
SYNOPSIS
========

EmuObject is a Python library that provides type safe immutable objects::

    class Person(Emu):
        @classmethod
        def schema(cls):
            return {
                "name": {"type": "string"},
                "age": {"type": "integer", "min": 0},
                "description": {"type": "string", "required": False},
            }
        
    p = Person(name="John", age=42)
    print(p.get('name'))
    print(p.get('description')) # error, because we have no description

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black