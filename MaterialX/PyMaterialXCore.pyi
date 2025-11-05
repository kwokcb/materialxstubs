import typing
from _typeshed import Incomplete
from typing import Callable, ClassVar, overload

ARRAY_PREFERRED_SEPARATOR: str
ARRAY_VALID_SEPARATORS: str
BSDF_TYPE_STRING: str
DEFAULT_TYPE_STRING: str
DISPLACEMENT_SHADER_TYPE_STRING: str
EDF_TYPE_STRING: str
FILENAME_TYPE_STRING: str
GEOMNAME_TYPE_STRING: str
GEOM_PATH_SEPARATOR: str
LIGHT_SHADER_TYPE_STRING: str
MATERIAL_TYPE_STRING: str
MULTI_OUTPUT_TYPE_STRING: str
NAME_PATH_SEPARATOR: str
NAME_PREFIX_SEPARATOR: str
NONE_TYPE_STRING: str
STRING_TYPE_STRING: str
SURFACE_MATERIAL_NODE_STRING: str
SURFACE_SHADER_TYPE_STRING: str
UDIM_SET_PROPERTY: str
UDIM_TOKEN: str
UNIVERSAL_GEOM_NAME: str
UV_TILE_TOKEN: str
VALUE_STRING_FALSE: str
VALUE_STRING_TRUE: str
VDF_TYPE_STRING: str
VOLUME_MATERIAL_NODE_STRING: str
VOLUME_SHADER_TYPE_STRING: str

class AttributeDef(TypedElement):
    CATEGORY: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def getAttrName(self) -> str:
        """getAttrName(self: MaterialX.PyMaterialXCore.AttributeDef) -> str

        Return the element's attrname string.
        """
    def getExportable(self) -> bool:
        """getExportable(self: MaterialX.PyMaterialXCore.AttributeDef) -> bool

        Return the exportable boolean for the element.

        Defaults to false if exportable is not set.
        """
    def getValueString(self) -> str:
        """getValueString(self: MaterialX.PyMaterialXCore.AttributeDef) -> str

        Return value string.
        """
    def hasAttrName(self) -> bool:
        """hasAttrName(self: MaterialX.PyMaterialXCore.AttributeDef) -> bool

        Return true if this element has an attrname string.
        """
    def hasValueString(self) -> bool:
        """hasValueString(self: MaterialX.PyMaterialXCore.AttributeDef) -> bool

        Return true if the given element has a value string.
        """
    def setAttrName(self, arg0: str) -> None:
        """setAttrName(self: MaterialX.PyMaterialXCore.AttributeDef, arg0: str) -> None

        Set the element's attrname string.
        """
    def setExportable(self, arg0: bool) -> None:
        """setExportable(self: MaterialX.PyMaterialXCore.AttributeDef, arg0: bool) -> None

        Set the exportable boolean for the element.
        """
    def setValueString(self, arg0: str) -> None:
        """setValueString(self: MaterialX.PyMaterialXCore.AttributeDef, arg0: str) -> None

        Set the value string of an element.
        """

class Backdrop(Element):
    CATEGORY: ClassVar[str] = ...  # read-only
    CONTAINS_ATTRIBUTE: ClassVar[str] = ...  # read-only
    HEIGHT_ATTRIBUTE: ClassVar[str] = ...  # read-only
    WIDTH_ATTRIBUTE: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def getContainsElements(self) -> list[TypedElement]:
        """getContainsElements(self: MaterialX.PyMaterialXCore.Backdrop) -> list[MaterialX.PyMaterialXCore.TypedElement]

        Return the vector of elements that this backdrop contains.
        """
    def getContainsString(self) -> str:
        """getContainsString(self: MaterialX.PyMaterialXCore.Backdrop) -> str

        Return the contains string for this backdrop.
        """
    def getHeight(self) -> float:
        """getHeight(self: MaterialX.PyMaterialXCore.Backdrop) -> float

        Return the height attribute of the backdrop.
        """
    def getWidth(self) -> float:
        """getWidth(self: MaterialX.PyMaterialXCore.Backdrop) -> float

        Return the width attribute of the backdrop.
        """
    def hasContainsString(self) -> bool:
        """hasContainsString(self: MaterialX.PyMaterialXCore.Backdrop) -> bool

        Return true if this backdrop has a contains string.
        """
    def hasHeight(self) -> bool:
        """hasHeight(self: MaterialX.PyMaterialXCore.Backdrop) -> bool

        Return true if this backdrop has a height attribute.
        """
    def hasWidth(self) -> bool:
        """hasWidth(self: MaterialX.PyMaterialXCore.Backdrop) -> bool

        Return true if this backdrop has a width attribute.
        """
    def setContainsElements(self, arg0: list[TypedElement]) -> None:
        """setContainsElements(self: MaterialX.PyMaterialXCore.Backdrop, arg0: list[MaterialX.PyMaterialXCore.TypedElement]) -> None

        Set the vector of elements that this backdrop contains.
        """
    def setContainsString(self, arg0: str) -> None:
        """setContainsString(self: MaterialX.PyMaterialXCore.Backdrop, arg0: str) -> None

        Set the contains string for this backdrop.
        """
    def setHeight(self, arg0: float) -> None:
        """setHeight(self: MaterialX.PyMaterialXCore.Backdrop, arg0: float) -> None

        Set the height attribute of the backdrop.
        """
    def setWidth(self, arg0: float) -> None:
        """setWidth(self: MaterialX.PyMaterialXCore.Backdrop, arg0: float) -> None

        Set the width attribute of the backdrop.
        """

class Collection(Element):
    CATEGORY: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def getExcludeGeom(self) -> str:
        """getExcludeGeom(self: MaterialX.PyMaterialXCore.Collection) -> str

        Return the exclude geometry string of this element.
        """
    def getIncludeCollectionString(self) -> str:
        """getIncludeCollectionString(self: MaterialX.PyMaterialXCore.Collection) -> str

        Return the include collection string of this element.
        """
    def getIncludeCollections(self) -> list[Collection]:
        """getIncludeCollections(self: MaterialX.PyMaterialXCore.Collection) -> list[MaterialX.PyMaterialXCore.Collection]

        Return the vector of collections that are directly included by this element.
        """
    def getIncludeGeom(self) -> str:
        """getIncludeGeom(self: MaterialX.PyMaterialXCore.Collection) -> str

        Return the include geometry string of this element.
        """
    def hasExcludeGeom(self) -> bool:
        """hasExcludeGeom(self: MaterialX.PyMaterialXCore.Collection) -> bool

        Return true if this element has an exclude geometry string.
        """
    def hasIncludeCollectionString(self) -> bool:
        """hasIncludeCollectionString(self: MaterialX.PyMaterialXCore.Collection) -> bool

        Return true if this element has an include collection string.
        """
    def hasIncludeCycle(self) -> bool:
        """hasIncludeCycle(self: MaterialX.PyMaterialXCore.Collection) -> bool

        Return true if the include chain for this element contains a cycle.
        """
    def hasIncludeGeom(self) -> bool:
        """hasIncludeGeom(self: MaterialX.PyMaterialXCore.Collection) -> bool

        Return true if this element has an include geometry string.
        """
    def matchesGeomString(self, arg0: str) -> bool:
        """matchesGeomString(self: MaterialX.PyMaterialXCore.Collection, arg0: str) -> bool

        Return true if this collection and the given geometry string have any geometries in common.
        """
    def setExcludeGeom(self, arg0: str) -> None:
        """setExcludeGeom(self: MaterialX.PyMaterialXCore.Collection, arg0: str) -> None

        Set the exclude geometry string of this element.
        """
    def setIncludeCollection(self, arg0: Collection) -> None:
        """setIncludeCollection(self: MaterialX.PyMaterialXCore.Collection, arg0: MaterialX.PyMaterialXCore.Collection) -> None

        Set the collection that is directly included by this element.
        """
    def setIncludeCollectionString(self, arg0: str) -> None:
        """setIncludeCollectionString(self: MaterialX.PyMaterialXCore.Collection, arg0: str) -> None

        Set the include collection string of this element.
        """
    def setIncludeCollections(self, arg0: list[Collection]) -> None:
        """setIncludeCollections(self: MaterialX.PyMaterialXCore.Collection, arg0: list[MaterialX.PyMaterialXCore.Collection]) -> None

        Set the vector of collections that are directly included by this element.
        """
    def setIncludeGeom(self, arg0: str) -> None:
        """setIncludeGeom(self: MaterialX.PyMaterialXCore.Collection, arg0: str) -> None

        Set the include geometry string of this element.
        """

class Color3(VectorBase):
    @overload
    def __init__(self) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: MaterialX.PyMaterialXCore.Color3) -> None

        2. __init__(self: MaterialX.PyMaterialXCore.Color3, arg0: float) -> None

        3. __init__(self: MaterialX.PyMaterialXCore.Color3, arg0: Annotated[list[float], FixedSize(3)]) -> None

        4. __init__(self: MaterialX.PyMaterialXCore.Color3, arg0: list[float]) -> None

        5. __init__(self: MaterialX.PyMaterialXCore.Color3, arg0: float, arg1: float, arg2: float) -> None
        """
    @overload
    def __init__(self, arg0: float) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: MaterialX.PyMaterialXCore.Color3) -> None

        2. __init__(self: MaterialX.PyMaterialXCore.Color3, arg0: float) -> None

        3. __init__(self: MaterialX.PyMaterialXCore.Color3, arg0: Annotated[list[float], FixedSize(3)]) -> None

        4. __init__(self: MaterialX.PyMaterialXCore.Color3, arg0: list[float]) -> None

        5. __init__(self: MaterialX.PyMaterialXCore.Color3, arg0: float, arg1: float, arg2: float) -> None
        """
    @overload
    def __init__(self, arg0) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: MaterialX.PyMaterialXCore.Color3) -> None

        2. __init__(self: MaterialX.PyMaterialXCore.Color3, arg0: float) -> None

        3. __init__(self: MaterialX.PyMaterialXCore.Color3, arg0: Annotated[list[float], FixedSize(3)]) -> None

        4. __init__(self: MaterialX.PyMaterialXCore.Color3, arg0: list[float]) -> None

        5. __init__(self: MaterialX.PyMaterialXCore.Color3, arg0: float, arg1: float, arg2: float) -> None
        """
    @overload
    def __init__(self, arg0: list[float]) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: MaterialX.PyMaterialXCore.Color3) -> None

        2. __init__(self: MaterialX.PyMaterialXCore.Color3, arg0: float) -> None

        3. __init__(self: MaterialX.PyMaterialXCore.Color3, arg0: Annotated[list[float], FixedSize(3)]) -> None

        4. __init__(self: MaterialX.PyMaterialXCore.Color3, arg0: list[float]) -> None

        5. __init__(self: MaterialX.PyMaterialXCore.Color3, arg0: float, arg1: float, arg2: float) -> None
        """
    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: MaterialX.PyMaterialXCore.Color3) -> None

        2. __init__(self: MaterialX.PyMaterialXCore.Color3, arg0: float) -> None

        3. __init__(self: MaterialX.PyMaterialXCore.Color3, arg0: Annotated[list[float], FixedSize(3)]) -> None

        4. __init__(self: MaterialX.PyMaterialXCore.Color3, arg0: list[float]) -> None

        5. __init__(self: MaterialX.PyMaterialXCore.Color3, arg0: float, arg1: float, arg2: float) -> None
        """
    def asTuple(self) -> tuple[float, float, float]:
        """asTuple(self: MaterialX.PyMaterialXCore.Color3) -> tuple[float, float, float]"""
    def copy(self) -> Color3:
        """copy(self: MaterialX.PyMaterialXCore.Color3) -> MaterialX.PyMaterialXCore.Color3

        Create a deep copy of the value.
        """
    def dot(self, arg0: Color3) -> float:
        """dot(self: MaterialX.PyMaterialXCore.Color3, arg0: MaterialX.PyMaterialXCore.Color3) -> float

        Return the dot product of two vectors.
        """
    def getMagnitude(self) -> float:
        """getMagnitude(self: MaterialX.PyMaterialXCore.Color3) -> float

        Return the magnitude of the vector.
        """
    def getNormalized(self) -> Color3:
        """getNormalized(self: MaterialX.PyMaterialXCore.Color3) -> MaterialX.PyMaterialXCore.Color3

        Return a normalized version of the given path, collapsing current path and parent path references so that 'a/.

        /b' and 'c/../d/../a/b' become 'a/b'.
        """
    def linearToSrgb(self) -> Color3:
        """linearToSrgb(self: MaterialX.PyMaterialXCore.Color3) -> MaterialX.PyMaterialXCore.Color3

        Transform the given color from linear RGB to the sRGB encoding, returning the result as a new value.
        """
    def srgbToLinear(self) -> Color3:
        """srgbToLinear(self: MaterialX.PyMaterialXCore.Color3) -> MaterialX.PyMaterialXCore.Color3

        Transform the given color from the sRGB encoding to linear RGB, returning the result as a new value.
        """
    def __add__(self, arg0: Color3) -> Color3:
        """__add__(self: MaterialX.PyMaterialXCore.Color3, arg0: MaterialX.PyMaterialXCore.Color3) -> MaterialX.PyMaterialXCore.Color3"""
    def __eq__(self, arg0: Color3) -> bool:
        """__eq__(self: MaterialX.PyMaterialXCore.Color3, arg0: MaterialX.PyMaterialXCore.Color3) -> bool"""
    def __getitem__(self, arg0: int) -> float:
        """__getitem__(self: MaterialX.PyMaterialXCore.Color3, arg0: int) -> float"""
    def __iter__(self) -> typing.Iterator[float]:
        """def __iter__(self) -> typing.Iterator[float]"""
    def __iadd__(self, arg0: Color3) -> Color3:
        """__iadd__(self: MaterialX.PyMaterialXCore.Color3, arg0: MaterialX.PyMaterialXCore.Color3) -> MaterialX.PyMaterialXCore.Color3"""
    @overload
    def __imul__(self, arg0: Color3) -> Color3:
        """__imul__(*args, **kwargs)
        Overloaded function.

        1. __imul__(self: MaterialX.PyMaterialXCore.Color3, arg0: MaterialX.PyMaterialXCore.Color3) -> MaterialX.PyMaterialXCore.Color3

        2. __imul__(self: MaterialX.PyMaterialXCore.Color3, arg0: float) -> MaterialX.PyMaterialXCore.Color3
        """
    @overload
    def __imul__(self, arg0: float) -> Color3:
        """__imul__(*args, **kwargs)
        Overloaded function.

        1. __imul__(self: MaterialX.PyMaterialXCore.Color3, arg0: MaterialX.PyMaterialXCore.Color3) -> MaterialX.PyMaterialXCore.Color3

        2. __imul__(self: MaterialX.PyMaterialXCore.Color3, arg0: float) -> MaterialX.PyMaterialXCore.Color3
        """
    def __isub__(self, arg0: Color3) -> Color3:
        """__isub__(self: MaterialX.PyMaterialXCore.Color3, arg0: MaterialX.PyMaterialXCore.Color3) -> MaterialX.PyMaterialXCore.Color3"""
    @overload
    def __itruediv__(self, arg0: Color3) -> Color3:
        """__itruediv__(*args, **kwargs)
        Overloaded function.

        1. __itruediv__(self: MaterialX.PyMaterialXCore.Color3, arg0: MaterialX.PyMaterialXCore.Color3) -> MaterialX.PyMaterialXCore.Color3

        2. __itruediv__(self: MaterialX.PyMaterialXCore.Color3, arg0: float) -> MaterialX.PyMaterialXCore.Color3
        """
    @overload
    def __itruediv__(self, arg0: float) -> Color3:
        """__itruediv__(*args, **kwargs)
        Overloaded function.

        1. __itruediv__(self: MaterialX.PyMaterialXCore.Color3, arg0: MaterialX.PyMaterialXCore.Color3) -> MaterialX.PyMaterialXCore.Color3

        2. __itruediv__(self: MaterialX.PyMaterialXCore.Color3, arg0: float) -> MaterialX.PyMaterialXCore.Color3
        """
    @staticmethod
    def __len__() -> int:
        """__len__() -> int"""
    @overload
    def __mul__(self, arg0: Color3) -> Color3:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: MaterialX.PyMaterialXCore.Color3, arg0: MaterialX.PyMaterialXCore.Color3) -> MaterialX.PyMaterialXCore.Color3

        2. __mul__(self: MaterialX.PyMaterialXCore.Color3, arg0: float) -> MaterialX.PyMaterialXCore.Color3
        """
    @overload
    def __mul__(self, arg0: float) -> Color3:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: MaterialX.PyMaterialXCore.Color3, arg0: MaterialX.PyMaterialXCore.Color3) -> MaterialX.PyMaterialXCore.Color3

        2. __mul__(self: MaterialX.PyMaterialXCore.Color3, arg0: float) -> MaterialX.PyMaterialXCore.Color3
        """
    def __ne__(self, arg0: Color3) -> bool:
        """__ne__(self: MaterialX.PyMaterialXCore.Color3, arg0: MaterialX.PyMaterialXCore.Color3) -> bool"""
    def __neg__(self) -> Color3:
        """__neg__(self: MaterialX.PyMaterialXCore.Color3) -> MaterialX.PyMaterialXCore.Color3"""
    def __pos__(self) -> Color3:
        """__pos__(self: MaterialX.PyMaterialXCore.Color3) -> MaterialX.PyMaterialXCore.Color3"""
    def __setitem__(self, arg0: int, arg1: float) -> None:
        """__setitem__(self: MaterialX.PyMaterialXCore.Color3, arg0: int, arg1: float) -> None"""
    def __sub__(self, arg0: Color3) -> Color3:
        """__sub__(self: MaterialX.PyMaterialXCore.Color3, arg0: MaterialX.PyMaterialXCore.Color3) -> MaterialX.PyMaterialXCore.Color3"""
    @overload
    def __truediv__(self, arg0: Color3) -> Color3:
        """__truediv__(*args, **kwargs)
        Overloaded function.

        1. __truediv__(self: MaterialX.PyMaterialXCore.Color3, arg0: MaterialX.PyMaterialXCore.Color3) -> MaterialX.PyMaterialXCore.Color3

        2. __truediv__(self: MaterialX.PyMaterialXCore.Color3, arg0: float) -> MaterialX.PyMaterialXCore.Color3
        """
    @overload
    def __truediv__(self, arg0: float) -> Color3:
        """__truediv__(*args, **kwargs)
        Overloaded function.

        1. __truediv__(self: MaterialX.PyMaterialXCore.Color3, arg0: MaterialX.PyMaterialXCore.Color3) -> MaterialX.PyMaterialXCore.Color3

        2. __truediv__(self: MaterialX.PyMaterialXCore.Color3, arg0: float) -> MaterialX.PyMaterialXCore.Color3
        """

class Color4(VectorBase):
    @overload
    def __init__(self) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: MaterialX.PyMaterialXCore.Color4) -> None

        2. __init__(self: MaterialX.PyMaterialXCore.Color4, arg0: float) -> None

        3. __init__(self: MaterialX.PyMaterialXCore.Color4, arg0: Annotated[list[float], FixedSize(4)]) -> None

        4. __init__(self: MaterialX.PyMaterialXCore.Color4, arg0: list[float]) -> None

        5. __init__(self: MaterialX.PyMaterialXCore.Color4, arg0: float, arg1: float, arg2: float, arg3: float) -> None
        """
    @overload
    def __init__(self, arg0: float) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: MaterialX.PyMaterialXCore.Color4) -> None

        2. __init__(self: MaterialX.PyMaterialXCore.Color4, arg0: float) -> None

        3. __init__(self: MaterialX.PyMaterialXCore.Color4, arg0: Annotated[list[float], FixedSize(4)]) -> None

        4. __init__(self: MaterialX.PyMaterialXCore.Color4, arg0: list[float]) -> None

        5. __init__(self: MaterialX.PyMaterialXCore.Color4, arg0: float, arg1: float, arg2: float, arg3: float) -> None
        """
    @overload
    def __init__(self, arg0) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: MaterialX.PyMaterialXCore.Color4) -> None

        2. __init__(self: MaterialX.PyMaterialXCore.Color4, arg0: float) -> None

        3. __init__(self: MaterialX.PyMaterialXCore.Color4, arg0: Annotated[list[float], FixedSize(4)]) -> None

        4. __init__(self: MaterialX.PyMaterialXCore.Color4, arg0: list[float]) -> None

        5. __init__(self: MaterialX.PyMaterialXCore.Color4, arg0: float, arg1: float, arg2: float, arg3: float) -> None
        """
    @overload
    def __init__(self, arg0: list[float]) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: MaterialX.PyMaterialXCore.Color4) -> None

        2. __init__(self: MaterialX.PyMaterialXCore.Color4, arg0: float) -> None

        3. __init__(self: MaterialX.PyMaterialXCore.Color4, arg0: Annotated[list[float], FixedSize(4)]) -> None

        4. __init__(self: MaterialX.PyMaterialXCore.Color4, arg0: list[float]) -> None

        5. __init__(self: MaterialX.PyMaterialXCore.Color4, arg0: float, arg1: float, arg2: float, arg3: float) -> None
        """
    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float, arg3: float) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: MaterialX.PyMaterialXCore.Color4) -> None

        2. __init__(self: MaterialX.PyMaterialXCore.Color4, arg0: float) -> None

        3. __init__(self: MaterialX.PyMaterialXCore.Color4, arg0: Annotated[list[float], FixedSize(4)]) -> None

        4. __init__(self: MaterialX.PyMaterialXCore.Color4, arg0: list[float]) -> None

        5. __init__(self: MaterialX.PyMaterialXCore.Color4, arg0: float, arg1: float, arg2: float, arg3: float) -> None
        """
    def asTuple(self) -> tuple[float, float, float, float]:
        """asTuple(self: MaterialX.PyMaterialXCore.Color4) -> tuple[float, float, float, float]"""
    def copy(self) -> Color4:
        """copy(self: MaterialX.PyMaterialXCore.Color4) -> MaterialX.PyMaterialXCore.Color4

        Create a deep copy of the value.
        """
    def dot(self, arg0: Color4) -> float:
        """dot(self: MaterialX.PyMaterialXCore.Color4, arg0: MaterialX.PyMaterialXCore.Color4) -> float

        Return the dot product of two vectors.
        """
    def getMagnitude(self) -> float:
        """getMagnitude(self: MaterialX.PyMaterialXCore.Color4) -> float

        Return the magnitude of the vector.
        """
    def getNormalized(self) -> Color4:
        """getNormalized(self: MaterialX.PyMaterialXCore.Color4) -> MaterialX.PyMaterialXCore.Color4

        Return a normalized version of the given path, collapsing current path and parent path references so that 'a/.

        /b' and 'c/../d/../a/b' become 'a/b'.
        """
    def __add__(self, arg0: Color4) -> Color4:
        """__add__(self: MaterialX.PyMaterialXCore.Color4, arg0: MaterialX.PyMaterialXCore.Color4) -> MaterialX.PyMaterialXCore.Color4"""
    def __eq__(self, arg0: Color4) -> bool:
        """__eq__(self: MaterialX.PyMaterialXCore.Color4, arg0: MaterialX.PyMaterialXCore.Color4) -> bool"""
    def __getitem__(self, arg0: int) -> float:
        """__getitem__(self: MaterialX.PyMaterialXCore.Color4, arg0: int) -> float"""
    def __iter__(self) -> typing.Iterator[float]:
        """def __iter__(self) -> typing.Iterator[float]"""
    def __iadd__(self, arg0: Color4) -> Color4:
        """__iadd__(self: MaterialX.PyMaterialXCore.Color4, arg0: MaterialX.PyMaterialXCore.Color4) -> MaterialX.PyMaterialXCore.Color4"""
    @overload
    def __imul__(self, arg0: Color4) -> Color4:
        """__imul__(*args, **kwargs)
        Overloaded function.

        1. __imul__(self: MaterialX.PyMaterialXCore.Color4, arg0: MaterialX.PyMaterialXCore.Color4) -> MaterialX.PyMaterialXCore.Color4

        2. __imul__(self: MaterialX.PyMaterialXCore.Color4, arg0: float) -> MaterialX.PyMaterialXCore.Color4
        """
    @overload
    def __imul__(self, arg0: float) -> Color4:
        """__imul__(*args, **kwargs)
        Overloaded function.

        1. __imul__(self: MaterialX.PyMaterialXCore.Color4, arg0: MaterialX.PyMaterialXCore.Color4) -> MaterialX.PyMaterialXCore.Color4

        2. __imul__(self: MaterialX.PyMaterialXCore.Color4, arg0: float) -> MaterialX.PyMaterialXCore.Color4
        """
    def __isub__(self, arg0: Color4) -> Color4:
        """__isub__(self: MaterialX.PyMaterialXCore.Color4, arg0: MaterialX.PyMaterialXCore.Color4) -> MaterialX.PyMaterialXCore.Color4"""
    @overload
    def __itruediv__(self, arg0: Color4) -> Color4:
        """__itruediv__(*args, **kwargs)
        Overloaded function.

        1. __itruediv__(self: MaterialX.PyMaterialXCore.Color4, arg0: MaterialX.PyMaterialXCore.Color4) -> MaterialX.PyMaterialXCore.Color4

        2. __itruediv__(self: MaterialX.PyMaterialXCore.Color4, arg0: float) -> MaterialX.PyMaterialXCore.Color4
        """
    @overload
    def __itruediv__(self, arg0: float) -> Color4:
        """__itruediv__(*args, **kwargs)
        Overloaded function.

        1. __itruediv__(self: MaterialX.PyMaterialXCore.Color4, arg0: MaterialX.PyMaterialXCore.Color4) -> MaterialX.PyMaterialXCore.Color4

        2. __itruediv__(self: MaterialX.PyMaterialXCore.Color4, arg0: float) -> MaterialX.PyMaterialXCore.Color4
        """
    @staticmethod
    def __len__() -> int:
        """__len__() -> int"""
    @overload
    def __mul__(self, arg0: Color4) -> Color4:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: MaterialX.PyMaterialXCore.Color4, arg0: MaterialX.PyMaterialXCore.Color4) -> MaterialX.PyMaterialXCore.Color4

        2. __mul__(self: MaterialX.PyMaterialXCore.Color4, arg0: float) -> MaterialX.PyMaterialXCore.Color4
        """
    @overload
    def __mul__(self, arg0: float) -> Color4:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: MaterialX.PyMaterialXCore.Color4, arg0: MaterialX.PyMaterialXCore.Color4) -> MaterialX.PyMaterialXCore.Color4

        2. __mul__(self: MaterialX.PyMaterialXCore.Color4, arg0: float) -> MaterialX.PyMaterialXCore.Color4
        """
    def __ne__(self, arg0: Color4) -> bool:
        """__ne__(self: MaterialX.PyMaterialXCore.Color4, arg0: MaterialX.PyMaterialXCore.Color4) -> bool"""
    def __neg__(self) -> Color4:
        """__neg__(self: MaterialX.PyMaterialXCore.Color4) -> MaterialX.PyMaterialXCore.Color4"""
    def __pos__(self) -> Color4:
        """__pos__(self: MaterialX.PyMaterialXCore.Color4) -> MaterialX.PyMaterialXCore.Color4"""
    def __setitem__(self, arg0: int, arg1: float) -> None:
        """__setitem__(self: MaterialX.PyMaterialXCore.Color4, arg0: int, arg1: float) -> None"""
    def __sub__(self, arg0: Color4) -> Color4:
        """__sub__(self: MaterialX.PyMaterialXCore.Color4, arg0: MaterialX.PyMaterialXCore.Color4) -> MaterialX.PyMaterialXCore.Color4"""
    @overload
    def __truediv__(self, arg0: Color4) -> Color4:
        """__truediv__(*args, **kwargs)
        Overloaded function.

        1. __truediv__(self: MaterialX.PyMaterialXCore.Color4, arg0: MaterialX.PyMaterialXCore.Color4) -> MaterialX.PyMaterialXCore.Color4

        2. __truediv__(self: MaterialX.PyMaterialXCore.Color4, arg0: float) -> MaterialX.PyMaterialXCore.Color4
        """
    @overload
    def __truediv__(self, arg0: float) -> Color4:
        """__truediv__(*args, **kwargs)
        Overloaded function.

        1. __truediv__(self: MaterialX.PyMaterialXCore.Color4, arg0: MaterialX.PyMaterialXCore.Color4) -> MaterialX.PyMaterialXCore.Color4

        2. __truediv__(self: MaterialX.PyMaterialXCore.Color4, arg0: float) -> MaterialX.PyMaterialXCore.Color4
        """

