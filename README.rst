=====================
The EmuObject Project
=====================
--------------------------------------
Type safe immutable objects for Python
--------------------------------------

========
SYNOPSIS
========

EmuObject is a Python library that provides type-safe (Emu)table objects. (Forgive the pun.)

.. code:: python
    
    from emuobject import Emu

    class Person(Emu):
        @classmethod
        def schema(cls):
            # cerberus schema
            return {
                "name": {"type": "string"},
                "age": {"type": "integer", "min": 0},
                "description": {"type": "string", "required": False},
            }

    def is_old_enough_to_vote(self) -> bool:
        return self.age >= 18
        
    p = Person(name="John", age=42)
    print(p.get('name'))
    print(p.get('description')) # error, because we have no description

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black