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
        """getAttrName(self: MaterialX.PyMaterialXCore.AttributeDef) -> str"""
    def getExportable(self) -> bool:
        """getExportable(self: MaterialX.PyMaterialXCore.AttributeDef) -> bool"""
    def getValueString(self) -> str:
        """getValueString(self: MaterialX.PyMaterialXCore.AttributeDef) -> str"""
    def hasAttrName(self) -> bool:
        """hasAttrName(self: MaterialX.PyMaterialXCore.AttributeDef) -> bool"""
    def hasValueString(self) -> bool:
        """hasValueString(self: MaterialX.PyMaterialXCore.AttributeDef) -> bool"""
    def setAttrName(self, arg0: str) -> None:
        """setAttrName(self: MaterialX.PyMaterialXCore.AttributeDef, arg0: str) -> None"""
    def setExportable(self, arg0: bool) -> None:
        """setExportable(self: MaterialX.PyMaterialXCore.AttributeDef, arg0: bool) -> None"""
    def setValueString(self, arg0: str) -> None:
        """setValueString(self: MaterialX.PyMaterialXCore.AttributeDef, arg0: str) -> None"""

class Backdrop(Element):
    CATEGORY: ClassVar[str] = ...  # read-only
    CONTAINS_ATTRIBUTE: ClassVar[str] = ...  # read-only
    HEIGHT_ATTRIBUTE: ClassVar[str] = ...  # read-only
    WIDTH_ATTRIBUTE: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def getContainsElements(self) -> list[TypedElement]:
        """getContainsElements(self: MaterialX.PyMaterialXCore.Backdrop) -> list[MaterialX.PyMaterialXCore.TypedElement]"""
    def getContainsString(self) -> str:
        """getContainsString(self: MaterialX.PyMaterialXCore.Backdrop) -> str"""
    def getHeight(self) -> float:
        """getHeight(self: MaterialX.PyMaterialXCore.Backdrop) -> float"""
    def getWidth(self) -> float:
        """getWidth(self: MaterialX.PyMaterialXCore.Backdrop) -> float"""
    def hasContainsString(self) -> bool:
        """hasContainsString(self: MaterialX.PyMaterialXCore.Backdrop) -> bool"""
    def hasHeight(self) -> bool:
        """hasHeight(self: MaterialX.PyMaterialXCore.Backdrop) -> bool"""
    def hasWidth(self) -> bool:
        """hasWidth(self: MaterialX.PyMaterialXCore.Backdrop) -> bool"""
    def setContainsElements(self, arg0: list[TypedElement]) -> None:
        """setContainsElements(self: MaterialX.PyMaterialXCore.Backdrop, arg0: list[MaterialX.PyMaterialXCore.TypedElement]) -> None"""
    def setContainsString(self, arg0: str) -> None:
        """setContainsString(self: MaterialX.PyMaterialXCore.Backdrop, arg0: str) -> None"""
    def setHeight(self, arg0: float) -> None:
        """setHeight(self: MaterialX.PyMaterialXCore.Backdrop, arg0: float) -> None"""
    def setWidth(self, arg0: float) -> None:
        """setWidth(self: MaterialX.PyMaterialXCore.Backdrop, arg0: float) -> None"""

class Collection(Element):
    CATEGORY: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def getExcludeGeom(self) -> str:
        """getExcludeGeom(self: MaterialX.PyMaterialXCore.Collection) -> str"""
    def getIncludeCollectionString(self) -> str:
        """getIncludeCollectionString(self: MaterialX.PyMaterialXCore.Collection) -> str"""
    def getIncludeCollections(self) -> list[Collection]:
        """getIncludeCollections(self: MaterialX.PyMaterialXCore.Collection) -> list[MaterialX.PyMaterialXCore.Collection]"""
    def getIncludeGeom(self) -> str:
        """getIncludeGeom(self: MaterialX.PyMaterialXCore.Collection) -> str"""
    def hasExcludeGeom(self) -> bool:
        """hasExcludeGeom(self: MaterialX.PyMaterialXCore.Collection) -> bool"""
    def hasIncludeCollectionString(self) -> bool:
        """hasIncludeCollectionString(self: MaterialX.PyMaterialXCore.Collection) -> bool"""
    def hasIncludeCycle(self) -> bool:
        """hasIncludeCycle(self: MaterialX.PyMaterialXCore.Collection) -> bool"""
    def hasIncludeGeom(self) -> bool:
        """hasIncludeGeom(self: MaterialX.PyMaterialXCore.Collection) -> bool"""
    def matchesGeomString(self, arg0: str) -> bool:
        """matchesGeomString(self: MaterialX.PyMaterialXCore.Collection, arg0: str) -> bool"""
    def setExcludeGeom(self, arg0: str) -> None:
        """setExcludeGeom(self: MaterialX.PyMaterialXCore.Collection, arg0: str) -> None"""
    def setIncludeCollection(self, arg0: Collection) -> None:
        """setIncludeCollection(self: MaterialX.PyMaterialXCore.Collection, arg0: MaterialX.PyMaterialXCore.Collection) -> None"""
    def setIncludeCollectionString(self, arg0: str) -> None:
        """setIncludeCollectionString(self: MaterialX.PyMaterialXCore.Collection, arg0: str) -> None"""
    def setIncludeCollections(self, arg0: list[Collection]) -> None:
        """setIncludeCollections(self: MaterialX.PyMaterialXCore.Collection, arg0: list[MaterialX.PyMaterialXCore.Collection]) -> None"""
    def setIncludeGeom(self, arg0: str) -> None:
        """setIncludeGeom(self: MaterialX.PyMaterialXCore.Collection, arg0: str) -> None"""

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
        """copy(self: MaterialX.PyMaterialXCore.Color3) -> MaterialX.PyMaterialXCore.Color3"""
    def dot(self, arg0: Color3) -> float:
        """dot(self: MaterialX.PyMaterialXCore.Color3, arg0: MaterialX.PyMaterialXCore.Color3) -> float"""
    def getMagnitude(self) -> float:
        """getMagnitude(self: MaterialX.PyMaterialXCore.Color3) -> float"""
    def getNormalized(self) -> Color3:
        """getNormalized(self: MaterialX.PyMaterialXCore.Color3) -> MaterialX.PyMaterialXCore.Color3"""
    def linearToSrgb(self) -> Color3:
        """linearToSrgb(self: MaterialX.PyMaterialXCore.Color3) -> MaterialX.PyMaterialXCore.Color3"""
    def srgbToLinear(self) -> Color3:
        """srgbToLinear(self: MaterialX.PyMaterialXCore.Color3) -> MaterialX.PyMaterialXCore.Color3"""
    def __add__(self, arg0: Color3) -> Color3:
        """__add__(self: MaterialX.PyMaterialXCore.Color3, arg0: MaterialX.PyMaterialXCore.Color3) -> MaterialX.PyMaterialXCore.Color3"""
    def __eq__(self, arg0: Color3) -> bool:
        """__eq__(self: MaterialX.PyMaterialXCore.Color3, arg0: MaterialX.PyMaterialXCore.Color3) -> bool"""
    def __getitem__(self, arg0: int) -> float:
        """__getitem__(self: MaterialX.PyMaterialXCore.Color3, arg0: int) -> float"""
    def __iter__(self) -> typing.Iterator[float]:
        """def __iter__(self) -> typing.Iterator[float]"""
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
        """copy(self: MaterialX.PyMaterialXCore.Color4) -> MaterialX.PyMaterialXCore.Color4"""
    def dot(self, arg0: Color4) -> float:
        """dot(self: MaterialX.PyMaterialXCore.Color4, arg0: MaterialX.PyMaterialXCore.Color4) -> float"""
    def getMagnitude(self) -> float:
        """getMagnitude(self: MaterialX.PyMaterialXCore.Color4) -> float"""
    def getNormalized(self) -> Color4:
        """getNormalized(self: MaterialX.PyMaterialXCore.Color4) -> MaterialX.PyMaterialXCore.Color4"""
    def __add__(self, arg0: Color4) -> Color4:
        """__add__(self: MaterialX.PyMaterialXCore.Color4, arg0: MaterialX.PyMaterialXCore.Color4) -> MaterialX.PyMaterialXCore.Color4"""
    def __eq__(self, arg0: Color4) -> bool:
        """__eq__(self: MaterialX.PyMaterialXCore.Color4, arg0: MaterialX.PyMaterialXCore.Color4) -> bool"""
    def __getitem__(self, arg0: int) -> float:
        """__getitem__(self: MaterialX.PyMaterialXCore.Color4, arg0: int) -> float"""
    def __iter__(self) -> typing.Iterator[float]:
        """def __iter__(self) -> typing.Iterator[float]"""
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
        """addAttributeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.AttributeDef"""
    def addCollection(self, name: str = ...) -> Collection:
        """addCollection(self: MaterialX.PyMaterialXCore.Document, name: str = '') -> MaterialX.PyMaterialXCore.Collection"""
    def addGeomInfo(self, name: str = ..., geom: str = ...) -> GeomInfo:
        """addGeomInfo(self: MaterialX.PyMaterialXCore.Document, name: str = '', geom: str = '/') -> MaterialX.PyMaterialXCore.GeomInfo"""
    def addGeomPropDef(self, arg0: str, arg1: str) -> GeomPropDef:
        """addGeomPropDef(self: MaterialX.PyMaterialXCore.Document, arg0: str, arg1: str) -> MaterialX.PyMaterialXCore.GeomPropDef"""
    def addImplementation(self, name: str = ...) -> Implementation:
        """addImplementation(self: MaterialX.PyMaterialXCore.Document, name: str = '') -> MaterialX.PyMaterialXCore.Implementation"""
    def addLook(self, name: str = ...) -> Look:
        """addLook(self: MaterialX.PyMaterialXCore.Document, name: str = '') -> MaterialX.PyMaterialXCore.Look"""
    def addLookGroup(self, name: str = ...) -> LookGroup:
        """addLookGroup(self: MaterialX.PyMaterialXCore.Document, name: str = '') -> MaterialX.PyMaterialXCore.LookGroup"""
    def addNodeDef(self, name: str = ..., type: str = ..., node: str = ...) -> NodeDef:
        """addNodeDef(self: MaterialX.PyMaterialXCore.Document, name: str = '', type: str = 'color3', node: str = '') -> MaterialX.PyMaterialXCore.NodeDef"""
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
        """addNodeGraph(self: MaterialX.PyMaterialXCore.Document, name: str = '') -> MaterialX.PyMaterialXCore.NodeGraph"""
    def addPropertySet(self, name: str = ...) -> PropertySet:
        """addPropertySet(self: MaterialX.PyMaterialXCore.Document, name: str = '') -> MaterialX.PyMaterialXCore.PropertySet"""
    def addTargetDef(self, arg0: str) -> TargetDef:
        """addTargetDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.TargetDef"""
    def addTypeDef(self, name: str = ...) -> TypeDef:
        """addTypeDef(self: MaterialX.PyMaterialXCore.Document, name: str = '') -> MaterialX.PyMaterialXCore.TypeDef"""
    def addUnitDef(self, arg0: str) -> UnitDef:
        """addUnitDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.UnitDef"""
    def addUnitTypeDef(self, arg0: str) -> UnitTypeDef:
        """addUnitTypeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.UnitTypeDef"""
    def addVariantSet(self, name: str = ...) -> VariantSet:
        """addVariantSet(self: MaterialX.PyMaterialXCore.Document, name: str = '') -> MaterialX.PyMaterialXCore.VariantSet"""
    def copy(self) -> Document:
        """copy(self: MaterialX.PyMaterialXCore.Document) -> MaterialX.PyMaterialXCore.Document"""
    def getAttributeDef(self, arg0: str) -> AttributeDef:
        """getAttributeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.AttributeDef"""
    def getAttributeDefs(self) -> list[AttributeDef]:
        """getAttributeDefs(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.AttributeDef]"""
    def getCollection(self, arg0: str) -> Collection:
        """getCollection(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.Collection"""
    def getCollections(self) -> list[Collection]:
        """getCollections(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.Collection]"""
    def getColorManagementConfig(self) -> str:
        """getColorManagementConfig(self: MaterialX.PyMaterialXCore.Document) -> str"""
    def getColorManagementSystem(self) -> str:
        """getColorManagementSystem(self: MaterialX.PyMaterialXCore.Document) -> str"""
    def getDataLibrary(self) -> Document:
        """getDataLibrary(self: MaterialX.PyMaterialXCore.Document) -> MaterialX.PyMaterialXCore.Document"""
    def getGeomInfo(self, arg0: str) -> GeomInfo:
        """getGeomInfo(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.GeomInfo"""
    def getGeomInfos(self) -> list[GeomInfo]:
        """getGeomInfos(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.GeomInfo]"""
    def getGeomPropDef(self, arg0: str) -> GeomPropDef:
        """getGeomPropDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.GeomPropDef"""
    def getGeomPropDefs(self) -> list[GeomPropDef]:
        """getGeomPropDefs(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.GeomPropDef]"""
    def getGeomPropValue(self, geomPropName: str, geom: str = ...) -> Value:
        """getGeomPropValue(self: MaterialX.PyMaterialXCore.Document, geomPropName: str, geom: str = '/') -> MaterialX.PyMaterialXCore.Value"""
    def getImplementation(self, arg0: str) -> Implementation:
        """getImplementation(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.Implementation"""
    def getImplementations(self) -> list[Implementation]:
        """getImplementations(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.Implementation]"""
    def getLook(self, arg0: str) -> Look:
        """getLook(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.Look"""
    def getLookGroup(self, arg0: str) -> LookGroup:
        """getLookGroup(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.LookGroup"""
    def getLookGroups(self) -> list[LookGroup]:
        """getLookGroups(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.LookGroup]"""
    def getLooks(self) -> list[Look]:
        """getLooks(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.Look]"""
    def getMatchingImplementations(self, arg0: str) -> list[InterfaceElement]:
        """getMatchingImplementations(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> list[MaterialX.PyMaterialXCore.InterfaceElement]"""
    def getMatchingNodeDefs(self, arg0: str) -> list[NodeDef]:
        """getMatchingNodeDefs(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> list[MaterialX.PyMaterialXCore.NodeDef]"""
    def getMatchingPorts(self, arg0: str) -> list[PortElement]:
        """getMatchingPorts(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> list[MaterialX.PyMaterialXCore.PortElement]"""
    def getMaterialOutputs(self) -> list[Output]:
        """getMaterialOutputs(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.Output]"""
    def getNodeDef(self, arg0: str) -> NodeDef:
        """getNodeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.NodeDef"""
    def getNodeDefs(self) -> list[NodeDef]:
        """getNodeDefs(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.NodeDef]"""
    def getNodeGraph(self, arg0: str) -> NodeGraph:
        """getNodeGraph(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.NodeGraph"""
    def getNodeGraphs(self) -> list[NodeGraph]:
        """getNodeGraphs(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.NodeGraph]"""
    def getPropertySet(self, arg0: str) -> PropertySet:
        """getPropertySet(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.PropertySet"""
    def getPropertySets(self) -> list[PropertySet]:
        """getPropertySets(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.PropertySet]"""
    def getReferencedSourceUris(self) -> set[str]:
        """getReferencedSourceUris(self: MaterialX.PyMaterialXCore.Document) -> set[str]"""
    def getTargetDef(self, arg0: str) -> TargetDef:
        """getTargetDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.TargetDef"""
    def getTargetDefs(self) -> list[TargetDef]:
        """getTargetDefs(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.TargetDef]"""
    def getTypeDef(self, arg0: str) -> TypeDef:
        """getTypeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.TypeDef"""
    def getTypeDefs(self) -> list[TypeDef]:
        """getTypeDefs(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.TypeDef]"""
    def getUnitDef(self, arg0: str) -> UnitDef:
        """getUnitDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.UnitDef"""
    def getUnitDefs(self) -> list[UnitDef]:
        """getUnitDefs(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.UnitDef]"""
    def getUnitTypeDef(self, arg0: str) -> UnitTypeDef:
        """getUnitTypeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.UnitTypeDef"""
    def getUnitTypeDefs(self) -> list[UnitTypeDef]:
        """getUnitTypeDefs(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.UnitTypeDef]"""
    def getVariantSet(self, arg0: str) -> VariantSet:
        """getVariantSet(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.VariantSet"""
    def getVariantSets(self) -> list[VariantSet]:
        """getVariantSets(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.VariantSet]"""
    def hasColorManagementConfig(self) -> bool:
        """hasColorManagementConfig(self: MaterialX.PyMaterialXCore.Document) -> bool"""
    def hasColorManagementSystem(self) -> bool:
        """hasColorManagementSystem(self: MaterialX.PyMaterialXCore.Document) -> bool"""
    def hasDataLibrary(self) -> bool:
        """hasDataLibrary(self: MaterialX.PyMaterialXCore.Document) -> bool"""
    def importLibrary(self, arg0: Document) -> None:
        """importLibrary(self: MaterialX.PyMaterialXCore.Document, arg0: MaterialX.PyMaterialXCore.Document) -> None"""
    def initialize(self) -> None:
        """initialize(self: MaterialX.PyMaterialXCore.Document) -> None"""
    def removeAttributeDef(self, arg0: str) -> None:
        """removeAttributeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None"""
    def removeCollection(self, arg0: str) -> None:
        """removeCollection(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None"""
    def removeGeomInfo(self, arg0: str) -> None:
        """removeGeomInfo(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None"""
    def removeGeomPropDef(self, arg0: str) -> None:
        """removeGeomPropDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None"""
    def removeImplementation(self, arg0: str) -> None:
        """removeImplementation(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None"""
    def removeLook(self, arg0: str) -> None:
        """removeLook(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None"""
    def removeLookGroup(self, arg0: str) -> None:
        """removeLookGroup(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None"""
    def removeNodeDef(self, arg0: str) -> None:
        """removeNodeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None"""
    def removeNodeGraph(self, arg0: str) -> None:
        """removeNodeGraph(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None"""
    def removePropertySet(self, arg0: str) -> None:
        """removePropertySet(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None"""
    def removeTargetDef(self, arg0: str) -> None:
        """removeTargetDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None"""
    def removeTypeDef(self, arg0: str) -> None:
        """removeTypeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None"""
    def removeUnitDef(self, arg0: str) -> None:
        """removeUnitDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None"""
    def removeUnitTypeDef(self, arg0: str) -> None:
        """removeUnitTypeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None"""
    def removeVariantSet(self, arg0: str) -> None:
        """removeVariantSet(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None"""
    def setColorManagementConfig(self, arg0: str) -> None:
        """setColorManagementConfig(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None"""
    def setColorManagementSystem(self, arg0: str) -> None:
        """setColorManagementSystem(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None"""
    def setDataLibrary(self, arg0: Document) -> None:
        """setDataLibrary(self: MaterialX.PyMaterialXCore.Document, arg0: MaterialX.PyMaterialXCore.Document) -> None"""
    def upgradeVersion(self) -> None:
        """upgradeVersion(self: MaterialX.PyMaterialXCore.Document) -> None"""