class CommentElement(Element):
    CATEGORY: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class Document(GraphElement):
    addMaterial: ClassVar[Callable] = ...
    getMaterials: ClassVar[Callable] = ...
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def addAttributeDef(self, arg0: str) -> AttributeDef:
        """addAttributeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.AttributeDef

        Add an AttributeDef to the document.

        Args:
            name: The name of the new AttributeDef. If no name is specified, then a unique name will automatically be generated.

        Returns:
            A shared pointer to the new AttributeDef.
        """
    def addCollection(self, name: str = ...) -> Collection:
        """addCollection(self: MaterialX.PyMaterialXCore.Document, name: str = '') -> MaterialX.PyMaterialXCore.Collection

        Add a Collection to the document.

        Args:
            name: The name of the new Collection. If no name is specified, then a unique name will automatically be generated.

        Returns:
            A shared pointer to the new Collection.
        """
    def addGeomInfo(self, name: str = ..., geom: str = ...) -> GeomInfo:
        """addGeomInfo(self: MaterialX.PyMaterialXCore.Document, name: str = '', geom: str = '/') -> MaterialX.PyMaterialXCore.GeomInfo

        Add a GeomInfo to the document.

        Args:
            name: The name of the new GeomInfo. If no name is specified, then a unique name will automatically be generated.
            geom: An optional geometry string for the GeomInfo.

        Returns:
            A shared pointer to the new GeomInfo.
        """
    def addGeomPropDef(self, arg0: str, arg1: str) -> GeomPropDef:
        """addGeomPropDef(self: MaterialX.PyMaterialXCore.Document, arg0: str, arg1: str) -> MaterialX.PyMaterialXCore.GeomPropDef

        Add a GeomPropDef to the document.

        Args:
            name: The name of the new GeomPropDef.
            geomprop: The geometric property to use for the GeomPropDef.

        Returns:
            A shared pointer to the new GeomPropDef.
        """
    def addImplementation(self, name: str = ...) -> Implementation:
        """addImplementation(self: MaterialX.PyMaterialXCore.Document, name: str = '') -> MaterialX.PyMaterialXCore.Implementation

        Add an Implementation to the document.

        Args:
            name: The name of the new Implementation. If no name is specified, then a unique name will automatically be generated.

        Returns:
            A shared pointer to the new Implementation.
        """
    def addLook(self, name: str = ...) -> Look:
        """addLook(self: MaterialX.PyMaterialXCore.Document, name: str = '') -> MaterialX.PyMaterialXCore.Look

        Add a Look to the document.

        Args:
            name: The name of the new Look. If no name is specified, then a unique name will automatically be generated.

        Returns:
            A shared pointer to the new Look.
        """
    def addLookGroup(self, name: str = ...) -> LookGroup:
        """addLookGroup(self: MaterialX.PyMaterialXCore.Document, name: str = '') -> MaterialX.PyMaterialXCore.LookGroup

        Add a LookGroup to the document.

        Args:
            name: The name of the new LookGroup. If no name is specified, then a unique name will automatically be generated.

        Returns:
            A shared pointer to the new LookGroup.
        """
    def addNodeDef(self, name: str = ..., type: str = ..., node: str = ...) -> NodeDef:
        """addNodeDef(self: MaterialX.PyMaterialXCore.Document, name: str = '', type: str = 'color3', node: str = '') -> MaterialX.PyMaterialXCore.NodeDef

        Add a NodeDef to the document.

        Args:
            name: The name of the new NodeDef. If no name is specified, then a unique name will automatically be generated.
            type: An optional type string. If specified, then the new NodeDef will be assigned an Output of the given type.
            node: An optional node string.

        Returns:
            A shared pointer to the new NodeDef.
        """
    @overload
    def addNodeDefFromGraph(self, arg0: NodeGraph, arg1: str, arg2: str, arg3: str) -> NodeDef:
        """addNodeDefFromGraph(*args, **kwargs)
        Overloaded function.

        1. addNodeDefFromGraph(self: MaterialX.PyMaterialXCore.Document, arg0: MaterialX.PyMaterialXCore.NodeGraph, arg1: str, arg2: str, arg3: str) -> MaterialX.PyMaterialXCore.NodeDef

        2. addNodeDefFromGraph(self: MaterialX.PyMaterialXCore.Document, arg0: MaterialX.PyMaterialXCore.NodeGraph, arg1: str, arg2: str, arg3: str, arg4: bool, arg5: str, arg6: str) -> MaterialX.PyMaterialXCore.NodeDef
        """
    @overload
    def addNodeDefFromGraph(self, arg0: NodeGraph, arg1: str, arg2: str, arg3: str, arg4: bool, arg5: str, arg6: str) -> NodeDef:
        """addNodeDefFromGraph(*args, **kwargs)
        Overloaded function.

        1. addNodeDefFromGraph(self: MaterialX.PyMaterialXCore.Document, arg0: MaterialX.PyMaterialXCore.NodeGraph, arg1: str, arg2: str, arg3: str) -> MaterialX.PyMaterialXCore.NodeDef

        2. addNodeDefFromGraph(self: MaterialX.PyMaterialXCore.Document, arg0: MaterialX.PyMaterialXCore.NodeGraph, arg1: str, arg2: str, arg3: str, arg4: bool, arg5: str, arg6: str) -> MaterialX.PyMaterialXCore.NodeDef
        """
    def addNodeGraph(self, name: str = ...) -> NodeGraph:
        """addNodeGraph(self: MaterialX.PyMaterialXCore.Document, name: str = '') -> MaterialX.PyMaterialXCore.NodeGraph

        Add a NodeGraph to the document.

        Args:
            name: The name of the new NodeGraph. If no name is specified, then a unique name will automatically be generated.

        Returns:
            A shared pointer to the new NodeGraph.
        """
    def addPropertySet(self, name: str = ...) -> PropertySet:
        """addPropertySet(self: MaterialX.PyMaterialXCore.Document, name: str = '') -> MaterialX.PyMaterialXCore.PropertySet

        Add a PropertySet to the document.

        Args:
            name: The name of the new PropertySet. If no name is specified, then a unique name will automatically be generated.

        Returns:
            A shared pointer to the new PropertySet.
        """
    def addTargetDef(self, arg0: str) -> TargetDef:
        """addTargetDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.TargetDef

        Add an TargetDef to the document.

        Args:
            name: The name of the new TargetDef. If no name is specified, then a unique name will automatically be generated.

        Returns:
            A shared pointer to the new TargetDef.
        """
    def addTypeDef(self, name: str = ...) -> TypeDef:
        """addTypeDef(self: MaterialX.PyMaterialXCore.Document, name: str = '') -> MaterialX.PyMaterialXCore.TypeDef

        Add a TypeDef to the document.

        Args:
            name: The name of the new TypeDef. If no name is specified, then a unique name will automatically be generated.

        Returns:
            A shared pointer to the new TypeDef.
        """
    def addUnitDef(self, arg0: str) -> UnitDef:
        """addUnitDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.UnitDef"""
    def addUnitTypeDef(self, arg0: str) -> UnitTypeDef:
        """addUnitTypeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.UnitTypeDef"""
    def addVariantSet(self, name: str = ...) -> VariantSet:
        """addVariantSet(self: MaterialX.PyMaterialXCore.Document, name: str = '') -> MaterialX.PyMaterialXCore.VariantSet

        Add a VariantSet to the document.

        Args:
            name: The name of the new VariantSet. If no name is specified, then a unique name will automatically be generated.

        Returns:
            A shared pointer to the new VariantSet.
        """
    def copy(self) -> Document:
        """copy(self: MaterialX.PyMaterialXCore.Document) -> MaterialX.PyMaterialXCore.Document

        Create a deep copy of the value.
        """
    def getAttributeDef(self, arg0: str) -> AttributeDef:
        """getAttributeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.AttributeDef

        Return the AttributeDef, if any, with the given name.
        """
    def getAttributeDefs(self) -> list[AttributeDef]:
        """getAttributeDefs(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.AttributeDef]

        Return a vector of all AttributeDef elements in the document.
        """
    def getCollection(self, arg0: str) -> Collection:
        """getCollection(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.Collection

        Return the Collection, if any, with the given name.
        """
    def getCollections(self) -> list[Collection]:
        """getCollections(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.Collection]

        Return a vector of all Collection elements in the document.
        """
    def getColorManagementConfig(self) -> str:
        """getColorManagementConfig(self: MaterialX.PyMaterialXCore.Document) -> str

        Return the color management config string.
        """
    def getColorManagementSystem(self) -> str:
        """getColorManagementSystem(self: MaterialX.PyMaterialXCore.Document) -> str

        Return the color management system string.
        """
    def getDataLibrary(self) -> Document:
        """getDataLibrary(self: MaterialX.PyMaterialXCore.Document) -> MaterialX.PyMaterialXCore.Document

        Return the data library, if any, referenced by this document.
        """
    def getGeomInfo(self, arg0: str) -> GeomInfo:
        """getGeomInfo(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.GeomInfo

        Return the GeomInfo, if any, with the given name.
        """
    def getGeomInfos(self) -> list[GeomInfo]:
        """getGeomInfos(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.GeomInfo]

        Return a vector of all GeomInfo elements in the document.
        """
    def getGeomPropDef(self, arg0: str) -> GeomPropDef:
        """getGeomPropDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.GeomPropDef

        Return the GeomPropDef, if any, with the given name.
        """
    def getGeomPropDefs(self) -> list[GeomPropDef]:
        """getGeomPropDefs(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.GeomPropDef]

        Return a vector of all GeomPropDef elements in the document.
        """
    def getGeomPropValue(self, geomPropName: str, geom: str = ...) -> Value:
        """getGeomPropValue(self: MaterialX.PyMaterialXCore.Document, geomPropName: str, geom: str = '/') -> MaterialX.PyMaterialXCore.Value

        Return the value of a geometric property for the given geometry string.
        """
    def getImplementation(self, arg0: str) -> Implementation:
        """getImplementation(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.Implementation

        Return the Implementation, if any, with the given name.
        """
    def getImplementations(self) -> list[Implementation]:
        """getImplementations(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.Implementation]

        Return a vector of all Implementation elements in the document.
        """
    def getLook(self, arg0: str) -> Look:
        """getLook(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.Look

        Return the Look, if any, with the given name.
        """
    def getLookGroup(self, arg0: str) -> LookGroup:
        """getLookGroup(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.LookGroup

        Return the LookGroup, if any, with the given name.
        """
    def getLookGroups(self) -> list[LookGroup]:
        """getLookGroups(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.LookGroup]

        Return a vector of all LookGroup elements in the document.
        """
    def getLooks(self) -> list[Look]:
        """getLooks(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.Look]

        Return a vector of all Look elements in the document.
        """
    def getMatchingImplementations(self, arg0: str) -> list[InterfaceElement]:
        """getMatchingImplementations(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> list[MaterialX.PyMaterialXCore.InterfaceElement]

        Return a vector of all node implementations that match the given NodeDef string.

        Note that a node implementation may be either an Implementation element or NodeGraph element.
        """
    def getMatchingNodeDefs(self, arg0: str) -> list[NodeDef]:
        """getMatchingNodeDefs(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> list[MaterialX.PyMaterialXCore.NodeDef]

        Return a vector of all NodeDef elements that match the given node name.
        """
    def getMatchingPorts(self, arg0: str) -> list[PortElement]:
        """getMatchingPorts(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> list[MaterialX.PyMaterialXCore.PortElement]

        Return a vector of all port elements that match the given node name.

        Port elements support spatially-varying upstream connections to nodes, and include both Input and Output elements.
        """
    def getMaterialOutputs(self) -> list[Output]:
        """getMaterialOutputs(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.Output]

        Return material-type outputs for all nodegraphs in the document.
        """
    def getNodeDef(self, arg0: str) -> NodeDef:
        """getNodeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.NodeDef

        Returns a nodedef for a given transform.
        """
    def getNodeDefs(self) -> list[NodeDef]:
        """getNodeDefs(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.NodeDef]

        Return a vector of all NodeDef elements in the document.
        """
    def getNodeGraph(self, arg0: str) -> NodeGraph:
        """getNodeGraph(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.NodeGraph

        Return the NodeGraph, if any, with the given name.
        """
    def getNodeGraphs(self) -> list[NodeGraph]:
        """getNodeGraphs(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.NodeGraph]

        Return a vector of all NodeGraph elements in the document.
        """
    def getPropertySet(self, arg0: str) -> PropertySet:
        """getPropertySet(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.PropertySet

        Return the PropertySet, if any, with the given name.
        """
    def getPropertySets(self) -> list[PropertySet]:
        """getPropertySets(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.PropertySet]

        Return a vector of all PropertySet elements in the document.
        """
    def getReferencedSourceUris(self) -> set[str]:
        """getReferencedSourceUris(self: MaterialX.PyMaterialXCore.Document) -> set[str]

        Get a list of source URIs referenced by the document.
        """
    def getTargetDef(self, arg0: str) -> TargetDef:
        """getTargetDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.TargetDef

        Return the AttributeDef, if any, with the given name.
        """
    def getTargetDefs(self) -> list[TargetDef]:
        """getTargetDefs(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.TargetDef]

        Return a vector of all TargetDef elements in the document.
        """
    def getTypeDef(self, arg0: str) -> TypeDef:
        """getTypeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.TypeDef

        Return the TypeDef, if any, with the given name.
        """
    def getTypeDefs(self) -> list[TypeDef]:
        """getTypeDefs(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.TypeDef]

        Return a vector of all TypeDef elements in the document.
        """
    def getUnitDef(self, arg0: str) -> UnitDef:
        """getUnitDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.UnitDef

        Return the UnitDef, if any, with the given name.
        """
    def getUnitDefs(self) -> list[UnitDef]:
        """getUnitDefs(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.UnitDef]

        Return a vector of all Member elements in the TypeDef.
        """
    def getUnitTypeDef(self, arg0: str) -> UnitTypeDef:
        """getUnitTypeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.UnitTypeDef

        Return the UnitTypeDef, if any, with the given name.
        """
    def getUnitTypeDefs(self) -> list[UnitTypeDef]:
        """getUnitTypeDefs(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.UnitTypeDef]

        Return a vector of all UnitTypeDef elements in the document.
        """
    def getVariantSet(self, arg0: str) -> VariantSet:
        """getVariantSet(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.VariantSet

        Return the VariantSet, if any, with the given name.
        """
    def getVariantSets(self) -> list[VariantSet]:
        """getVariantSets(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.VariantSet]

        Return a vector of all VariantSet elements in the document.
        """
    def hasColorManagementConfig(self) -> bool:
        """hasColorManagementConfig(self: MaterialX.PyMaterialXCore.Document) -> bool

        Return true if a color management config string has been set.
        """
    def hasColorManagementSystem(self) -> bool:
        """hasColorManagementSystem(self: MaterialX.PyMaterialXCore.Document) -> bool

        Return true if a color management system string has been set.
        """
    def hasDataLibrary(self) -> bool:
        """hasDataLibrary(self: MaterialX.PyMaterialXCore.Document) -> bool

        Return true if this document has a data library.
        """
    def importLibrary(self, arg0: Document) -> None:
        """importLibrary(self: MaterialX.PyMaterialXCore.Document, arg0: MaterialX.PyMaterialXCore.Document) -> None

        Import the given data library into this document.

        Args:
            library: The data library to be imported.
        """
    def initialize(self) -> None:
        """initialize(self: MaterialX.PyMaterialXCore.Document) -> None

        Initialize with the given implementation element.

        Initialization must set the name and hash for the implementation, as well as any other data needed to emit code for the node.
        """
    def removeAttributeDef(self, arg0: str) -> None:
        """removeAttributeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None

        Remove the AttributeDef, if any, with the given name.
        """
    def removeCollection(self, arg0: str) -> None:
        """removeCollection(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None

        Remove the Collection, if any, with the given name.
        """
    def removeGeomInfo(self, arg0: str) -> None:
        """removeGeomInfo(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None

        Remove the GeomInfo, if any, with the given name.
        """
    def removeGeomPropDef(self, arg0: str) -> None:
        """removeGeomPropDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None

        Remove the GeomPropDef, if any, with the given name.
        """
    def removeImplementation(self, arg0: str) -> None:
        """removeImplementation(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None

        Remove the Implementation, if any, with the given name.
        """
    def removeLook(self, arg0: str) -> None:
        """removeLook(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None

        Remove the Look, if any, with the given name.
        """
    def removeLookGroup(self, arg0: str) -> None:
        """removeLookGroup(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None

        Remove the LookGroup, if any, with the given name.
        """
    def removeNodeDef(self, arg0: str) -> None:
        """removeNodeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None

        Remove the NodeDef, if any, with the given name.
        """
    def removeNodeGraph(self, arg0: str) -> None:
        """removeNodeGraph(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None

        Remove the NodeGraph, if any, with the given name.
        """
    def removePropertySet(self, arg0: str) -> None:
        """removePropertySet(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None

        Remove the PropertySet, if any, with the given name.
        """
    def removeTargetDef(self, arg0: str) -> None:
        """removeTargetDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None

        Remove the TargetDef, if any, with the given name.
        """
    def removeTypeDef(self, arg0: str) -> None:
        """removeTypeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None

        Remove the TypeDef, if any, with the given name.
        """
    def removeUnitDef(self, arg0: str) -> None:
        """removeUnitDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None

        Remove the UnitDef, if any, with the given name.
        """
    def removeUnitTypeDef(self, arg0: str) -> None:
        """removeUnitTypeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None

        Remove the UnitTypeDef, if any, with the given name.
        """
    def removeVariantSet(self, arg0: str) -> None:
        """removeVariantSet(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None

        Remove the VariantSet, if any, with the given name.
        """
    def setColorManagementConfig(self, arg0: str) -> None:
        """setColorManagementConfig(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None

        Set the color management config string.
        """
    def setColorManagementSystem(self, arg0: str) -> None:
        """setColorManagementSystem(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None

        Set the color management system string.
        """
    def setDataLibrary(self, arg0: Document) -> None:
        """setDataLibrary(self: MaterialX.PyMaterialXCore.Document, arg0: MaterialX.PyMaterialXCore.Document) -> None

        Store a reference to a data library in this document.
        """
    def upgradeVersion(self) -> None:
        """upgradeVersion(self: MaterialX.PyMaterialXCore.Document) -> None

        Upgrade the content of this document from earlier supported versions to the library version.
        """

class Edge:
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def getConnectingElement(self) -> Element:
        """getConnectingElement(self: MaterialX.PyMaterialXCore.Edge) -> MaterialX.PyMaterialXCore.Element

        Return the connecting element of the edge, if any.
        """
    def getDownstreamElement(self) -> Element:
        """getDownstreamElement(self: MaterialX.PyMaterialXCore.Edge) -> MaterialX.PyMaterialXCore.Element

        Return the downstream element of the edge.
        """
    def getName(self) -> str:
        """getName(self: MaterialX.PyMaterialXCore.Edge) -> str

        Return the ColorManagementSystem name.
        """
    def getUpstreamElement(self) -> Element:
        """getUpstreamElement(self: MaterialX.PyMaterialXCore.Edge) -> MaterialX.PyMaterialXCore.Element

        Return the upstream element of the edge.
        """

