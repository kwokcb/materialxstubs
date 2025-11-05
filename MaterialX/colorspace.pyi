from .PyMaterialXCore import *
from _typeshed import Incomplete

def getColorSpaces(cms: str = 'ocio', config: Incomplete | None = None):
    """Return a list containing the names of all supported color spaces.
       By default, the OCIO color management system and default MaterialX
       config are used."""
def transformColor(color, sourceColorSpace, destColorSpace, cms: str = 'ocio', config: Incomplete | None = None):
    """Given a MaterialX color and the names of two supported color spaces,
       transform the color from the source to the destination color space.
       By default, the OCIO color management system and default MaterialX
       config are used."""
def getDefaultOCIOConfig():
    """Return the default OCIO config packaged with this Python library.
       Raises ImportError if the PyOpenColorIO module cannot be imported."""