class Edge:
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def getConnectingElement(self) -> Element:
        """getConnectingElement(self: MaterialX.PyMaterialXCore.Edge) -> MaterialX.PyMaterialXCore.Element"""
    def getDownstreamElement(self) -> Element:
        """getDownstreamElement(self: MaterialX.PyMaterialXCore.Edge) -> MaterialX.PyMaterialXCore.Element"""
    def getName(self) -> str:
        """getName(self: MaterialX.PyMaterialXCore.Edge) -> str"""
    def getUpstreamElement(self) -> Element:
        """getUpstreamElement(self: MaterialX.PyMaterialXCore.Edge) -> MaterialX.PyMaterialXCore.Element"""

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
        """addChildOfCategory(self: MaterialX.PyMaterialXCore.Element, category: str, name: str = '') -> MaterialX.PyMaterialXCore.Element"""
    def asString(self) -> str:
        """asString(self: MaterialX.PyMaterialXCore.Element) -> str"""
    def changeChildCategory(self, arg0: Element, arg1: str) -> Element:
        """changeChildCategory(self: MaterialX.PyMaterialXCore.Element, arg0: MaterialX.PyMaterialXCore.Element, arg1: str) -> MaterialX.PyMaterialXCore.Element"""
    def clearContent(self) -> None:
        """clearContent(self: MaterialX.PyMaterialXCore.Element) -> None"""
    def copyContentFrom(self, arg0: Element) -> None:
        """copyContentFrom(self: MaterialX.PyMaterialXCore.Element, arg0: MaterialX.PyMaterialXCore.Element) -> None"""
    def createStringResolver(self, *args, **kwargs):
        """createStringResolver(self: MaterialX.PyMaterialXCore.Element, geom: str = '') -> MaterialX_v1_39_4::StringResolver"""
    def createValidChildName(self, arg0: str) -> str:
        """createValidChildName(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> str"""
    def getActiveColorSpace(self) -> str:
        """getActiveColorSpace(self: MaterialX.PyMaterialXCore.Element) -> str"""
    def getActiveFilePrefix(self) -> str:
        """getActiveFilePrefix(self: MaterialX.PyMaterialXCore.Element) -> str"""
    def getActiveGeomPrefix(self) -> str:
        """getActiveGeomPrefix(self: MaterialX.PyMaterialXCore.Element) -> str"""
    def getActiveSourceUri(self) -> str:
        """getActiveSourceUri(self: MaterialX.PyMaterialXCore.Element) -> str"""
    def getAttribute(self, arg0: str) -> str:
        """getAttribute(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> str"""
    def getAttributeNames(self) -> list[str]:
        """getAttributeNames(self: MaterialX.PyMaterialXCore.Element) -> list[str]"""
    def getCategory(self) -> str:
        """getCategory(self: MaterialX.PyMaterialXCore.Element) -> str"""
    def getChildIndex(self, arg0: str) -> int:
        """getChildIndex(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> int"""
    def getChildren(self) -> list[Element]:
        """getChildren(self: MaterialX.PyMaterialXCore.Element) -> list[MaterialX.PyMaterialXCore.Element]"""
    def getColorSpace(self) -> str:
        """getColorSpace(self: MaterialX.PyMaterialXCore.Element) -> str"""
    def getDescendant(self, arg0: str) -> Element:
        """getDescendant(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> MaterialX.PyMaterialXCore.Element"""
    def getDocString(self) -> str:
        """getDocString(self: MaterialX.PyMaterialXCore.Element) -> str"""
    def getDocument(self, *args, **kwargs):
        """getDocument(self: MaterialX.PyMaterialXCore.Element) -> MaterialX_v1_39_4::Document"""
    def getFilePrefix(self) -> str:
        """getFilePrefix(self: MaterialX.PyMaterialXCore.Element) -> str"""
    def getGeomPrefix(self) -> str:
        """getGeomPrefix(self: MaterialX.PyMaterialXCore.Element) -> str"""
    def getInheritString(self) -> str:
        """getInheritString(self: MaterialX.PyMaterialXCore.Element) -> str"""
    def getInheritsFrom(self) -> Element:
        """getInheritsFrom(self: MaterialX.PyMaterialXCore.Element) -> MaterialX.PyMaterialXCore.Element"""
    def getName(self) -> str:
        """getName(self: MaterialX.PyMaterialXCore.Element) -> str"""
    def getNamePath(self, relativeTo: Element = ...) -> str:
        """getNamePath(self: MaterialX.PyMaterialXCore.Element, relativeTo: MaterialX.PyMaterialXCore.Element = None) -> str"""
    def getNamespace(self) -> str:
        """getNamespace(self: MaterialX.PyMaterialXCore.Element) -> str"""
    def getParent(self) -> Element:
        """getParent(self: MaterialX.PyMaterialXCore.Element) -> MaterialX.PyMaterialXCore.Element"""
    def getQualifiedName(self, arg0: str) -> str:
        """getQualifiedName(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> str"""
    def getRoot(self) -> Element:
        """getRoot(self: MaterialX.PyMaterialXCore.Element) -> MaterialX.PyMaterialXCore.Element"""
    def getSelf(self) -> Element:
        """getSelf(self: MaterialX.PyMaterialXCore.Element) -> MaterialX.PyMaterialXCore.Element"""
    def getSourceUri(self) -> str:
        """getSourceUri(self: MaterialX.PyMaterialXCore.Element) -> str"""
    def getUpstreamEdge(self, *args, **kwargs):
        """getUpstreamEdge(self: MaterialX.PyMaterialXCore.Element, index: int = 0) -> MaterialX_v1_39_4::Edge"""
    def getUpstreamEdgeCount(self) -> int:
        """getUpstreamEdgeCount(self: MaterialX.PyMaterialXCore.Element) -> int"""
    def getUpstreamElement(self, index: int = ...) -> Element:
        """getUpstreamElement(self: MaterialX.PyMaterialXCore.Element, index: int = 0) -> MaterialX.PyMaterialXCore.Element"""
    def hasAttribute(self, arg0: str) -> bool:
        """hasAttribute(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> bool"""
    def hasColorSpace(self) -> bool:
        """hasColorSpace(self: MaterialX.PyMaterialXCore.Element) -> bool"""
    def hasFilePrefix(self) -> bool:
        """hasFilePrefix(self: MaterialX.PyMaterialXCore.Element) -> bool"""
    def hasGeomPrefix(self) -> bool:
        """hasGeomPrefix(self: MaterialX.PyMaterialXCore.Element) -> bool"""
    def hasInheritString(self) -> bool:
        """hasInheritString(self: MaterialX.PyMaterialXCore.Element) -> bool"""
    def hasInheritanceCycle(self) -> bool:
        """hasInheritanceCycle(self: MaterialX.PyMaterialXCore.Element) -> bool"""
    def hasInheritedBase(self, arg0: Element) -> bool:
        """hasInheritedBase(self: MaterialX.PyMaterialXCore.Element, arg0: MaterialX.PyMaterialXCore.Element) -> bool"""
    def hasNamespace(self) -> bool:
        """hasNamespace(self: MaterialX.PyMaterialXCore.Element) -> bool"""
    def hasSourceUri(self) -> bool:
        """hasSourceUri(self: MaterialX.PyMaterialXCore.Element) -> bool"""
    def isEquivalent(self, arg0: Element, arg1) -> tuple[bool, str]:
        """isEquivalent(self: MaterialX.PyMaterialXCore.Element, arg0: MaterialX.PyMaterialXCore.Element, arg1: MaterialX_v1_39_4::ElementEquivalenceOptions) -> tuple[bool, str]"""
    def removeAttribute(self, arg0: str) -> None:
        """removeAttribute(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None"""
    def removeChild(self, arg0: str) -> None:
        """removeChild(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None"""
    def setAttribute(self, arg0: str, arg1: str) -> None:
        """setAttribute(self: MaterialX.PyMaterialXCore.Element, arg0: str, arg1: str) -> None"""
    def setCategory(self, arg0: str) -> None:
        """setCategory(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None"""
    def setChildIndex(self, arg0: str, arg1: int) -> None:
        """setChildIndex(self: MaterialX.PyMaterialXCore.Element, arg0: str, arg1: int) -> None"""
    def setColorSpace(self, arg0: str) -> None:
        """setColorSpace(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None"""
    def setDocString(self, arg0: str) -> None:
        """setDocString(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None"""
    def setFilePrefix(self, arg0: str) -> None:
        """setFilePrefix(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None"""
    def setGeomPrefix(self, arg0: str) -> None:
        """setGeomPrefix(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None"""
    def setInheritString(self, arg0: str) -> None:
        """setInheritString(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None"""
    def setInheritsFrom(self, arg0: Element) -> None:
        """setInheritsFrom(self: MaterialX.PyMaterialXCore.Element, arg0: MaterialX.PyMaterialXCore.Element) -> None"""
    def setName(self, arg0: str) -> None:
        """setName(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None"""
    def setNamespace(self, arg0: str) -> None:
        """setNamespace(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None"""
    def setSourceUri(self, arg0: str) -> None:
        """setSourceUri(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None"""
    def traverseGraph(self, *args, **kwargs):
        """traverseGraph(self: MaterialX.PyMaterialXCore.Element) -> MaterialX_v1_39_4::GraphIterator"""
    def traverseInheritance(self, *args, **kwargs):
        """traverseInheritance(self: MaterialX.PyMaterialXCore.Element) -> MaterialX_v1_39_4::InheritanceIterator"""
    def traverseTree(self, *args, **kwargs):
        """traverseTree(self: MaterialX.PyMaterialXCore.Element) -> MaterialX_v1_39_4::TreeIterator"""
    def validate(self) -> tuple[bool, str]:
        """validate(self: MaterialX.PyMaterialXCore.Element) -> tuple[bool, str]"""
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
        """getCollection(self: MaterialX.PyMaterialXCore.GeomElement) -> MaterialX_v1_39_4::Collection"""
    def getCollectionString(self) -> str:
        """getCollectionString(self: MaterialX.PyMaterialXCore.GeomElement) -> str"""
    def getGeom(self) -> str:
        """getGeom(self: MaterialX.PyMaterialXCore.GeomElement) -> str"""
    def hasCollectionString(self) -> bool:
        """hasCollectionString(self: MaterialX.PyMaterialXCore.GeomElement) -> bool"""
    def hasGeom(self) -> bool:
        """hasGeom(self: MaterialX.PyMaterialXCore.GeomElement) -> bool"""
    def setCollection(self, arg0) -> None:
        """setCollection(self: MaterialX.PyMaterialXCore.GeomElement, arg0: MaterialX_v1_39_4::Collection) -> None"""
    def setCollectionString(self, arg0: str) -> None:
        """setCollectionString(self: MaterialX.PyMaterialXCore.GeomElement, arg0: str) -> None"""
    def setGeom(self, arg0: str) -> None:
        """setGeom(self: MaterialX.PyMaterialXCore.GeomElement, arg0: str) -> None"""