class Element:
    COLOR_SPACE_ATTRIBUTE: ClassVar[str] = ...  # read-only
    DOC_ATTRIBUTE: ClassVar[str] = ...  # read-only
    FILE_PREFIX_ATTRIBUTE: ClassVar[str] = ...  # read-only
    GEOM_PREFIX_ATTRIBUTE: ClassVar[str] = ...  # read-only
    INHERIT_ATTRIBUTE: ClassVar[str] = ...  # read-only
    NAMESPACE_ATTRIBUTE: ClassVar[str] = ...  # read-only
    NAME_ATTRIBUTE: ClassVar[str] = ...  # read-only
    XPOS_ATTRIBUTE: ClassVar[str] = ...  # read-only
    YPOS_ATTRIBUTE: ClassVar[str] = ...  # read-only
    addChild: ClassVar[Callable] = ...
    getChild: ClassVar[Callable] = ...
    getChildOfType: ClassVar[Callable] = ...
    getChildrenOfType: ClassVar[Callable] = ...
    isA: ClassVar[Callable] = ...
    removeChildOfType: ClassVar[Callable] = ...
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def addChildOfCategory(self, category: str, name: str = ...) -> Element:
        """addChildOfCategory(self: MaterialX.PyMaterialXCore.Element, category: str, name: str = '') -> MaterialX.PyMaterialXCore.Element

        Add a child element of the given category and name.

        Args:
            category: The category string of the new child element. If the category string is recognized, then the corresponding Element subclass is generated; otherwise, a GenericElement is generated.
            name: The name of the new child element. If no name is specified, then a unique name will automatically be generated.

        Returns:
            A shared pointer to the new child element.
        """
    def asString(self) -> str:
        """asString(self: MaterialX.PyMaterialXCore.Element) -> str

        Return a single-line description of this element, including its category, name, and attributes.
        """
    def changeChildCategory(self, arg0: Element, arg1: str) -> Element:
        """changeChildCategory(self: MaterialX.PyMaterialXCore.Element, arg0: MaterialX.PyMaterialXCore.Element, arg1: str) -> MaterialX.PyMaterialXCore.Element

        Change the category of the given child element.

        Args:
            child: The child element that will be modified.
            category: The new category string for the child element.

        Returns:
            A shared pointer to a new child element, containing the contents of the original child but with a new category and subclass.
        """
    def clearContent(self) -> None:
        """clearContent(self: MaterialX.PyMaterialXCore.Element) -> None

        Clear all attributes and descendants from this element.
        """
    def copyContentFrom(self, arg0: Element) -> None:
        """copyContentFrom(self: MaterialX.PyMaterialXCore.Element, arg0: MaterialX.PyMaterialXCore.Element) -> None

        Copy all attributes and descendants from the given element to this one.

        Args:
            source: The element from which content is copied.
        """
    def createStringResolver(self, *args, **kwargs):
        '''createStringResolver(self: MaterialX.PyMaterialXCore.Element, geom: str = \'\') -> MaterialX_v1_39_5::StringResolver

        Construct a StringResolver at the scope of this element.

        Args:
            geom: An optional geometry name, which will be used to select the applicable set of geometry token substitutions. By default, no geometry token substitutions are applied. If the universal geometry name "/" is given, then all geometry token substitutions are applied,

        Returns:
            A shared pointer to a StringResolver.
        '''
    def createValidChildName(self, arg0: str) -> str:
        """createValidChildName(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> str

        Using the input name as a starting point, modify it to create a valid, unique name for a child element.
        """
    def getActiveColorSpace(self) -> str:
        """getActiveColorSpace(self: MaterialX.PyMaterialXCore.Element) -> str

        Return the color space string that is active at the scope of this element, taking all ancestor elements into account.
        """
    def getActiveFilePrefix(self) -> str:
        """getActiveFilePrefix(self: MaterialX.PyMaterialXCore.Element) -> str

        Return the file prefix string that is active at the scope of this element, taking all ancestor elements into account.
        """
    def getActiveGeomPrefix(self) -> str:
        """getActiveGeomPrefix(self: MaterialX.PyMaterialXCore.Element) -> str

        Return the geom prefix string that is active at the scope of this element, taking all ancestor elements into account.
        """
    def getActiveSourceUri(self) -> str:
        """getActiveSourceUri(self: MaterialX.PyMaterialXCore.Element) -> str

        Return the source URI that is active at the scope of this element, taking all ancestor elements into account.
        """
    def getAttribute(self, arg0: str) -> str:
        """getAttribute(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> str

        Return the value string of the given attribute.

        If the given attribute is not present, then an empty string is returned.
        """
    def getAttributeNames(self) -> list[str]:
        """getAttributeNames(self: MaterialX.PyMaterialXCore.Element) -> list[str]

        Return a vector of stored attribute names, in the order they were set.
        """
    def getCategory(self) -> str:
        '''getCategory(self: MaterialX.PyMaterialXCore.Element) -> str

        Return the element\'s category string.

        The category of a MaterialX element represents its role within the document, with common examples being "material", "nodegraph", and "image".
        '''
    def getChildIndex(self, arg0: str) -> int:
        """getChildIndex(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> int

        Return the index of the child, if any, with the given name.

        If no child with the given name is found, then -1 is returned.
        """
    def getChildren(self) -> list[Element]:
        """getChildren(self: MaterialX.PyMaterialXCore.Element) -> list[MaterialX.PyMaterialXCore.Element]

        Return a constant vector of all child elements.

        The returned vector maintains the order in which children were added.
        """
    def getColorSpace(self) -> str:
        """getColorSpace(self: MaterialX.PyMaterialXCore.Element) -> str

        Return the element's color space string.
        """
    def getDescendant(self, arg0: str) -> Element:
        """getDescendant(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> MaterialX.PyMaterialXCore.Element

        Return the element specified by the given hierarchical name path, relative to the current element.

        Args:
            namePath: The relative name path of the specified element.
        """
    def getDocString(self) -> str:
        """getDocString(self: MaterialX.PyMaterialXCore.Element) -> str

        Return the documentation string of this element.
        """
    def getDocument(self, *args, **kwargs):
        """getDocument(self: MaterialX.PyMaterialXCore.Element) -> MaterialX_v1_39_5::Document

        Return the root document of our tree.
        """
    def getFilePrefix(self) -> str:
        """getFilePrefix(self: MaterialX.PyMaterialXCore.Element) -> str

        Return the element's file prefix string.
        """
    def getGeomPrefix(self) -> str:
        """getGeomPrefix(self: MaterialX.PyMaterialXCore.Element) -> str

        Return the element's geom prefix string.
        """
    def getInheritString(self) -> str:
        """getInheritString(self: MaterialX.PyMaterialXCore.Element) -> str

        Return the inherit string of this element.
        """
    def getInheritsFrom(self) -> Element:
        """getInheritsFrom(self: MaterialX.PyMaterialXCore.Element) -> MaterialX.PyMaterialXCore.Element

        Return the element, if any, that this one directly inherits from.
        """
    def getName(self) -> str:
        """getName(self: MaterialX.PyMaterialXCore.Element) -> str

        Return the ColorManagementSystem name.
        """
    def getNamePath(self, relativeTo: Element = ...) -> str:
        """getNamePath(self: MaterialX.PyMaterialXCore.Element, relativeTo: MaterialX.PyMaterialXCore.Element = None) -> str

        Return the element's hierarchical name path, relative to the root document.

        Args:
            relativeTo: If a valid ancestor element is specified, then the returned path will be relative to this ancestor.
        """
    def getNamespace(self) -> str:
        """getNamespace(self: MaterialX.PyMaterialXCore.Element) -> str

        Return the namespace string of this element.
        """
    def getParent(self) -> Element:
        """getParent(self: MaterialX.PyMaterialXCore.Element) -> MaterialX.PyMaterialXCore.Element

        Return our parent element.
        """
    def getQualifiedName(self, arg0: str) -> str:
        """getQualifiedName(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> str

        Return a qualified version of the given name, taking the namespace at the scope of this element into account.
        """
    def getRoot(self) -> Element:
        """getRoot(self: MaterialX.PyMaterialXCore.Element) -> MaterialX.PyMaterialXCore.Element

        Return the root element of our tree.
        """
    def getSelf(self) -> Element:
        """getSelf(self: MaterialX.PyMaterialXCore.Element) -> MaterialX.PyMaterialXCore.Element

        Return our self pointer.
        """
    def getSourceUri(self) -> str:
        """getSourceUri(self: MaterialX.PyMaterialXCore.Element) -> str

        Return the element's source URI.
        """
    def getUpstreamEdge(self, *args, **kwargs):
        """getUpstreamEdge(self: MaterialX.PyMaterialXCore.Element, index: int = 0) -> MaterialX_v1_39_5::Edge

        Return the Edge with the given index that lies directly upstream from this element in the dataflow graph.

        Args:
            index: An optional index of the edge to be returned, where the valid index range may be determined with getUpstreamEdgeCount.

        Returns:
            The upstream Edge, if valid, or an empty Edge object.
        """
    def getUpstreamEdgeCount(self) -> int:
        """getUpstreamEdgeCount(self: MaterialX.PyMaterialXCore.Element) -> int

        Return the number of queryable upstream edges for this element.
        """
    def getUpstreamElement(self, index: int = ...) -> Element:
        """getUpstreamElement(self: MaterialX.PyMaterialXCore.Element, index: int = 0) -> MaterialX.PyMaterialXCore.Element

        Return the upstream element of the edge.
        """
    def hasAttribute(self, arg0: str) -> bool:
        """hasAttribute(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> bool

        Return true if the given attribute is present.
        """
    def hasColorSpace(self) -> bool:
        """hasColorSpace(self: MaterialX.PyMaterialXCore.Element) -> bool

        Return true if the given element has a color space string.
        """
    def hasFilePrefix(self) -> bool:
        """hasFilePrefix(self: MaterialX.PyMaterialXCore.Element) -> bool

        Return true if the given element has a file prefix string.
        """
    def hasGeomPrefix(self) -> bool:
        """hasGeomPrefix(self: MaterialX.PyMaterialXCore.Element) -> bool

        Return true if the given element has a geom prefix string.
        """
    def hasInheritString(self) -> bool:
        """hasInheritString(self: MaterialX.PyMaterialXCore.Element) -> bool

        Return true if this element has an inherit string.
        """
    def hasInheritanceCycle(self) -> bool:
        """hasInheritanceCycle(self: MaterialX.PyMaterialXCore.Element) -> bool

        Return true if the inheritance chain for this element contains a cycle.
        """
    def hasInheritedBase(self, arg0: Element) -> bool:
        """hasInheritedBase(self: MaterialX.PyMaterialXCore.Element, arg0: MaterialX.PyMaterialXCore.Element) -> bool

        Return true if this element has the given element as an inherited base, taking the full inheritance chain into account.
        """
    def hasNamespace(self) -> bool:
        """hasNamespace(self: MaterialX.PyMaterialXCore.Element) -> bool

        Return true if this element has a namespace string.
        """
    def hasSourceUri(self) -> bool:
        """hasSourceUri(self: MaterialX.PyMaterialXCore.Element) -> bool

        Return true if this element has a source URI.
        """
    def isEquivalent(self, arg0: Element, arg1) -> tuple[bool, str]:
        """isEquivalent(self: MaterialX.PyMaterialXCore.Element, arg0: MaterialX.PyMaterialXCore.Element, arg1: MaterialX_v1_39_5::ElementEquivalenceOptions) -> tuple[bool, str]

        Return true if the given element tree, including all descendents, is considered to be equivalent to this one based on the equivalence criteria provided.

        Args:
            rhs: Element to compare against
            options: Equivalence criteria
            message: Optional text description of differences

        Returns:
            True if the elements are equivalent. False otherwise.
        """
    def removeAttribute(self, arg0: str) -> None:
        """removeAttribute(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None

        Remove the given attribute, if present.
        """
    def removeChild(self, arg0: str) -> None:
        """removeChild(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None

        Remove the child element, if any, with the given name.
        """
    def setAttribute(self, arg0: str, arg1: str) -> None:
        """setAttribute(self: MaterialX.PyMaterialXCore.Element, arg0: str, arg1: str) -> None

        Set the value string of the given attribute.
        """
    def setCategory(self, arg0: str) -> None:
        """setCategory(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None

        Set the element's category string.
        """
    def setChildIndex(self, arg0: str, arg1: int) -> None:
        """setChildIndex(self: MaterialX.PyMaterialXCore.Element, arg0: str, arg1: int) -> None

        Set the index of the child, if any, with the given name.

        If the given index is out of bounds, then an exception is thrown.
        """
    def setColorSpace(self, arg0: str) -> None:
        """setColorSpace(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None

        Set the element's color space string.
        """
    def setDocString(self, arg0: str) -> None:
        """setDocString(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None

        Set the documentation string of this element.
        """
    def setFilePrefix(self, arg0: str) -> None:
        """setFilePrefix(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None

        Set the element's file prefix string.
        """
    def setGeomPrefix(self, arg0: str) -> None:
        """setGeomPrefix(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None

        Set the element's geom prefix string.
        """
    def setInheritString(self, arg0: str) -> None:
        """setInheritString(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None

        Set the inherit string of this element.
        """
    def setInheritsFrom(self, arg0: Element) -> None:
        """setInheritsFrom(self: MaterialX.PyMaterialXCore.Element, arg0: MaterialX.PyMaterialXCore.Element) -> None

        Set the element that this one directly inherits from.
        """
    def setName(self, arg0: str) -> None:
        """setName(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None

        Set the element's name string.
        """
    def setNamespace(self, arg0: str) -> None:
        """setNamespace(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None

        Set the namespace string of this element.
        """
    def setSourceUri(self, arg0: str) -> None:
        """setSourceUri(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None

        Set the element's source URI.

        Args:
            sourceUri: A URI string representing the resource from which this element originates. This string may be used by serialization and deserialization routines to maintain hierarchies of include references.
        """
    def traverseGraph(self, *args, **kwargs):
        """traverseGraph(self: MaterialX.PyMaterialXCore.Element) -> MaterialX_v1_39_5::GraphIterator

        Traverse the dataflow graph from the given element to each of its upstream sources in depth-first order, using pre-order visitation.

        Returns:
            A GraphIterator object.
        """
    def traverseInheritance(self, *args, **kwargs):
        """traverseInheritance(self: MaterialX.PyMaterialXCore.Element) -> MaterialX_v1_39_5::InheritanceIterator

        Traverse the inheritance chain from the given element to each element from which it inherits.

        Returns:
            An InheritanceIterator object.
        """
    def traverseTree(self, *args, **kwargs):
        """traverseTree(self: MaterialX.PyMaterialXCore.Element) -> MaterialX_v1_39_5::TreeIterator

        Traverse the tree from the given element to each of its descendants in depth-first order, using pre-order visitation.

        Returns:
            A TreeIterator object.
        """
    def validate(self) -> tuple[bool, str]:
        """validate(self: MaterialX.PyMaterialXCore.Element) -> tuple[bool, str]

        Validate that the given element tree, including all descendants, is consistent with the MaterialX specification.
        """
    def __eq__(self, arg0: Element) -> bool:
        """__eq__(self: MaterialX.PyMaterialXCore.Element, arg0: MaterialX.PyMaterialXCore.Element) -> bool"""
    def __ne__(self, arg0: Element) -> bool:
        """__ne__(self: MaterialX.PyMaterialXCore.Element, arg0: MaterialX.PyMaterialXCore.Element) -> bool"""

class ElementEquivalenceOptions:
    attributeExclusionList: set[str]
    floatFormat: Incomplete
    floatPrecision: int
    performValueComparisons: bool
    def __init__(self) -> None:
        """__init__(self: MaterialX.PyMaterialXCore.ElementEquivalenceOptions) -> None"""

class ElementPredicate:
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class Exception(Exception): ...

class ExceptionFoundCycle(Exception): ...

class ExceptionOrphanedElement(Exception): ...

class GenericElement(Element):
    CATEGORY: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class GeomElement(Element):
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def getCollection(self, *args, **kwargs):
        """getCollection(self: MaterialX.PyMaterialXCore.GeomElement) -> MaterialX_v1_39_5::Collection

        Return the Collection, if any, with the given name.
        """
    def getCollectionString(self) -> str:
        """getCollectionString(self: MaterialX.PyMaterialXCore.GeomElement) -> str

        Return the collection string of this element.
        """
    def getGeom(self) -> str:
        """getGeom(self: MaterialX.PyMaterialXCore.GeomElement) -> str

        Return the geometry string of this element.
        """
    def hasCollectionString(self) -> bool:
        """hasCollectionString(self: MaterialX.PyMaterialXCore.GeomElement) -> bool

        Return true if this element has a collection string.
        """
    def hasGeom(self) -> bool:
        """hasGeom(self: MaterialX.PyMaterialXCore.GeomElement) -> bool

        Return true if this element has a geometry string.
        """
    def setCollection(self, arg0) -> None:
        """setCollection(self: MaterialX.PyMaterialXCore.GeomElement, arg0: MaterialX_v1_39_5::Collection) -> None

        Assign a Collection to this element.
        """
    def setCollectionString(self, arg0: str) -> None:
        """setCollectionString(self: MaterialX.PyMaterialXCore.GeomElement, arg0: str) -> None

        Set the collection string of this element.
        """
    def setGeom(self, arg0: str) -> None:
        """setGeom(self: MaterialX.PyMaterialXCore.GeomElement, arg0: str) -> None

        Set the geometry string of this element.
        """

class GeomInfo(GeomElement):
    CATEGORY: ClassVar[str] = ...  # read-only
    addGeomAttr: ClassVar[Callable] = ...
    setGeomAttrValue: ClassVar[Callable] = ...
    setGeomPropValue: ClassVar[Callable] = ...
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def addGeomProp(self, *args, **kwargs):
        """addGeomProp(self: MaterialX.PyMaterialXCore.GeomInfo, arg0: str) -> MaterialX_v1_39_5::GeomProp

        Add a GeomProp to this element.

        Args:
            name: The name of the new GeomProp. If no name is specified, then a unique name will automatically be generated.

        Returns:
            A shared pointer to the new GeomProp.
        """
    def addToken(self, name: str = ...) -> Token:
        """addToken(self: MaterialX.PyMaterialXCore.GeomInfo, name: str = 'color3') -> MaterialX.PyMaterialXCore.Token

        Add a Token to this element.

        Args:
            name: The name of the new Token. If no name is specified, then a unique name will automatically be generated.

        Returns:
            A shared pointer to the new Token.
        """
    def getGeomProp(self, *args, **kwargs):
        """getGeomProp(self: MaterialX.PyMaterialXCore.GeomInfo, arg0: str) -> MaterialX_v1_39_5::GeomProp

        Return the GeomProp, if any, with the given name.
        """
    def getGeomProps(self, *args, **kwargs):
        """getGeomProps(self: MaterialX.PyMaterialXCore.GeomInfo) -> list[MaterialX_v1_39_5::GeomProp]

        Return a vector of all GeomProp elements.
        """
    def getToken(self, arg0: str) -> Token:
        """getToken(self: MaterialX.PyMaterialXCore.GeomInfo, arg0: str) -> MaterialX.PyMaterialXCore.Token

        Return the Token, if any, with the given name.
        """
    def getTokens(self) -> list[Token]:
        """getTokens(self: MaterialX.PyMaterialXCore.GeomInfo) -> list[MaterialX.PyMaterialXCore.Token]

        Return a vector of all Token elements.
        """
    def removeGeomProp(self, arg0: str) -> None:
        """removeGeomProp(self: MaterialX.PyMaterialXCore.GeomInfo, arg0: str) -> None

        Remove the GeomProp, if any, with the given name.
        """
    def removeToken(self, arg0: str) -> None:
        """removeToken(self: MaterialX.PyMaterialXCore.GeomInfo, arg0: str) -> None

        Remove the Token, if any, with the given name.
        """
    def setTokenValue(self, arg0: str, arg1: str) -> Token:
        """setTokenValue(self: MaterialX.PyMaterialXCore.GeomInfo, arg0: str, arg1: str) -> MaterialX.PyMaterialXCore.Token

        Set the string value of a Token by its name, creating a child element to hold the Token if needed.
        """

class GeomProp(ValueElement):
    CATEGORY: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class GeomPropDef(TypedElement):
    CATEGORY: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @overload
    def getGeomProp(self) -> str:
        """getGeomProp(*args, **kwargs)
        Overloaded function.

        1. getGeomProp(self: MaterialX.PyMaterialXCore.GeomPropDef) -> str

        Return the GeomProp, if any, with the given name.

        2. getGeomProp(self: MaterialX.PyMaterialXCore.GeomPropDef) -> str

        Return the GeomProp, if any, with the given name.
        """
    @overload
    def getGeomProp(self) -> str:
        """getGeomProp(*args, **kwargs)
        Overloaded function.

        1. getGeomProp(self: MaterialX.PyMaterialXCore.GeomPropDef) -> str

        Return the GeomProp, if any, with the given name.

        2. getGeomProp(self: MaterialX.PyMaterialXCore.GeomPropDef) -> str

        Return the GeomProp, if any, with the given name.
        """
    def getIndex(self) -> str:
        """getIndex(self: MaterialX.PyMaterialXCore.GeomPropDef) -> str

        Return the index string of this element.
        """
    def getSpace(self) -> str:
        """getSpace(self: MaterialX.PyMaterialXCore.GeomPropDef) -> str

        Return the geometric space string of this element.
        """
    @overload
    def hasGeomProp(self) -> bool:
        """hasGeomProp(*args, **kwargs)
        Overloaded function.

        1. hasGeomProp(self: MaterialX.PyMaterialXCore.GeomPropDef) -> bool

        Return true if this element has a geometric property string.

        2. hasGeomProp(self: MaterialX.PyMaterialXCore.GeomPropDef) -> bool

        Return true if this element has a geometric property string.
        """
    @overload
    def hasGeomProp(self) -> bool:
        """hasGeomProp(*args, **kwargs)
        Overloaded function.

        1. hasGeomProp(self: MaterialX.PyMaterialXCore.GeomPropDef) -> bool

        Return true if this element has a geometric property string.

        2. hasGeomProp(self: MaterialX.PyMaterialXCore.GeomPropDef) -> bool

        Return true if this element has a geometric property string.
        """
    def hasIndex(self) -> bool:
        """hasIndex(self: MaterialX.PyMaterialXCore.GeomPropDef) -> bool

        Return true if this element has an index string.
        """
    def hasSpace(self) -> bool:
        """hasSpace(self: MaterialX.PyMaterialXCore.GeomPropDef) -> bool

        Return true if this element has a geometric space string.
        """
    @overload
    def setGeomProp(self, arg0: str) -> None:
        """setGeomProp(*args, **kwargs)
        Overloaded function.

        1. setGeomProp(self: MaterialX.PyMaterialXCore.GeomPropDef, arg0: str) -> None

        Set the geometric property string of this element.

        2. setGeomProp(self: MaterialX.PyMaterialXCore.GeomPropDef, arg0: str) -> None

        Set the geometric property string of this element.
        """
    @overload
    def setGeomProp(self, arg0: str) -> None:
        """setGeomProp(*args, **kwargs)
        Overloaded function.

        1. setGeomProp(self: MaterialX.PyMaterialXCore.GeomPropDef, arg0: str) -> None

        Set the geometric property string of this element.

        2. setGeomProp(self: MaterialX.PyMaterialXCore.GeomPropDef, arg0: str) -> None

        Set the geometric property string of this element.
        """
    def setIndex(self, arg0: str) -> None:
        """setIndex(self: MaterialX.PyMaterialXCore.GeomPropDef, arg0: str) -> None

        Set the index string of this element.
        """
    def setSpace(self, arg0: str) -> None:
        """setSpace(self: MaterialX.PyMaterialXCore.GeomPropDef, arg0: str) -> None

        Set the geometric space string of this element.
        """

class GraphElement(InterfaceElement):
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def addBackdrop(self, *args, **kwargs):
        """addBackdrop(self: MaterialX.PyMaterialXCore.GraphElement, name: str = '') -> MaterialX_v1_39_5::Backdrop

        Add a Backdrop to the graph.
        """
    def addGeomNode(self, arg0: GeomPropDef, arg1: str) -> Node:
        """addGeomNode(self: MaterialX.PyMaterialXCore.GraphElement, arg0: MaterialX.PyMaterialXCore.GeomPropDef, arg1: str) -> MaterialX.PyMaterialXCore.Node

        If not yet present, add a geometry node to this graph matching the given property definition and name prefix.
        """
    def addMaterialNode(self, name: str = ..., shaderNode: Node = ...) -> Node:
        """addMaterialNode(self: MaterialX.PyMaterialXCore.GraphElement, name: str = '', shaderNode: MaterialX.PyMaterialXCore.Node = None) -> MaterialX.PyMaterialXCore.Node

        Add a material node to the graph, optionally connecting it to the given shader node.
        """
    def addNode(self, category: str, name: str = ..., type: str = ...) -> Node:
        """addNode(self: MaterialX.PyMaterialXCore.GraphElement, category: str, name: str = '', type: str = 'color3') -> MaterialX.PyMaterialXCore.Node

        Add a Node to the graph.

        Args:
            category: The category of the new Node.
            name: The name of the new Node. If no name is specified, then a unique name will automatically be generated.
            type: An optional type string.

        Returns:
            A shared pointer to the new Node.
        """
    def addNodeInstance(self, nodeDef: NodeDef, name: str = ...) -> Node:
        """addNodeInstance(self: MaterialX.PyMaterialXCore.GraphElement, nodeDef: MaterialX.PyMaterialXCore.NodeDef, name: str = '') -> MaterialX.PyMaterialXCore.Node

        Add a Node that is an instance of the given NodeDef.
        """
    def asStringDot(self) -> str:
        """asStringDot(self: MaterialX.PyMaterialXCore.GraphElement) -> str

        Convert this graph to a string in the DOT language syntax.

        This can be used to visualise the graph using GraphViz (http://www.graphviz.org).

        If declarations for the contained nodes are provided as nodedefs in the owning document, then they will be used to provide additional formatting details.
        """
    def flattenSubgraphs(self, target: str = ..., filter: Callable[[Node], bool] = ...) -> None:
        """flattenSubgraphs(self: MaterialX.PyMaterialXCore.GraphElement, target: str = '', filter: Callable[[MaterialX.PyMaterialXCore.Node], bool] = None) -> None

        Flatten all subgraphs at the root scope of this graph element, recursively replacing each graph-defined node with its equivalent node network.

        Args:
            target: An optional target string to be used in specifying which node definitions are used in this process.
            filter: An optional node predicate specifying which nodes should be included and excluded from this process.
        """
    def getBackdrop(self, *args, **kwargs):
        """getBackdrop(self: MaterialX.PyMaterialXCore.GraphElement, arg0: str) -> MaterialX_v1_39_5::Backdrop

        Return the Backdrop, if any, with the given name.
        """
    def getBackdrops(self, *args, **kwargs):
        """getBackdrops(self: MaterialX.PyMaterialXCore.GraphElement) -> list[MaterialX_v1_39_5::Backdrop]

        Return a vector of all Backdrop elements in the graph.
        """
    def getMaterialNodes(self) -> list[Node]:
        """getMaterialNodes(self: MaterialX.PyMaterialXCore.GraphElement) -> list[MaterialX.PyMaterialXCore.Node]

        Return a vector of all material nodes.
        """
    def getNode(self, arg0: str) -> Node:
        """getNode(self: MaterialX.PyMaterialXCore.GraphElement, arg0: str) -> MaterialX.PyMaterialXCore.Node

        Return the Node, if any, with the given name.
        """
    def getNodes(self, category: str = ...) -> list[Node]:
        """getNodes(self: MaterialX.PyMaterialXCore.GraphElement, category: str = '') -> list[MaterialX.PyMaterialXCore.Node]

        Return a vector of all Nodes in the graph, optionally filtered by the given category string.
        """
    def removeBackdrop(self, arg0: str) -> None:
        """removeBackdrop(self: MaterialX.PyMaterialXCore.GraphElement, arg0: str) -> None

        Remove the Backdrop, if any, with the given name.
        """
    def removeNode(self, arg0: str) -> None:
        """removeNode(self: MaterialX.PyMaterialXCore.GraphElement, arg0: str) -> None

        Remove the Node, if any, with the given name.
        """
    def topologicalSort(self) -> list[Element]:
        """topologicalSort(self: MaterialX.PyMaterialXCore.GraphElement) -> list[MaterialX.PyMaterialXCore.Element]

        Return a vector of all children (nodes and outputs) sorted in topological order.
        """

class GraphIterator:
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def getConnectingElement(self) -> Element:
        """getConnectingElement(self: MaterialX.PyMaterialXCore.GraphIterator) -> MaterialX.PyMaterialXCore.Element

        Return the connecting element of the edge, if any.
        """
    def getDownstreamElement(self) -> Element:
        """getDownstreamElement(self: MaterialX.PyMaterialXCore.GraphIterator) -> MaterialX.PyMaterialXCore.Element

        Return the downstream element of the edge.
        """
    def getElementDepth(self) -> int:
        """getElementDepth(self: MaterialX.PyMaterialXCore.GraphIterator) -> int

        Return the element depth of the current traversal, where a single edge between two elements represents a depth of one.
        """
    def getNodeDepth(self) -> int:
        """getNodeDepth(self: MaterialX.PyMaterialXCore.GraphIterator) -> int

        Return the node depth of the current traversal, where a single edge between two nodes represents a depth of one.
        """
    def getPruneSubgraph(self) -> bool:
        """getPruneSubgraph(self: MaterialX.PyMaterialXCore.GraphIterator) -> bool

        Return the prune subgraph flag, which controls whether the current subgraph is pruned from traversal.
        """
    def getUpstreamElement(self) -> Element:
        """getUpstreamElement(self: MaterialX.PyMaterialXCore.GraphIterator) -> MaterialX.PyMaterialXCore.Element

        Return the upstream element of the edge.
        """
    def getUpstreamIndex(self) -> int:
        """getUpstreamIndex(self: MaterialX.PyMaterialXCore.GraphIterator) -> int

        Return the index of the current edge within the range of upstream edges available to the downstream element.
        """
    def setPruneSubgraph(self, arg0: bool) -> None:
        """setPruneSubgraph(self: MaterialX.PyMaterialXCore.GraphIterator, arg0: bool) -> None

        Set the prune subgraph flag, which controls whether the current subgraph is pruned from traversal.

        Args:
            prune: If set to true, then the current subgraph will be pruned.
        """
    def __iter__(self) -> GraphIterator:
        """__iter__(self: MaterialX.PyMaterialXCore.GraphIterator) -> MaterialX.PyMaterialXCore.GraphIterator"""
    def __next__(self) -> Edge:
        """__next__(self: MaterialX.PyMaterialXCore.GraphIterator) -> MaterialX.PyMaterialXCore.Edge"""

