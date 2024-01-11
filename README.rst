=====================
The emuobject Project
=====================
--------------------------------------
Type-safe immutable objects for Python
--------------------------------------

========
SYNOPSIS
========

emuobject is a Python library that provides type-safe (Emu)table objects. (Forgive the pun.)

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
        
    p = Person({name="John", age=42})
    print(p.get('name'))
    print(p.get('description')) # error, because we have no description

Rationale
=========

When working on large projects, there are two key issues which can crop up with object-oriented code:

- The type you got was not the type you expected
- The data you want was not the data you expected

emuobject attempts to handle both.

In "Pythonic" objects, we don't do data validation. For the above ``Person`` class, we might write
``person.age = "forty-two"`` and it would work just fine until we tried to do something with it later.
This is a problem, because it means that we can't trust the data we get back from our objects. Here's an
example:

    if person.is_old_enough_to_vote():
        do_something_with(person)
        add_to_voter_queue(person)

In the above, if ``do_something_with`` changes the age of the person to 17 or less, then
``add_to_voter_queue`` has an object in an invalid state, despite our having a guard clause.

If you read one of the many of the "object-oriented programming is bad" articles on the web,
you'll often find that many of their arguments go away in the face of immutable objects.

emuobject requires you to define a ``schema`` method which returns a `cerberus <https://docs.python-cerberus.org/en/stable/>`_
schema. When you create an object, it will be validated against this schema, and if it fails, an exception
is thrown.

Because the object is immutable, this validation happens only once upon instantiation.

Other Stuff
----------- 

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black