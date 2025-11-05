from .PyMaterialXCore import *

def getTypeString(value):
    """Return the MaterialX type string associated with the given Python value
       If the type of the given Python value is not recognized by MaterialX,
       then None is returned.

       Examples:
           getTypeString(1.0) -> 'float'
           getTypeString(mx.Color3(1)) -> 'color3'"""
def getValueString(value):
    """Return the MaterialX value string associated with the given Python value
       If the type of the given Python value is not recognized by MaterialX,
       then None is returned

       Examples:
           getValueString(0.1) -> '0.1'
           getValueString(mx.Color3(0.1, 0.2, 0.3)) -> '0.1, 0.2, 0.3'"""
def createValueFromStrings(valueString, typeString):
    """Convert a MaterialX value and type strings to the corresponding
       Python value.  If the given conversion cannot be performed, then None
       is returned.

       Examples:
           createValueFromStrings('0.1', 'float') -> 0.1
           createValueFromStrings('0.1, 0.2, 0.3', 'color3') -> mx.Color3(0.1, 0.2, 0.3)"""
def isColorType(t):
    """Return True if the given type is a MaterialX color."""
def isColorValue(value):
    """Return True if the given value is a MaterialX color."""
def stringToBoolean(value):
    """Return boolean value found in a string. Throws and exception if a boolean value could not be parsed"""