class Implementation(InterfaceElement):
    CATEGORY: ClassVar[str] = ...  # read-only
    FILE_ATTRIBUTE: ClassVar[str] = ...  # read-only
    FUNCTION_ATTRIBUTE: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def getFile(self) -> str:
        """getFile(self: MaterialX.PyMaterialXCore.Implementation) -> str

        Return the file string for the Implementation.
        """
    def getFunction(self) -> str:
        """getFunction(self: MaterialX.PyMaterialXCore.Implementation) -> str

        Return the function string for the Implementation.
        """
    def getNodeDef(self) -> NodeDef:
        """getNodeDef(self: MaterialX.PyMaterialXCore.Implementation) -> MaterialX.PyMaterialXCore.NodeDef

        Returns a nodedef for a given transform.
        """
    def getNodeGraph(self) -> str:
        """getNodeGraph(self: MaterialX.PyMaterialXCore.Implementation) -> str

        Return the NodeGraph, if any, with the given name.
        """
    def hasFile(self) -> bool:
        """hasFile(self: MaterialX.PyMaterialXCore.Implementation) -> bool

        Return true if the given Implementation has a file string.
        """
    def hasFunction(self) -> bool:
        """hasFunction(self: MaterialX.PyMaterialXCore.Implementation) -> bool

        Return true if the given Implementation has a function string.
        """
    def hasNodeGraph(self) -> bool:
        """hasNodeGraph(self: MaterialX.PyMaterialXCore.Implementation) -> bool

        Return true if the given Implementation has a nodegraph string.
        """
    def setFile(self, arg0: str) -> None:
        """setFile(self: MaterialX.PyMaterialXCore.Implementation, arg0: str) -> None

        Set the file string for the Implementation.
        """
    def setFunction(self, arg0: str) -> None:
        """setFunction(self: MaterialX.PyMaterialXCore.Implementation, arg0: str) -> None

        Set the function string for the Implementation.
        """
    def setNodeDef(self, arg0: NodeDef) -> None:
        """setNodeDef(self: MaterialX.PyMaterialXCore.Implementation, arg0: MaterialX.PyMaterialXCore.NodeDef) -> None

        Set the NodeDef element referenced by the Implementation.
        """
    def setNodeGraph(self, arg0: str) -> None:
        """setNodeGraph(self: MaterialX.PyMaterialXCore.Implementation, arg0: str) -> None

        Set the nodegraph string for the Implementation.
        """

class InheritanceIterator:
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def __iter__(self) -> InheritanceIterator:
        """__iter__(self: MaterialX.PyMaterialXCore.InheritanceIterator) -> MaterialX.PyMaterialXCore.InheritanceIterator"""
    def __next__(self) -> Element:
        """__next__(self: MaterialX.PyMaterialXCore.InheritanceIterator) -> MaterialX.PyMaterialXCore.Element"""

class Input(PortElement):
    CATEGORY: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def getConnectedNode(self, *args, **kwargs):
        """getConnectedNode(self: MaterialX.PyMaterialXCore.Input) -> MaterialX_v1_39_5::Node

        Return the node, if any, to which this input is connected.
        """
    def getDefaultGeomProp(self, *args, **kwargs):
        """getDefaultGeomProp(self: MaterialX.PyMaterialXCore.Input) -> MaterialX_v1_39_5::GeomPropDef

        Return the GeomPropDef element to use, if defined for this input.
        """
    def getDefaultGeomPropString(self) -> str:
        """getDefaultGeomPropString(self: MaterialX.PyMaterialXCore.Input) -> str

        Return the defaultgeomprop string for the input.
        """
    def getInterfaceInput(self) -> Input:
        """getInterfaceInput(self: MaterialX.PyMaterialXCore.Input) -> MaterialX.PyMaterialXCore.Input

        Return the input on the parent graph corresponding to the interface name for this input.
        """
    def hasDefaultGeomPropString(self) -> bool:
        """hasDefaultGeomPropString(self: MaterialX.PyMaterialXCore.Input) -> bool

        Return true if the given input has a defaultgeomprop string.
        """
    def setConnectedInterfaceName(self, arg0: str) -> None:
        """setConnectedInterfaceName(self: MaterialX.PyMaterialXCore.Input, arg0: str) -> None

        Connects this input to a corresponding interface with the given name.

        If the interface name specified is an empty string then any existing connection is removed.
        """
    def setDefaultGeomPropString(self, arg0: str) -> None:
        """setDefaultGeomPropString(self: MaterialX.PyMaterialXCore.Input, arg0: str) -> None

        Set the defaultgeomprop string for the input.
        """

class InterfaceElement(TypedElement):
    NODE_DEF_ATTRIBUTE: ClassVar[str] = ...  # read-only
    addBindInput: ClassVar[Callable] = ...
    addBindParam: ClassVar[Callable] = ...
    addParameter: ClassVar[Callable] = ...
    getActiveParameters: ClassVar[Callable] = ...
    getBindInputs: ClassVar[Callable] = ...
    getBindParams: ClassVar[Callable] = ...
    getBindTokens: ClassVar[Callable] = ...
    getInputValue: ClassVar[Callable] = ...
    getParameterValue: ClassVar[Callable] = ...
    getParameterValueString: ClassVar[Callable] = ...
    getParameters: ClassVar[Callable] = ...
    setInputValue: ClassVar[Callable] = ...
    setParameterValue: ClassVar[Callable] = ...
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def addInput(self, name: str = ..., type: str = ...) -> Input:
        """addInput(self: MaterialX.PyMaterialXCore.InterfaceElement, name: str = '', type: str = 'color3') -> MaterialX.PyMaterialXCore.Input

        Add an Input to this interface.

        Args:
            name: The name of the new Input. If no name is specified, then a unique name will automatically be generated.
            type: An optional type string.

        Returns:
            A shared pointer to the new Input.
        """
    def addOutput(self, name: str = ..., type: str = ...) -> Output:
        """addOutput(self: MaterialX.PyMaterialXCore.InterfaceElement, name: str = '', type: str = 'color3') -> MaterialX.PyMaterialXCore.Output

        Add an Output to this interface.

        Args:
            name: The name of the new Output. If no name is specified, then a unique name will automatically be generated.
            type: An optional type string.

        Returns:
            A shared pointer to the new Output.
        """
    def addToken(self, name: str = ...) -> Token:
        """addToken(self: MaterialX.PyMaterialXCore.InterfaceElement, name: str = 'color3') -> MaterialX.PyMaterialXCore.Token

        Add a Token to this element.

        Args:
            name: The name of the new Token. If no name is specified, then a unique name will automatically be generated.

        Returns:
            A shared pointer to the new Token.
        """
    def clearContent(self) -> None:
        """clearContent(self: MaterialX.PyMaterialXCore.InterfaceElement) -> None

        Clear all attributes and descendants from this element.
        """
    def getActiveInput(self, arg0: str) -> Input:
        """getActiveInput(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> MaterialX.PyMaterialXCore.Input

        Return the first Input with the given name that belongs to this interface, taking interface inheritance into account.
        """
    def getActiveInputs(self) -> list[Input]:
        """getActiveInputs(self: MaterialX.PyMaterialXCore.InterfaceElement) -> list[MaterialX.PyMaterialXCore.Input]

        Return a vector of all Input elements that belong to this interface, taking inheritance into account.
        """
    def getActiveOutput(self, arg0: str) -> Output:
        """getActiveOutput(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> MaterialX.PyMaterialXCore.Output

        Return the first Output with the given name that belongs to this interface, taking interface inheritance into account.
        """
    def getActiveOutputs(self) -> list[Output]:
        """getActiveOutputs(self: MaterialX.PyMaterialXCore.InterfaceElement) -> list[MaterialX.PyMaterialXCore.Output]

        Return a vector of all Output elements that belong to this interface, taking inheritance into account.
        """
    def getActiveToken(self, arg0: str) -> Token:
        """getActiveToken(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> MaterialX.PyMaterialXCore.Token

        Return the first Token with the given name that belongs to this interface, taking interface inheritance into account.
        """
    def getActiveTokens(self) -> list[Token]:
        """getActiveTokens(self: MaterialX.PyMaterialXCore.InterfaceElement) -> list[MaterialX.PyMaterialXCore.Token]

        Return a vector of all Token elements that belong to this interface, taking inheritance into account.
        """
    def getActiveValueElement(self, arg0: str) -> ValueElement:
        """getActiveValueElement(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> MaterialX.PyMaterialXCore.ValueElement

        Return the first value element with the given name that belongs to this interface, taking interface inheritance into account.

        Examples of value elements are Input, Output, and Token.
        """
    def getActiveValueElements(self) -> list[ValueElement]:
        """getActiveValueElements(self: MaterialX.PyMaterialXCore.InterfaceElement) -> list[MaterialX.PyMaterialXCore.ValueElement]

        Return a vector of all value elements that belong to this interface, taking inheritance into account.

        Examples of value elements are Input, Output, and Token.
        """
    def getConnectedOutput(self, arg0: str) -> Output:
        """getConnectedOutput(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> MaterialX.PyMaterialXCore.Output

        Return the output connected to the given input.

        If the given input is not present, then an empty OutputPtr is returned.
        """
    def getDeclaration(self, target: str = ...) -> InterfaceElement:
        """getDeclaration(self: MaterialX.PyMaterialXCore.InterfaceElement, target: str = '') -> MaterialX.PyMaterialXCore.InterfaceElement

        Return the first declaration of this interface, optionally filtered by the given target name.
        """
    def getDefaultVersion(self) -> bool:
        """getDefaultVersion(self: MaterialX.PyMaterialXCore.InterfaceElement) -> bool

        Return the default version flag of this element.
        """
    def getInput(self, arg0: str) -> Input:
        """getInput(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> MaterialX.PyMaterialXCore.Input

        Return the Input, if any, with the given name.
        """
    def getInputCount(self) -> int:
        """getInputCount(self: MaterialX.PyMaterialXCore.InterfaceElement) -> int

        Return the number of Input elements.
        """
    def getInputs(self) -> list[Input]:
        """getInputs(self: MaterialX.PyMaterialXCore.InterfaceElement) -> list[MaterialX.PyMaterialXCore.Input]

        Return a vector of all Input elements.
        """
    def getNodeDefString(self) -> str:
        """getNodeDefString(self: MaterialX.PyMaterialXCore.InterfaceElement) -> str

        Return the NodeDef string for the interface.
        """
    def getOutput(self, arg0: str) -> Output:
        """getOutput(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> MaterialX.PyMaterialXCore.Output

        Return the Output, if any, with the given name.
        """
    def getOutputCount(self) -> int:
        """getOutputCount(self: MaterialX.PyMaterialXCore.InterfaceElement) -> int

        Return the number of Output elements.
        """
    def getOutputs(self) -> list[Output]:
        """getOutputs(self: MaterialX.PyMaterialXCore.InterfaceElement) -> list[MaterialX.PyMaterialXCore.Output]

        Return a vector of all Output elements.
        """
    def getTarget(self) -> str:
        """getTarget(self: MaterialX.PyMaterialXCore.InterfaceElement) -> str

        Return a unique identifier for the target this generator is for.
        """
    def getToken(self, arg0: str) -> Token:
        """getToken(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> MaterialX.PyMaterialXCore.Token

        Return the Token, if any, with the given name.
        """
    def getTokenValue(self, arg0: str) -> str:
        """getTokenValue(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> str

        Return the string value of a Token by its name, or an empty string if the given Token is not present.
        """
    def getTokens(self) -> list[Token]:
        """getTokens(self: MaterialX.PyMaterialXCore.InterfaceElement) -> list[MaterialX.PyMaterialXCore.Token]

        Return a vector of all Token elements.
        """
    def getVersionIntegers(self) -> tuple[int, int]:
        """getVersionIntegers(self: MaterialX.PyMaterialXCore.InterfaceElement) -> tuple[int, int]

        Return the major and minor versions as an integer pair.
        """
    def getVersionString(self) -> str:
        """getVersionString(self: MaterialX.PyMaterialXCore.InterfaceElement) -> str

        Return the version string of this interface.
        """
    def hasExactInputMatch(self, declaration: InterfaceElement, message: str = ...) -> bool:
        """hasExactInputMatch(self: MaterialX.PyMaterialXCore.InterfaceElement, declaration: MaterialX.PyMaterialXCore.InterfaceElement, message: str = None) -> bool

        Return true if this instance has an exact input match with the given declaration, where each input of this the instance corresponds to a declaration input of the same name and type.

        If an exact input match is not found, and the optional message argument is provided, then an error message will be appended to the given string.
        """
    def hasNodeDefString(self) -> bool:
        """hasNodeDefString(self: MaterialX.PyMaterialXCore.InterfaceElement) -> bool

        Return true if the given interface has a NodeDef string.
        """
    def hasTarget(self) -> bool:
        """hasTarget(self: MaterialX.PyMaterialXCore.InterfaceElement) -> bool

        Return true if the given interface has a target string.
        """
    def hasVersionString(self) -> bool:
        """hasVersionString(self: MaterialX.PyMaterialXCore.InterfaceElement) -> bool

        Return true if this interface has a version string.
        """
    def removeInput(self, arg0: str) -> None:
        """removeInput(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> None

        Remove the Input, if any, with the given name.
        """
    def removeOutput(self, arg0: str) -> None:
        """removeOutput(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> None

        Remove the Output, if any, with the given name.
        """
    def removeToken(self, arg0: str) -> None:
        """removeToken(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> None

        Remove the Token, if any, with the given name.
        """
    def setConnectedOutput(self, arg0: str, arg1: Output) -> None:
        """setConnectedOutput(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str, arg1: MaterialX.PyMaterialXCore.Output) -> None

        Set the output to which the given input is connected, creating a child input if needed.

        If the node argument is null, then any existing output connection on the input will be cleared.
        """
    def setDefaultVersion(self, arg0: bool) -> None:
        """setDefaultVersion(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: bool) -> None

        Set the default version flag of this element.
        """
    def setNodeDefString(self, arg0: str) -> None:
        """setNodeDefString(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> None

        Set the NodeDef string for the interface.
        """
    def setTarget(self, arg0: str) -> None:
        """setTarget(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> None

        Set the target string of this interface.
        """
    def setTokenValue(self, arg0: str, arg1: str) -> Token:
        """setTokenValue(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str, arg1: str) -> MaterialX.PyMaterialXCore.Token

        Set the string value of a Token by its name, creating a child element to hold the Token if needed.
        """
    def setVersionIntegers(self, arg0: int, arg1: int) -> None:
        """setVersionIntegers(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: int, arg1: int) -> None

        Set the major and minor versions as an integer pair.
        """
    def setVersionString(self, arg0: str) -> None:
        """setVersionString(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> None

        Set the version string of this interface.
        """

class LinearUnitConverter(UnitConverter):
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @overload
    def convert(self, arg0: float, arg1: str, arg2: str) -> float:
        """convert(*args, **kwargs)
        Overloaded function.

        1. convert(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: float, arg1: str, arg2: str) -> float

        Convert a given value in a given unit to a desired unit.

        Args:
            input: Input value to convert
            inputUnit: Unit of input value
            outputUnit: Unit for output value

        2. convert(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: MaterialX.PyMaterialXCore.Vector2, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector2

        Convert a given value in a given unit to a desired unit.

        Args:
            input: Input value to convert
            inputUnit: Unit of input value
            outputUnit: Unit for output value

        3. convert(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: MaterialX.PyMaterialXCore.Vector3, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector3

        Convert a given value in a given unit to a desired unit.

        Args:
            input: Input value to convert
            inputUnit: Unit of input value
            outputUnit: Unit for output value

        4. convert(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: MaterialX.PyMaterialXCore.Vector4, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector4

        Convert a given value in a given unit to a desired unit.

        Args:
            input: Input value to convert
            inputUnit: Unit of input value
            outputUnit: Unit for output value
        """
    @overload
    def convert(self, arg0: Vector2, arg1: str, arg2: str) -> Vector2:
        """convert(*args, **kwargs)
        Overloaded function.

        1. convert(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: float, arg1: str, arg2: str) -> float

        Convert a given value in a given unit to a desired unit.

        Args:
            input: Input value to convert
            inputUnit: Unit of input value
            outputUnit: Unit for output value

        2. convert(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: MaterialX.PyMaterialXCore.Vector2, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector2

        Convert a given value in a given unit to a desired unit.

        Args:
            input: Input value to convert
            inputUnit: Unit of input value
            outputUnit: Unit for output value

        3. convert(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: MaterialX.PyMaterialXCore.Vector3, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector3

        Convert a given value in a given unit to a desired unit.

        Args:
            input: Input value to convert
            inputUnit: Unit of input value
            outputUnit: Unit for output value

        4. convert(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: MaterialX.PyMaterialXCore.Vector4, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector4

        Convert a given value in a given unit to a desired unit.

        Args:
            input: Input value to convert
            inputUnit: Unit of input value
            outputUnit: Unit for output value
        """
    @overload
    def convert(self, arg0: Vector3, arg1: str, arg2: str) -> Vector3:
        """convert(*args, **kwargs)
        Overloaded function.

        1. convert(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: float, arg1: str, arg2: str) -> float

        Convert a given value in a given unit to a desired unit.

        Args:
            input: Input value to convert
            inputUnit: Unit of input value
            outputUnit: Unit for output value

        2. convert(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: MaterialX.PyMaterialXCore.Vector2, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector2

        Convert a given value in a given unit to a desired unit.

        Args:
            input: Input value to convert
            inputUnit: Unit of input value
            outputUnit: Unit for output value

        3. convert(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: MaterialX.PyMaterialXCore.Vector3, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector3

        Convert a given value in a given unit to a desired unit.

        Args:
            input: Input value to convert
            inputUnit: Unit of input value
            outputUnit: Unit for output value

        4. convert(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: MaterialX.PyMaterialXCore.Vector4, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector4

        Convert a given value in a given unit to a desired unit.

        Args:
            input: Input value to convert
            inputUnit: Unit of input value
            outputUnit: Unit for output value
        """
    @overload
    def convert(self, arg0: Vector4, arg1: str, arg2: str) -> Vector4:
        """convert(*args, **kwargs)
        Overloaded function.

        1. convert(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: float, arg1: str, arg2: str) -> float

        Convert a given value in a given unit to a desired unit.

        Args:
            input: Input value to convert
            inputUnit: Unit of input value
            outputUnit: Unit for output value

        2. convert(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: MaterialX.PyMaterialXCore.Vector2, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector2

        Convert a given value in a given unit to a desired unit.

        Args:
            input: Input value to convert
            inputUnit: Unit of input value
            outputUnit: Unit for output value

        3. convert(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: MaterialX.PyMaterialXCore.Vector3, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector3

        Convert a given value in a given unit to a desired unit.

        Args:
            input: Input value to convert
            inputUnit: Unit of input value
            outputUnit: Unit for output value

        4. convert(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: MaterialX.PyMaterialXCore.Vector4, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector4

        Convert a given value in a given unit to a desired unit.

        Args:
            input: Input value to convert
            inputUnit: Unit of input value
            outputUnit: Unit for output value
        """
    @staticmethod
    def create(arg0: UnitTypeDef) -> LinearUnitConverter:
        """create(arg0: MaterialX.PyMaterialXCore.UnitTypeDef) -> MaterialX.PyMaterialXCore.LinearUnitConverter"""
    def getUnitAsInteger(self, arg0: str) -> int:
        """getUnitAsInteger(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: str) -> int

        Given a unit name return a value that it can map to as an integer.

        Returns -1 value if not found
        """
    def getUnitFromInteger(self, arg0: int) -> str:
        """getUnitFromInteger(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: int) -> str

        Given an integer index return the unit name in the map used by the converter.

        Returns Empty string if not found
        """
    def getUnitScale(self) -> dict[str, float]:
        """getUnitScale(self: MaterialX.PyMaterialXCore.LinearUnitConverter) -> dict[str, float]

        Return the mappings from unit names to the scale value defined by a linear converter.
        """

class Look(Element):
    CATEGORY: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def addMaterialAssign(self, *args, **kwargs):
        """addMaterialAssign(self: MaterialX.PyMaterialXCore.Look, name: str = '', material: str = '') -> MaterialX_v1_39_5::MaterialAssign

        Add a MaterialAssign to the look.

        Args:
            name: The name of the new MaterialAssign. If no name is specified, then a unique name will automatically be generated.
            material: An optional material string, which should match the name of the material node to be assigned.

        Returns:
            A shared pointer to the new MaterialAssign.
        """
    def addPropertyAssign(self, name: str = ...) -> PropertyAssign:
        """addPropertyAssign(self: MaterialX.PyMaterialXCore.Look, name: str = '') -> MaterialX.PyMaterialXCore.PropertyAssign

        Add a PropertyAssign to the look.

        Args:
            name: The name of the new PropertyAssign. If no name is specified, then a unique name will automatically be generated.

        Returns:
            A shared pointer to the new PropertyAssign.
        """
    def addPropertySetAssign(self, name: str = ...) -> PropertySetAssign:
        """addPropertySetAssign(self: MaterialX.PyMaterialXCore.Look, name: str = '') -> MaterialX.PyMaterialXCore.PropertySetAssign

        Add a PropertySetAssign to the look.

        Args:
            name: The name of the new PropertySetAssign. If no name is specified, then a unique name will automatically be generated.

        Returns:
            A shared pointer to the new PropertySetAssign.
        """
    def addVariantAssign(self, *args, **kwargs):
        """addVariantAssign(self: MaterialX.PyMaterialXCore.Look, name: str = '') -> MaterialX_v1_39_5::VariantAssign

        Add a VariantAssign to the look.

        Args:
            name: The name of the new VariantAssign. If no name is specified, then a unique name will automatically be generated.

        Returns:
            A shared pointer to the new VariantAssign.
        """
    def addVisibility(self, *args, **kwargs):
        """addVisibility(self: MaterialX.PyMaterialXCore.Look, name: str = '') -> MaterialX_v1_39_5::Visibility

        Add a Visibility to the look.

        Args:
            name: The name of the new Visibility. If no name is specified, then a unique name will automatically be generated.

        Returns:
            A shared pointer to the new Visibility.
        """
    def getActiveMaterialAssigns(self, *args, **kwargs):
        """getActiveMaterialAssigns(self: MaterialX.PyMaterialXCore.Look) -> list[MaterialX_v1_39_5::MaterialAssign]

        Return a vector of all MaterialAssign elements that belong to this look, taking look inheritance into account.
        """
    def getActivePropertyAssigns(self) -> list[PropertyAssign]:
        """getActivePropertyAssigns(self: MaterialX.PyMaterialXCore.Look) -> list[MaterialX.PyMaterialXCore.PropertyAssign]

        Return a vector of all PropertyAssign elements that belong to this look, taking look inheritance into account.
        """
    def getActivePropertySetAssigns(self) -> list[PropertySetAssign]:
        """getActivePropertySetAssigns(self: MaterialX.PyMaterialXCore.Look) -> list[MaterialX.PyMaterialXCore.PropertySetAssign]

        Return a vector of all PropertySetAssign elements that belong to this look, taking look inheritance into account.
        """
    def getActiveVariantAssigns(self, *args, **kwargs):
        """getActiveVariantAssigns(self: MaterialX.PyMaterialXCore.Look) -> list[MaterialX_v1_39_5::VariantAssign]

        Return a vector of all VariantAssign elements that belong to this look, taking look inheritance into account.
        """
    def getActiveVisibilities(self, *args, **kwargs):
        """getActiveVisibilities(self: MaterialX.PyMaterialXCore.Look) -> list[MaterialX_v1_39_5::Visibility]

        Return a vector of all Visibility elements that belong to this look, taking look inheritance into account.
        """
    def getMaterialAssign(self, *args, **kwargs):
        """getMaterialAssign(self: MaterialX.PyMaterialXCore.Look, arg0: str) -> MaterialX_v1_39_5::MaterialAssign

        Return the MaterialAssign, if any, with the given name.
        """
    def getMaterialAssigns(self, *args, **kwargs):
        """getMaterialAssigns(self: MaterialX.PyMaterialXCore.Look) -> list[MaterialX_v1_39_5::MaterialAssign]

        Return a vector of all MaterialAssign elements in the look.
        """
    def getPropertyAssign(self, arg0: str) -> PropertyAssign:
        """getPropertyAssign(self: MaterialX.PyMaterialXCore.Look, arg0: str) -> MaterialX.PyMaterialXCore.PropertyAssign

        Return the PropertyAssign, if any, with the given name.
        """
    def getPropertyAssigns(self) -> list[PropertyAssign]:
        """getPropertyAssigns(self: MaterialX.PyMaterialXCore.Look) -> list[MaterialX.PyMaterialXCore.PropertyAssign]

        Return a vector of all PropertyAssign elements in the look.
        """
    def getPropertySetAssign(self, arg0: str) -> PropertySetAssign:
        """getPropertySetAssign(self: MaterialX.PyMaterialXCore.Look, arg0: str) -> MaterialX.PyMaterialXCore.PropertySetAssign

        Return the PropertySetAssign, if any, with the given name.
        """
    def getPropertySetAssigns(self) -> list[PropertySetAssign]:
        """getPropertySetAssigns(self: MaterialX.PyMaterialXCore.Look) -> list[MaterialX.PyMaterialXCore.PropertySetAssign]

        Return a vector of all PropertySetAssign elements in the look.
        """
    def getVariantAssign(self, *args, **kwargs):
        """getVariantAssign(self: MaterialX.PyMaterialXCore.Look, arg0: str) -> MaterialX_v1_39_5::VariantAssign

        Return the VariantAssign, if any, with the given name.
        """
    def getVariantAssigns(self, *args, **kwargs):
        """getVariantAssigns(self: MaterialX.PyMaterialXCore.Look) -> list[MaterialX_v1_39_5::VariantAssign]

        Return a vector of all VariantAssign elements in the look.
        """
    def getVisibilities(self, *args, **kwargs):
        """getVisibilities(self: MaterialX.PyMaterialXCore.Look) -> list[MaterialX_v1_39_5::Visibility]

        Return a vector of all Visibility elements in the look.
        """
    def getVisibility(self, *args, **kwargs):
        """getVisibility(self: MaterialX.PyMaterialXCore.Look, arg0: str) -> MaterialX_v1_39_5::Visibility

        Return the Visibility, if any, with the given name.
        """
    def removeMaterialAssign(self, arg0: str) -> None:
        """removeMaterialAssign(self: MaterialX.PyMaterialXCore.Look, arg0: str) -> None

        Remove the MaterialAssign, if any, with the given name.
        """
    def removePropertyAssign(self, arg0: str) -> None:
        """removePropertyAssign(self: MaterialX.PyMaterialXCore.Look, arg0: str) -> None

        Remove the PropertyAssign, if any, with the given name.
        """
    def removePropertySetAssign(self, arg0: str) -> None:
        """removePropertySetAssign(self: MaterialX.PyMaterialXCore.Look, arg0: str) -> None

        Remove the PropertySetAssign, if any, with the given name.
        """
    def removeVariantAssign(self, arg0: str) -> None:
        """removeVariantAssign(self: MaterialX.PyMaterialXCore.Look, arg0: str) -> None

        Remove the VariantAssign, if any, with the given name.
        """
    def removeVisibility(self, arg0: str) -> None:
        """removeVisibility(self: MaterialX.PyMaterialXCore.Look, arg0: str) -> None

        Remove the Visibility, if any, with the given name.
        """