class GeomInfo(GeomElement):
    CATEGORY: ClassVar[str] = ...  # read-only
    addGeomAttr: ClassVar[Callable] = ...
    setGeomAttrValue: ClassVar[Callable] = ...
    setGeomPropValue: ClassVar[Callable] = ...
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def addGeomProp(self, *args, **kwargs):
        """addGeomProp(self: MaterialX.PyMaterialXCore.GeomInfo, arg0: str) -> MaterialX_v1_39_4::GeomProp"""
    def addToken(self, name: str = ...) -> Token:
        """addToken(self: MaterialX.PyMaterialXCore.GeomInfo, name: str = 'color3') -> MaterialX.PyMaterialXCore.Token"""
    def getGeomProp(self, *args, **kwargs):
        """getGeomProp(self: MaterialX.PyMaterialXCore.GeomInfo, arg0: str) -> MaterialX_v1_39_4::GeomProp"""
    def getGeomProps(self, *args, **kwargs):
        """getGeomProps(self: MaterialX.PyMaterialXCore.GeomInfo) -> list[MaterialX_v1_39_4::GeomProp]"""
    def getToken(self, arg0: str) -> Token:
        """getToken(self: MaterialX.PyMaterialXCore.GeomInfo, arg0: str) -> MaterialX.PyMaterialXCore.Token"""
    def getTokens(self) -> list[Token]:
        """getTokens(self: MaterialX.PyMaterialXCore.GeomInfo) -> list[MaterialX.PyMaterialXCore.Token]"""
    def removeGeomProp(self, arg0: str) -> None:
        """removeGeomProp(self: MaterialX.PyMaterialXCore.GeomInfo, arg0: str) -> None"""
    def removeToken(self, arg0: str) -> None:
        """removeToken(self: MaterialX.PyMaterialXCore.GeomInfo, arg0: str) -> None"""
    def setTokenValue(self, arg0: str, arg1: str) -> Token:
        """setTokenValue(self: MaterialX.PyMaterialXCore.GeomInfo, arg0: str, arg1: str) -> MaterialX.PyMaterialXCore.Token"""

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

        2. getGeomProp(self: MaterialX.PyMaterialXCore.GeomPropDef) -> str
        """
    @overload
    def getGeomProp(self) -> str:
        """getGeomProp(*args, **kwargs)
        Overloaded function.

        1. getGeomProp(self: MaterialX.PyMaterialXCore.GeomPropDef) -> str

        2. getGeomProp(self: MaterialX.PyMaterialXCore.GeomPropDef) -> str
        """
    def getIndex(self) -> str:
        """getIndex(self: MaterialX.PyMaterialXCore.GeomPropDef) -> str"""
    def getSpace(self) -> str:
        """getSpace(self: MaterialX.PyMaterialXCore.GeomPropDef) -> str"""
    @overload
    def hasGeomProp(self) -> bool:
        """hasGeomProp(*args, **kwargs)
        Overloaded function.

        1. hasGeomProp(self: MaterialX.PyMaterialXCore.GeomPropDef) -> bool

        2. hasGeomProp(self: MaterialX.PyMaterialXCore.GeomPropDef) -> bool
        """
    @overload
    def hasGeomProp(self) -> bool:
        """hasGeomProp(*args, **kwargs)
        Overloaded function.

        1. hasGeomProp(self: MaterialX.PyMaterialXCore.GeomPropDef) -> bool

        2. hasGeomProp(self: MaterialX.PyMaterialXCore.GeomPropDef) -> bool
        """
    def hasIndex(self) -> bool:
        """hasIndex(self: MaterialX.PyMaterialXCore.GeomPropDef) -> bool"""
    def hasSpace(self) -> bool:
        """hasSpace(self: MaterialX.PyMaterialXCore.GeomPropDef) -> bool"""
    @overload
    def setGeomProp(self, arg0: str) -> None:
        """setGeomProp(*args, **kwargs)
        Overloaded function.

        1. setGeomProp(self: MaterialX.PyMaterialXCore.GeomPropDef, arg0: str) -> None

        2. setGeomProp(self: MaterialX.PyMaterialXCore.GeomPropDef, arg0: str) -> None
        """
    @overload
    def setGeomProp(self, arg0: str) -> None:
        """setGeomProp(*args, **kwargs)
        Overloaded function.

        1. setGeomProp(self: MaterialX.PyMaterialXCore.GeomPropDef, arg0: str) -> None

        2. setGeomProp(self: MaterialX.PyMaterialXCore.GeomPropDef, arg0: str) -> None
        """
    def setIndex(self, arg0: str) -> None:
        """setIndex(self: MaterialX.PyMaterialXCore.GeomPropDef, arg0: str) -> None"""
    def setSpace(self, arg0: str) -> None:
        """setSpace(self: MaterialX.PyMaterialXCore.GeomPropDef, arg0: str) -> None"""

class GraphElement(InterfaceElement):
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def addBackdrop(self, *args, **kwargs):
        """addBackdrop(self: MaterialX.PyMaterialXCore.GraphElement, name: str = '') -> MaterialX_v1_39_4::Backdrop"""
    def addGeomNode(self, arg0: GeomPropDef, arg1: str) -> Node:
        """addGeomNode(self: MaterialX.PyMaterialXCore.GraphElement, arg0: MaterialX.PyMaterialXCore.GeomPropDef, arg1: str) -> MaterialX.PyMaterialXCore.Node"""
    def addMaterialNode(self, name: str = ..., shaderNode: Node = ...) -> Node:
        """addMaterialNode(self: MaterialX.PyMaterialXCore.GraphElement, name: str = '', shaderNode: MaterialX.PyMaterialXCore.Node = None) -> MaterialX.PyMaterialXCore.Node"""
    def addNode(self, category: str, name: str = ..., type: str = ...) -> Node:
        """addNode(self: MaterialX.PyMaterialXCore.GraphElement, category: str, name: str = '', type: str = 'color3') -> MaterialX.PyMaterialXCore.Node"""
    def addNodeInstance(self, nodeDef: NodeDef, name: str = ...) -> Node:
        """addNodeInstance(self: MaterialX.PyMaterialXCore.GraphElement, nodeDef: MaterialX.PyMaterialXCore.NodeDef, name: str = '') -> MaterialX.PyMaterialXCore.Node"""
    def asStringDot(self) -> str:
        """asStringDot(self: MaterialX.PyMaterialXCore.GraphElement) -> str"""
    def flattenSubgraphs(self, target: str = ..., filter: Callable[[Node], bool] = ...) -> None:
        """flattenSubgraphs(self: MaterialX.PyMaterialXCore.GraphElement, target: str = '', filter: Callable[[MaterialX.PyMaterialXCore.Node], bool] = None) -> None"""
    def getBackdrop(self, *args, **kwargs):
        """getBackdrop(self: MaterialX.PyMaterialXCore.GraphElement, arg0: str) -> MaterialX_v1_39_4::Backdrop"""
    def getBackdrops(self, *args, **kwargs):
        """getBackdrops(self: MaterialX.PyMaterialXCore.GraphElement) -> list[MaterialX_v1_39_4::Backdrop]"""
    def getMaterialNodes(self) -> list[Node]:
        """getMaterialNodes(self: MaterialX.PyMaterialXCore.GraphElement) -> list[MaterialX.PyMaterialXCore.Node]"""
    def getNode(self, arg0: str) -> Node:
        """getNode(self: MaterialX.PyMaterialXCore.GraphElement, arg0: str) -> MaterialX.PyMaterialXCore.Node"""
    def getNodes(self, category: str = ...) -> list[Node]:
        """getNodes(self: MaterialX.PyMaterialXCore.GraphElement, category: str = '') -> list[MaterialX.PyMaterialXCore.Node]"""
    def removeBackdrop(self, arg0: str) -> None:
        """removeBackdrop(self: MaterialX.PyMaterialXCore.GraphElement, arg0: str) -> None"""
    def removeNode(self, arg0: str) -> None:
        """removeNode(self: MaterialX.PyMaterialXCore.GraphElement, arg0: str) -> None"""
    def topologicalSort(self) -> list[Element]:
        """topologicalSort(self: MaterialX.PyMaterialXCore.GraphElement) -> list[MaterialX.PyMaterialXCore.Element]"""

class GraphIterator:
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def getConnectingElement(self) -> Element:
        """getConnectingElement(self: MaterialX.PyMaterialXCore.GraphIterator) -> MaterialX.PyMaterialXCore.Element"""
    def getDownstreamElement(self) -> Element:
        """getDownstreamElement(self: MaterialX.PyMaterialXCore.GraphIterator) -> MaterialX.PyMaterialXCore.Element"""
    def getElementDepth(self) -> int:
        """getElementDepth(self: MaterialX.PyMaterialXCore.GraphIterator) -> int"""
    def getNodeDepth(self) -> int:
        """getNodeDepth(self: MaterialX.PyMaterialXCore.GraphIterator) -> int"""
    def getPruneSubgraph(self) -> bool:
        """getPruneSubgraph(self: MaterialX.PyMaterialXCore.GraphIterator) -> bool"""
    def getUpstreamElement(self) -> Element:
        """getUpstreamElement(self: MaterialX.PyMaterialXCore.GraphIterator) -> MaterialX.PyMaterialXCore.Element"""
    def getUpstreamIndex(self) -> int:
        """getUpstreamIndex(self: MaterialX.PyMaterialXCore.GraphIterator) -> int"""
    def setPruneSubgraph(self, arg0: bool) -> None:
        """setPruneSubgraph(self: MaterialX.PyMaterialXCore.GraphIterator, arg0: bool) -> None"""
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
        """getFile(self: MaterialX.PyMaterialXCore.Implementation) -> str"""
    def getFunction(self) -> str:
        """getFunction(self: MaterialX.PyMaterialXCore.Implementation) -> str"""
    def getNodeDef(self) -> NodeDef:
        """getNodeDef(self: MaterialX.PyMaterialXCore.Implementation) -> MaterialX.PyMaterialXCore.NodeDef"""
    def getNodeGraph(self) -> str:
        """getNodeGraph(self: MaterialX.PyMaterialXCore.Implementation) -> str"""
    def hasFile(self) -> bool:
        """hasFile(self: MaterialX.PyMaterialXCore.Implementation) -> bool"""
    def hasFunction(self) -> bool:
        """hasFunction(self: MaterialX.PyMaterialXCore.Implementation) -> bool"""
    def hasNodeGraph(self) -> bool:
        """hasNodeGraph(self: MaterialX.PyMaterialXCore.Implementation) -> bool"""
    def setFile(self, arg0: str) -> None:
        """setFile(self: MaterialX.PyMaterialXCore.Implementation, arg0: str) -> None"""
    def setFunction(self, arg0: str) -> None:
        """setFunction(self: MaterialX.PyMaterialXCore.Implementation, arg0: str) -> None"""
    def setNodeDef(self, arg0: NodeDef) -> None:
        """setNodeDef(self: MaterialX.PyMaterialXCore.Implementation, arg0: MaterialX.PyMaterialXCore.NodeDef) -> None"""
    def setNodeGraph(self, arg0: str) -> None:
        """setNodeGraph(self: MaterialX.PyMaterialXCore.Implementation, arg0: str) -> None"""

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
        """getConnectedNode(self: MaterialX.PyMaterialXCore.Input) -> MaterialX_v1_39_4::Node"""
    def getDefaultGeomProp(self, *args, **kwargs):
        """getDefaultGeomProp(self: MaterialX.PyMaterialXCore.Input) -> MaterialX_v1_39_4::GeomPropDef"""
    def getDefaultGeomPropString(self) -> str:
        """getDefaultGeomPropString(self: MaterialX.PyMaterialXCore.Input) -> str"""
    def getInterfaceInput(self) -> Input:
        """getInterfaceInput(self: MaterialX.PyMaterialXCore.Input) -> MaterialX.PyMaterialXCore.Input"""
    def hasDefaultGeomPropString(self) -> bool:
        """hasDefaultGeomPropString(self: MaterialX.PyMaterialXCore.Input) -> bool"""
    def setConnectedInterfaceName(self, arg0: str) -> None:
        """setConnectedInterfaceName(self: MaterialX.PyMaterialXCore.Input, arg0: str) -> None"""
    def setDefaultGeomPropString(self, arg0: str) -> None:
        """setDefaultGeomPropString(self: MaterialX.PyMaterialXCore.Input, arg0: str) -> None"""

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
        """addInput(self: MaterialX.PyMaterialXCore.InterfaceElement, name: str = '', type: str = 'color3') -> MaterialX.PyMaterialXCore.Input"""
    def addOutput(self, name: str = ..., type: str = ...) -> Output:
        """addOutput(self: MaterialX.PyMaterialXCore.InterfaceElement, name: str = '', type: str = 'color3') -> MaterialX.PyMaterialXCore.Output"""
    def addToken(self, name: str = ...) -> Token:
        """addToken(self: MaterialX.PyMaterialXCore.InterfaceElement, name: str = 'color3') -> MaterialX.PyMaterialXCore.Token"""
    def clearContent(self) -> None:
        """clearContent(self: MaterialX.PyMaterialXCore.InterfaceElement) -> None"""
    def getActiveInput(self, arg0: str) -> Input:
        """getActiveInput(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> MaterialX.PyMaterialXCore.Input"""
    def getActiveInputs(self) -> list[Input]:
        """getActiveInputs(self: MaterialX.PyMaterialXCore.InterfaceElement) -> list[MaterialX.PyMaterialXCore.Input]"""
    def getActiveOutput(self, arg0: str) -> Output:
        """getActiveOutput(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> MaterialX.PyMaterialXCore.Output"""
    def getActiveOutputs(self) -> list[Output]:
        """getActiveOutputs(self: MaterialX.PyMaterialXCore.InterfaceElement) -> list[MaterialX.PyMaterialXCore.Output]"""
    def getActiveToken(self, arg0: str) -> Token:
        """getActiveToken(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> MaterialX.PyMaterialXCore.Token"""
    def getActiveTokens(self) -> list[Token]:
        """getActiveTokens(self: MaterialX.PyMaterialXCore.InterfaceElement) -> list[MaterialX.PyMaterialXCore.Token]"""
    def getActiveValueElement(self, arg0: str) -> ValueElement:
        """getActiveValueElement(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> MaterialX.PyMaterialXCore.ValueElement"""
    def getActiveValueElements(self) -> list[ValueElement]:
        """getActiveValueElements(self: MaterialX.PyMaterialXCore.InterfaceElement) -> list[MaterialX.PyMaterialXCore.ValueElement]"""
    def getConnectedOutput(self, arg0: str) -> Output:
        """getConnectedOutput(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> MaterialX.PyMaterialXCore.Output"""
    def getDeclaration(self, target: str = ...) -> InterfaceElement:
        """getDeclaration(self: MaterialX.PyMaterialXCore.InterfaceElement, target: str = '') -> MaterialX.PyMaterialXCore.InterfaceElement"""
    def getDefaultVersion(self) -> bool:
        """getDefaultVersion(self: MaterialX.PyMaterialXCore.InterfaceElement) -> bool"""
    def getInput(self, arg0: str) -> Input:
        """getInput(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> MaterialX.PyMaterialXCore.Input"""
    def getInputCount(self) -> int:
        """getInputCount(self: MaterialX.PyMaterialXCore.InterfaceElement) -> int"""
    def getInputs(self) -> list[Input]:
        """getInputs(self: MaterialX.PyMaterialXCore.InterfaceElement) -> list[MaterialX.PyMaterialXCore.Input]"""
    def getNodeDefString(self) -> str:
        """getNodeDefString(self: MaterialX.PyMaterialXCore.InterfaceElement) -> str"""
    def getOutput(self, arg0: str) -> Output:
        """getOutput(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> MaterialX.PyMaterialXCore.Output"""
    def getOutputCount(self) -> int:
        """getOutputCount(self: MaterialX.PyMaterialXCore.InterfaceElement) -> int"""
    def getOutputs(self) -> list[Output]:
        """getOutputs(self: MaterialX.PyMaterialXCore.InterfaceElement) -> list[MaterialX.PyMaterialXCore.Output]"""
    def getTarget(self) -> str:
        """getTarget(self: MaterialX.PyMaterialXCore.InterfaceElement) -> str"""
    def getToken(self, arg0: str) -> Token:
        """getToken(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> MaterialX.PyMaterialXCore.Token"""
    def getTokenValue(self, arg0: str) -> str:
        """getTokenValue(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> str"""
    def getTokens(self) -> list[Token]:
        """getTokens(self: MaterialX.PyMaterialXCore.InterfaceElement) -> list[MaterialX.PyMaterialXCore.Token]"""
    def getVersionIntegers(self) -> tuple[int, int]:
        """getVersionIntegers(self: MaterialX.PyMaterialXCore.InterfaceElement) -> tuple[int, int]"""
    def getVersionString(self) -> str:
        """getVersionString(self: MaterialX.PyMaterialXCore.InterfaceElement) -> str"""
    def hasExactInputMatch(self, declaration: InterfaceElement, message: str = ...) -> bool:
        """hasExactInputMatch(self: MaterialX.PyMaterialXCore.InterfaceElement, declaration: MaterialX.PyMaterialXCore.InterfaceElement, message: str = None) -> bool"""
    def hasNodeDefString(self) -> bool:
        """hasNodeDefString(self: MaterialX.PyMaterialXCore.InterfaceElement) -> bool"""
    def hasTarget(self) -> bool:
        """hasTarget(self: MaterialX.PyMaterialXCore.InterfaceElement) -> bool"""
    def hasVersionString(self) -> bool:
        """hasVersionString(self: MaterialX.PyMaterialXCore.InterfaceElement) -> bool"""
    def removeInput(self, arg0: str) -> None:
        """removeInput(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> None"""
    def removeOutput(self, arg0: str) -> None:
        """removeOutput(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> None"""
    def removeToken(self, arg0: str) -> None:
        """removeToken(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> None"""
    def setConnectedOutput(self, arg0: str, arg1: Output) -> None:
        """setConnectedOutput(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str, arg1: MaterialX.PyMaterialXCore.Output) -> None"""
    def setDefaultVersion(self, arg0: bool) -> None:
        """setDefaultVersion(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: bool) -> None"""
    def setNodeDefString(self, arg0: str) -> None:
        """setNodeDefString(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> None"""
    def setTarget(self, arg0: str) -> None:
        """setTarget(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> None"""
    def setTokenValue(self, arg0: str, arg1: str) -> Token:
        """setTokenValue(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str, arg1: str) -> MaterialX.PyMaterialXCore.Token"""
    def setVersionIntegers(self, arg0: int, arg1: int) -> None:
        """setVersionIntegers(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: int, arg1: int) -> None"""
    def setVersionString(self, arg0: str) -> None:
        """setVersionString(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> None"""

class LinearUnitConverter(UnitConverter):
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @overload
    def convert(self, arg0: float, arg1: str, arg2: str) -> float:
        """convert(*args, **kwargs)
        Overloaded function.

        1. convert(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: float, arg1: str, arg2: str) -> float

        2. convert(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: MaterialX.PyMaterialXCore.Vector2, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector2

        3. convert(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: MaterialX.PyMaterialXCore.Vector3, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector3

        4. convert(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: MaterialX.PyMaterialXCore.Vector4, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector4
        """
    @overload
    def convert(self, arg0: Vector2, arg1: str, arg2: str) -> Vector2:
        """convert(*args, **kwargs)
        Overloaded function.

        1. convert(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: float, arg1: str, arg2: str) -> float

        2. convert(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: MaterialX.PyMaterialXCore.Vector2, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector2

        3. convert(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: MaterialX.PyMaterialXCore.Vector3, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector3

        4. convert(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: MaterialX.PyMaterialXCore.Vector4, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector4
        """
    @overload
    def convert(self, arg0: Vector3, arg1: str, arg2: str) -> Vector3:
        """convert(*args, **kwargs)
        Overloaded function.

        1. convert(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: float, arg1: str, arg2: str) -> float

        2. convert(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: MaterialX.PyMaterialXCore.Vector2, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector2

        3. convert(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: MaterialX.PyMaterialXCore.Vector3, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector3

        4. convert(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: MaterialX.PyMaterialXCore.Vector4, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector4
        """
    @overload
    def convert(self, arg0: Vector4, arg1: str, arg2: str) -> Vector4:
        """convert(*args, **kwargs)
        Overloaded function.

        1. convert(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: float, arg1: str, arg2: str) -> float

        2. convert(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: MaterialX.PyMaterialXCore.Vector2, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector2

        3. convert(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: MaterialX.PyMaterialXCore.Vector3, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector3

        4. convert(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: MaterialX.PyMaterialXCore.Vector4, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector4
        """
    @staticmethod
    def create(arg0: UnitTypeDef) -> LinearUnitConverter:
        """create(arg0: MaterialX.PyMaterialXCore.UnitTypeDef) -> MaterialX.PyMaterialXCore.LinearUnitConverter"""
    def getUnitAsInteger(self, arg0: str) -> int:
        """getUnitAsInteger(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: str) -> int"""
    def getUnitFromInteger(self, arg0: int) -> str:
        """getUnitFromInteger(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: int) -> str"""
    def getUnitScale(self) -> dict[str, float]:
        """getUnitScale(self: MaterialX.PyMaterialXCore.LinearUnitConverter) -> dict[str, float]"""

class Look(Element):
    CATEGORY: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def addMaterialAssign(self, *args, **kwargs):
        """addMaterialAssign(self: MaterialX.PyMaterialXCore.Look, name: str = '', material: str = '') -> MaterialX_v1_39_4::MaterialAssign"""
    def addPropertyAssign(self, name: str = ...) -> PropertyAssign:
        """addPropertyAssign(self: MaterialX.PyMaterialXCore.Look, name: str = '') -> MaterialX.PyMaterialXCore.PropertyAssign"""
    def addPropertySetAssign(self, name: str = ...) -> PropertySetAssign:
        """addPropertySetAssign(self: MaterialX.PyMaterialXCore.Look, name: str = '') -> MaterialX.PyMaterialXCore.PropertySetAssign"""
    def addVariantAssign(self, *args, **kwargs):
        """addVariantAssign(self: MaterialX.PyMaterialXCore.Look, name: str = '') -> MaterialX_v1_39_4::VariantAssign"""
    def addVisibility(self, *args, **kwargs):
        """addVisibility(self: MaterialX.PyMaterialXCore.Look, name: str = '') -> MaterialX_v1_39_4::Visibility"""
    def getActiveMaterialAssigns(self, *args, **kwargs):
        """getActiveMaterialAssigns(self: MaterialX.PyMaterialXCore.Look) -> list[MaterialX_v1_39_4::MaterialAssign]"""
    def getActivePropertyAssigns(self) -> list[PropertyAssign]:
        """getActivePropertyAssigns(self: MaterialX.PyMaterialXCore.Look) -> list[MaterialX.PyMaterialXCore.PropertyAssign]"""
    def getActivePropertySetAssigns(self) -> list[PropertySetAssign]:
        """getActivePropertySetAssigns(self: MaterialX.PyMaterialXCore.Look) -> list[MaterialX.PyMaterialXCore.PropertySetAssign]"""
    def getActiveVariantAssigns(self, *args, **kwargs):
        """getActiveVariantAssigns(self: MaterialX.PyMaterialXCore.Look) -> list[MaterialX_v1_39_4::VariantAssign]"""
    def getActiveVisibilities(self, *args, **kwargs):
        """getActiveVisibilities(self: MaterialX.PyMaterialXCore.Look) -> list[MaterialX_v1_39_4::Visibility]"""
    def getMaterialAssign(self, *args, **kwargs):
        """getMaterialAssign(self: MaterialX.PyMaterialXCore.Look, arg0: str) -> MaterialX_v1_39_4::MaterialAssign"""
    def getMaterialAssigns(self, *args, **kwargs):
        """getMaterialAssigns(self: MaterialX.PyMaterialXCore.Look) -> list[MaterialX_v1_39_4::MaterialAssign]"""
    def getPropertyAssign(self, arg0: str) -> PropertyAssign:
        """getPropertyAssign(self: MaterialX.PyMaterialXCore.Look, arg0: str) -> MaterialX.PyMaterialXCore.PropertyAssign"""
    def getPropertyAssigns(self) -> list[PropertyAssign]:
        """getPropertyAssigns(self: MaterialX.PyMaterialXCore.Look) -> list[MaterialX.PyMaterialXCore.PropertyAssign]"""
    def getPropertySetAssign(self, arg0: str) -> PropertySetAssign:
        """getPropertySetAssign(self: MaterialX.PyMaterialXCore.Look, arg0: str) -> MaterialX.PyMaterialXCore.PropertySetAssign"""
    def getPropertySetAssigns(self) -> list[PropertySetAssign]:
        """getPropertySetAssigns(self: MaterialX.PyMaterialXCore.Look) -> list[MaterialX.PyMaterialXCore.PropertySetAssign]"""
    def getVariantAssign(self, *args, **kwargs):
        """getVariantAssign(self: MaterialX.PyMaterialXCore.Look, arg0: str) -> MaterialX_v1_39_4::VariantAssign"""
    def getVariantAssigns(self, *args, **kwargs):
        """getVariantAssigns(self: MaterialX.PyMaterialXCore.Look) -> list[MaterialX_v1_39_4::VariantAssign]"""
    def getVisibilities(self, *args, **kwargs):
        """getVisibilities(self: MaterialX.PyMaterialXCore.Look) -> list[MaterialX_v1_39_4::Visibility]"""
    def getVisibility(self, *args, **kwargs):
        """getVisibility(self: MaterialX.PyMaterialXCore.Look, arg0: str) -> MaterialX_v1_39_4::Visibility"""
    def removeMaterialAssign(self, arg0: str) -> None:
        """removeMaterialAssign(self: MaterialX.PyMaterialXCore.Look, arg0: str) -> None"""
    def removePropertyAssign(self, arg0: str) -> None:
        """removePropertyAssign(self: MaterialX.PyMaterialXCore.Look, arg0: str) -> None"""
    def removePropertySetAssign(self, arg0: str) -> None:
        """removePropertySetAssign(self: MaterialX.PyMaterialXCore.Look, arg0: str) -> None"""
    def removeVariantAssign(self, arg0: str) -> None:
        """removeVariantAssign(self: MaterialX.PyMaterialXCore.Look, arg0: str) -> None"""
    def removeVisibility(self, arg0: str) -> None:
        """removeVisibility(self: MaterialX.PyMaterialXCore.Look, arg0: str) -> None"""

class LookGroup(Element):
    ACTIVE_ATTRIBUTE: ClassVar[str] = ...  # read-only
    CATEGORY: ClassVar[str] = ...  # read-only
    LOOKS_ATTRIBUTE: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def getActiveLook(self) -> str:
        """getActiveLook(self: MaterialX.PyMaterialXCore.LookGroup) -> str"""
    def getLooks(self) -> str:
        """getLooks(self: MaterialX.PyMaterialXCore.LookGroup) -> str"""
    def setActiveLook(self, arg0: str) -> None:
        """setActiveLook(self: MaterialX.PyMaterialXCore.LookGroup, arg0: str) -> None"""
    def setLooks(self, arg0: str) -> None:
        """setLooks(self: MaterialX.PyMaterialXCore.LookGroup, arg0: str) -> None"""

class MaterialAssign(GeomElement):
    CATEGORY: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def getExclusive(self) -> bool:
        """getExclusive(self: MaterialX.PyMaterialXCore.MaterialAssign) -> bool"""
    def getMaterial(self) -> str:
        """getMaterial(self: MaterialX.PyMaterialXCore.MaterialAssign) -> str"""
    def getMaterialOutputs(self) -> list[Output]:
        """getMaterialOutputs(self: MaterialX.PyMaterialXCore.MaterialAssign) -> list[MaterialX.PyMaterialXCore.Output]"""
    def getReferencedMaterial(self, *args, **kwargs):
        """getReferencedMaterial(self: MaterialX.PyMaterialXCore.MaterialAssign) -> MaterialX_v1_39_4::Node"""
    def hasMaterial(self) -> bool:
        """hasMaterial(self: MaterialX.PyMaterialXCore.MaterialAssign) -> bool"""
    def setExclusive(self, arg0: bool) -> None:
        """setExclusive(self: MaterialX.PyMaterialXCore.MaterialAssign, arg0: bool) -> None"""
    def setMaterial(self, arg0: str) -> None:
        """setMaterial(self: MaterialX.PyMaterialXCore.MaterialAssign, arg0: str) -> None"""

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
        """copy(self: MaterialX.PyMaterialXCore.Matrix33) -> MaterialX.PyMaterialXCore.Matrix33"""
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
        """getAdjugate(self: MaterialX.PyMaterialXCore.Matrix33) -> MaterialX.PyMaterialXCore.Matrix33"""
    def getDeterminant(self) -> float:
        """getDeterminant(self: MaterialX.PyMaterialXCore.Matrix33) -> float"""
    def getInverse(self) -> Matrix33:
        """getInverse(self: MaterialX.PyMaterialXCore.Matrix33) -> MaterialX.PyMaterialXCore.Matrix33"""
    def getTranspose(self) -> Matrix33:
        """getTranspose(self: MaterialX.PyMaterialXCore.Matrix33) -> MaterialX.PyMaterialXCore.Matrix33"""
    def isEquivalent(self, arg0: Matrix33, arg1: float) -> bool:
        """isEquivalent(self: MaterialX.PyMaterialXCore.Matrix33, arg0: MaterialX.PyMaterialXCore.Matrix33, arg1: float) -> bool"""
    def multiply(self, arg0: Vector3) -> Vector3:
        """multiply(self: MaterialX.PyMaterialXCore.Matrix33, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3"""
    @staticmethod
    def numColumns() -> int:
        """numColumns() -> int"""
    @staticmethod
    def numRows() -> int:
        """numRows() -> int"""
    def transformNormal(self, arg0: Vector3) -> Vector3:
        """transformNormal(self: MaterialX.PyMaterialXCore.Matrix33, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3"""
    def transformPoint(self, arg0: Vector2) -> Vector2:
        """transformPoint(self: MaterialX.PyMaterialXCore.Matrix33, arg0: MaterialX.PyMaterialXCore.Vector2) -> MaterialX.PyMaterialXCore.Vector2"""
    def transformVector(self, arg0: Vector2) -> Vector2:
        """transformVector(self: MaterialX.PyMaterialXCore.Matrix33, arg0: MaterialX.PyMaterialXCore.Vector2) -> MaterialX.PyMaterialXCore.Vector2"""
    def __add__(self, arg0: Matrix33) -> Matrix33:
        """__add__(self: MaterialX.PyMaterialXCore.Matrix33, arg0: MaterialX.PyMaterialXCore.Matrix33) -> MaterialX.PyMaterialXCore.Matrix33"""
    def __eq__(self, arg0: Matrix33) -> bool:
        """__eq__(self: MaterialX.PyMaterialXCore.Matrix33, arg0: MaterialX.PyMaterialXCore.Matrix33) -> bool"""
    def __getitem__(self, arg0: tuple[int, int]) -> float:
        """__getitem__(self: MaterialX.PyMaterialXCore.Matrix33, arg0: tuple[int, int]) -> float"""
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
        """copy(self: MaterialX.PyMaterialXCore.Matrix44) -> MaterialX.PyMaterialXCore.Matrix44"""
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
        """getAdjugate(self: MaterialX.PyMaterialXCore.Matrix44) -> MaterialX.PyMaterialXCore.Matrix44"""
    def getDeterminant(self) -> float:
        """getDeterminant(self: MaterialX.PyMaterialXCore.Matrix44) -> float"""
    def getInverse(self) -> Matrix44:
        """getInverse(self: MaterialX.PyMaterialXCore.Matrix44) -> MaterialX.PyMaterialXCore.Matrix44"""
    def getTranspose(self) -> Matrix44:
        """getTranspose(self: MaterialX.PyMaterialXCore.Matrix44) -> MaterialX.PyMaterialXCore.Matrix44"""
    def isEquivalent(self, arg0: Matrix44, arg1: float) -> bool:
        """isEquivalent(self: MaterialX.PyMaterialXCore.Matrix44, arg0: MaterialX.PyMaterialXCore.Matrix44, arg1: float) -> bool"""
    def multiply(self, arg0: Vector4) -> Vector4:
        """multiply(self: MaterialX.PyMaterialXCore.Matrix44, arg0: MaterialX.PyMaterialXCore.Vector4) -> MaterialX.PyMaterialXCore.Vector4"""
    @staticmethod
    def numColumns() -> int:
        """numColumns() -> int"""
    @staticmethod
    def numRows() -> int:
        """numRows() -> int"""
    def transformNormal(self, arg0: Vector3) -> Vector3:
        """transformNormal(self: MaterialX.PyMaterialXCore.Matrix44, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3"""
    def transformPoint(self, arg0: Vector3) -> Vector3:
        """transformPoint(self: MaterialX.PyMaterialXCore.Matrix44, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3"""
    def transformVector(self, arg0: Vector3) -> Vector3:
        """transformVector(self: MaterialX.PyMaterialXCore.Matrix44, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3"""
    def __add__(self, arg0: Matrix44) -> Matrix44:
        """__add__(self: MaterialX.PyMaterialXCore.Matrix44, arg0: MaterialX.PyMaterialXCore.Matrix44) -> MaterialX.PyMaterialXCore.Matrix44"""
    def __eq__(self, arg0: Matrix44) -> bool:
        """__eq__(self: MaterialX.PyMaterialXCore.Matrix44, arg0: MaterialX.PyMaterialXCore.Matrix44) -> bool"""
    def __getitem__(self, arg0: tuple[int, int]) -> float:
        """__getitem__(self: MaterialX.PyMaterialXCore.Matrix44, arg0: tuple[int, int]) -> float"""
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
        """addInputFromNodeDef(self: MaterialX.PyMaterialXCore.Node, arg0: str) -> MaterialX.PyMaterialXCore.Input"""
    def addInputsFromNodeDef(self) -> None:
        """addInputsFromNodeDef(self: MaterialX.PyMaterialXCore.Node) -> None"""
    def getConnectedNode(self, arg0: str) -> Node:
        """getConnectedNode(self: MaterialX.PyMaterialXCore.Node, arg0: str) -> MaterialX.PyMaterialXCore.Node"""
    def getConnectedNodeName(self, arg0: str) -> str:
        """getConnectedNodeName(self: MaterialX.PyMaterialXCore.Node, arg0: str) -> str"""
    def getDownstreamPorts(self) -> list[PortElement]:
        """getDownstreamPorts(self: MaterialX.PyMaterialXCore.Node) -> list[MaterialX.PyMaterialXCore.PortElement]"""
    def getImplementation(self, target: str = ...) -> InterfaceElement:
        """getImplementation(self: MaterialX.PyMaterialXCore.Node, target: str = '') -> MaterialX.PyMaterialXCore.InterfaceElement"""
    def getNodeDef(self, target: str = ..., allowRoughMatch: bool = ...) -> NodeDef:
        """getNodeDef(self: MaterialX.PyMaterialXCore.Node, target: str = '', allowRoughMatch: bool = False) -> MaterialX.PyMaterialXCore.NodeDef"""
    def setConnectedNode(self, arg0: str, arg1: Node) -> None:
        """setConnectedNode(self: MaterialX.PyMaterialXCore.Node, arg0: str, arg1: MaterialX.PyMaterialXCore.Node) -> None"""
    def setConnectedNodeName(self, arg0: str, arg1: str) -> None:
        """setConnectedNodeName(self: MaterialX.PyMaterialXCore.Node, arg0: str, arg1: str) -> None"""

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

        2. getImplementation(self: MaterialX.PyMaterialXCore.NodeDef, target: str = '') -> MaterialX.PyMaterialXCore.InterfaceElement
        """
    @overload
    def getImplementation(self, target: str = ...) -> InterfaceElement:
        """getImplementation(*args, **kwargs)
        Overloaded function.

        1. getImplementation(self: MaterialX.PyMaterialXCore.NodeDef, arg0: str) -> MaterialX.PyMaterialXCore.InterfaceElement

        2. getImplementation(self: MaterialX.PyMaterialXCore.NodeDef, target: str = '') -> MaterialX.PyMaterialXCore.InterfaceElement
        """
    def getNodeGroup(self) -> str:
        """getNodeGroup(self: MaterialX.PyMaterialXCore.NodeDef) -> str"""
    def getNodeString(self) -> str:
        """getNodeString(self: MaterialX.PyMaterialXCore.NodeDef) -> str"""
    def hasNodeGroup(self) -> bool:
        """hasNodeGroup(self: MaterialX.PyMaterialXCore.NodeDef) -> bool"""
    def hasNodeString(self) -> bool:
        """hasNodeString(self: MaterialX.PyMaterialXCore.NodeDef) -> bool"""
    def isVersionCompatible(self, arg0: str) -> bool:
        """isVersionCompatible(self: MaterialX.PyMaterialXCore.NodeDef, arg0: str) -> bool"""
    def setNodeGroup(self, arg0: str) -> None:
        """setNodeGroup(self: MaterialX.PyMaterialXCore.NodeDef, arg0: str) -> None"""
    def setNodeString(self, arg0: str) -> None:
        """setNodeString(self: MaterialX.PyMaterialXCore.NodeDef, arg0: str) -> None"""

class NodeGraph(GraphElement):
    CATEGORY: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def addInterfaceName(self, arg0: str, arg1: str) -> Input:
        """addInterfaceName(self: MaterialX.PyMaterialXCore.NodeGraph, arg0: str, arg1: str) -> MaterialX.PyMaterialXCore.Input"""
    def getDeclaration(self, arg0: str) -> InterfaceElement:
        """getDeclaration(self: MaterialX.PyMaterialXCore.NodeGraph, arg0: str) -> MaterialX.PyMaterialXCore.InterfaceElement"""
    def getDownstreamPorts(self) -> list[PortElement]:
        """getDownstreamPorts(self: MaterialX.PyMaterialXCore.NodeGraph) -> list[MaterialX.PyMaterialXCore.PortElement]"""
    def getMaterialOutputs(self) -> list[Output]:
        """getMaterialOutputs(self: MaterialX.PyMaterialXCore.NodeGraph) -> list[MaterialX.PyMaterialXCore.Output]"""
    def getNodeDef(self) -> NodeDef:
        """getNodeDef(self: MaterialX.PyMaterialXCore.NodeGraph) -> MaterialX.PyMaterialXCore.NodeDef"""
    def modifyInterfaceName(self, arg0: str, arg1: str) -> None:
        """modifyInterfaceName(self: MaterialX.PyMaterialXCore.NodeGraph, arg0: str, arg1: str) -> None"""
    def removeInterfaceName(self, arg0: str) -> None:
        """removeInterfaceName(self: MaterialX.PyMaterialXCore.NodeGraph, arg0: str) -> None"""
    def setNodeDef(self, arg0: NodeDef) -> None:
        """setNodeDef(self: MaterialX.PyMaterialXCore.NodeGraph, arg0: MaterialX.PyMaterialXCore.NodeDef) -> None"""

class NodePredicate:
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class Output(PortElement):
    CATEGORY: ClassVar[str] = ...  # read-only
    DEFAULT_INPUT_ATTRIBUTE: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def hasUpstreamCycle(self) -> bool:
        """hasUpstreamCycle(self: MaterialX.PyMaterialXCore.Output) -> bool"""

class PortElement(ValueElement):
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def getConnectedNode(self, *args, **kwargs):
        """getConnectedNode(self: MaterialX.PyMaterialXCore.PortElement) -> MaterialX_v1_39_4::Node"""
    def getConnectedOutput(self, *args, **kwargs):
        """getConnectedOutput(self: MaterialX.PyMaterialXCore.PortElement) -> MaterialX_v1_39_4::Output"""
    def getNodeGraphString(self) -> str:
        """getNodeGraphString(self: MaterialX.PyMaterialXCore.PortElement) -> str"""
    def getNodeName(self) -> str:
        """getNodeName(self: MaterialX.PyMaterialXCore.PortElement) -> str"""
    def getOutputString(self) -> str:
        """getOutputString(self: MaterialX.PyMaterialXCore.PortElement) -> str"""
    def hasNodeGraphString(self) -> bool:
        """hasNodeGraphString(self: MaterialX.PyMaterialXCore.PortElement) -> bool"""
    def hasOutputString(self) -> bool:
        """hasOutputString(self: MaterialX.PyMaterialXCore.PortElement) -> bool"""
    def setConnectedNode(self, arg0) -> None:
        """setConnectedNode(self: MaterialX.PyMaterialXCore.PortElement, arg0: MaterialX_v1_39_4::Node) -> None"""
    def setConnectedOutput(self, arg0) -> None:
        """setConnectedOutput(self: MaterialX.PyMaterialXCore.PortElement, arg0: MaterialX_v1_39_4::Output) -> None"""
    def setNodeGraphString(self, arg0: str) -> None:
        """setNodeGraphString(self: MaterialX.PyMaterialXCore.PortElement, arg0: str) -> None"""
    def setNodeName(self, arg0: str) -> None:
        """setNodeName(self: MaterialX.PyMaterialXCore.PortElement, arg0: str) -> None"""
    def setOutputString(self, arg0: str) -> None:
        """setOutputString(self: MaterialX.PyMaterialXCore.PortElement, arg0: str) -> None"""

class Property(ValueElement):
    CATEGORY: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class PropertyAssign(ValueElement):
    CATEGORY: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def getCollection(self) -> Collection:
        """getCollection(self: MaterialX.PyMaterialXCore.PropertyAssign) -> MaterialX.PyMaterialXCore.Collection"""
    def getCollectionString(self) -> str:
        """getCollectionString(self: MaterialX.PyMaterialXCore.PropertyAssign) -> str"""
    def getGeom(self) -> str:
        """getGeom(self: MaterialX.PyMaterialXCore.PropertyAssign) -> str"""
    def getProperty(self) -> str:
        """getProperty(self: MaterialX.PyMaterialXCore.PropertyAssign) -> str"""
    def hasCollectionString(self) -> bool:
        """hasCollectionString(self: MaterialX.PyMaterialXCore.PropertyAssign) -> bool"""
    def hasGeom(self) -> bool:
        """hasGeom(self: MaterialX.PyMaterialXCore.PropertyAssign) -> bool"""
    def hasProperty(self) -> bool:
        """hasProperty(self: MaterialX.PyMaterialXCore.PropertyAssign) -> bool"""
    def setCollection(self, arg0: Collection) -> None:
        """setCollection(self: MaterialX.PyMaterialXCore.PropertyAssign, arg0: MaterialX.PyMaterialXCore.Collection) -> None"""
    def setCollectionString(self, arg0: str) -> None:
        """setCollectionString(self: MaterialX.PyMaterialXCore.PropertyAssign, arg0: str) -> None"""
    def setGeom(self, arg0: str) -> None:
        """setGeom(self: MaterialX.PyMaterialXCore.PropertyAssign, arg0: str) -> None"""
    def setProperty(self, arg0: str) -> None:
        """setProperty(self: MaterialX.PyMaterialXCore.PropertyAssign, arg0: str) -> None"""

class PropertySet(Element):
    CATEGORY: ClassVar[str] = ...  # read-only
    getPropertyValue: ClassVar[Callable] = ...
    setPropertyValue: ClassVar[Callable] = ...
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def addProperty(self, arg0: str) -> Property:
        """addProperty(self: MaterialX.PyMaterialXCore.PropertySet, arg0: str) -> MaterialX.PyMaterialXCore.Property"""
    def getProperties(self) -> list[Property]:
        """getProperties(self: MaterialX.PyMaterialXCore.PropertySet) -> list[MaterialX.PyMaterialXCore.Property]"""
    def removeProperty(self, arg0: str) -> None:
        """removeProperty(self: MaterialX.PyMaterialXCore.PropertySet, arg0: str) -> None"""

class PropertySetAssign(GeomElement):
    CATEGORY: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def getPropertySet(self) -> PropertySet:
        """getPropertySet(self: MaterialX.PyMaterialXCore.PropertySetAssign) -> MaterialX.PyMaterialXCore.PropertySet"""
    def getPropertySetString(self) -> str:
        """getPropertySetString(self: MaterialX.PyMaterialXCore.PropertySetAssign) -> str"""
    def hasPropertySetString(self) -> bool:
        """hasPropertySetString(self: MaterialX.PyMaterialXCore.PropertySetAssign) -> bool"""
    def setPropertySet(self, arg0: PropertySet) -> None:
        """setPropertySet(self: MaterialX.PyMaterialXCore.PropertySetAssign, arg0: MaterialX.PyMaterialXCore.PropertySet) -> None"""
    def setPropertySetString(self, arg0: str) -> None:
        """setPropertySetString(self: MaterialX.PyMaterialXCore.PropertySetAssign, arg0: str) -> None"""

class StringResolver:
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def getFilePrefix(self) -> str:
        """getFilePrefix(self: MaterialX.PyMaterialXCore.StringResolver) -> str"""
    def getFilenameSubstitutions(self) -> dict[str, str]:
        """getFilenameSubstitutions(self: MaterialX.PyMaterialXCore.StringResolver) -> dict[str, str]"""
    def getGeomNameSubstitutions(self) -> dict[str, str]:
        """getGeomNameSubstitutions(self: MaterialX.PyMaterialXCore.StringResolver) -> dict[str, str]"""
    def getGeomPrefix(self) -> str:
        """getGeomPrefix(self: MaterialX.PyMaterialXCore.StringResolver) -> str"""
    def resolve(self, arg0: str, arg1: str) -> str:
        """resolve(self: MaterialX.PyMaterialXCore.StringResolver, arg0: str, arg1: str) -> str"""
    def setFilePrefix(self, arg0: str) -> None:
        """setFilePrefix(self: MaterialX.PyMaterialXCore.StringResolver, arg0: str) -> None"""
    def setFilenameSubstitution(self, arg0: str, arg1: str) -> None:
        """setFilenameSubstitution(self: MaterialX.PyMaterialXCore.StringResolver, arg0: str, arg1: str) -> None"""
    def setGeomNameSubstitution(self, arg0: str, arg1: str) -> None:
        """setGeomNameSubstitution(self: MaterialX.PyMaterialXCore.StringResolver, arg0: str, arg1: str) -> None"""
    def setGeomPrefix(self, arg0: str) -> None:
        """setGeomPrefix(self: MaterialX.PyMaterialXCore.StringResolver, arg0: str) -> None"""
    def setUdimString(self, arg0: str) -> None:
        """setUdimString(self: MaterialX.PyMaterialXCore.StringResolver, arg0: str) -> None"""
    def setUvTileString(self, arg0: str) -> None:
        """setUvTileString(self: MaterialX.PyMaterialXCore.StringResolver, arg0: str) -> None"""

class TargetDef(TypedElement):
    CATEGORY: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def getMatchingTargets(self) -> list[str]:
        """getMatchingTargets(self: MaterialX.PyMaterialXCore.TargetDef) -> list[str]"""

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
        """getElementDepth(self: MaterialX.PyMaterialXCore.TreeIterator) -> int"""
    def getPruneSubtree(self) -> bool:
        """getPruneSubtree(self: MaterialX.PyMaterialXCore.TreeIterator) -> bool"""
    def setPruneSubtree(self, arg0: bool) -> None:
        """setPruneSubtree(self: MaterialX.PyMaterialXCore.TreeIterator, arg0: bool) -> None"""
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
        """addMember(self: MaterialX.PyMaterialXCore.TypeDef, name: str = '') -> MaterialX_v1_39_4::Member"""
    def getContext(self) -> str:
        """getContext(self: MaterialX.PyMaterialXCore.TypeDef) -> str"""
    def getMember(self, *args, **kwargs):
        """getMember(self: MaterialX.PyMaterialXCore.TypeDef, arg0: str) -> MaterialX_v1_39_4::Member"""
    def getMembers(self, *args, **kwargs):
        """getMembers(self: MaterialX.PyMaterialXCore.TypeDef) -> list[MaterialX_v1_39_4::Member]"""
    def getSemantic(self) -> str:
        """getSemantic(self: MaterialX.PyMaterialXCore.TypeDef) -> str"""
    def hasContext(self) -> bool:
        """hasContext(self: MaterialX.PyMaterialXCore.TypeDef) -> bool"""
    def hasSemantic(self) -> bool:
        """hasSemantic(self: MaterialX.PyMaterialXCore.TypeDef) -> bool"""
    def removeMember(self, arg0: str) -> None:
        """removeMember(self: MaterialX.PyMaterialXCore.TypeDef, arg0: str) -> None"""
    def setContext(self, arg0: str) -> None:
        """setContext(self: MaterialX.PyMaterialXCore.TypeDef, arg0: str) -> None"""
    def setSemantic(self, arg0: str) -> None:
        """setSemantic(self: MaterialX.PyMaterialXCore.TypeDef, arg0: str) -> None"""

class TypedElement(Element):
    TYPE_ATTRIBUTE: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def getType(self) -> str:
        """getType(self: MaterialX.PyMaterialXCore.TypedElement) -> str"""
    def getTypeDef(self, *args, **kwargs):
        """getTypeDef(self: MaterialX.PyMaterialXCore.TypedElement) -> MaterialX_v1_39_4::TypeDef"""
    def hasType(self) -> bool:
        """hasType(self: MaterialX.PyMaterialXCore.TypedElement) -> bool"""
    def isColorType(self) -> bool:
        """isColorType(self: MaterialX.PyMaterialXCore.TypedElement) -> bool"""
    def isMultiOutputType(self) -> bool:
        """isMultiOutputType(self: MaterialX.PyMaterialXCore.TypedElement) -> bool"""
    def setType(self, arg0: str) -> None:
        """setType(self: MaterialX.PyMaterialXCore.TypedElement, arg0: str) -> None"""

class TypedValue_boolean(Value):
    TYPE: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def createValue(arg0: bool) -> Value:
        """createValue(arg0: bool) -> MaterialX.PyMaterialXCore.Value"""
    def getData(self) -> bool:
        """getData(self: MaterialX.PyMaterialXCore.TypedValue_boolean) -> bool"""
    def getValueString(self) -> str:
        """getValueString(self: MaterialX.PyMaterialXCore.TypedValue_boolean) -> str"""

class TypedValue_booleanarray(Value):
    TYPE: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def createValue(arg0: list[bool]) -> Value:
        """createValue(arg0: list[bool]) -> MaterialX.PyMaterialXCore.Value"""
    def getData(self) -> list[bool]:
        """getData(self: MaterialX.PyMaterialXCore.TypedValue_booleanarray) -> list[bool]"""
    def getValueString(self) -> str:
        """getValueString(self: MaterialX.PyMaterialXCore.TypedValue_booleanarray) -> str"""

class TypedValue_color3(Value):
    TYPE: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def createValue(arg0) -> Value:
        """createValue(arg0: MaterialX_v1_39_4::Color3) -> MaterialX.PyMaterialXCore.Value"""
    def getData(self, *args, **kwargs):
        """getData(self: MaterialX.PyMaterialXCore.TypedValue_color3) -> MaterialX_v1_39_4::Color3"""
    def getValueString(self) -> str:
        """getValueString(self: MaterialX.PyMaterialXCore.TypedValue_color3) -> str"""

class TypedValue_color4(Value):
    TYPE: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def createValue(arg0) -> Value:
        """createValue(arg0: MaterialX_v1_39_4::Color4) -> MaterialX.PyMaterialXCore.Value"""
    def getData(self, *args, **kwargs):
        """getData(self: MaterialX.PyMaterialXCore.TypedValue_color4) -> MaterialX_v1_39_4::Color4"""
    def getValueString(self) -> str:
        """getValueString(self: MaterialX.PyMaterialXCore.TypedValue_color4) -> str"""

class TypedValue_float(Value):
    TYPE: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def createValue(arg0: float) -> Value:
        """createValue(arg0: float) -> MaterialX.PyMaterialXCore.Value"""
    def getData(self) -> float:
        """getData(self: MaterialX.PyMaterialXCore.TypedValue_float) -> float"""
    def getValueString(self) -> str:
        """getValueString(self: MaterialX.PyMaterialXCore.TypedValue_float) -> str"""

class TypedValue_floatarray(Value):
    TYPE: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def createValue(arg0: list[float]) -> Value:
        """createValue(arg0: list[float]) -> MaterialX.PyMaterialXCore.Value"""
    def getData(self) -> list[float]:
        """getData(self: MaterialX.PyMaterialXCore.TypedValue_floatarray) -> list[float]"""
    def getValueString(self) -> str:
        """getValueString(self: MaterialX.PyMaterialXCore.TypedValue_floatarray) -> str"""

class TypedValue_integer(Value):
    TYPE: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def createValue(arg0: int) -> Value:
        """createValue(arg0: int) -> MaterialX.PyMaterialXCore.Value"""
    def getData(self) -> int:
        """getData(self: MaterialX.PyMaterialXCore.TypedValue_integer) -> int"""
    def getValueString(self) -> str:
        """getValueString(self: MaterialX.PyMaterialXCore.TypedValue_integer) -> str"""

class TypedValue_integerarray(Value):
    TYPE: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def createValue(arg0: list[int]) -> Value:
        """createValue(arg0: list[int]) -> MaterialX.PyMaterialXCore.Value"""
    def getData(self) -> list[int]:
        """getData(self: MaterialX.PyMaterialXCore.TypedValue_integerarray) -> list[int]"""
    def getValueString(self) -> str:
        """getValueString(self: MaterialX.PyMaterialXCore.TypedValue_integerarray) -> str"""

class TypedValue_matrix33(Value):
    TYPE: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def createValue(arg0) -> Value:
        """createValue(arg0: MaterialX_v1_39_4::Matrix33) -> MaterialX.PyMaterialXCore.Value"""
    def getData(self, *args, **kwargs):
        """getData(self: MaterialX.PyMaterialXCore.TypedValue_matrix33) -> MaterialX_v1_39_4::Matrix33"""
    def getValueString(self) -> str:
        """getValueString(self: MaterialX.PyMaterialXCore.TypedValue_matrix33) -> str"""

class TypedValue_matrix44(Value):
    TYPE: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def createValue(arg0) -> Value:
        """createValue(arg0: MaterialX_v1_39_4::Matrix44) -> MaterialX.PyMaterialXCore.Value"""
    def getData(self, *args, **kwargs):
        """getData(self: MaterialX.PyMaterialXCore.TypedValue_matrix44) -> MaterialX_v1_39_4::Matrix44"""
    def getValueString(self) -> str:
        """getValueString(self: MaterialX.PyMaterialXCore.TypedValue_matrix44) -> str"""

class TypedValue_string(Value):
    TYPE: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def createValue(arg0: str) -> Value:
        """createValue(arg0: str) -> MaterialX.PyMaterialXCore.Value"""
    def getData(self) -> str:
        """getData(self: MaterialX.PyMaterialXCore.TypedValue_string) -> str"""
    def getValueString(self) -> str:
        """getValueString(self: MaterialX.PyMaterialXCore.TypedValue_string) -> str"""

class TypedValue_stringarray(Value):
    TYPE: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def createValue(arg0: list[str]) -> Value:
        """createValue(arg0: list[str]) -> MaterialX.PyMaterialXCore.Value"""
    def getData(self) -> list[str]:
        """getData(self: MaterialX.PyMaterialXCore.TypedValue_stringarray) -> list[str]"""
    def getValueString(self) -> str:
        """getValueString(self: MaterialX.PyMaterialXCore.TypedValue_stringarray) -> str"""

class TypedValue_vector2(Value):
    TYPE: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def createValue(arg0) -> Value:
        """createValue(arg0: MaterialX_v1_39_4::Vector2) -> MaterialX.PyMaterialXCore.Value"""
    def getData(self, *args, **kwargs):
        """getData(self: MaterialX.PyMaterialXCore.TypedValue_vector2) -> MaterialX_v1_39_4::Vector2"""
    def getValueString(self) -> str:
        """getValueString(self: MaterialX.PyMaterialXCore.TypedValue_vector2) -> str"""

class TypedValue_vector3(Value):
    TYPE: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def createValue(arg0) -> Value:
        """createValue(arg0: MaterialX_v1_39_4::Vector3) -> MaterialX.PyMaterialXCore.Value"""
    def getData(self, *args, **kwargs):
        """getData(self: MaterialX.PyMaterialXCore.TypedValue_vector3) -> MaterialX_v1_39_4::Vector3"""
    def getValueString(self) -> str:
        """getValueString(self: MaterialX.PyMaterialXCore.TypedValue_vector3) -> str"""

class TypedValue_vector4(Value):
    TYPE: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def createValue(arg0) -> Value:
        """createValue(arg0: MaterialX_v1_39_4::Vector4) -> MaterialX.PyMaterialXCore.Value"""
    def getData(self, *args, **kwargs):
        """getData(self: MaterialX.PyMaterialXCore.TypedValue_vector4) -> MaterialX_v1_39_4::Vector4"""
    def getValueString(self) -> str:
        """getValueString(self: MaterialX.PyMaterialXCore.TypedValue_vector4) -> str"""

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

        2. convert(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: MaterialX.PyMaterialXCore.Vector2, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector2

        3. convert(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: MaterialX.PyMaterialXCore.Vector3, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector3

        4. convert(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: MaterialX.PyMaterialXCore.Vector4, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector4
        """
    @overload
    def convert(self, arg0: Vector2, arg1: str, arg2: str) -> Vector2:
        """convert(*args, **kwargs)
        Overloaded function.

        1. convert(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: float, arg1: str, arg2: str) -> float

        2. convert(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: MaterialX.PyMaterialXCore.Vector2, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector2

        3. convert(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: MaterialX.PyMaterialXCore.Vector3, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector3

        4. convert(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: MaterialX.PyMaterialXCore.Vector4, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector4
        """
    @overload
    def convert(self, arg0: Vector3, arg1: str, arg2: str) -> Vector3:
        """convert(*args, **kwargs)
        Overloaded function.

        1. convert(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: float, arg1: str, arg2: str) -> float

        2. convert(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: MaterialX.PyMaterialXCore.Vector2, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector2

        3. convert(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: MaterialX.PyMaterialXCore.Vector3, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector3

        4. convert(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: MaterialX.PyMaterialXCore.Vector4, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector4
        """
    @overload
    def convert(self, arg0: Vector4, arg1: str, arg2: str) -> Vector4:
        """convert(*args, **kwargs)
        Overloaded function.

        1. convert(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: float, arg1: str, arg2: str) -> float

        2. convert(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: MaterialX.PyMaterialXCore.Vector2, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector2

        3. convert(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: MaterialX.PyMaterialXCore.Vector3, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector3

        4. convert(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: MaterialX.PyMaterialXCore.Vector4, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector4
        """
    def getUnitAsInteger(self, arg0: str) -> int:
        """getUnitAsInteger(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: str) -> int"""
    def getUnitFromInteger(self, arg0: int) -> str:
        """getUnitFromInteger(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: int) -> str"""

class UnitConverterRegistry:
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def addUnitConverter(self, arg0: UnitTypeDef, arg1: UnitConverter) -> bool:
        """addUnitConverter(self: MaterialX.PyMaterialXCore.UnitConverterRegistry, arg0: MaterialX.PyMaterialXCore.UnitTypeDef, arg1: MaterialX.PyMaterialXCore.UnitConverter) -> bool"""
    def clearUnitConverters(self) -> None:
        """clearUnitConverters(self: MaterialX.PyMaterialXCore.UnitConverterRegistry) -> None"""
    @staticmethod
    def create() -> UnitConverterRegistry:
        """create() -> MaterialX.PyMaterialXCore.UnitConverterRegistry"""
    def getUnitConverter(self, arg0: UnitTypeDef) -> UnitConverter:
        """getUnitConverter(self: MaterialX.PyMaterialXCore.UnitConverterRegistry, arg0: MaterialX.PyMaterialXCore.UnitTypeDef) -> MaterialX.PyMaterialXCore.UnitConverter"""
    def removeUnitConverter(self, arg0: UnitTypeDef) -> bool:
        """removeUnitConverter(self: MaterialX.PyMaterialXCore.UnitConverterRegistry, arg0: MaterialX.PyMaterialXCore.UnitTypeDef) -> bool"""

class UnitDef(Element):
    CATEGORY: ClassVar[str] = ...  # read-only
    UNITTYPE_ATTRIBUTE: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def addUnit(self, arg0: str) -> Unit:
        """addUnit(self: MaterialX.PyMaterialXCore.UnitDef, arg0: str) -> MaterialX.PyMaterialXCore.Unit"""
    def getUnit(self, arg0: str) -> Unit:
        """getUnit(self: MaterialX.PyMaterialXCore.UnitDef, arg0: str) -> MaterialX.PyMaterialXCore.Unit"""
    def getUnitType(self) -> str:
        """getUnitType(self: MaterialX.PyMaterialXCore.UnitDef) -> str"""
    def getUnits(self) -> list[Unit]:
        """getUnits(self: MaterialX.PyMaterialXCore.UnitDef) -> list[MaterialX.PyMaterialXCore.Unit]"""
    def hasUnitType(self) -> bool:
        """hasUnitType(self: MaterialX.PyMaterialXCore.UnitDef) -> bool"""
    def setUnitType(self, arg0: str) -> None:
        """setUnitType(self: MaterialX.PyMaterialXCore.UnitDef, arg0: str) -> None"""

class UnitTypeDef(Element):
    CATEGORY: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def getUnitDefs(self) -> list[UnitDef]:
        """getUnitDefs(self: MaterialX.PyMaterialXCore.UnitTypeDef) -> list[MaterialX.PyMaterialXCore.UnitDef]"""

class Value:
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def createValueFromStrings(value: str, type: str, typeDefPtr=...) -> Value:
        """createValueFromStrings(value: str, type: str, typeDefPtr: MaterialX_v1_39_4::TypeDef = None) -> MaterialX.PyMaterialXCore.Value"""
    def getTypeString(self) -> str:
        """getTypeString(self: MaterialX.PyMaterialXCore.Value) -> str"""
    def getValueString(self) -> str:
        """getValueString(self: MaterialX.PyMaterialXCore.Value) -> str"""

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
        """getActiveUnit(self: MaterialX.PyMaterialXCore.ValueElement) -> str"""
    def getImplementationName(self) -> str:
        """getImplementationName(self: MaterialX.PyMaterialXCore.ValueElement) -> str"""
    def getInterfaceName(self) -> str:
        """getInterfaceName(self: MaterialX.PyMaterialXCore.ValueElement) -> str"""
    def getIsUniform(self) -> bool:
        """getIsUniform(self: MaterialX.PyMaterialXCore.ValueElement) -> bool"""
    def getResolvedValueString(self, resolver=...) -> str:
        """getResolvedValueString(self: MaterialX.PyMaterialXCore.ValueElement, resolver: MaterialX_v1_39_4::StringResolver = None) -> str"""
    def getUnit(self) -> str:
        """getUnit(self: MaterialX.PyMaterialXCore.ValueElement) -> str"""
    def getUnitType(self) -> str:
        """getUnitType(self: MaterialX.PyMaterialXCore.ValueElement) -> str"""
    def getValueString(self) -> str:
        """getValueString(self: MaterialX.PyMaterialXCore.ValueElement) -> str"""
    def hasImplementationName(self) -> bool:
        """hasImplementationName(self: MaterialX.PyMaterialXCore.ValueElement) -> bool"""
    def hasInterfaceName(self) -> bool:
        """hasInterfaceName(self: MaterialX.PyMaterialXCore.ValueElement) -> bool"""
    def hasUnit(self) -> bool:
        """hasUnit(self: MaterialX.PyMaterialXCore.ValueElement) -> bool"""
    def hasUnitType(self) -> bool:
        """hasUnitType(self: MaterialX.PyMaterialXCore.ValueElement) -> bool"""
    def hasValueString(self) -> bool:
        """hasValueString(self: MaterialX.PyMaterialXCore.ValueElement) -> bool"""
    def setImplementationName(self, arg0: str) -> None:
        """setImplementationName(self: MaterialX.PyMaterialXCore.ValueElement, arg0: str) -> None"""
    def setInterfaceName(self, arg0: str) -> None:
        """setInterfaceName(self: MaterialX.PyMaterialXCore.ValueElement, arg0: str) -> None"""
    def setIsUniform(self, arg0: bool) -> None:
        """setIsUniform(self: MaterialX.PyMaterialXCore.ValueElement, arg0: bool) -> None"""
    def setUnit(self, arg0: str) -> None:
        """setUnit(self: MaterialX.PyMaterialXCore.ValueElement, arg0: str) -> None"""
    def setUnitType(self, arg0: str) -> None:
        """setUnitType(self: MaterialX.PyMaterialXCore.ValueElement, arg0: str) -> None"""
    def setValueString(self, arg0: str) -> None:
        """setValueString(self: MaterialX.PyMaterialXCore.ValueElement, arg0: str) -> None"""

class Variant(InterfaceElement):
    CATEGORY: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class VariantAssign(Element):
    CATEGORY: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def getVariantSetString(self) -> str:
        """getVariantSetString(self: MaterialX.PyMaterialXCore.VariantAssign) -> str"""
    def getVariantString(self) -> str:
        """getVariantString(self: MaterialX.PyMaterialXCore.VariantAssign) -> str"""
    def hasVariantSetString(self) -> bool:
        """hasVariantSetString(self: MaterialX.PyMaterialXCore.VariantAssign) -> bool"""
    def hasVariantString(self) -> bool:
        """hasVariantString(self: MaterialX.PyMaterialXCore.VariantAssign) -> bool"""
    def setVariantSetString(self, arg0: str) -> None:
        """setVariantSetString(self: MaterialX.PyMaterialXCore.VariantAssign, arg0: str) -> None"""
    def setVariantString(self, arg0: str) -> None:
        """setVariantString(self: MaterialX.PyMaterialXCore.VariantAssign, arg0: str) -> None"""

class VariantSet(Element):
    CATEGORY: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def addVariant(self, name: str = ...) -> Variant:
        """addVariant(self: MaterialX.PyMaterialXCore.VariantSet, name: str = '') -> MaterialX.PyMaterialXCore.Variant"""
    def getVariant(self, arg0: str) -> Variant:
        """getVariant(self: MaterialX.PyMaterialXCore.VariantSet, arg0: str) -> MaterialX.PyMaterialXCore.Variant"""
    def getVariants(self) -> list[Variant]:
        """getVariants(self: MaterialX.PyMaterialXCore.VariantSet) -> list[MaterialX.PyMaterialXCore.Variant]"""
    def removeVariant(self, arg0: str) -> None:
        """removeVariant(self: MaterialX.PyMaterialXCore.VariantSet, arg0: str) -> None"""

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
        """copy(self: MaterialX.PyMaterialXCore.Vector2) -> MaterialX.PyMaterialXCore.Vector2"""
    def cross(self, arg0: Vector2) -> float:
        """cross(self: MaterialX.PyMaterialXCore.Vector2, arg0: MaterialX.PyMaterialXCore.Vector2) -> float"""
    def dot(self, arg0: Vector2) -> float:
        """dot(self: MaterialX.PyMaterialXCore.Vector2, arg0: MaterialX.PyMaterialXCore.Vector2) -> float"""
    def getMagnitude(self) -> float:
        """getMagnitude(self: MaterialX.PyMaterialXCore.Vector2) -> float"""
    def getNormalized(self) -> Vector2:
        """getNormalized(self: MaterialX.PyMaterialXCore.Vector2) -> MaterialX.PyMaterialXCore.Vector2"""
    def __add__(self, arg0: Vector2) -> Vector2:
        """__add__(self: MaterialX.PyMaterialXCore.Vector2, arg0: MaterialX.PyMaterialXCore.Vector2) -> MaterialX.PyMaterialXCore.Vector2"""
    def __eq__(self, arg0: Vector2) -> bool:
        """__eq__(self: MaterialX.PyMaterialXCore.Vector2, arg0: MaterialX.PyMaterialXCore.Vector2) -> bool"""
    def __getitem__(self, arg0: int) -> float:
        """__getitem__(self: MaterialX.PyMaterialXCore.Vector2, arg0: int) -> float"""
    def __iter__(self) -> typing.Iterator[float]:
        """def __iter__(self) -> typing.Iterator[float]"""
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
        """copy(self: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3"""
    def cross(self, arg0: Vector3) -> Vector3:
        """cross(self: MaterialX.PyMaterialXCore.Vector3, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3"""
    def dot(self, arg0: Vector3) -> float:
        """dot(self: MaterialX.PyMaterialXCore.Vector3, arg0: MaterialX.PyMaterialXCore.Vector3) -> float"""
    def getMagnitude(self) -> float:
        """getMagnitude(self: MaterialX.PyMaterialXCore.Vector3) -> float"""
    def getNormalized(self) -> Vector3:
        """getNormalized(self: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3"""
    def __add__(self, arg0: Vector3) -> Vector3:
        """__add__(self: MaterialX.PyMaterialXCore.Vector3, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3"""
    def __eq__(self, arg0: Vector3) -> bool:
        """__eq__(self: MaterialX.PyMaterialXCore.Vector3, arg0: MaterialX.PyMaterialXCore.Vector3) -> bool"""
    def __getitem__(self, arg0: int) -> float:
        """__getitem__(self: MaterialX.PyMaterialXCore.Vector3, arg0: int) -> float"""
    def __iter__(self) -> typing.Iterator[float]:
        """def __iter__(self) -> typing.Iterator[float]"""
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
        """copy(self: MaterialX.PyMaterialXCore.Vector4) -> MaterialX.PyMaterialXCore.Vector4"""
    def dot(self, arg0: Vector4) -> float:
        """dot(self: MaterialX.PyMaterialXCore.Vector4, arg0: MaterialX.PyMaterialXCore.Vector4) -> float"""
    def getMagnitude(self) -> float:
        """getMagnitude(self: MaterialX.PyMaterialXCore.Vector4) -> float"""
    def getNormalized(self) -> Vector4:
        """getNormalized(self: MaterialX.PyMaterialXCore.Vector4) -> MaterialX.PyMaterialXCore.Vector4"""
    def __add__(self, arg0: Vector4) -> Vector4:
        """__add__(self: MaterialX.PyMaterialXCore.Vector4, arg0: MaterialX.PyMaterialXCore.Vector4) -> MaterialX.PyMaterialXCore.Vector4"""
    def __eq__(self, arg0: Vector4) -> bool:
        """__eq__(self: MaterialX.PyMaterialXCore.Vector4, arg0: MaterialX.PyMaterialXCore.Vector4) -> bool"""
    def __getitem__(self, arg0: int) -> float:
        """__getitem__(self: MaterialX.PyMaterialXCore.Vector4, arg0: int) -> float"""
    def __iter__(self) -> typing.Iterator[float]:
        """def __iter__(self) -> typing.Iterator[float]"""
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
        """getViewerCollection(self: MaterialX.PyMaterialXCore.Visibility) -> str"""
    def getViewerGeom(self) -> str:
        """getViewerGeom(self: MaterialX.PyMaterialXCore.Visibility) -> str"""
    def getVisibilityType(self) -> str:
        """getVisibilityType(self: MaterialX.PyMaterialXCore.Visibility) -> str"""
    def getVisible(self) -> bool:
        """getVisible(self: MaterialX.PyMaterialXCore.Visibility) -> bool"""
    def hasViewerCollection(self) -> bool:
        """hasViewerCollection(self: MaterialX.PyMaterialXCore.Visibility) -> bool"""
    def hasViewerGeom(self) -> bool:
        """hasViewerGeom(self: MaterialX.PyMaterialXCore.Visibility) -> bool"""
    def hasVisibilityType(self) -> bool:
        """hasVisibilityType(self: MaterialX.PyMaterialXCore.Visibility) -> bool"""
    def setViewerCollection(self, arg0: str) -> None:
        """setViewerCollection(self: MaterialX.PyMaterialXCore.Visibility, arg0: str) -> None"""
    def setViewerGeom(self, arg0: str) -> None:
        """setViewerGeom(self: MaterialX.PyMaterialXCore.Visibility, arg0: str) -> None"""
    def setVisibilityType(self, arg0: str) -> None:
        """setVisibilityType(self: MaterialX.PyMaterialXCore.Visibility, arg0: str) -> None"""
    def setVisible(self, arg0: bool) -> None:
        """setVisible(self: MaterialX.PyMaterialXCore.Visibility, arg0: bool) -> None"""

def createDocument(*args, **kwargs):
    """createDocument() -> MaterialX_v1_39_4::Document"""
def createNamePath(arg0: list[str]) -> str:
    """createNamePath(arg0: list[str]) -> str"""
def createValidName(name: str, replaceChar: str = ...) -> str:
    """createValidName(name: str, replaceChar: str = '_') -> str"""
def geomStringsMatch(arg0: str, arg1: str, arg2: bool) -> bool:
    """geomStringsMatch(arg0: str, arg1: str, arg2: bool) -> bool"""
def getConnectedOutputs(arg0: Node) -> list[Output]:
    """getConnectedOutputs(arg0: MaterialX.PyMaterialXCore.Node) -> list[MaterialX.PyMaterialXCore.Output]"""
def getGeometryBindings(materialNode, geom: str = ...) -> list[MaterialAssign]:
    """getGeometryBindings(materialNode: MaterialX_v1_39_4::Node, geom: str = '/') -> list[MaterialX.PyMaterialXCore.MaterialAssign]"""
def getShaderNodes(materialNode: Node, nodeType: str = ..., target: str = ...) -> list[Node]:
    """getShaderNodes(materialNode: MaterialX.PyMaterialXCore.Node, nodeType: str = 'surfaceshader', target: str = '') -> list[MaterialX.PyMaterialXCore.Node]"""
def getVersionIntegers() -> tuple[int, int, int]:
    """getVersionIntegers() -> tuple[int, int, int]"""
def getVersionString() -> str:
    """getVersionString() -> str"""
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
