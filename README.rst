Help on module emuobject.Emu in emuobject:

NAME
    emuobject.Emu

CLASSES
    abc.ABC(builtins.object)
        Emu
    
    class Emu(abc.ABC)
     |  Emu(fields: dict) -> None
     |  
     |  Method resolution order:
     |      Emu
     |      abc.ABC
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, fields: dict) -> None
     |      Creates an Emu object. The fields must be a dictionary. The schema method must be overridden in a subclass.
     |      :param fields: A dictionary of field names and their values.
     |  
     |  allows(self, field: str) -> bool
     |      Returns True if the field is allowed (e.g., it's defined in the schema method), False otherwise.
     |      :param field: The field name
     |  
     |  definition(self, field) -> dict
     |      Returns the definition for a single field. Returns None if the field is not defined.:w
     |      :param key: The field name
     |  
     |  get(self, field: str)
     |      Returns the value of the field, or raises an exception if the field is not allowed or not present.
     |      :param field: The field name
     |  
     |  has(self, field: str) -> bool
     |      Returns True if the field is present in the object, False otherwise.
     |      :param field: The field name
     |  
     |  ----------------------------------------------------------------------
     |  Class methods defined here:
     |  
     |  schema() -> dict from abc.ABCMeta
     |      This should be overridden in a subclass to return a dictionary of field names and their types.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables
     |  
     |  __weakref__
     |      list of weak references to the object
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  __abstractmethods__ = frozenset({'schema'})

FILE
    /Users/ovid/projects/python/emuobject/emuobject/Emu.py