class LookGroup(Element):
    ACTIVE_ATTRIBUTE: ClassVar[str] = ...  # read-only
    CATEGORY: ClassVar[str] = ...  # read-only
    LOOKS_ATTRIBUTE: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def getActiveLook(self) -> str:
        """getActiveLook(self: MaterialX.PyMaterialXCore.LookGroup) -> str

        Return the active look, if any.
        """
    def getLooks(self) -> str:
        """getLooks(self: MaterialX.PyMaterialXCore.LookGroup) -> str

        Return a vector of all Look elements in the document.
        """
    def setActiveLook(self, arg0: str) -> None:
        """setActiveLook(self: MaterialX.PyMaterialXCore.LookGroup, arg0: str) -> None

        Set the active look.
        """
    def setLooks(self, arg0: str) -> None:
        """setLooks(self: MaterialX.PyMaterialXCore.LookGroup, arg0: str) -> None

        Set comma-separated list of looks.
        """

class MaterialAssign(GeomElement):
    CATEGORY: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def getExclusive(self) -> bool:
        """getExclusive(self: MaterialX.PyMaterialXCore.MaterialAssign) -> bool

        Return the exclusive boolean for the MaterialAssign.
        """
    def getMaterial(self) -> str:
        """getMaterial(self: MaterialX.PyMaterialXCore.MaterialAssign) -> str

        Return the material string for the MaterialAssign.
        """
    def getMaterialOutputs(self) -> list[Output]:
        """getMaterialOutputs(self: MaterialX.PyMaterialXCore.MaterialAssign) -> list[MaterialX.PyMaterialXCore.Output]

        Return material-type outputs for all nodegraphs in the document.
        """
    def getReferencedMaterial(self, *args, **kwargs):
        """getReferencedMaterial(self: MaterialX.PyMaterialXCore.MaterialAssign) -> MaterialX_v1_39_5::Node

        Return the material node, if any, referenced by the MaterialAssign.
        """
    def hasMaterial(self) -> bool:
        """hasMaterial(self: MaterialX.PyMaterialXCore.MaterialAssign) -> bool

        Return true if the given MaterialAssign has a material string.
        """
    def setExclusive(self, arg0: bool) -> None:
        """setExclusive(self: MaterialX.PyMaterialXCore.MaterialAssign, arg0: bool) -> None

        Set the exclusive boolean for the MaterialAssign.
        """
    def setMaterial(self, arg0: str) -> None:
        """setMaterial(self: MaterialX.PyMaterialXCore.MaterialAssign, arg0: str) -> None

        Set the material string for the MaterialAssign.
        """

class Matrix33(MatrixBase):
    IDENTITY: ClassVar[Matrix33] = ...  # read-only
    @overload
    def __init__(self) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: MaterialX.PyMaterialXCore.Matrix33) -> None

        2. __init__(self: MaterialX.PyMaterialXCore.Matrix33, arg0: float) -> None

        3. __init__(self: MaterialX.PyMaterialXCore.Matrix33, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float) -> None
        """
    @overload
    def __init__(self, arg0: float) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: MaterialX.PyMaterialXCore.Matrix33) -> None

        2. __init__(self: MaterialX.PyMaterialXCore.Matrix33, arg0: float) -> None

        3. __init__(self: MaterialX.PyMaterialXCore.Matrix33, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float) -> None
        """
    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: MaterialX.PyMaterialXCore.Matrix33) -> None

        2. __init__(self: MaterialX.PyMaterialXCore.Matrix33, arg0: float) -> None

        3. __init__(self: MaterialX.PyMaterialXCore.Matrix33, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float) -> None
        """
    def copy(self) -> Matrix33:
        """copy(self: MaterialX.PyMaterialXCore.Matrix33) -> MaterialX.PyMaterialXCore.Matrix33

        Create a deep copy of the value.
        """
    @staticmethod
    def createRotation(arg0: float) -> Matrix33:
        """createRotation(arg0: float) -> MaterialX.PyMaterialXCore.Matrix33"""
    @staticmethod
    def createScale(arg0: Vector2) -> Matrix33:
        """createScale(arg0: MaterialX.PyMaterialXCore.Vector2) -> MaterialX.PyMaterialXCore.Matrix33"""
    @staticmethod
    def createTranslation(arg0: Vector2) -> Matrix33:
        """createTranslation(arg0: MaterialX.PyMaterialXCore.Vector2) -> MaterialX.PyMaterialXCore.Matrix33"""
    def getAdjugate(self) -> Matrix33:
        """getAdjugate(self: MaterialX.PyMaterialXCore.Matrix33) -> MaterialX.PyMaterialXCore.Matrix33

        Return the adjugate of the matrix.
        """
    def getDeterminant(self) -> float:
        """getDeterminant(self: MaterialX.PyMaterialXCore.Matrix33) -> float

        Return the determinant of the matrix.
        """
    def getInverse(self) -> Matrix33:
        """getInverse(self: MaterialX.PyMaterialXCore.Matrix33) -> MaterialX.PyMaterialXCore.Matrix33

        Return the inverse of the matrix.
        """
    def getTranspose(self) -> Matrix33:
        """getTranspose(self: MaterialX.PyMaterialXCore.Matrix33) -> MaterialX.PyMaterialXCore.Matrix33

        Return the transpose of the matrix.
        """
    def isEquivalent(self, arg0: Matrix33, arg1: float) -> bool:
        """isEquivalent(self: MaterialX.PyMaterialXCore.Matrix33, arg0: MaterialX.PyMaterialXCore.Matrix33, arg1: float) -> bool

        Return true if the given element tree, including all descendents, is considered to be equivalent to this one based on the equivalence criteria provided.

        Args:
            rhs: Element to compare against
            options: Equivalence criteria
            message: Optional text description of differences

        Returns:
            True if the elements are equivalent. False otherwise.
        """
    def multiply(self, arg0: Vector3) -> Vector3:
        """multiply(self: MaterialX.PyMaterialXCore.Matrix33, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3

        Return the product of this matrix and a 3D vector.
        """
    @staticmethod
    def numColumns() -> int:
        """numColumns() -> int"""
    @staticmethod
    def numRows() -> int:
        """numRows() -> int"""
    def transformNormal(self, arg0: Vector3) -> Vector3:
        """transformNormal(self: MaterialX.PyMaterialXCore.Matrix33, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3

        Transform the given 3D normal vector.
        """
    def transformPoint(self, arg0: Vector2) -> Vector2:
        """transformPoint(self: MaterialX.PyMaterialXCore.Matrix33, arg0: MaterialX.PyMaterialXCore.Vector2) -> MaterialX.PyMaterialXCore.Vector2

        Transform the given 2D point.
        """
    def transformVector(self, arg0: Vector2) -> Vector2:
        """transformVector(self: MaterialX.PyMaterialXCore.Matrix33, arg0: MaterialX.PyMaterialXCore.Vector2) -> MaterialX.PyMaterialXCore.Vector2

        Transform the given 2D direction vector.
        """
    def __add__(self, arg0: Matrix33) -> Matrix33:
        """__add__(self: MaterialX.PyMaterialXCore.Matrix33, arg0: MaterialX.PyMaterialXCore.Matrix33) -> MaterialX.PyMaterialXCore.Matrix33"""
    def __eq__(self, arg0: Matrix33) -> bool:
        """__eq__(self: MaterialX.PyMaterialXCore.Matrix33, arg0: MaterialX.PyMaterialXCore.Matrix33) -> bool"""
    def __getitem__(self, arg0: tuple[int, int]) -> float:
        """__getitem__(self: MaterialX.PyMaterialXCore.Matrix33, arg0: tuple[int, int]) -> float"""
    def __iadd__(self, arg0: Matrix33) -> Matrix33:
        """__iadd__(self: MaterialX.PyMaterialXCore.Matrix33, arg0: MaterialX.PyMaterialXCore.Matrix33) -> MaterialX.PyMaterialXCore.Matrix33"""
    @overload
    def __imul__(self, arg0: float) -> Matrix33:
        """__imul__(*args, **kwargs)
        Overloaded function.

        1. __imul__(self: MaterialX.PyMaterialXCore.Matrix33, arg0: float) -> MaterialX.PyMaterialXCore.Matrix33

        2. __imul__(self: MaterialX.PyMaterialXCore.Matrix33, arg0: MaterialX.PyMaterialXCore.Matrix33) -> MaterialX.PyMaterialXCore.Matrix33
        """
    @overload
    def __imul__(self, arg0: Matrix33) -> Matrix33:
        """__imul__(*args, **kwargs)
        Overloaded function.

        1. __imul__(self: MaterialX.PyMaterialXCore.Matrix33, arg0: float) -> MaterialX.PyMaterialXCore.Matrix33

        2. __imul__(self: MaterialX.PyMaterialXCore.Matrix33, arg0: MaterialX.PyMaterialXCore.Matrix33) -> MaterialX.PyMaterialXCore.Matrix33
        """
    def __isub__(self, arg0: Matrix33) -> Matrix33:
        """__isub__(self: MaterialX.PyMaterialXCore.Matrix33, arg0: MaterialX.PyMaterialXCore.Matrix33) -> MaterialX.PyMaterialXCore.Matrix33"""
    @overload
    def __itruediv__(self, arg0: float) -> Matrix33:
        """__itruediv__(*args, **kwargs)
        Overloaded function.

        1. __itruediv__(self: MaterialX.PyMaterialXCore.Matrix33, arg0: float) -> MaterialX.PyMaterialXCore.Matrix33

        2. __itruediv__(self: MaterialX.PyMaterialXCore.Matrix33, arg0: MaterialX.PyMaterialXCore.Matrix33) -> MaterialX.PyMaterialXCore.Matrix33
        """
    @overload
    def __itruediv__(self, arg0: Matrix33) -> Matrix33:
        """__itruediv__(*args, **kwargs)
        Overloaded function.

        1. __itruediv__(self: MaterialX.PyMaterialXCore.Matrix33, arg0: float) -> MaterialX.PyMaterialXCore.Matrix33

        2. __itruediv__(self: MaterialX.PyMaterialXCore.Matrix33, arg0: MaterialX.PyMaterialXCore.Matrix33) -> MaterialX.PyMaterialXCore.Matrix33
        """
    @staticmethod
    def __len__() -> int:
        """__len__() -> int"""
    @overload
    def __mul__(self, arg0: Matrix33) -> Matrix33:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: MaterialX.PyMaterialXCore.Matrix33, arg0: MaterialX.PyMaterialXCore.Matrix33) -> MaterialX.PyMaterialXCore.Matrix33

        2. __mul__(self: MaterialX.PyMaterialXCore.Matrix33, arg0: float) -> MaterialX.PyMaterialXCore.Matrix33
        """
    @overload
    def __mul__(self, arg0: float) -> Matrix33:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: MaterialX.PyMaterialXCore.Matrix33, arg0: MaterialX.PyMaterialXCore.Matrix33) -> MaterialX.PyMaterialXCore.Matrix33

        2. __mul__(self: MaterialX.PyMaterialXCore.Matrix33, arg0: float) -> MaterialX.PyMaterialXCore.Matrix33
        """
    def __ne__(self, arg0: Matrix33) -> bool:
        """__ne__(self: MaterialX.PyMaterialXCore.Matrix33, arg0: MaterialX.PyMaterialXCore.Matrix33) -> bool"""
    def __neg__(self) -> Matrix33:
        """__neg__(self: MaterialX.PyMaterialXCore.Matrix33) -> MaterialX.PyMaterialXCore.Matrix33"""
    def __pos__(self) -> Matrix33:
        """__pos__(self: MaterialX.PyMaterialXCore.Matrix33) -> MaterialX.PyMaterialXCore.Matrix33"""
    def __setitem__(self, arg0: tuple[int, int], arg1: float) -> None:
        """__setitem__(self: MaterialX.PyMaterialXCore.Matrix33, arg0: tuple[int, int], arg1: float) -> None"""
    def __sub__(self, arg0: Matrix33) -> Matrix33:
        """__sub__(self: MaterialX.PyMaterialXCore.Matrix33, arg0: MaterialX.PyMaterialXCore.Matrix33) -> MaterialX.PyMaterialXCore.Matrix33"""
    @overload
    def __truediv__(self, arg0: Matrix33) -> Matrix33:
        """__truediv__(*args, **kwargs)
        Overloaded function.

        1. __truediv__(self: MaterialX.PyMaterialXCore.Matrix33, arg0: MaterialX.PyMaterialXCore.Matrix33) -> MaterialX.PyMaterialXCore.Matrix33

        2. __truediv__(self: MaterialX.PyMaterialXCore.Matrix33, arg0: float) -> MaterialX.PyMaterialXCore.Matrix33
        """
    @overload
    def __truediv__(self, arg0: float) -> Matrix33:
        """__truediv__(*args, **kwargs)
        Overloaded function.

        1. __truediv__(self: MaterialX.PyMaterialXCore.Matrix33, arg0: MaterialX.PyMaterialXCore.Matrix33) -> MaterialX.PyMaterialXCore.Matrix33

        2. __truediv__(self: MaterialX.PyMaterialXCore.Matrix33, arg0: float) -> MaterialX.PyMaterialXCore.Matrix33
        """

class Matrix44(MatrixBase):
    IDENTITY: ClassVar[Matrix44] = ...  # read-only
    @overload
    def __init__(self) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: MaterialX.PyMaterialXCore.Matrix44) -> None

        2. __init__(self: MaterialX.PyMaterialXCore.Matrix44, arg0: float) -> None

        3. __init__(self: MaterialX.PyMaterialXCore.Matrix44, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float, arg11: float, arg12: float, arg13: float, arg14: float, arg15: float) -> None
        """
    @overload
    def __init__(self, arg0: float) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: MaterialX.PyMaterialXCore.Matrix44) -> None

        2. __init__(self: MaterialX.PyMaterialXCore.Matrix44, arg0: float) -> None

        3. __init__(self: MaterialX.PyMaterialXCore.Matrix44, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float, arg11: float, arg12: float, arg13: float, arg14: float, arg15: float) -> None
        """
    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float, arg11: float, arg12: float, arg13: float, arg14: float, arg15: float) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: MaterialX.PyMaterialXCore.Matrix44) -> None

        2. __init__(self: MaterialX.PyMaterialXCore.Matrix44, arg0: float) -> None

        3. __init__(self: MaterialX.PyMaterialXCore.Matrix44, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float, arg11: float, arg12: float, arg13: float, arg14: float, arg15: float) -> None
        """
    def copy(self) -> Matrix44:
        """copy(self: MaterialX.PyMaterialXCore.Matrix44) -> MaterialX.PyMaterialXCore.Matrix44

        Create a deep copy of the value.
        """
    @staticmethod
    def createRotationX(arg0: float) -> Matrix44:
        """createRotationX(arg0: float) -> MaterialX.PyMaterialXCore.Matrix44"""
    @staticmethod
    def createRotationY(arg0: float) -> Matrix44:
        """createRotationY(arg0: float) -> MaterialX.PyMaterialXCore.Matrix44"""
    @staticmethod
    def createRotationZ(arg0: float) -> Matrix44:
        """createRotationZ(arg0: float) -> MaterialX.PyMaterialXCore.Matrix44"""
    @staticmethod
    def createScale(arg0: Vector3) -> Matrix44:
        """createScale(arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Matrix44"""
    @staticmethod
    def createTranslation(arg0: Vector3) -> Matrix44:
        """createTranslation(arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Matrix44"""
    def getAdjugate(self) -> Matrix44:
        """getAdjugate(self: MaterialX.PyMaterialXCore.Matrix44) -> MaterialX.PyMaterialXCore.Matrix44

        Return the adjugate of the matrix.
        """
    def getDeterminant(self) -> float:
        """getDeterminant(self: MaterialX.PyMaterialXCore.Matrix44) -> float

        Return the determinant of the matrix.
        """
    def getInverse(self) -> Matrix44:
        """getInverse(self: MaterialX.PyMaterialXCore.Matrix44) -> MaterialX.PyMaterialXCore.Matrix44

        Return the inverse of the matrix.
        """
    def getTranspose(self) -> Matrix44:
        """getTranspose(self: MaterialX.PyMaterialXCore.Matrix44) -> MaterialX.PyMaterialXCore.Matrix44

        Return the transpose of the matrix.
        """
    def isEquivalent(self, arg0: Matrix44, arg1: float) -> bool:
        """isEquivalent(self: MaterialX.PyMaterialXCore.Matrix44, arg0: MaterialX.PyMaterialXCore.Matrix44, arg1: float) -> bool

        Return true if the given element tree, including all descendents, is considered to be equivalent to this one based on the equivalence criteria provided.

        Args:
            rhs: Element to compare against
            options: Equivalence criteria
            message: Optional text description of differences

        Returns:
            True if the elements are equivalent. False otherwise.
        """
    def multiply(self, arg0: Vector4) -> Vector4:
        """multiply(self: MaterialX.PyMaterialXCore.Matrix44, arg0: MaterialX.PyMaterialXCore.Vector4) -> MaterialX.PyMaterialXCore.Vector4

        Return the product of this matrix and a 3D vector.
        """
    @staticmethod
    def numColumns() -> int:
        """numColumns() -> int"""
    @staticmethod
    def numRows() -> int:
        """numRows() -> int"""
    def transformNormal(self, arg0: Vector3) -> Vector3:
        """transformNormal(self: MaterialX.PyMaterialXCore.Matrix44, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3

        Transform the given 3D normal vector.
        """
    def transformPoint(self, arg0: Vector3) -> Vector3:
        """transformPoint(self: MaterialX.PyMaterialXCore.Matrix44, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3

        Transform the given 2D point.
        """
    def transformVector(self, arg0: Vector3) -> Vector3:
        """transformVector(self: MaterialX.PyMaterialXCore.Matrix44, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3

        Transform the given 2D direction vector.
        """
    def __add__(self, arg0: Matrix44) -> Matrix44:
        """__add__(self: MaterialX.PyMaterialXCore.Matrix44, arg0: MaterialX.PyMaterialXCore.Matrix44) -> MaterialX.PyMaterialXCore.Matrix44"""
    def __eq__(self, arg0: Matrix44) -> bool:
        """__eq__(self: MaterialX.PyMaterialXCore.Matrix44, arg0: MaterialX.PyMaterialXCore.Matrix44) -> bool"""
    def __getitem__(self, arg0: tuple[int, int]) -> float:
        """__getitem__(self: MaterialX.PyMaterialXCore.Matrix44, arg0: tuple[int, int]) -> float"""
    def __iadd__(self, arg0: Matrix44) -> Matrix44:
        """__iadd__(self: MaterialX.PyMaterialXCore.Matrix44, arg0: MaterialX.PyMaterialXCore.Matrix44) -> MaterialX.PyMaterialXCore.Matrix44"""
    @overload
    def __imul__(self, arg0: float) -> Matrix44:
        """__imul__(*args, **kwargs)
        Overloaded function.

        1. __imul__(self: MaterialX.PyMaterialXCore.Matrix44, arg0: float) -> MaterialX.PyMaterialXCore.Matrix44

        2. __imul__(self: MaterialX.PyMaterialXCore.Matrix44, arg0: MaterialX.PyMaterialXCore.Matrix44) -> MaterialX.PyMaterialXCore.Matrix44
        """
    @overload
    def __imul__(self, arg0: Matrix44) -> Matrix44:
        """__imul__(*args, **kwargs)
        Overloaded function.

        1. __imul__(self: MaterialX.PyMaterialXCore.Matrix44, arg0: float) -> MaterialX.PyMaterialXCore.Matrix44

        2. __imul__(self: MaterialX.PyMaterialXCore.Matrix44, arg0: MaterialX.PyMaterialXCore.Matrix44) -> MaterialX.PyMaterialXCore.Matrix44
        """
    def __isub__(self, arg0: Matrix44) -> Matrix44:
        """__isub__(self: MaterialX.PyMaterialXCore.Matrix44, arg0: MaterialX.PyMaterialXCore.Matrix44) -> MaterialX.PyMaterialXCore.Matrix44"""
    @overload
    def __itruediv__(self, arg0: float) -> Matrix44:
        """__itruediv__(*args, **kwargs)
        Overloaded function.

        1. __itruediv__(self: MaterialX.PyMaterialXCore.Matrix44, arg0: float) -> MaterialX.PyMaterialXCore.Matrix44

        2. __itruediv__(self: MaterialX.PyMaterialXCore.Matrix44, arg0: MaterialX.PyMaterialXCore.Matrix44) -> MaterialX.PyMaterialXCore.Matrix44
        """
    @overload
    def __itruediv__(self, arg0: Matrix44) -> Matrix44:
        """__itruediv__(*args, **kwargs)
        Overloaded function.

        1. __itruediv__(self: MaterialX.PyMaterialXCore.Matrix44, arg0: float) -> MaterialX.PyMaterialXCore.Matrix44

        2. __itruediv__(self: MaterialX.PyMaterialXCore.Matrix44, arg0: MaterialX.PyMaterialXCore.Matrix44) -> MaterialX.PyMaterialXCore.Matrix44
        """
    @staticmethod
    def __len__() -> int:
        """__len__() -> int"""
    @overload
    def __mul__(self, arg0: Matrix44) -> Matrix44:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: MaterialX.PyMaterialXCore.Matrix44, arg0: MaterialX.PyMaterialXCore.Matrix44) -> MaterialX.PyMaterialXCore.Matrix44

        2. __mul__(self: MaterialX.PyMaterialXCore.Matrix44, arg0: float) -> MaterialX.PyMaterialXCore.Matrix44
        """
    @overload
    def __mul__(self, arg0: float) -> Matrix44:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: MaterialX.PyMaterialXCore.Matrix44, arg0: MaterialX.PyMaterialXCore.Matrix44) -> MaterialX.PyMaterialXCore.Matrix44

        2. __mul__(self: MaterialX.PyMaterialXCore.Matrix44, arg0: float) -> MaterialX.PyMaterialXCore.Matrix44
        """
    def __ne__(self, arg0: Matrix44) -> bool:
        """__ne__(self: MaterialX.PyMaterialXCore.Matrix44, arg0: MaterialX.PyMaterialXCore.Matrix44) -> bool"""
    def __neg__(self) -> Matrix44:
        """__neg__(self: MaterialX.PyMaterialXCore.Matrix44) -> MaterialX.PyMaterialXCore.Matrix44"""
    def __pos__(self) -> Matrix44:
        """__pos__(self: MaterialX.PyMaterialXCore.Matrix44) -> MaterialX.PyMaterialXCore.Matrix44"""
    def __setitem__(self, arg0: tuple[int, int], arg1: float) -> None:
        """__setitem__(self: MaterialX.PyMaterialXCore.Matrix44, arg0: tuple[int, int], arg1: float) -> None"""
    def __sub__(self, arg0: Matrix44) -> Matrix44:
        """__sub__(self: MaterialX.PyMaterialXCore.Matrix44, arg0: MaterialX.PyMaterialXCore.Matrix44) -> MaterialX.PyMaterialXCore.Matrix44"""
    @overload
    def __truediv__(self, arg0: Matrix44) -> Matrix44:
        """__truediv__(*args, **kwargs)
        Overloaded function.

        1. __truediv__(self: MaterialX.PyMaterialXCore.Matrix44, arg0: MaterialX.PyMaterialXCore.Matrix44) -> MaterialX.PyMaterialXCore.Matrix44

        2. __truediv__(self: MaterialX.PyMaterialXCore.Matrix44, arg0: float) -> MaterialX.PyMaterialXCore.Matrix44
        """
    @overload
    def __truediv__(self, arg0: float) -> Matrix44:
        """__truediv__(*args, **kwargs)
        Overloaded function.

        1. __truediv__(self: MaterialX.PyMaterialXCore.Matrix44, arg0: MaterialX.PyMaterialXCore.Matrix44) -> MaterialX.PyMaterialXCore.Matrix44

        2. __truediv__(self: MaterialX.PyMaterialXCore.Matrix44, arg0: float) -> MaterialX.PyMaterialXCore.Matrix44
        """

class MatrixBase:
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class Member(TypedElement):
    CATEGORY: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class NewlineElement(Element):
    CATEGORY: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class Node(InterfaceElement):
    CATEGORY: ClassVar[str] = ...  # read-only
    addShaderRef: ClassVar[Callable] = ...
    getActiveShaderRefs: ClassVar[Callable] = ...
    getReferencedNodeDef: ClassVar[Callable] = ...
    getShaderRefs: ClassVar[Callable] = ...
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def addInputFromNodeDef(self, arg0: str) -> Input:
        """addInputFromNodeDef(self: MaterialX.PyMaterialXCore.Node, arg0: str) -> MaterialX.PyMaterialXCore.Input

        Add an input based on the corresponding input for the associated node definition.

        If the input already exists on the node it will just be returned.
        """
    def addInputsFromNodeDef(self) -> None:
        """addInputsFromNodeDef(self: MaterialX.PyMaterialXCore.Node) -> None

        Add inputs based on the corresponding associated node definition.
        """
    def getConnectedNode(self, arg0: str) -> Node:
        """getConnectedNode(self: MaterialX.PyMaterialXCore.Node, arg0: str) -> MaterialX.PyMaterialXCore.Node

        Return the node, if any, to which this input is connected.
        """
    def getConnectedNodeName(self, arg0: str) -> str:
        """getConnectedNodeName(self: MaterialX.PyMaterialXCore.Node, arg0: str) -> str

        Return the name of the Node connected to the given input.

        If the given input is not present, then an empty string is returned.
        """
    def getDownstreamPorts(self) -> list[PortElement]:
        """getDownstreamPorts(self: MaterialX.PyMaterialXCore.Node) -> list[MaterialX.PyMaterialXCore.PortElement]

        Return a vector of all downstream ports that connect to this node, ordered by the names of the port elements.
        """
    def getImplementation(self, target: str = ...) -> InterfaceElement:
        """getImplementation(self: MaterialX.PyMaterialXCore.Node, target: str = '') -> MaterialX.PyMaterialXCore.InterfaceElement

        Return the Implementation, if any, with the given name.
        """
    def getNodeDef(self, target: str = ..., allowRoughMatch: bool = ...) -> NodeDef:
        """getNodeDef(self: MaterialX.PyMaterialXCore.Node, target: str = '', allowRoughMatch: bool = False) -> MaterialX.PyMaterialXCore.NodeDef

        Returns a nodedef for a given transform.
        """
    def setConnectedNode(self, arg0: str, arg1: Node) -> None:
        """setConnectedNode(self: MaterialX.PyMaterialXCore.Node, arg0: str, arg1: MaterialX.PyMaterialXCore.Node) -> None

        Set the node to which the given input is connected, creating a child input if needed.

        If the node argument is null, then any existing node connection on the input will be cleared.
        """
    def setConnectedNodeName(self, arg0: str, arg1: str) -> None:
        """setConnectedNodeName(self: MaterialX.PyMaterialXCore.Node, arg0: str, arg1: str) -> None

        Set the name of the Node connected to the given input, creating a child element for the input if needed.
        """

class NodeDef(InterfaceElement):
    ADJUSTMENT_NODE_GROUP: ClassVar[str] = ...  # read-only
    CATEGORY: ClassVar[str] = ...  # read-only
    CHANNEL_NODE_GROUP: ClassVar[str] = ...  # read-only
    CONDITIONAL_NODE_GROUP: ClassVar[str] = ...  # read-only
    GEOMETRIC_NODE_GROUP: ClassVar[str] = ...  # read-only
    NODE_ATTRIBUTE: ClassVar[str] = ...  # read-only
    ORGANIZATION_NODE_GROUP: ClassVar[str] = ...  # read-only
    PROCEDURAL_NODE_GROUP: ClassVar[str] = ...  # read-only
    TEXTURE_NODE_GROUP: ClassVar[str] = ...  # read-only
    TRANSLATION_NODE_GROUP: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @overload
    def getImplementation(self, arg0: str) -> InterfaceElement:
        """getImplementation(*args, **kwargs)
        Overloaded function.

        1. getImplementation(self: MaterialX.PyMaterialXCore.NodeDef, arg0: str) -> MaterialX.PyMaterialXCore.InterfaceElement

        Return the Implementation, if any, with the given name.

        2. getImplementation(self: MaterialX.PyMaterialXCore.NodeDef, target: str = '') -> MaterialX.PyMaterialXCore.InterfaceElement

        Return the Implementation, if any, with the given name.
        """
    @overload
    def getImplementation(self, target: str = ...) -> InterfaceElement:
        """getImplementation(*args, **kwargs)
        Overloaded function.

        1. getImplementation(self: MaterialX.PyMaterialXCore.NodeDef, arg0: str) -> MaterialX.PyMaterialXCore.InterfaceElement

        Return the Implementation, if any, with the given name.

        2. getImplementation(self: MaterialX.PyMaterialXCore.NodeDef, target: str = '') -> MaterialX.PyMaterialXCore.InterfaceElement

        Return the Implementation, if any, with the given name.
        """
    def getNodeGroup(self) -> str:
        """getNodeGroup(self: MaterialX.PyMaterialXCore.NodeDef) -> str

        Return the node group of the NodeDef.
        """
    def getNodeString(self) -> str:
        """getNodeString(self: MaterialX.PyMaterialXCore.NodeDef) -> str

        Return the node string of the NodeDef.
        """
    def hasNodeGroup(self) -> bool:
        """hasNodeGroup(self: MaterialX.PyMaterialXCore.NodeDef) -> bool

        Return true if the given NodeDef has a node group.
        """
    def hasNodeString(self) -> bool:
        """hasNodeString(self: MaterialX.PyMaterialXCore.NodeDef) -> bool

        Return true if the given NodeDef has a node string.
        """
    def isVersionCompatible(self, arg0: str) -> bool:
        """isVersionCompatible(self: MaterialX.PyMaterialXCore.NodeDef, arg0: str) -> bool

        Return true if the given version string is compatible with this NodeDef.

        This may be used to test, for example, whether a NodeDef and Node may be used together.
        """
    def setNodeGroup(self, arg0: str) -> None:
        """setNodeGroup(self: MaterialX.PyMaterialXCore.NodeDef, arg0: str) -> None

        Set the node group of the NodeDef.
        """
    def setNodeString(self, arg0: str) -> None:
        """setNodeString(self: MaterialX.PyMaterialXCore.NodeDef, arg0: str) -> None

        Set the node string of the NodeDef.
        """

class NodeGraph(GraphElement):
    CATEGORY: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def addInterfaceName(self, arg0: str, arg1: str) -> Input:
        """addInterfaceName(self: MaterialX.PyMaterialXCore.NodeGraph, arg0: str, arg1: str) -> MaterialX.PyMaterialXCore.Input

        Add an interface name to an existing NodeDef associated with this NodeGraph.

        Args:
            inputPath: Path to an input descendant of this graph.
            interfaceName: The new interface name.

        Returns:
            Interface input.
        """
    def getDeclaration(self, arg0: str) -> InterfaceElement:
        """getDeclaration(self: MaterialX.PyMaterialXCore.NodeGraph, arg0: str) -> MaterialX.PyMaterialXCore.InterfaceElement

        Return the first declaration of this interface, optionally filtered by the given target name.
        """
    def getDownstreamPorts(self) -> list[PortElement]:
        """getDownstreamPorts(self: MaterialX.PyMaterialXCore.NodeGraph) -> list[MaterialX.PyMaterialXCore.PortElement]

        Return a vector of all downstream ports that connect to this node, ordered by the names of the port elements.
        """
    def getMaterialOutputs(self) -> list[Output]:
        """getMaterialOutputs(self: MaterialX.PyMaterialXCore.NodeGraph) -> list[MaterialX.PyMaterialXCore.Output]

        Return material-type outputs for all nodegraphs in the document.
        """
    def getNodeDef(self) -> NodeDef:
        """getNodeDef(self: MaterialX.PyMaterialXCore.NodeGraph) -> MaterialX.PyMaterialXCore.NodeDef

        Returns a nodedef for a given transform.
        """
    def modifyInterfaceName(self, arg0: str, arg1: str) -> None:
        """modifyInterfaceName(self: MaterialX.PyMaterialXCore.NodeGraph, arg0: str, arg1: str) -> None

        Modify the interface name on an existing NodeDef associated with this NodeGraph.

        Args:
            inputPath: Path to an input descendant of this graph.
            interfaceName: The new interface name.
        """
    def removeInterfaceName(self, arg0: str) -> None:
        """removeInterfaceName(self: MaterialX.PyMaterialXCore.NodeGraph, arg0: str) -> None

        Remove an interface name from an existing NodeDef associated with this NodeGraph.

        Args:
            inputPath: Path to an input descendant of this graph.
        """
    def setNodeDef(self, arg0: NodeDef) -> None:
        """setNodeDef(self: MaterialX.PyMaterialXCore.NodeGraph, arg0: MaterialX.PyMaterialXCore.NodeDef) -> None

        Set the NodeDef element referenced by the Implementation.
        """

class NodePredicate:
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class Output(PortElement):
    CATEGORY: ClassVar[str] = ...  # read-only
    DEFAULT_INPUT_ATTRIBUTE: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def hasUpstreamCycle(self) -> bool:
        """hasUpstreamCycle(self: MaterialX.PyMaterialXCore.Output) -> bool

        Return true if a cycle exists in any upstream path from this element.
        """

class PortElement(ValueElement):
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def getConnectedNode(self, *args, **kwargs):
        """getConnectedNode(self: MaterialX.PyMaterialXCore.PortElement) -> MaterialX_v1_39_5::Node

        Return the node, if any, to which this input is connected.
        """
    def getConnectedOutput(self, *args, **kwargs):
        """getConnectedOutput(self: MaterialX.PyMaterialXCore.PortElement) -> MaterialX_v1_39_5::Output

        Return the output connected to the given input.

        If the given input is not present, then an empty OutputPtr is returned.
        """
    def getNodeGraphString(self) -> str:
        """getNodeGraphString(self: MaterialX.PyMaterialXCore.PortElement) -> str

        Return the node graph string of this element.
        """
    def getNodeName(self) -> str:
        """getNodeName(self: MaterialX.PyMaterialXCore.PortElement) -> str

        Return the node name string of this element.
        """
    def getOutputString(self) -> str:
        """getOutputString(self: MaterialX.PyMaterialXCore.PortElement) -> str

        Return the output string of this element.
        """
    def hasNodeGraphString(self) -> bool:
        """hasNodeGraphString(self: MaterialX.PyMaterialXCore.PortElement) -> bool

        Return true if this element has a node graph string.
        """
    def hasOutputString(self) -> bool:
        """hasOutputString(self: MaterialX.PyMaterialXCore.PortElement) -> bool

        Return true if this element has an output string.
        """
    def setConnectedNode(self, arg0) -> None:
        """setConnectedNode(self: MaterialX.PyMaterialXCore.PortElement, arg0: MaterialX_v1_39_5::Node) -> None

        Set the node to which the given input is connected, creating a child input if needed.

        If the node argument is null, then any existing node connection on the input will be cleared.
        """
    def setConnectedOutput(self, arg0) -> None:
        """setConnectedOutput(self: MaterialX.PyMaterialXCore.PortElement, arg0: MaterialX_v1_39_5::Output) -> None

        Set the output to which the given input is connected, creating a child input if needed.

        If the node argument is null, then any existing output connection on the input will be cleared.
        """
    def setNodeGraphString(self, arg0: str) -> None:
        """setNodeGraphString(self: MaterialX.PyMaterialXCore.PortElement, arg0: str) -> None

        Set the node graph string of this element.
        """
    def setNodeName(self, arg0: str) -> None:
        """setNodeName(self: MaterialX.PyMaterialXCore.PortElement, arg0: str) -> None

        Set the node name string of this element, creating a connection to the Node with the given name within the same NodeGraph.
        """
    def setOutputString(self, arg0: str) -> None:
        """setOutputString(self: MaterialX.PyMaterialXCore.PortElement, arg0: str) -> None

        Set the output string of this element.
        """

class Property(ValueElement):
    CATEGORY: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class PropertyAssign(ValueElement):
    CATEGORY: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def getCollection(self) -> Collection:
        """getCollection(self: MaterialX.PyMaterialXCore.PropertyAssign) -> MaterialX.PyMaterialXCore.Collection

        Return the Collection, if any, with the given name.
        """
    def getCollectionString(self) -> str:
        """getCollectionString(self: MaterialX.PyMaterialXCore.PropertyAssign) -> str

        Return the collection string of this element.
        """
    def getGeom(self) -> str:
        """getGeom(self: MaterialX.PyMaterialXCore.PropertyAssign) -> str

        Return the geometry string of this element.
        """
    def getProperty(self) -> str:
        """getProperty(self: MaterialX.PyMaterialXCore.PropertyAssign) -> str

        Return the property string of this element.
        """
    def hasCollectionString(self) -> bool:
        """hasCollectionString(self: MaterialX.PyMaterialXCore.PropertyAssign) -> bool

        Return true if this element has a collection string.
        """
    def hasGeom(self) -> bool:
        """hasGeom(self: MaterialX.PyMaterialXCore.PropertyAssign) -> bool

        Return true if this element has a geometry string.
        """
    def hasProperty(self) -> bool:
        """hasProperty(self: MaterialX.PyMaterialXCore.PropertyAssign) -> bool

        Return true if this element has a property string.
        """
    def setCollection(self, arg0: Collection) -> None:
        """setCollection(self: MaterialX.PyMaterialXCore.PropertyAssign, arg0: MaterialX.PyMaterialXCore.Collection) -> None

        Assign a Collection to this element.
        """
    def setCollectionString(self, arg0: str) -> None:
        """setCollectionString(self: MaterialX.PyMaterialXCore.PropertyAssign, arg0: str) -> None

        Set the collection string of this element.
        """
    def setGeom(self, arg0: str) -> None:
        """setGeom(self: MaterialX.PyMaterialXCore.PropertyAssign, arg0: str) -> None

        Set the geometry string of this element.
        """
    def setProperty(self, arg0: str) -> None:
        """setProperty(self: MaterialX.PyMaterialXCore.PropertyAssign, arg0: str) -> None

        Set the property string of this element.
        """

class PropertySet(Element):
    CATEGORY: ClassVar[str] = ...  # read-only
    getPropertyValue: ClassVar[Callable] = ...
    setPropertyValue: ClassVar[Callable] = ...
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def addProperty(self, arg0: str) -> Property:
        """addProperty(self: MaterialX.PyMaterialXCore.PropertySet, arg0: str) -> MaterialX.PyMaterialXCore.Property

        Add a Property to the set.

        Args:
            name: The name of the new Property. If no name is specified, then a unique name will automatically be generated.

        Returns:
            A shared pointer to the new Property.
        """
    def getProperties(self) -> list[Property]:
        """getProperties(self: MaterialX.PyMaterialXCore.PropertySet) -> list[MaterialX.PyMaterialXCore.Property]

        Return a vector of all Property elements in the set.
        """
    def removeProperty(self, arg0: str) -> None:
        """removeProperty(self: MaterialX.PyMaterialXCore.PropertySet, arg0: str) -> None

        Remove the Property with the given name, if present.
        """

class PropertySetAssign(GeomElement):
    CATEGORY: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def getPropertySet(self) -> PropertySet:
        """getPropertySet(self: MaterialX.PyMaterialXCore.PropertySetAssign) -> MaterialX.PyMaterialXCore.PropertySet

        Return the PropertySet, if any, with the given name.
        """
    def getPropertySetString(self) -> str:
        """getPropertySetString(self: MaterialX.PyMaterialXCore.PropertySetAssign) -> str

        Return the property set string of this element.
        """
    def hasPropertySetString(self) -> bool:
        """hasPropertySetString(self: MaterialX.PyMaterialXCore.PropertySetAssign) -> bool

        Return true if this element has a property set string.
        """
    def setPropertySet(self, arg0: PropertySet) -> None:
        """setPropertySet(self: MaterialX.PyMaterialXCore.PropertySetAssign, arg0: MaterialX.PyMaterialXCore.PropertySet) -> None

        Assign a property set to this element.
        """
    def setPropertySetString(self, arg0: str) -> None:
        """setPropertySetString(self: MaterialX.PyMaterialXCore.PropertySetAssign, arg0: str) -> None

        Set the property set string of this element.
        """

class StringResolver:
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def getFilePrefix(self) -> str:
        """getFilePrefix(self: MaterialX.PyMaterialXCore.StringResolver) -> str

        Return the element's file prefix string.
        """
    def getFilenameSubstitutions(self) -> dict[str, str]:
        """getFilenameSubstitutions(self: MaterialX.PyMaterialXCore.StringResolver) -> dict[str, str]

        Return the map of filename substring substitutions.
        """
    def getGeomNameSubstitutions(self) -> dict[str, str]:
        """getGeomNameSubstitutions(self: MaterialX.PyMaterialXCore.StringResolver) -> dict[str, str]

        Return the map of geometry name substring substitutions.
        """
    def getGeomPrefix(self) -> str:
        """getGeomPrefix(self: MaterialX.PyMaterialXCore.StringResolver) -> str

        Return the element's geom prefix string.
        """
    def resolve(self, arg0: str, arg1: str) -> str:
        """resolve(self: MaterialX.PyMaterialXCore.StringResolver, arg0: str, arg1: str) -> str

        Given an input string and type, apply all appropriate modifiers and return the resulting string.
        """
    def setFilePrefix(self, arg0: str) -> None:
        """setFilePrefix(self: MaterialX.PyMaterialXCore.StringResolver, arg0: str) -> None

        Set the element's file prefix string.
        """
    def setFilenameSubstitution(self, arg0: str, arg1: str) -> None:
        """setFilenameSubstitution(self: MaterialX.PyMaterialXCore.StringResolver, arg0: str, arg1: str) -> None

        Set an arbitrary substring substitution for filename data values.
        """
    def setGeomNameSubstitution(self, arg0: str, arg1: str) -> None:
        """setGeomNameSubstitution(self: MaterialX.PyMaterialXCore.StringResolver, arg0: str, arg1: str) -> None

        Set an arbitrary substring substitution for geometry name data values.
        """
    def setGeomPrefix(self, arg0: str) -> None:
        """setGeomPrefix(self: MaterialX.PyMaterialXCore.StringResolver, arg0: str) -> None

        Set the element's geom prefix string.
        """
    def setUdimString(self, arg0: str) -> None:
        """setUdimString(self: MaterialX.PyMaterialXCore.StringResolver, arg0: str) -> None

        Set the UDIM substring substitution for filename data values.

        This string will be used to replace the standard <UDIM> token.
        """
    def setUvTileString(self, arg0: str) -> None:
        """setUvTileString(self: MaterialX.PyMaterialXCore.StringResolver, arg0: str) -> None

        Set the UV-tile substring substitution for filename data values.

        This string will be used to replace the standard <UVTILE> token.
        """

class TargetDef(TypedElement):
    CATEGORY: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def getMatchingTargets(self) -> list[str]:
        """getMatchingTargets(self: MaterialX.PyMaterialXCore.TargetDef) -> list[str]

        Return a vector of target names that is matching this targetdef either by itself of by its inheritance.

        The vector is ordered by priority starting with this targetdef itself and then upwards in the inheritance hierarchy.
        """

class Token(ValueElement):
    CATEGORY: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class TreeIterator:
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def getElement(self) -> Element:
        """getElement(self: MaterialX.PyMaterialXCore.TreeIterator) -> MaterialX.PyMaterialXCore.Element"""
    def getElementDepth(self) -> int:
        """getElementDepth(self: MaterialX.PyMaterialXCore.TreeIterator) -> int

        Return the element depth of the current traversal, where a single edge between two elements represents a depth of one.
        """
    def getPruneSubtree(self) -> bool:
        """getPruneSubtree(self: MaterialX.PyMaterialXCore.TreeIterator) -> bool

        Return the prune subtree flag, which controls whether the current subtree is pruned from traversal.
        """
    def setPruneSubtree(self, arg0: bool) -> None:
        """setPruneSubtree(self: MaterialX.PyMaterialXCore.TreeIterator, arg0: bool) -> None

        Set the prune subtree flag, which controls whether the current subtree is pruned from traversal.

        Args:
            prune: If set to true, then the current subtree will be pruned.
        """
    def __iter__(self) -> TreeIterator:
        """__iter__(self: MaterialX.PyMaterialXCore.TreeIterator) -> MaterialX.PyMaterialXCore.TreeIterator"""
    def __next__(self) -> Element:
        """__next__(self: MaterialX.PyMaterialXCore.TreeIterator) -> MaterialX.PyMaterialXCore.Element"""

class TypeDef(Element):
    CATEGORY: ClassVar[str] = ...  # read-only
    CONTEXT_ATTRIBUTE: ClassVar[str] = ...  # read-only
    SEMANTIC_ATTRIBUTE: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def addMember(self, *args, **kwargs):
        """addMember(self: MaterialX.PyMaterialXCore.TypeDef, name: str = '') -> MaterialX_v1_39_5::Member

        Add a Member to the TypeDef.

        Args:
            name: The name of the new Member. If no name is specified, then a unique name will automatically be generated.

        Returns:
            A shared pointer to the new Member.
        """
    def getContext(self) -> str:
        """getContext(self: MaterialX.PyMaterialXCore.TypeDef) -> str

        Return the context string of the TypeDef.
        """
    def getMember(self, *args, **kwargs):
        """getMember(self: MaterialX.PyMaterialXCore.TypeDef, arg0: str) -> MaterialX_v1_39_5::Member

        Return the Member, if any, with the given name.
        """
    def getMembers(self, *args, **kwargs):
        """getMembers(self: MaterialX.PyMaterialXCore.TypeDef) -> list[MaterialX_v1_39_5::Member]"""
    def getSemantic(self) -> str:
        """getSemantic(self: MaterialX.PyMaterialXCore.TypeDef) -> str

        Return the variable semantic of this port.
        """
    def hasContext(self) -> bool:
        """hasContext(self: MaterialX.PyMaterialXCore.TypeDef) -> bool

        Return true if the given TypeDef has a context string.
        """
    def hasSemantic(self) -> bool:
        """hasSemantic(self: MaterialX.PyMaterialXCore.TypeDef) -> bool

        Return true if the given TypeDef has a semantic string.
        """
    def removeMember(self, arg0: str) -> None:
        """removeMember(self: MaterialX.PyMaterialXCore.TypeDef, arg0: str) -> None

        Remove the Member, if any, with the given name.
        """
    def setContext(self, arg0: str) -> None:
        """setContext(self: MaterialX.PyMaterialXCore.TypeDef, arg0: str) -> None

        Set the context string of the TypeDef.
        """
    def setSemantic(self, arg0: str) -> None:
        """setSemantic(self: MaterialX.PyMaterialXCore.TypeDef, arg0: str) -> None

        Set the variable semantic of this port.
        """

class TypedElement(Element):
    TYPE_ATTRIBUTE: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def getType(self) -> str:
        """getType(self: MaterialX.PyMaterialXCore.TypedElement) -> str

        Get stream attribute name.
        """
    def getTypeDef(self, *args, **kwargs):
        """getTypeDef(self: MaterialX.PyMaterialXCore.TypedElement) -> MaterialX_v1_39_5::TypeDef

        Return the TypeDef, if any, with the given name.
        """
    def hasType(self) -> bool:
        """hasType(self: MaterialX.PyMaterialXCore.TypedElement) -> bool

        Return true if the given element has a type string.
        """
    def isColorType(self) -> bool:
        """isColorType(self: MaterialX.PyMaterialXCore.TypedElement) -> bool

        Return true if the element is of color type.
        """
    def isMultiOutputType(self) -> bool:
        """isMultiOutputType(self: MaterialX.PyMaterialXCore.TypedElement) -> bool

        Return true if the element is of multi-output type.
        """
    def setType(self, arg0: str) -> None:
        """setType(self: MaterialX.PyMaterialXCore.TypedElement, arg0: str) -> None

        Set the data type for this port.
        """

class TypedValue_boolean(Value):
    TYPE: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def createValue(arg0: bool) -> Value:
        """createValue(arg0: bool) -> MaterialX.PyMaterialXCore.Value"""
    def getData(self) -> bool:
        """getData(self: MaterialX.PyMaterialXCore.TypedValue_boolean) -> bool

        Return the raw float vector.
        """
    def getValueString(self) -> str:
        """getValueString(self: MaterialX.PyMaterialXCore.TypedValue_boolean) -> str

        Return value string.
        """

class TypedValue_booleanarray(Value):
    TYPE: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def createValue(arg0: list[bool]) -> Value:
        """createValue(arg0: list[bool]) -> MaterialX.PyMaterialXCore.Value"""
    def getData(self) -> list[bool]:
        """getData(self: MaterialX.PyMaterialXCore.TypedValue_booleanarray) -> list[bool]

        Return the raw float vector.
        """
    def getValueString(self) -> str:
        """getValueString(self: MaterialX.PyMaterialXCore.TypedValue_booleanarray) -> str

        Return value string.
        """

class TypedValue_color3(Value):
    TYPE: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def createValue(arg0) -> Value:
        """createValue(arg0: MaterialX_v1_39_5::Color3) -> MaterialX.PyMaterialXCore.Value"""
    def getData(self, *args, **kwargs):
        """getData(self: MaterialX.PyMaterialXCore.TypedValue_color3) -> MaterialX_v1_39_5::Color3

        Return the raw float vector.
        """
    def getValueString(self) -> str:
        """getValueString(self: MaterialX.PyMaterialXCore.TypedValue_color3) -> str

        Return value string.
        """

class TypedValue_color4(Value):
    TYPE: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def createValue(arg0) -> Value:
        """createValue(arg0: MaterialX_v1_39_5::Color4) -> MaterialX.PyMaterialXCore.Value"""
    def getData(self, *args, **kwargs):
        """getData(self: MaterialX.PyMaterialXCore.TypedValue_color4) -> MaterialX_v1_39_5::Color4

        Return the raw float vector.
        """
    def getValueString(self) -> str:
        """getValueString(self: MaterialX.PyMaterialXCore.TypedValue_color4) -> str

        Return value string.
        """

class TypedValue_float(Value):
    TYPE: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def createValue(arg0: float) -> Value:
        """createValue(arg0: float) -> MaterialX.PyMaterialXCore.Value"""
    def getData(self) -> float:
        """getData(self: MaterialX.PyMaterialXCore.TypedValue_float) -> float

        Return the raw float vector.
        """
    def getValueString(self) -> str:
        """getValueString(self: MaterialX.PyMaterialXCore.TypedValue_float) -> str

        Return value string.
        """

class TypedValue_floatarray(Value):
    TYPE: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def createValue(arg0: list[float]) -> Value:
        """createValue(arg0: list[float]) -> MaterialX.PyMaterialXCore.Value"""
    def getData(self) -> list[float]:
        """getData(self: MaterialX.PyMaterialXCore.TypedValue_floatarray) -> list[float]

        Return the raw float vector.
        """
    def getValueString(self) -> str:
        """getValueString(self: MaterialX.PyMaterialXCore.TypedValue_floatarray) -> str

        Return value string.
        """

class TypedValue_integer(Value):
    TYPE: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def createValue(arg0: int) -> Value:
        """createValue(arg0: int) -> MaterialX.PyMaterialXCore.Value"""
    def getData(self) -> int:
        """getData(self: MaterialX.PyMaterialXCore.TypedValue_integer) -> int

        Return the raw float vector.
        """
    def getValueString(self) -> str:
        """getValueString(self: MaterialX.PyMaterialXCore.TypedValue_integer) -> str

        Return value string.
        """

class TypedValue_integerarray(Value):
    TYPE: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def createValue(arg0: list[int]) -> Value:
        """createValue(arg0: list[int]) -> MaterialX.PyMaterialXCore.Value"""
    def getData(self) -> list[int]:
        """getData(self: MaterialX.PyMaterialXCore.TypedValue_integerarray) -> list[int]

        Return the raw float vector.
        """
    def getValueString(self) -> str:
        """getValueString(self: MaterialX.PyMaterialXCore.TypedValue_integerarray) -> str

        Return value string.
        """

class TypedValue_matrix33(Value):
    TYPE: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def createValue(arg0) -> Value:
        """createValue(arg0: MaterialX_v1_39_5::Matrix33) -> MaterialX.PyMaterialXCore.Value"""
    def getData(self, *args, **kwargs):
        """getData(self: MaterialX.PyMaterialXCore.TypedValue_matrix33) -> MaterialX_v1_39_5::Matrix33

        Return the raw float vector.
        """
    def getValueString(self) -> str:
        """getValueString(self: MaterialX.PyMaterialXCore.TypedValue_matrix33) -> str

        Return value string.
        """

class TypedValue_matrix44(Value):
    TYPE: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def createValue(arg0) -> Value:
        """createValue(arg0: MaterialX_v1_39_5::Matrix44) -> MaterialX.PyMaterialXCore.Value"""
    def getData(self, *args, **kwargs):
        """getData(self: MaterialX.PyMaterialXCore.TypedValue_matrix44) -> MaterialX_v1_39_5::Matrix44

        Return the raw float vector.
        """
    def getValueString(self) -> str:
        """getValueString(self: MaterialX.PyMaterialXCore.TypedValue_matrix44) -> str

        Return value string.
        """

class TypedValue_string(Value):
    TYPE: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def createValue(arg0: str) -> Value:
        """createValue(arg0: str) -> MaterialX.PyMaterialXCore.Value"""
    def getData(self) -> str:
        """getData(self: MaterialX.PyMaterialXCore.TypedValue_string) -> str

        Return the raw float vector.
        """
    def getValueString(self) -> str:
        """getValueString(self: MaterialX.PyMaterialXCore.TypedValue_string) -> str

        Return value string.
        """

class TypedValue_stringarray(Value):
    TYPE: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def createValue(arg0: list[str]) -> Value:
        """createValue(arg0: list[str]) -> MaterialX.PyMaterialXCore.Value"""
    def getData(self) -> list[str]:
        """getData(self: MaterialX.PyMaterialXCore.TypedValue_stringarray) -> list[str]

        Return the raw float vector.
        """
    def getValueString(self) -> str:
        """getValueString(self: MaterialX.PyMaterialXCore.TypedValue_stringarray) -> str

        Return value string.
        """

class TypedValue_vector2(Value):
    TYPE: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def createValue(arg0) -> Value:
        """createValue(arg0: MaterialX_v1_39_5::Vector2) -> MaterialX.PyMaterialXCore.Value"""
    def getData(self, *args, **kwargs):
        """getData(self: MaterialX.PyMaterialXCore.TypedValue_vector2) -> MaterialX_v1_39_5::Vector2

        Return the raw float vector.
        """
    def getValueString(self) -> str:
        """getValueString(self: MaterialX.PyMaterialXCore.TypedValue_vector2) -> str

        Return value string.
        """

class TypedValue_vector3(Value):
    TYPE: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def createValue(arg0) -> Value:
        """createValue(arg0: MaterialX_v1_39_5::Vector3) -> MaterialX.PyMaterialXCore.Value"""
    def getData(self, *args, **kwargs):
        """getData(self: MaterialX.PyMaterialXCore.TypedValue_vector3) -> MaterialX_v1_39_5::Vector3

        Return the raw float vector.
        """
    def getValueString(self) -> str:
        """getValueString(self: MaterialX.PyMaterialXCore.TypedValue_vector3) -> str

        Return value string.
        """

class TypedValue_vector4(Value):
    TYPE: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def createValue(arg0) -> Value:
        """createValue(arg0: MaterialX_v1_39_5::Vector4) -> MaterialX.PyMaterialXCore.Value"""
    def getData(self, *args, **kwargs):
        """getData(self: MaterialX.PyMaterialXCore.TypedValue_vector4) -> MaterialX_v1_39_5::Vector4

        Return the raw float vector.
        """
    def getValueString(self) -> str:
        """getValueString(self: MaterialX.PyMaterialXCore.TypedValue_vector4) -> str

        Return value string.
        """

class Unit(Element):
    CATEGORY: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class UnitConverter:
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @overload
    def convert(self, arg0: float, arg1: str, arg2: str) -> float:
        """convert(*args, **kwargs)
        Overloaded function.

        1. convert(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: float, arg1: str, arg2: str) -> float

        Convert a given value in a given unit to a desired unit.

        Args:
            input: Input value to convert
            inputUnit: Unit of input value
            outputUnit: Unit for output value

        2. convert(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: MaterialX.PyMaterialXCore.Vector2, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector2

        Convert a given value in a given unit to a desired unit.

        Args:
            input: Input value to convert
            inputUnit: Unit of input value
            outputUnit: Unit for output value

        3. convert(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: MaterialX.PyMaterialXCore.Vector3, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector3

        Convert a given value in a given unit to a desired unit.

        Args:
            input: Input value to convert
            inputUnit: Unit of input value
            outputUnit: Unit for output value

        4. convert(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: MaterialX.PyMaterialXCore.Vector4, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector4

        Convert a given value in a given unit to a desired unit.

        Args:
            input: Input value to convert
            inputUnit: Unit of input value
            outputUnit: Unit for output value
        """
    @overload
    def convert(self, arg0: Vector2, arg1: str, arg2: str) -> Vector2:
        """convert(*args, **kwargs)
        Overloaded function.

        1. convert(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: float, arg1: str, arg2: str) -> float

        Convert a given value in a given unit to a desired unit.

        Args:
            input: Input value to convert
            inputUnit: Unit of input value
            outputUnit: Unit for output value

        2. convert(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: MaterialX.PyMaterialXCore.Vector2, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector2

        Convert a given value in a given unit to a desired unit.

        Args:
            input: Input value to convert
            inputUnit: Unit of input value
            outputUnit: Unit for output value

        3. convert(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: MaterialX.PyMaterialXCore.Vector3, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector3

        Convert a given value in a given unit to a desired unit.

        Args:
            input: Input value to convert
            inputUnit: Unit of input value
            outputUnit: Unit for output value

        4. convert(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: MaterialX.PyMaterialXCore.Vector4, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector4

        Convert a given value in a given unit to a desired unit.

        Args:
            input: Input value to convert
            inputUnit: Unit of input value
            outputUnit: Unit for output value
        """
    @overload
    def convert(self, arg0: Vector3, arg1: str, arg2: str) -> Vector3:
        """convert(*args, **kwargs)
        Overloaded function.

        1. convert(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: float, arg1: str, arg2: str) -> float

        Convert a given value in a given unit to a desired unit.

        Args:
            input: Input value to convert
            inputUnit: Unit of input value
            outputUnit: Unit for output value

        2. convert(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: MaterialX.PyMaterialXCore.Vector2, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector2

        Convert a given value in a given unit to a desired unit.

        Args:
            input: Input value to convert
            inputUnit: Unit of input value
            outputUnit: Unit for output value

        3. convert(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: MaterialX.PyMaterialXCore.Vector3, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector3

        Convert a given value in a given unit to a desired unit.

        Args:
            input: Input value to convert
            inputUnit: Unit of input value
            outputUnit: Unit for output value

        4. convert(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: MaterialX.PyMaterialXCore.Vector4, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector4

        Convert a given value in a given unit to a desired unit.

        Args:
            input: Input value to convert
            inputUnit: Unit of input value
            outputUnit: Unit for output value
        """
    @overload
    def convert(self, arg0: Vector4, arg1: str, arg2: str) -> Vector4:
        """convert(*args, **kwargs)
        Overloaded function.

        1. convert(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: float, arg1: str, arg2: str) -> float

        Convert a given value in a given unit to a desired unit.

        Args:
            input: Input value to convert
            inputUnit: Unit of input value
            outputUnit: Unit for output value

        2. convert(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: MaterialX.PyMaterialXCore.Vector2, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector2

        Convert a given value in a given unit to a desired unit.

        Args:
            input: Input value to convert
            inputUnit: Unit of input value
            outputUnit: Unit for output value

        3. convert(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: MaterialX.PyMaterialXCore.Vector3, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector3

        Convert a given value in a given unit to a desired unit.

        Args:
            input: Input value to convert
            inputUnit: Unit of input value
            outputUnit: Unit for output value

        4. convert(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: MaterialX.PyMaterialXCore.Vector4, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector4

        Convert a given value in a given unit to a desired unit.

        Args:
            input: Input value to convert
            inputUnit: Unit of input value
            outputUnit: Unit for output value
        """
    def getUnitAsInteger(self, arg0: str) -> int:
        """getUnitAsInteger(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: str) -> int

        Given a unit name return a value that it can map to as an integer.

        Returns -1 value if not found
        """
    def getUnitFromInteger(self, arg0: int) -> str:
        """getUnitFromInteger(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: int) -> str

        Given an integer index return the unit name in the map used by the converter.

        Returns Empty string if not found
        """

class UnitConverterRegistry:
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def addUnitConverter(self, arg0: UnitTypeDef, arg1: UnitConverter) -> bool:
        """addUnitConverter(self: MaterialX.PyMaterialXCore.UnitConverterRegistry, arg0: MaterialX.PyMaterialXCore.UnitTypeDef, arg1: MaterialX.PyMaterialXCore.UnitConverter) -> bool

        Add a unit converter for a given UnitDef.

        Returns false if a converter has already been registered for the given UnitDef
        """
    def clearUnitConverters(self) -> None:
        """clearUnitConverters(self: MaterialX.PyMaterialXCore.UnitConverterRegistry) -> None

        Clear all unit converters from the registry.
        """
    @staticmethod
    def create() -> UnitConverterRegistry:
        """create() -> MaterialX.PyMaterialXCore.UnitConverterRegistry"""
    def getUnitConverter(self, arg0: UnitTypeDef) -> UnitConverter:
        """getUnitConverter(self: MaterialX.PyMaterialXCore.UnitConverterRegistry, arg0: MaterialX.PyMaterialXCore.UnitTypeDef) -> MaterialX.PyMaterialXCore.UnitConverter

        Get a unit converter for a given UnitDef Returns any empty pointer if a converter does not exist for the given UnitDef.
        """
    def removeUnitConverter(self, arg0: UnitTypeDef) -> bool:
        """removeUnitConverter(self: MaterialX.PyMaterialXCore.UnitConverterRegistry, arg0: MaterialX.PyMaterialXCore.UnitTypeDef) -> bool

        Remove a unit converter for a given UnitDef.

        Returns false if a converter does not exist for the given UnitDef
        """

class UnitDef(Element):
    CATEGORY: ClassVar[str] = ...  # read-only
    UNITTYPE_ATTRIBUTE: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def addUnit(self, arg0: str) -> Unit:
        """addUnit(self: MaterialX.PyMaterialXCore.UnitDef, arg0: str) -> MaterialX.PyMaterialXCore.Unit

        Add a Unit to the UnitDef.

        Args:
            name: The name of the new Unit. An exception is thrown if the name provided is an empty string.

        Returns:
            A shared pointer to the new Unit.
        """
    def getUnit(self, arg0: str) -> Unit:
        """getUnit(self: MaterialX.PyMaterialXCore.UnitDef, arg0: str) -> MaterialX.PyMaterialXCore.Unit

        Return the unit type for the value on this port.
        """
    def getUnitType(self) -> str:
        """getUnitType(self: MaterialX.PyMaterialXCore.UnitDef) -> str

        Return the unit type string.
        """
    def getUnits(self) -> list[Unit]:
        """getUnits(self: MaterialX.PyMaterialXCore.UnitDef) -> list[MaterialX.PyMaterialXCore.Unit]

        Return a vector of all Unit elements in the UnitDef.
        """
    def hasUnitType(self) -> bool:
        """hasUnitType(self: MaterialX.PyMaterialXCore.UnitDef) -> bool

        Return true if the given element has a unittype string.
        """
    def setUnitType(self, arg0: str) -> None:
        """setUnitType(self: MaterialX.PyMaterialXCore.UnitDef, arg0: str) -> None

        Set the element's unittype string.
        """

class UnitTypeDef(Element):
    CATEGORY: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def getUnitDefs(self) -> list[UnitDef]:
        """getUnitDefs(self: MaterialX.PyMaterialXCore.UnitTypeDef) -> list[MaterialX.PyMaterialXCore.UnitDef]

        Return a vector of all Member elements in the TypeDef.
        """

class Value:
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def createValueFromStrings(value: str, type: str, typeDefPtr=...) -> Value:
        """createValueFromStrings(value: str, type: str, typeDefPtr: MaterialX_v1_39_5::TypeDef = None) -> MaterialX.PyMaterialXCore.Value"""
    def getTypeString(self) -> str:
        """getTypeString(self: MaterialX.PyMaterialXCore.Value) -> str

        Return type string.
        """
    def getValueString(self) -> str:
        """getValueString(self: MaterialX.PyMaterialXCore.Value) -> str

        Return value string.
        """

class ValueElement(TypedElement):
    ENUM_ATTRIBUTE: ClassVar[str] = ...  # read-only
    ENUM_VALUES_ATTRIBUTE: ClassVar[str] = ...  # read-only
    IMPLEMENTATION_NAME_ATTRIBUTE: ClassVar[str] = ...  # read-only
    IMPLEMENTATION_TYPE_ATTRIBUTE: ClassVar[str] = ...  # read-only
    INTERFACE_NAME_ATTRIBUTE: ClassVar[str] = ...  # read-only
    UI_ADVANCED_ATTRIBUTE: ClassVar[str] = ...  # read-only
    UI_FOLDER_ATTRIBUTE: ClassVar[str] = ...  # read-only
    UI_MAX_ATTRIBUTE: ClassVar[str] = ...  # read-only
    UI_MIN_ATTRIBUTE: ClassVar[str] = ...  # read-only
    UI_NAME_ATTRIBUTE: ClassVar[str] = ...  # read-only
    UI_SOFT_MAX_ATTRIBUTE: ClassVar[str] = ...  # read-only
    UI_SOFT_MIN_ATTRIBUTE: ClassVar[str] = ...  # read-only
    UI_STEP_ATTRIBUTE: ClassVar[str] = ...  # read-only
    UNIT_ATTRIBUTE: ClassVar[str] = ...  # read-only
    VALUE_ATTRIBUTE: ClassVar[str] = ...  # read-only
    getDefaultValue: ClassVar[Callable] = ...
    getValue: ClassVar[Callable] = ...
    setValue: ClassVar[Callable] = ...
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def getActiveUnit(self) -> str:
        """getActiveUnit(self: MaterialX.PyMaterialXCore.ValueElement) -> str

        Return the unit defined by the associated NodeDef if this element is a child of a Node.
        """
    def getImplementationName(self) -> str:
        """getImplementationName(self: MaterialX.PyMaterialXCore.ValueElement) -> str

        Return the implementation name of an element.
        """
    def getInterfaceName(self) -> str:
        """getInterfaceName(self: MaterialX.PyMaterialXCore.ValueElement) -> str

        Return the interface name of an element.
        """
    def getIsUniform(self) -> bool:
        """getIsUniform(self: MaterialX.PyMaterialXCore.ValueElement) -> bool

        The the uniform attribute flag for this element.
        """
    def getResolvedValueString(self, resolver=...) -> str:
        """getResolvedValueString(self: MaterialX.PyMaterialXCore.ValueElement, resolver: MaterialX_v1_39_5::StringResolver = None) -> str

        Return the resolved value string of an element, applying any string substitutions that are defined at the element's scope.

        Args:
            resolver: An optional string resolver, which will be used to apply string substitutions. By default, a new string resolver will be created at this scope and applied to the return value.
        """
    def getUnit(self) -> str:
        """getUnit(self: MaterialX.PyMaterialXCore.ValueElement) -> str

        Return the unit type for the value on this port.
        """
    def getUnitType(self) -> str:
        """getUnitType(self: MaterialX.PyMaterialXCore.ValueElement) -> str

        Return the unit type string.
        """
    def getValueString(self) -> str:
        """getValueString(self: MaterialX.PyMaterialXCore.ValueElement) -> str

        Return value string.
        """
    def hasImplementationName(self) -> bool:
        """hasImplementationName(self: MaterialX.PyMaterialXCore.ValueElement) -> bool

        Return true if the given element has an implementation name.
        """
    def hasInterfaceName(self) -> bool:
        """hasInterfaceName(self: MaterialX.PyMaterialXCore.ValueElement) -> bool

        Return true if the given element has an interface name.
        """
    def hasUnit(self) -> bool:
        """hasUnit(self: MaterialX.PyMaterialXCore.ValueElement) -> bool

        Return true if the given element has a unit string.
        """
    def hasUnitType(self) -> bool:
        """hasUnitType(self: MaterialX.PyMaterialXCore.ValueElement) -> bool

        Return true if the given element has a unittype string.
        """
    def hasValueString(self) -> bool:
        """hasValueString(self: MaterialX.PyMaterialXCore.ValueElement) -> bool

        Return true if the given element has a value string.
        """
    def setImplementationName(self, arg0: str) -> None:
        """setImplementationName(self: MaterialX.PyMaterialXCore.ValueElement, arg0: str) -> None

        Set the implementation name of an element.
        """
    def setInterfaceName(self, arg0: str) -> None:
        """setInterfaceName(self: MaterialX.PyMaterialXCore.ValueElement, arg0: str) -> None

        Set the interface name of an element.
        """
    def setIsUniform(self, arg0: bool) -> None:
        """setIsUniform(self: MaterialX.PyMaterialXCore.ValueElement, arg0: bool) -> None

        Set the uniform attribute flag on this element.
        """
    def setUnit(self, arg0: str) -> None:
        """setUnit(self: MaterialX.PyMaterialXCore.ValueElement, arg0: str) -> None

        Set a unit type for the value on this port.
        """
    def setUnitType(self, arg0: str) -> None:
        """setUnitType(self: MaterialX.PyMaterialXCore.ValueElement, arg0: str) -> None

        Set the element's unittype string.
        """
    def setValueString(self, arg0: str) -> None:
        """setValueString(self: MaterialX.PyMaterialXCore.ValueElement, arg0: str) -> None

        Set the value string of an element.
        """

class Variant(InterfaceElement):
    CATEGORY: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class VariantAssign(Element):
    CATEGORY: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def getVariantSetString(self) -> str:
        """getVariantSetString(self: MaterialX.PyMaterialXCore.VariantAssign) -> str

        Return the element's variant set string.
        """
    def getVariantString(self) -> str:
        """getVariantString(self: MaterialX.PyMaterialXCore.VariantAssign) -> str

        Return the element's variant string.
        """
    def hasVariantSetString(self) -> bool:
        """hasVariantSetString(self: MaterialX.PyMaterialXCore.VariantAssign) -> bool

        Return true if the given element has a variant set string.
        """
    def hasVariantString(self) -> bool:
        """hasVariantString(self: MaterialX.PyMaterialXCore.VariantAssign) -> bool

        Return true if the given element has a variant string.
        """
    def setVariantSetString(self, arg0: str) -> None:
        """setVariantSetString(self: MaterialX.PyMaterialXCore.VariantAssign, arg0: str) -> None

        Set the element's variant set string.
        """
    def setVariantString(self, arg0: str) -> None:
        """setVariantString(self: MaterialX.PyMaterialXCore.VariantAssign, arg0: str) -> None

        Set the element's variant string.
        """

class VariantSet(Element):
    CATEGORY: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def addVariant(self, name: str = ...) -> Variant:
        """addVariant(self: MaterialX.PyMaterialXCore.VariantSet, name: str = '') -> MaterialX.PyMaterialXCore.Variant

        Add a Variant to the variant set.

        Args:
            name: The name of the new Variant. If no name is specified, then a unique name will automatically be generated.

        Returns:
            A shared pointer to the new Variant.
        """
    def getVariant(self, arg0: str) -> Variant:
        """getVariant(self: MaterialX.PyMaterialXCore.VariantSet, arg0: str) -> MaterialX.PyMaterialXCore.Variant

        Return the Variant, if any, with the given name.
        """
    def getVariants(self) -> list[Variant]:
        """getVariants(self: MaterialX.PyMaterialXCore.VariantSet) -> list[MaterialX.PyMaterialXCore.Variant]

        Return a vector of all Variant elements in the look.
        """
    def removeVariant(self, arg0: str) -> None:
        """removeVariant(self: MaterialX.PyMaterialXCore.VariantSet, arg0: str) -> None

        Remove the Variant, if any, with the given name.
        """

class Vector2(VectorBase):
    @overload
    def __init__(self) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: MaterialX.PyMaterialXCore.Vector2) -> None

        2. __init__(self: MaterialX.PyMaterialXCore.Vector2, arg0: float) -> None

        3. __init__(self: MaterialX.PyMaterialXCore.Vector2, arg0: Annotated[list[float], FixedSize(2)]) -> None

        4. __init__(self: MaterialX.PyMaterialXCore.Vector2, arg0: list[float]) -> None

        5. __init__(self: MaterialX.PyMaterialXCore.Vector2, arg0: float, arg1: float) -> None
        """
    @overload
    def __init__(self, arg0: float) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: MaterialX.PyMaterialXCore.Vector2) -> None

        2. __init__(self: MaterialX.PyMaterialXCore.Vector2, arg0: float) -> None

        3. __init__(self: MaterialX.PyMaterialXCore.Vector2, arg0: Annotated[list[float], FixedSize(2)]) -> None

        4. __init__(self: MaterialX.PyMaterialXCore.Vector2, arg0: list[float]) -> None

        5. __init__(self: MaterialX.PyMaterialXCore.Vector2, arg0: float, arg1: float) -> None
        """
    @overload
    def __init__(self, arg0) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: MaterialX.PyMaterialXCore.Vector2) -> None

        2. __init__(self: MaterialX.PyMaterialXCore.Vector2, arg0: float) -> None

        3. __init__(self: MaterialX.PyMaterialXCore.Vector2, arg0: Annotated[list[float], FixedSize(2)]) -> None

        4. __init__(self: MaterialX.PyMaterialXCore.Vector2, arg0: list[float]) -> None

        5. __init__(self: MaterialX.PyMaterialXCore.Vector2, arg0: float, arg1: float) -> None
        """
    @overload
    def __init__(self, arg0: list[float]) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: MaterialX.PyMaterialXCore.Vector2) -> None

        2. __init__(self: MaterialX.PyMaterialXCore.Vector2, arg0: float) -> None

        3. __init__(self: MaterialX.PyMaterialXCore.Vector2, arg0: Annotated[list[float], FixedSize(2)]) -> None

        4. __init__(self: MaterialX.PyMaterialXCore.Vector2, arg0: list[float]) -> None

        5. __init__(self: MaterialX.PyMaterialXCore.Vector2, arg0: float, arg1: float) -> None
        """
    @overload
    def __init__(self, arg0: float, arg1: float) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: MaterialX.PyMaterialXCore.Vector2) -> None

        2. __init__(self: MaterialX.PyMaterialXCore.Vector2, arg0: float) -> None

        3. __init__(self: MaterialX.PyMaterialXCore.Vector2, arg0: Annotated[list[float], FixedSize(2)]) -> None

        4. __init__(self: MaterialX.PyMaterialXCore.Vector2, arg0: list[float]) -> None

        5. __init__(self: MaterialX.PyMaterialXCore.Vector2, arg0: float, arg1: float) -> None
        """
    def asTuple(self) -> tuple[float, float]:
        """asTuple(self: MaterialX.PyMaterialXCore.Vector2) -> tuple[float, float]"""
    def copy(self) -> Vector2:
        """copy(self: MaterialX.PyMaterialXCore.Vector2) -> MaterialX.PyMaterialXCore.Vector2

        Create a deep copy of the value.
        """
    def cross(self, arg0: Vector2) -> float:
        """cross(self: MaterialX.PyMaterialXCore.Vector2, arg0: MaterialX.PyMaterialXCore.Vector2) -> float

        Return the cross product of two vectors.
        """
    def dot(self, arg0: Vector2) -> float:
        """dot(self: MaterialX.PyMaterialXCore.Vector2, arg0: MaterialX.PyMaterialXCore.Vector2) -> float

        Return the dot product of two vectors.
        """
    def getMagnitude(self) -> float:
        """getMagnitude(self: MaterialX.PyMaterialXCore.Vector2) -> float

        Return the magnitude of the vector.
        """
    def getNormalized(self) -> Vector2:
        """getNormalized(self: MaterialX.PyMaterialXCore.Vector2) -> MaterialX.PyMaterialXCore.Vector2

        Return a normalized version of the given path, collapsing current path and parent path references so that 'a/.

        /b' and 'c/../d/../a/b' become 'a/b'.
        """
    def __add__(self, arg0: Vector2) -> Vector2:
        """__add__(self: MaterialX.PyMaterialXCore.Vector2, arg0: MaterialX.PyMaterialXCore.Vector2) -> MaterialX.PyMaterialXCore.Vector2"""
    def __eq__(self, arg0: Vector2) -> bool:
        """__eq__(self: MaterialX.PyMaterialXCore.Vector2, arg0: MaterialX.PyMaterialXCore.Vector2) -> bool"""
    def __getitem__(self, arg0: int) -> float:
        """__getitem__(self: MaterialX.PyMaterialXCore.Vector2, arg0: int) -> float"""
    def __iter__(self) -> typing.Iterator[float]:
        """def __iter__(self) -> typing.Iterator[float]"""
    def __iadd__(self, arg0: Vector2) -> Vector2:
        """__iadd__(self: MaterialX.PyMaterialXCore.Vector2, arg0: MaterialX.PyMaterialXCore.Vector2) -> MaterialX.PyMaterialXCore.Vector2"""
    @overload
    def __imul__(self, arg0: Vector2) -> Vector2:
        """__imul__(*args, **kwargs)
        Overloaded function.

        1. __imul__(self: MaterialX.PyMaterialXCore.Vector2, arg0: MaterialX.PyMaterialXCore.Vector2) -> MaterialX.PyMaterialXCore.Vector2

        2. __imul__(self: MaterialX.PyMaterialXCore.Vector2, arg0: float) -> MaterialX.PyMaterialXCore.Vector2
        """
    @overload
    def __imul__(self, arg0: float) -> Vector2:
        """__imul__(*args, **kwargs)
        Overloaded function.

        1. __imul__(self: MaterialX.PyMaterialXCore.Vector2, arg0: MaterialX.PyMaterialXCore.Vector2) -> MaterialX.PyMaterialXCore.Vector2

        2. __imul__(self: MaterialX.PyMaterialXCore.Vector2, arg0: float) -> MaterialX.PyMaterialXCore.Vector2
        """
    def __isub__(self, arg0: Vector2) -> Vector2:
        """__isub__(self: MaterialX.PyMaterialXCore.Vector2, arg0: MaterialX.PyMaterialXCore.Vector2) -> MaterialX.PyMaterialXCore.Vector2"""
    @overload
    def __itruediv__(self, arg0: Vector2) -> Vector2:
        """__itruediv__(*args, **kwargs)
        Overloaded function.

        1. __itruediv__(self: MaterialX.PyMaterialXCore.Vector2, arg0: MaterialX.PyMaterialXCore.Vector2) -> MaterialX.PyMaterialXCore.Vector2

        2. __itruediv__(self: MaterialX.PyMaterialXCore.Vector2, arg0: float) -> MaterialX.PyMaterialXCore.Vector2
        """
    @overload
    def __itruediv__(self, arg0: float) -> Vector2:
        """__itruediv__(*args, **kwargs)
        Overloaded function.

        1. __itruediv__(self: MaterialX.PyMaterialXCore.Vector2, arg0: MaterialX.PyMaterialXCore.Vector2) -> MaterialX.PyMaterialXCore.Vector2

        2. __itruediv__(self: MaterialX.PyMaterialXCore.Vector2, arg0: float) -> MaterialX.PyMaterialXCore.Vector2
        """
    @staticmethod
    def __len__() -> int:
        """__len__() -> int"""
    @overload
    def __mul__(self, arg0: Vector2) -> Vector2:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: MaterialX.PyMaterialXCore.Vector2, arg0: MaterialX.PyMaterialXCore.Vector2) -> MaterialX.PyMaterialXCore.Vector2

        2. __mul__(self: MaterialX.PyMaterialXCore.Vector2, arg0: float) -> MaterialX.PyMaterialXCore.Vector2
        """
    @overload
    def __mul__(self, arg0: float) -> Vector2:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: MaterialX.PyMaterialXCore.Vector2, arg0: MaterialX.PyMaterialXCore.Vector2) -> MaterialX.PyMaterialXCore.Vector2

        2. __mul__(self: MaterialX.PyMaterialXCore.Vector2, arg0: float) -> MaterialX.PyMaterialXCore.Vector2
        """
    def __ne__(self, arg0: Vector2) -> bool:
        """__ne__(self: MaterialX.PyMaterialXCore.Vector2, arg0: MaterialX.PyMaterialXCore.Vector2) -> bool"""
    def __neg__(self) -> Vector2:
        """__neg__(self: MaterialX.PyMaterialXCore.Vector2) -> MaterialX.PyMaterialXCore.Vector2"""
    def __pos__(self) -> Vector2:
        """__pos__(self: MaterialX.PyMaterialXCore.Vector2) -> MaterialX.PyMaterialXCore.Vector2"""
    def __setitem__(self, arg0: int, arg1: float) -> None:
        """__setitem__(self: MaterialX.PyMaterialXCore.Vector2, arg0: int, arg1: float) -> None"""
    def __sub__(self, arg0: Vector2) -> Vector2:
        """__sub__(self: MaterialX.PyMaterialXCore.Vector2, arg0: MaterialX.PyMaterialXCore.Vector2) -> MaterialX.PyMaterialXCore.Vector2"""
    @overload
    def __truediv__(self, arg0: Vector2) -> Vector2:
        """__truediv__(*args, **kwargs)
        Overloaded function.

        1. __truediv__(self: MaterialX.PyMaterialXCore.Vector2, arg0: MaterialX.PyMaterialXCore.Vector2) -> MaterialX.PyMaterialXCore.Vector2

        2. __truediv__(self: MaterialX.PyMaterialXCore.Vector2, arg0: float) -> MaterialX.PyMaterialXCore.Vector2
        """
    @overload
    def __truediv__(self, arg0: float) -> Vector2:
        """__truediv__(*args, **kwargs)
        Overloaded function.

        1. __truediv__(self: MaterialX.PyMaterialXCore.Vector2, arg0: MaterialX.PyMaterialXCore.Vector2) -> MaterialX.PyMaterialXCore.Vector2

        2. __truediv__(self: MaterialX.PyMaterialXCore.Vector2, arg0: float) -> MaterialX.PyMaterialXCore.Vector2
        """

class Vector3(VectorBase):
    @overload
    def __init__(self) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: MaterialX.PyMaterialXCore.Vector3) -> None

        2. __init__(self: MaterialX.PyMaterialXCore.Vector3, arg0: float) -> None

        3. __init__(self: MaterialX.PyMaterialXCore.Vector3, arg0: Annotated[list[float], FixedSize(3)]) -> None

        4. __init__(self: MaterialX.PyMaterialXCore.Vector3, arg0: list[float]) -> None

        5. __init__(self: MaterialX.PyMaterialXCore.Vector3, arg0: float, arg1: float, arg2: float) -> None
        """
    @overload
    def __init__(self, arg0: float) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: MaterialX.PyMaterialXCore.Vector3) -> None

        2. __init__(self: MaterialX.PyMaterialXCore.Vector3, arg0: float) -> None

        3. __init__(self: MaterialX.PyMaterialXCore.Vector3, arg0: Annotated[list[float], FixedSize(3)]) -> None

        4. __init__(self: MaterialX.PyMaterialXCore.Vector3, arg0: list[float]) -> None

        5. __init__(self: MaterialX.PyMaterialXCore.Vector3, arg0: float, arg1: float, arg2: float) -> None
        """
    @overload
    def __init__(self, arg0) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: MaterialX.PyMaterialXCore.Vector3) -> None

        2. __init__(self: MaterialX.PyMaterialXCore.Vector3, arg0: float) -> None

        3. __init__(self: MaterialX.PyMaterialXCore.Vector3, arg0: Annotated[list[float], FixedSize(3)]) -> None

        4. __init__(self: MaterialX.PyMaterialXCore.Vector3, arg0: list[float]) -> None

        5. __init__(self: MaterialX.PyMaterialXCore.Vector3, arg0: float, arg1: float, arg2: float) -> None
        """
    @overload
    def __init__(self, arg0: list[float]) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: MaterialX.PyMaterialXCore.Vector3) -> None

        2. __init__(self: MaterialX.PyMaterialXCore.Vector3, arg0: float) -> None

        3. __init__(self: MaterialX.PyMaterialXCore.Vector3, arg0: Annotated[list[float], FixedSize(3)]) -> None

        4. __init__(self: MaterialX.PyMaterialXCore.Vector3, arg0: list[float]) -> None

        5. __init__(self: MaterialX.PyMaterialXCore.Vector3, arg0: float, arg1: float, arg2: float) -> None
        """
    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: MaterialX.PyMaterialXCore.Vector3) -> None

        2. __init__(self: MaterialX.PyMaterialXCore.Vector3, arg0: float) -> None

        3. __init__(self: MaterialX.PyMaterialXCore.Vector3, arg0: Annotated[list[float], FixedSize(3)]) -> None

        4. __init__(self: MaterialX.PyMaterialXCore.Vector3, arg0: list[float]) -> None

        5. __init__(self: MaterialX.PyMaterialXCore.Vector3, arg0: float, arg1: float, arg2: float) -> None
        """
    def asTuple(self) -> tuple[float, float, float]:
        """asTuple(self: MaterialX.PyMaterialXCore.Vector3) -> tuple[float, float, float]"""
    def copy(self) -> Vector3:
        """copy(self: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3

        Create a deep copy of the value.
        """
    def cross(self, arg0: Vector3) -> Vector3:
        """cross(self: MaterialX.PyMaterialXCore.Vector3, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3

        Return the cross product of two vectors.
        """
    def dot(self, arg0: Vector3) -> float:
        """dot(self: MaterialX.PyMaterialXCore.Vector3, arg0: MaterialX.PyMaterialXCore.Vector3) -> float

        Return the dot product of two vectors.
        """
    def getMagnitude(self) -> float:
        """getMagnitude(self: MaterialX.PyMaterialXCore.Vector3) -> float

        Return the magnitude of the vector.
        """
    def getNormalized(self) -> Vector3:
        """getNormalized(self: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3

        Return a normalized version of the given path, collapsing current path and parent path references so that 'a/.

        /b' and 'c/../d/../a/b' become 'a/b'.
        """
    def __add__(self, arg0: Vector3) -> Vector3:
        """__add__(self: MaterialX.PyMaterialXCore.Vector3, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3"""
    def __eq__(self, arg0: Vector3) -> bool:
        """__eq__(self: MaterialX.PyMaterialXCore.Vector3, arg0: MaterialX.PyMaterialXCore.Vector3) -> bool"""
    def __getitem__(self, arg0: int) -> float:
        """__getitem__(self: MaterialX.PyMaterialXCore.Vector3, arg0: int) -> float"""
    def __iter__(self) -> typing.Iterator[float]:
        """def __iter__(self) -> typing.Iterator[float]"""
    def __iadd__(self, arg0: Vector3) -> Vector3:
        """__iadd__(self: MaterialX.PyMaterialXCore.Vector3, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3"""
    @overload
    def __imul__(self, arg0: Vector3) -> Vector3:
        """__imul__(*args, **kwargs)
        Overloaded function.

        1. __imul__(self: MaterialX.PyMaterialXCore.Vector3, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3

        2. __imul__(self: MaterialX.PyMaterialXCore.Vector3, arg0: float) -> MaterialX.PyMaterialXCore.Vector3
        """
    @overload
    def __imul__(self, arg0: float) -> Vector3:
        """__imul__(*args, **kwargs)
        Overloaded function.

        1. __imul__(self: MaterialX.PyMaterialXCore.Vector3, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3

        2. __imul__(self: MaterialX.PyMaterialXCore.Vector3, arg0: float) -> MaterialX.PyMaterialXCore.Vector3
        """
    def __isub__(self, arg0: Vector3) -> Vector3:
        """__isub__(self: MaterialX.PyMaterialXCore.Vector3, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3"""
    @overload
    def __itruediv__(self, arg0: Vector3) -> Vector3:
        """__itruediv__(*args, **kwargs)
        Overloaded function.

        1. __itruediv__(self: MaterialX.PyMaterialXCore.Vector3, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3

        2. __itruediv__(self: MaterialX.PyMaterialXCore.Vector3, arg0: float) -> MaterialX.PyMaterialXCore.Vector3
        """
    @overload
    def __itruediv__(self, arg0: float) -> Vector3:
        """__itruediv__(*args, **kwargs)
        Overloaded function.

        1. __itruediv__(self: MaterialX.PyMaterialXCore.Vector3, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3

        2. __itruediv__(self: MaterialX.PyMaterialXCore.Vector3, arg0: float) -> MaterialX.PyMaterialXCore.Vector3
        """
    @staticmethod
    def __len__() -> int:
        """__len__() -> int"""
    @overload
    def __mul__(self, arg0: Vector3) -> Vector3:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: MaterialX.PyMaterialXCore.Vector3, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3

        2. __mul__(self: MaterialX.PyMaterialXCore.Vector3, arg0: float) -> MaterialX.PyMaterialXCore.Vector3
        """
    @overload
    def __mul__(self, arg0: float) -> Vector3:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: MaterialX.PyMaterialXCore.Vector3, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3

        2. __mul__(self: MaterialX.PyMaterialXCore.Vector3, arg0: float) -> MaterialX.PyMaterialXCore.Vector3
        """
    def __ne__(self, arg0: Vector3) -> bool:
        """__ne__(self: MaterialX.PyMaterialXCore.Vector3, arg0: MaterialX.PyMaterialXCore.Vector3) -> bool"""
    def __neg__(self) -> Vector3:
        """__neg__(self: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3"""
    def __pos__(self) -> Vector3:
        """__pos__(self: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3"""
    def __setitem__(self, arg0: int, arg1: float) -> None:
        """__setitem__(self: MaterialX.PyMaterialXCore.Vector3, arg0: int, arg1: float) -> None"""
    def __sub__(self, arg0: Vector3) -> Vector3:
        """__sub__(self: MaterialX.PyMaterialXCore.Vector3, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3"""
    @overload
    def __truediv__(self, arg0: Vector3) -> Vector3:
        """__truediv__(*args, **kwargs)
        Overloaded function.

        1. __truediv__(self: MaterialX.PyMaterialXCore.Vector3, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3

        2. __truediv__(self: MaterialX.PyMaterialXCore.Vector3, arg0: float) -> MaterialX.PyMaterialXCore.Vector3
        """
    @overload
    def __truediv__(self, arg0: float) -> Vector3:
        """__truediv__(*args, **kwargs)
        Overloaded function.

        1. __truediv__(self: MaterialX.PyMaterialXCore.Vector3, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3

        2. __truediv__(self: MaterialX.PyMaterialXCore.Vector3, arg0: float) -> MaterialX.PyMaterialXCore.Vector3
        """

class Vector4(VectorBase):
    @overload
    def __init__(self) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: MaterialX.PyMaterialXCore.Vector4) -> None

        2. __init__(self: MaterialX.PyMaterialXCore.Vector4, arg0: float) -> None

        3. __init__(self: MaterialX.PyMaterialXCore.Vector4, arg0: Annotated[list[float], FixedSize(4)]) -> None

        4. __init__(self: MaterialX.PyMaterialXCore.Vector4, arg0: list[float]) -> None

        5. __init__(self: MaterialX.PyMaterialXCore.Vector4, arg0: float, arg1: float, arg2: float, arg3: float) -> None
        """
    @overload
    def __init__(self, arg0: float) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: MaterialX.PyMaterialXCore.Vector4) -> None

        2. __init__(self: MaterialX.PyMaterialXCore.Vector4, arg0: float) -> None

        3. __init__(self: MaterialX.PyMaterialXCore.Vector4, arg0: Annotated[list[float], FixedSize(4)]) -> None

        4. __init__(self: MaterialX.PyMaterialXCore.Vector4, arg0: list[float]) -> None

        5. __init__(self: MaterialX.PyMaterialXCore.Vector4, arg0: float, arg1: float, arg2: float, arg3: float) -> None
        """
    @overload
    def __init__(self, arg0) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: MaterialX.PyMaterialXCore.Vector4) -> None

        2. __init__(self: MaterialX.PyMaterialXCore.Vector4, arg0: float) -> None

        3. __init__(self: MaterialX.PyMaterialXCore.Vector4, arg0: Annotated[list[float], FixedSize(4)]) -> None

        4. __init__(self: MaterialX.PyMaterialXCore.Vector4, arg0: list[float]) -> None

        5. __init__(self: MaterialX.PyMaterialXCore.Vector4, arg0: float, arg1: float, arg2: float, arg3: float) -> None
        """
    @overload
    def __init__(self, arg0: list[float]) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: MaterialX.PyMaterialXCore.Vector4) -> None

        2. __init__(self: MaterialX.PyMaterialXCore.Vector4, arg0: float) -> None

        3. __init__(self: MaterialX.PyMaterialXCore.Vector4, arg0: Annotated[list[float], FixedSize(4)]) -> None

        4. __init__(self: MaterialX.PyMaterialXCore.Vector4, arg0: list[float]) -> None

        5. __init__(self: MaterialX.PyMaterialXCore.Vector4, arg0: float, arg1: float, arg2: float, arg3: float) -> None
        """
    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float, arg3: float) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: MaterialX.PyMaterialXCore.Vector4) -> None

        2. __init__(self: MaterialX.PyMaterialXCore.Vector4, arg0: float) -> None

        3. __init__(self: MaterialX.PyMaterialXCore.Vector4, arg0: Annotated[list[float], FixedSize(4)]) -> None

        4. __init__(self: MaterialX.PyMaterialXCore.Vector4, arg0: list[float]) -> None

        5. __init__(self: MaterialX.PyMaterialXCore.Vector4, arg0: float, arg1: float, arg2: float, arg3: float) -> None
        """
    def asTuple(self) -> tuple[float, float, float, float]:
        """asTuple(self: MaterialX.PyMaterialXCore.Vector4) -> tuple[float, float, float, float]"""
    def copy(self) -> Vector4:
        """copy(self: MaterialX.PyMaterialXCore.Vector4) -> MaterialX.PyMaterialXCore.Vector4

        Create a deep copy of the value.
        """
    def dot(self, arg0: Vector4) -> float:
        """dot(self: MaterialX.PyMaterialXCore.Vector4, arg0: MaterialX.PyMaterialXCore.Vector4) -> float

        Return the dot product of two vectors.
        """
    def getMagnitude(self) -> float:
        """getMagnitude(self: MaterialX.PyMaterialXCore.Vector4) -> float

        Return the magnitude of the vector.
        """
    def getNormalized(self) -> Vector4:
        """getNormalized(self: MaterialX.PyMaterialXCore.Vector4) -> MaterialX.PyMaterialXCore.Vector4

        Return a normalized version of the given path, collapsing current path and parent path references so that 'a/.

        /b' and 'c/../d/../a/b' become 'a/b'.
        """
    def __add__(self, arg0: Vector4) -> Vector4:
        """__add__(self: MaterialX.PyMaterialXCore.Vector4, arg0: MaterialX.PyMaterialXCore.Vector4) -> MaterialX.PyMaterialXCore.Vector4"""
    def __eq__(self, arg0: Vector4) -> bool:
        """__eq__(self: MaterialX.PyMaterialXCore.Vector4, arg0: MaterialX.PyMaterialXCore.Vector4) -> bool"""
    def __getitem__(self, arg0: int) -> float:
        """__getitem__(self: MaterialX.PyMaterialXCore.Vector4, arg0: int) -> float"""
    def __iter__(self) -> typing.Iterator[float]:
        """def __iter__(self) -> typing.Iterator[float]"""
    def __iadd__(self, arg0: Vector4) -> Vector4:
        """__iadd__(self: MaterialX.PyMaterialXCore.Vector4, arg0: MaterialX.PyMaterialXCore.Vector4) -> MaterialX.PyMaterialXCore.Vector4"""
    @overload
    def __imul__(self, arg0: Vector4) -> Vector4:
        """__imul__(*args, **kwargs)
        Overloaded function.

        1. __imul__(self: MaterialX.PyMaterialXCore.Vector4, arg0: MaterialX.PyMaterialXCore.Vector4) -> MaterialX.PyMaterialXCore.Vector4

        2. __imul__(self: MaterialX.PyMaterialXCore.Vector4, arg0: float) -> MaterialX.PyMaterialXCore.Vector4
        """
    @overload
    def __imul__(self, arg0: float) -> Vector4:
        """__imul__(*args, **kwargs)
        Overloaded function.

        1. __imul__(self: MaterialX.PyMaterialXCore.Vector4, arg0: MaterialX.PyMaterialXCore.Vector4) -> MaterialX.PyMaterialXCore.Vector4

        2. __imul__(self: MaterialX.PyMaterialXCore.Vector4, arg0: float) -> MaterialX.PyMaterialXCore.Vector4
        """
    def __isub__(self, arg0: Vector4) -> Vector4:
        """__isub__(self: MaterialX.PyMaterialXCore.Vector4, arg0: MaterialX.PyMaterialXCore.Vector4) -> MaterialX.PyMaterialXCore.Vector4"""
    @overload
    def __itruediv__(self, arg0: Vector4) -> Vector4:
        """__itruediv__(*args, **kwargs)
        Overloaded function.

        1. __itruediv__(self: MaterialX.PyMaterialXCore.Vector4, arg0: MaterialX.PyMaterialXCore.Vector4) -> MaterialX.PyMaterialXCore.Vector4

        2. __itruediv__(self: MaterialX.PyMaterialXCore.Vector4, arg0: float) -> MaterialX.PyMaterialXCore.Vector4
        """
    @overload
    def __itruediv__(self, arg0: float) -> Vector4:
        """__itruediv__(*args, **kwargs)
        Overloaded function.

        1. __itruediv__(self: MaterialX.PyMaterialXCore.Vector4, arg0: MaterialX.PyMaterialXCore.Vector4) -> MaterialX.PyMaterialXCore.Vector4

        2. __itruediv__(self: MaterialX.PyMaterialXCore.Vector4, arg0: float) -> MaterialX.PyMaterialXCore.Vector4
        """
    @staticmethod
    def __len__() -> int:
        """__len__() -> int"""
    @overload
    def __mul__(self, arg0: Vector4) -> Vector4:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: MaterialX.PyMaterialXCore.Vector4, arg0: MaterialX.PyMaterialXCore.Vector4) -> MaterialX.PyMaterialXCore.Vector4

        2. __mul__(self: MaterialX.PyMaterialXCore.Vector4, arg0: float) -> MaterialX.PyMaterialXCore.Vector4
        """
    @overload
    def __mul__(self, arg0: float) -> Vector4:
        """__mul__(*args, **kwargs)
        Overloaded function.

        1. __mul__(self: MaterialX.PyMaterialXCore.Vector4, arg0: MaterialX.PyMaterialXCore.Vector4) -> MaterialX.PyMaterialXCore.Vector4

        2. __mul__(self: MaterialX.PyMaterialXCore.Vector4, arg0: float) -> MaterialX.PyMaterialXCore.Vector4
        """
    def __ne__(self, arg0: Vector4) -> bool:
        """__ne__(self: MaterialX.PyMaterialXCore.Vector4, arg0: MaterialX.PyMaterialXCore.Vector4) -> bool"""
    def __neg__(self) -> Vector4:
        """__neg__(self: MaterialX.PyMaterialXCore.Vector4) -> MaterialX.PyMaterialXCore.Vector4"""
    def __pos__(self) -> Vector4:
        """__pos__(self: MaterialX.PyMaterialXCore.Vector4) -> MaterialX.PyMaterialXCore.Vector4"""
    def __setitem__(self, arg0: int, arg1: float) -> None:
        """__setitem__(self: MaterialX.PyMaterialXCore.Vector4, arg0: int, arg1: float) -> None"""
    def __sub__(self, arg0: Vector4) -> Vector4:
        """__sub__(self: MaterialX.PyMaterialXCore.Vector4, arg0: MaterialX.PyMaterialXCore.Vector4) -> MaterialX.PyMaterialXCore.Vector4"""
    @overload
    def __truediv__(self, arg0: Vector4) -> Vector4:
        """__truediv__(*args, **kwargs)
        Overloaded function.

        1. __truediv__(self: MaterialX.PyMaterialXCore.Vector4, arg0: MaterialX.PyMaterialXCore.Vector4) -> MaterialX.PyMaterialXCore.Vector4

        2. __truediv__(self: MaterialX.PyMaterialXCore.Vector4, arg0: float) -> MaterialX.PyMaterialXCore.Vector4
        """
    @overload
    def __truediv__(self, arg0: float) -> Vector4:
        """__truediv__(*args, **kwargs)
        Overloaded function.

        1. __truediv__(self: MaterialX.PyMaterialXCore.Vector4, arg0: MaterialX.PyMaterialXCore.Vector4) -> MaterialX.PyMaterialXCore.Vector4

        2. __truediv__(self: MaterialX.PyMaterialXCore.Vector4, arg0: float) -> MaterialX.PyMaterialXCore.Vector4
        """

class VectorBase:
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class Visibility(GeomElement):
    CATEGORY: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def getViewerCollection(self) -> str:
        """getViewerCollection(self: MaterialX.PyMaterialXCore.Visibility) -> str

        Return the viewer collection string of the element.
        """
    def getViewerGeom(self) -> str:
        """getViewerGeom(self: MaterialX.PyMaterialXCore.Visibility) -> str

        Return the viewer geom string of the element.
        """
    def getVisibilityType(self) -> str:
        """getVisibilityType(self: MaterialX.PyMaterialXCore.Visibility) -> str

        Return the visibility type string of the element.
        """
    def getVisible(self) -> bool:
        """getVisible(self: MaterialX.PyMaterialXCore.Visibility) -> bool

        Return the visible boolean of the element.
        """
    def hasViewerCollection(self) -> bool:
        """hasViewerCollection(self: MaterialX.PyMaterialXCore.Visibility) -> bool

        Return true if the given element has a viewer collection string.
        """
    def hasViewerGeom(self) -> bool:
        """hasViewerGeom(self: MaterialX.PyMaterialXCore.Visibility) -> bool

        Return true if the given element has a viewer geom string.
        """
    def hasVisibilityType(self) -> bool:
        """hasVisibilityType(self: MaterialX.PyMaterialXCore.Visibility) -> bool

        Return true if the given element has a visibility type string.
        """
    def setViewerCollection(self, arg0: str) -> None:
        """setViewerCollection(self: MaterialX.PyMaterialXCore.Visibility, arg0: str) -> None

        Set the viewer geom string of the element.
        """
    def setViewerGeom(self, arg0: str) -> None:
        """setViewerGeom(self: MaterialX.PyMaterialXCore.Visibility, arg0: str) -> None

        Set the viewer geom string of the element.
        """
    def setVisibilityType(self, arg0: str) -> None:
        """setVisibilityType(self: MaterialX.PyMaterialXCore.Visibility, arg0: str) -> None

        Set the visibility type string of the element.
        """
    def setVisible(self, arg0: bool) -> None:
        """setVisible(self: MaterialX.PyMaterialXCore.Visibility, arg0: bool) -> None

        Set the visible boolean of the element.
        """

def createDocument(*args, **kwargs):
    """createDocument() -> MaterialX_v1_39_5::Document

    Create a new document of the given subclass.

    Create a new Document.
    """
def createNamePath(arg0: list[str]) -> str:
    """createNamePath(arg0: list[str]) -> str"""
def createValidName(name: str, replaceChar: str = ...) -> str:
    """createValidName(name: str, replaceChar: str = '_') -> str"""
def geomStringsMatch(arg0: str, arg1: str, arg2: bool) -> bool:
    """geomStringsMatch(arg0: str, arg1: str, arg2: bool) -> bool"""
def getConnectedOutputs(arg0: Node) -> list[Output]:
    """getConnectedOutputs(arg0: MaterialX.PyMaterialXCore.Node) -> list[MaterialX.PyMaterialXCore.Output]"""
def getGeometryBindings(materialNode, geom: str = ...) -> list[MaterialAssign]:
    """getGeometryBindings(materialNode: MaterialX_v1_39_5::Node, geom: str = '/') -> list[MaterialX.PyMaterialXCore.MaterialAssign]"""
def getShaderNodes(materialNode: Node, nodeType: str = ..., target: str = ...) -> list[Node]:
    """getShaderNodes(materialNode: MaterialX.PyMaterialXCore.Node, nodeType: str = 'surfaceshader', target: str = '') -> list[MaterialX.PyMaterialXCore.Node]"""
def getVersionIntegers() -> tuple[int, int, int]:
    """getVersionIntegers() -> tuple[int, int, int]

    Return the major and minor versions as an integer pair.
    """
def getVersionString() -> str:
    """getVersionString() -> str

    Return the version string of this interface.
    """
def incrementName(arg0: str) -> str:
    """incrementName(arg0: str) -> str"""
def isValidName(arg0: str) -> bool:
    """isValidName(arg0: str) -> bool"""
def joinStrings(arg0: list[str], arg1: str) -> str:
    """joinStrings(arg0: list[str], arg1: str) -> str"""
def parentNamePath(arg0: str) -> str:
    """parentNamePath(arg0: str) -> str"""
def prettyPrint(arg0: Element) -> str:
    """prettyPrint(arg0: MaterialX.PyMaterialXCore.Element) -> str"""
def replaceSubstrings(arg0: str, arg1: dict[str, str]) -> str:
    """replaceSubstrings(arg0: str, arg1: dict[str, str]) -> str"""
def splitNamePath(arg0: str) -> list[str]:
    """splitNamePath(arg0: str) -> list[str]"""
def splitString(arg0: str, arg1: str) -> list[str]:
    """splitString(arg0: str, arg1: str) -> list[str]"""
def stringEndsWith(arg0: str, arg1: str) -> bool:
    """stringEndsWith(arg0: str, arg1: str) -> bool"""
def stringStartsWith(arg0: str, arg1: str) -> bool:
    """stringStartsWith(arg0: str, arg1: str) -> bool"""
def targetStringsMatch(arg0: str, arg1: str) -> bool:
    """targetStringsMatch(arg0: str, arg1: str) -> bool"""
