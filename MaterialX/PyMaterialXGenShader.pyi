import MaterialX.PyMaterialXCore
import MaterialX.PyMaterialXFormat
import typing
from _typeshed import Incomplete
from typing import Callable, ClassVar, overload

HW_ATTR_TRANSPARENT: str
HW_LIGHT_DATA: str
HW_PIXEL_OUTPUTS: str
HW_PRIVATE_UNIFORMS: str
HW_PUBLIC_UNIFORMS: str
HW_VERTEX_DATA: str
HW_VERTEX_INPUTS: str
PIXEL_STAGE: str
SHADER_INTERFACE_COMPLETE: ShaderInterfaceType
SHADER_INTERFACE_REDUCED: ShaderInterfaceType
SPECULAR_ENVIRONMENT_FIS: HwSpecularEnvironmentMethod
SPECULAR_ENVIRONMENT_NONE: HwSpecularEnvironmentMethod
SPECULAR_ENVIRONMENT_PREFILTER: HwSpecularEnvironmentMethod
VERTEX_STAGE: str

class ApplicationVariableHandler:
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class ColorManagementSystem:
    def __init__(self) -> None:
        """__init__(self: MaterialX.PyMaterialXGenShader.ColorManagementSystem) -> None"""
    def getName(self) -> str:
        """getName(self: MaterialX.PyMaterialXGenShader.ColorManagementSystem) -> str

        Return the ColorManagementSystem name.
        """
    def loadLibrary(self, arg0: MaterialX.PyMaterialXCore.Document) -> None:
        """loadLibrary(self: MaterialX.PyMaterialXGenShader.ColorManagementSystem, arg0: MaterialX.PyMaterialXCore.Document) -> None

        Load a library of implementations from the provided document, replacing any previously loaded content.
        """
    def supportsTransform(self, arg0: ColorSpaceTransform) -> bool:
        """supportsTransform(self: MaterialX.PyMaterialXGenShader.ColorManagementSystem, arg0: MaterialX.PyMaterialXGenShader.ColorSpaceTransform) -> bool

        Returns whether this color management system supports a provided transform.
        """

class ColorSpaceTransform:
    sourceSpace: str
    targetSpace: str
    type: Incomplete
    def __init__(self, arg0: str, arg1: str, arg2) -> None:
        """__init__(self: MaterialX.PyMaterialXGenShader.ColorSpaceTransform, arg0: str, arg1: str, arg2: MaterialX_v1_39_5::TypeDesc) -> None"""

class DefaultColorManagementSystem(ColorManagementSystem):
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def create(arg0: str) -> DefaultColorManagementSystem:
        """create(arg0: str) -> MaterialX.PyMaterialXGenShader.DefaultColorManagementSystem"""
    def getName(self) -> str:
        """getName(self: MaterialX.PyMaterialXGenShader.DefaultColorManagementSystem) -> str

        Return the ColorManagementSystem name.
        """

class GenContext:
    def __init__(self, arg0: ShaderGenerator) -> None:
        """__init__(self: MaterialX.PyMaterialXGenShader.GenContext, arg0: MaterialX.PyMaterialXGenShader.ShaderGenerator) -> None"""
    def getApplicationVariableHandler(self, *args, **kwargs):
        """getApplicationVariableHandler(self: MaterialX.PyMaterialXGenShader.GenContext) -> Callable[[MaterialX_v1_39_5::ShaderNode, MaterialX.PyMaterialXGenShader.GenContext], None]

        Get handler for application variables.
        """
    def getOptions(self, *args, **kwargs):
        """getOptions(self: MaterialX.PyMaterialXGenShader.GenContext) -> MaterialX_v1_39_5::GenOptions

        Return shader generation options.
        """
    def getShaderGenerator(self) -> ShaderGenerator:
        """getShaderGenerator(self: MaterialX.PyMaterialXGenShader.GenContext) -> MaterialX.PyMaterialXGenShader.ShaderGenerator

        Return shader generatior.
        """
    def getTypeDesc(self, *args, **kwargs):
        """getTypeDesc(self: MaterialX.PyMaterialXGenShader.GenContext, arg0: str) -> MaterialX_v1_39_5::TypeDesc

        Return a TypeDesc for the given type name.
        """
    def pushUserData(self, arg0: str, arg1) -> None:
        """pushUserData(self: MaterialX.PyMaterialXGenShader.GenContext, arg0: str, arg1: MaterialX_v1_39_5::GenUserData) -> None

        Add user data to the context to make it available during shader generator.
        """
    @overload
    def registerSourceCodeSearchPath(self, arg0: MaterialX.PyMaterialXFormat.FilePath) -> None:
        """registerSourceCodeSearchPath(*args, **kwargs)
        Overloaded function.

        1. registerSourceCodeSearchPath(self: MaterialX.PyMaterialXGenShader.GenContext, arg0: MaterialX.PyMaterialXFormat.FilePath) -> None

        Register a user search path for finding source code during code generation.

        2. registerSourceCodeSearchPath(self: MaterialX.PyMaterialXGenShader.GenContext, arg0: MaterialX.PyMaterialXFormat.FileSearchPath) -> None

        Register a user search path for finding source code during code generation.
        """
    @overload
    def registerSourceCodeSearchPath(self, arg0: MaterialX.PyMaterialXFormat.FileSearchPath) -> None:
        """registerSourceCodeSearchPath(*args, **kwargs)
        Overloaded function.

        1. registerSourceCodeSearchPath(self: MaterialX.PyMaterialXGenShader.GenContext, arg0: MaterialX.PyMaterialXFormat.FilePath) -> None

        Register a user search path for finding source code during code generation.

        2. registerSourceCodeSearchPath(self: MaterialX.PyMaterialXGenShader.GenContext, arg0: MaterialX.PyMaterialXFormat.FileSearchPath) -> None

        Register a user search path for finding source code during code generation.
        """
    def resolveSourceFile(self, arg0: MaterialX.PyMaterialXFormat.FilePath, arg1: MaterialX.PyMaterialXFormat.FilePath) -> MaterialX.PyMaterialXFormat.FilePath:
        """resolveSourceFile(self: MaterialX.PyMaterialXGenShader.GenContext, arg0: MaterialX.PyMaterialXFormat.FilePath, arg1: MaterialX.PyMaterialXFormat.FilePath) -> MaterialX.PyMaterialXFormat.FilePath

        Resolve a source code filename, first checking the given local path then checking any file paths registered by the user.
        """
    def setApplicationVariableHandler(self, arg0) -> None:
        """setApplicationVariableHandler(self: MaterialX.PyMaterialXGenShader.GenContext, arg0: Callable[[MaterialX_v1_39_5::ShaderNode, MaterialX.PyMaterialXGenShader.GenContext], None]) -> None

        Set handler for application variables.
        """

class GenOptions:
    addUpstreamDependencies: bool
    emitColorTransforms: bool
    fileTextureVerticalFlip: bool
    hwAmbientOcclusion: bool
    hwImplicitBitangents: bool
    hwMaxActiveLightSources: int
    hwNormalizeUdimTexCoords: bool
    hwShadowMap: bool
    hwSpecularEnvironmentMethod: HwSpecularEnvironmentMethod
    hwSrgbEncodeOutput: bool
    hwTransparency: bool
    hwWriteAlbedoTable: bool
    hwWriteDepthMoments: bool
    hwWriteEnvPrefilter: bool
    libraryPrefix: MaterialX.PyMaterialXFormat.FilePath
    shaderInterfaceType: ShaderInterfaceType
    targetColorSpaceOverride: str
    targetDistanceUnit: str
    def __init__(self) -> None:
        """__init__(self: MaterialX.PyMaterialXGenShader.GenOptions) -> None"""

class GenUserData:
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def getSelf(self) -> GenUserData:
        """getSelf(self: MaterialX.PyMaterialXGenShader.GenUserData) -> MaterialX.PyMaterialXGenShader.GenUserData

        Return our self pointer.
        """

class HwResourceBindingContext(GenUserData):
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def emitDirectives(self, arg0: GenContext, arg1: ShaderStage) -> None:
        """emitDirectives(self: MaterialX.PyMaterialXGenShader.HwResourceBindingContext, arg0: MaterialX.PyMaterialXGenShader.GenContext, arg1: MaterialX.PyMaterialXGenShader.ShaderStage) -> None"""
    def emitResourceBindings(self, arg0: GenContext, arg1: VariableBlock, arg2: ShaderStage) -> None:
        """emitResourceBindings(self: MaterialX.PyMaterialXGenShader.HwResourceBindingContext, arg0: MaterialX.PyMaterialXGenShader.GenContext, arg1: MaterialX.PyMaterialXGenShader.VariableBlock, arg2: MaterialX.PyMaterialXGenShader.ShaderStage) -> None"""

class HwShaderGenerator(ShaderGenerator):
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def bindLightShader(self, arg0: int, arg1: GenContext) -> None:
        """bindLightShader(self: MaterialX.PyMaterialXCore.NodeDef, arg0: int, arg1: MaterialX.PyMaterialXGenShader.GenContext) -> None"""
    def unbindLightShader(self, arg0: GenContext) -> None:
        """unbindLightShader(self: int, arg0: MaterialX.PyMaterialXGenShader.GenContext) -> None"""
    def unbindLightShaders(self) -> None:
        """unbindLightShaders(self: MaterialX.PyMaterialXGenShader.GenContext) -> None"""

class HwSpecularEnvironmentMethod:
    __members__: ClassVar[dict] = ...  # read-only
    SPECULAR_ENVIRONMENT_FIS: ClassVar[HwSpecularEnvironmentMethod] = ...
    SPECULAR_ENVIRONMENT_NONE: ClassVar[HwSpecularEnvironmentMethod] = ...
    SPECULAR_ENVIRONMENT_PREFILTER: ClassVar[HwSpecularEnvironmentMethod] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: MaterialX.PyMaterialXGenShader.HwSpecularEnvironmentMethod, value: int) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: MaterialX.PyMaterialXGenShader.HwSpecularEnvironmentMethod) -> int"""
    def __int__(self) -> int:
        """__int__(self: MaterialX.PyMaterialXGenShader.HwSpecularEnvironmentMethod) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class Shader:
    def __init__(self, arg0: str, arg1) -> None:
        """__init__(self: MaterialX.PyMaterialXGenShader.Shader, arg0: str, arg1: MaterialX_v1_39_5::ShaderGraph) -> None"""
    def getAttribute(self, arg0: str) -> MaterialX.PyMaterialXCore.Value:
        """getAttribute(self: MaterialX.PyMaterialXGenShader.Shader, arg0: str) -> MaterialX.PyMaterialXCore.Value

        Return the value string of the given attribute.

        If the given attribute is not present, then an empty string is returned.
        """
    def getName(self) -> str:
        """getName(self: MaterialX.PyMaterialXGenShader.Shader) -> str

        Return the ColorManagementSystem name.
        """
    def getSourceCode(self, arg0: str) -> str:
        """getSourceCode(self: MaterialX.PyMaterialXGenShader.Shader, arg0: str) -> str

        Return the shader source code for a given shader stage.
        """
    def getStage(self, *args, **kwargs):
        """getStage(*args, **kwargs)
        Overloaded function.

        1. getStage(self: MaterialX.PyMaterialXGenShader.Shader, arg0: int) -> MaterialX_v1_39_5::ShaderStage

        Return a stage by name.

        2. getStage(self: MaterialX.PyMaterialXGenShader.Shader, arg0: str) -> MaterialX_v1_39_5::ShaderStage

        Return a stage by name.
        """
    def hasAttribute(self, arg0: str) -> bool:
        """hasAttribute(self: MaterialX.PyMaterialXGenShader.Shader, arg0: str) -> bool

        Return true if the given attribute is present.
        """
    def hasStage(self, arg0: str) -> bool:
        """hasStage(self: MaterialX.PyMaterialXGenShader.Shader, arg0: str) -> bool

        Return if stage exists.
        """
    def numStages(self) -> int:
        """numStages(self: MaterialX.PyMaterialXGenShader.Shader) -> int

        Return the number of shader stages for this shader.
        """
    @overload
    def setAttribute(self, arg0: str) -> None:
        """setAttribute(*args, **kwargs)
        Overloaded function.

        1. setAttribute(self: MaterialX.PyMaterialXGenShader.Shader, arg0: str) -> None

        Set the value string of the given attribute.

        2. setAttribute(self: MaterialX.PyMaterialXGenShader.Shader, arg0: str, arg1: MaterialX.PyMaterialXCore.Value) -> None

        Set the value string of the given attribute.
        """
    @overload
    def setAttribute(self, arg0: str, arg1: MaterialX.PyMaterialXCore.Value) -> None:
        """setAttribute(*args, **kwargs)
        Overloaded function.

        1. setAttribute(self: MaterialX.PyMaterialXGenShader.Shader, arg0: str) -> None

        Set the value string of the given attribute.

        2. setAttribute(self: MaterialX.PyMaterialXGenShader.Shader, arg0: str, arg1: MaterialX.PyMaterialXCore.Value) -> None

        Set the value string of the given attribute.
        """

class ShaderGenerator:
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def generate(self, arg0: str, arg1: MaterialX.PyMaterialXCore.Element, arg2) -> Shader:
        """generate(self: MaterialX.PyMaterialXGenShader.ShaderGenerator, arg0: str, arg1: MaterialX.PyMaterialXCore.Element, arg2: MaterialX_v1_39_5::GenContext) -> MaterialX.PyMaterialXGenShader.Shader

        Generate a shader starting from the given element, translating the element and all dependencies upstream into shader code.
        """
    def getColorManagementSystem(self) -> ColorManagementSystem:
        """getColorManagementSystem(self: MaterialX.PyMaterialXGenShader.ShaderGenerator) -> MaterialX.PyMaterialXGenShader.ColorManagementSystem

        Return the color management system string.
        """
    def getTarget(self) -> str:
        """getTarget(self: MaterialX.PyMaterialXGenShader.ShaderGenerator) -> str

        Return a unique identifier for the target this generator is for.
        """
    def getTokenSubstitutions(self) -> dict[str, str]:
        """getTokenSubstitutions(self: MaterialX.PyMaterialXGenShader.ShaderGenerator) -> dict[str, str]

        Return the map of token substitutions used by the generator.
        """
    def getUnitSystem(self, *args, **kwargs):
        """getUnitSystem(self: MaterialX.PyMaterialXGenShader.ShaderGenerator) -> MaterialX_v1_39_5::UnitSystem

        Returns the unit system.
        """
    def registerShaderMetadata(self, arg0: MaterialX.PyMaterialXCore.Document, arg1) -> None:
        """registerShaderMetadata(self: MaterialX.PyMaterialXGenShader.ShaderGenerator, arg0: MaterialX.PyMaterialXCore.Document, arg1: MaterialX_v1_39_5::GenContext) -> None

        Register metadata that should be exported to the generated shaders.
        """
    def registerTypeDefs(self, arg0: MaterialX.PyMaterialXCore.Document) -> None:
        """registerTypeDefs(self: MaterialX.PyMaterialXGenShader.ShaderGenerator, arg0: MaterialX.PyMaterialXCore.Document) -> None

        Register type definitions from the document.
        """
    def setColorManagementSystem(self, arg0: ColorManagementSystem) -> None:
        """setColorManagementSystem(self: MaterialX.PyMaterialXGenShader.ShaderGenerator, arg0: MaterialX.PyMaterialXGenShader.ColorManagementSystem) -> None

        Set the color management system string.
        """
    def setUnitSystem(self, arg0) -> None:
        """setUnitSystem(self: MaterialX.PyMaterialXGenShader.ShaderGenerator, arg0: MaterialX_v1_39_5::UnitSystem) -> None

        Sets the unit system.
        """

class ShaderInterfaceType:
    __members__: ClassVar[dict] = ...  # read-only
    SHADER_INTERFACE_COMPLETE: ClassVar[ShaderInterfaceType] = ...
    SHADER_INTERFACE_REDUCED: ClassVar[ShaderInterfaceType] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: MaterialX.PyMaterialXGenShader.ShaderInterfaceType, value: int) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: MaterialX.PyMaterialXGenShader.ShaderInterfaceType) -> int"""
    def __int__(self) -> int:
        """__int__(self: MaterialX.PyMaterialXGenShader.ShaderInterfaceType) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class ShaderPort:
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def getColorSpace(self) -> str:
        """getColorSpace(self: MaterialX.PyMaterialXGenShader.ShaderPort) -> str

        Return the element's color space string.
        """
    def getFullName(self) -> str:
        """getFullName(self: MaterialX.PyMaterialXGenShader.ShaderPort) -> str

        Return the name of this port.
        """
    def getGeomProp(self) -> str:
        """getGeomProp(self: MaterialX.PyMaterialXGenShader.ShaderPort) -> str

        Return the GeomProp, if any, with the given name.
        """
    def getName(self) -> str:
        """getName(self: MaterialX.PyMaterialXGenShader.ShaderPort) -> str

        Return the ColorManagementSystem name.
        """
    def getPath(self) -> str:
        """getPath(self: MaterialX.PyMaterialXGenShader.ShaderPort) -> str

        Return the path to this port.
        """
    def getSemantic(self) -> str:
        """getSemantic(self: MaterialX.PyMaterialXGenShader.ShaderPort) -> str

        Return the variable semantic of this port.
        """
    def getType(self, *args, **kwargs):
        """getType(self: MaterialX.PyMaterialXGenShader.ShaderPort) -> MaterialX_v1_39_5::TypeDesc

        Get stream attribute name.
        """
    def getUnit(self) -> str:
        """getUnit(self: MaterialX.PyMaterialXGenShader.ShaderPort) -> str

        Return the unit type for the value on this port.
        """
    def getValue(self) -> MaterialX.PyMaterialXCore.Value:
        """getValue(self: MaterialX.PyMaterialXGenShader.ShaderPort) -> MaterialX.PyMaterialXCore.Value

        Returns a value formatted according to this type syntax.

        The value is constructed from the given value object.
        """
    def getValueString(self) -> str:
        """getValueString(self: MaterialX.PyMaterialXGenShader.ShaderPort) -> str

        Return value string.
        """
    def getVariable(self) -> str:
        """getVariable(self: MaterialX.PyMaterialXGenShader.ShaderPort) -> str

        Return the variable name of this port.
        """
    def isEmitted(self) -> bool:
        """isEmitted(self: MaterialX.PyMaterialXGenShader.ShaderPort) -> bool

        Return the emitted state of this port.
        """
    def isUniform(self) -> bool:
        """isUniform(self: MaterialX.PyMaterialXGenShader.ShaderPort) -> bool

        Return the uniform flag on this port.
        """
    def setColorSpace(self, arg0: str) -> None:
        """setColorSpace(self: MaterialX.PyMaterialXGenShader.ShaderPort, arg0: str) -> None

        Set the element's color space string.
        """
    def setGeomProp(self, arg0: str) -> None:
        """setGeomProp(self: MaterialX.PyMaterialXGenShader.ShaderPort, arg0: str) -> None

        Set the geometric property string of this element.
        """
    def setName(self, arg0: str) -> None:
        """setName(self: MaterialX.PyMaterialXGenShader.ShaderPort, arg0: str) -> None

        Set the element's name string.
        """
    def setPath(self, arg0: str) -> None:
        """setPath(self: MaterialX.PyMaterialXGenShader.ShaderPort, arg0: str) -> None

        Set the path to this port.
        """
    def setSemantic(self, arg0: str) -> None:
        """setSemantic(self: MaterialX.PyMaterialXGenShader.ShaderPort, arg0: str) -> None

        Set the variable semantic of this port.
        """
    def setType(self, arg0) -> None:
        """setType(self: MaterialX.PyMaterialXGenShader.ShaderPort, arg0: MaterialX_v1_39_5::TypeDesc) -> None

        Set the data type for this port.
        """
    def setUnit(self, arg0: str) -> None:
        """setUnit(self: MaterialX.PyMaterialXGenShader.ShaderPort, arg0: str) -> None

        Set a unit type for the value on this port.
        """
    def setValue(self, arg0: MaterialX.PyMaterialXCore.Value, arg1: bool) -> None:
        """setValue(self: MaterialX.PyMaterialXGenShader.ShaderPort, arg0: MaterialX.PyMaterialXCore.Value, arg1: bool) -> None

        Set the typed value of an element from a C-style string.
        """
    def setVariable(self, arg0: str) -> None:
        """setVariable(self: MaterialX.PyMaterialXGenShader.ShaderPort, arg0: str) -> None

        Set the variable name of this port.
        """

class ShaderPortPredicate:
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class ShaderStage:
    def __init__(self, arg0: str, arg1) -> None:
        """__init__(self: MaterialX.PyMaterialXGenShader.ShaderStage, arg0: str, arg1: MaterialX_v1_39_5::Syntax) -> None"""
    def getConstantBlock(self) -> VariableBlock:
        """getConstantBlock(self: MaterialX.PyMaterialXGenShader.ShaderStage) -> MaterialX.PyMaterialXGenShader.VariableBlock

        Return the constant variable block.
        """
    def getFunctionName(self) -> str:
        """getFunctionName(self: MaterialX.PyMaterialXGenShader.ShaderStage) -> str

        Return the stage function name.
        """
    def getIncludes(self) -> set[str]:
        """getIncludes(self: MaterialX.PyMaterialXGenShader.ShaderStage) -> set[str]

        Return a set of all include files.
        """
    def getInputBlock(self, arg0: str) -> VariableBlock:
        """getInputBlock(self: MaterialX.PyMaterialXGenShader.ShaderStage, arg0: str) -> MaterialX.PyMaterialXGenShader.VariableBlock

        Return the input variable block with given name.
        """
    def getInputBlocks(self) -> dict[str, VariableBlock]:
        """getInputBlocks(self: MaterialX.PyMaterialXGenShader.ShaderStage) -> dict[str, MaterialX.PyMaterialXGenShader.VariableBlock]

        Return a map of all input blocks.
        """
    def getName(self) -> str:
        """getName(self: MaterialX.PyMaterialXGenShader.ShaderStage) -> str

        Return the ColorManagementSystem name.
        """
    def getOutputBlock(self, arg0: str) -> VariableBlock:
        """getOutputBlock(self: MaterialX.PyMaterialXGenShader.ShaderStage, arg0: str) -> MaterialX.PyMaterialXGenShader.VariableBlock

        Return the output variable block with given name.
        """
    def getOutputBlocks(self) -> dict[str, VariableBlock]:
        """getOutputBlocks(self: MaterialX.PyMaterialXGenShader.ShaderStage) -> dict[str, MaterialX.PyMaterialXGenShader.VariableBlock]

        Return a map of all output blocks.
        """
    def getSourceCode(self) -> str:
        """getSourceCode(self: MaterialX.PyMaterialXGenShader.ShaderStage) -> str

        Return the shader source code for a given shader stage.
        """
    def getSourceDependencies(self) -> set[str]:
        """getSourceDependencies(self: MaterialX.PyMaterialXGenShader.ShaderStage) -> set[str]

        Return a set of all source dependencies.
        """
    def getUniformBlock(self, arg0: str) -> VariableBlock:
        """getUniformBlock(self: MaterialX.PyMaterialXGenShader.ShaderStage, arg0: str) -> MaterialX.PyMaterialXGenShader.VariableBlock

        Return the uniform variable block with given name.
        """
    def getUniformBlocks(self) -> dict[str, VariableBlock]:
        """getUniformBlocks(self: MaterialX.PyMaterialXGenShader.ShaderStage) -> dict[str, MaterialX.PyMaterialXGenShader.VariableBlock]

        Return a map of all uniform blocks.
        """

class ShaderTranslator:
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def create() -> ShaderTranslator:
        """create() -> MaterialX.PyMaterialXGenShader.ShaderTranslator"""
    def translateAllMaterials(self, arg0: MaterialX.PyMaterialXCore.Document, arg1: str) -> None:
        """translateAllMaterials(self: MaterialX.PyMaterialXGenShader.ShaderTranslator, arg0: MaterialX.PyMaterialXCore.Document, arg1: str) -> None

        Translate each material in the input document to the destination shading model.
        """
    def translateShader(self, arg0: MaterialX.PyMaterialXCore.Node, arg1: str) -> None:
        """translateShader(self: MaterialX.PyMaterialXGenShader.ShaderTranslator, arg0: MaterialX.PyMaterialXCore.Node, arg1: str) -> None

        Translate a shader node to the destination shading model.
        """

class TypeDesc:
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def getBaseType(self) -> int:
        """getBaseType(self: MaterialX.PyMaterialXGenShader.TypeDesc) -> int

        Return the base type of the image.
        """
    def getName(self) -> str:
        """getName(self: MaterialX.PyMaterialXGenShader.TypeDesc) -> str

        Return the ColorManagementSystem name.
        """
    def getSemantic(self) -> int:
        """getSemantic(self: MaterialX.PyMaterialXGenShader.TypeDesc) -> int

        Return the variable semantic of this port.
        """
    def getSize(self) -> int:
        """getSize(self: MaterialX.PyMaterialXGenShader.TypeDesc) -> int

        Get the number of elements.
        """
    def isAggregate(self) -> bool:
        """isAggregate(self: MaterialX.PyMaterialXGenShader.TypeDesc) -> bool

        Return true if the type is an aggregate type.
        """
    def isArray(self) -> bool:
        """isArray(self: MaterialX.PyMaterialXGenShader.TypeDesc) -> bool

        Return true if the type is an array type.
        """
    def isClosure(self) -> bool:
        """isClosure(self: MaterialX.PyMaterialXGenShader.TypeDesc) -> bool

        Return true if the type represents a closure.
        """
    def isFloat2(self) -> bool:
        """isFloat2(self: MaterialX.PyMaterialXGenShader.TypeDesc) -> bool

        Return true if the type is an aggregate of 2 floats.
        """
    def isFloat3(self) -> bool:
        """isFloat3(self: MaterialX.PyMaterialXGenShader.TypeDesc) -> bool

        Return true if the type is an aggregate of 3 floats.
        """
    def isFloat4(self) -> bool:
        """isFloat4(self: MaterialX.PyMaterialXGenShader.TypeDesc) -> bool

        Return true if the type is an aggregate of 4 floats.
        """
    def isScalar(self) -> bool:
        """isScalar(self: MaterialX.PyMaterialXGenShader.TypeDesc) -> bool

        Return true if the type is a scalar type.
        """

class UnitSystem:
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def create(arg0: str) -> UnitSystem:
        """create(arg0: str) -> MaterialX.PyMaterialXGenShader.UnitSystem"""
    def getName(self) -> str:
        """getName(self: MaterialX.PyMaterialXGenShader.UnitSystem) -> str

        Return the ColorManagementSystem name.
        """
    def getUnitConverterRegistry(self) -> MaterialX.PyMaterialXCore.UnitConverterRegistry:
        """getUnitConverterRegistry(self: MaterialX.PyMaterialXGenShader.UnitSystem) -> MaterialX.PyMaterialXCore.UnitConverterRegistry

        Returns the currently assigned unit converter registry.
        """
    def loadLibrary(self, arg0: MaterialX.PyMaterialXCore.Document) -> None:
        """loadLibrary(self: MaterialX.PyMaterialXGenShader.UnitSystem, arg0: MaterialX.PyMaterialXCore.Document) -> None

        Load a library of implementations from the provided document, replacing any previously loaded content.
        """
    def setUnitConverterRegistry(self, arg0: MaterialX.PyMaterialXCore.UnitConverterRegistry) -> None:
        """setUnitConverterRegistry(self: MaterialX.PyMaterialXGenShader.UnitSystem, arg0: MaterialX.PyMaterialXCore.UnitConverterRegistry) -> None

        Assign unit converter registry replacing any previous assignment.
        """
    def supportsTransform(self, arg0: UnitTransform) -> bool:
        """supportsTransform(self: MaterialX.PyMaterialXGenShader.UnitSystem, arg0: MaterialX.PyMaterialXGenShader.UnitTransform) -> bool

        Returns whether this color management system supports a provided transform.
        """

class UnitTransform:
    sourceUnit: str
    targetUnit: str
    type: TypeDesc
    unitType: TypeDesc
    def __init__(self, arg0: str, arg1: str, arg2: TypeDesc, arg3: str) -> None:
        """__init__(self: MaterialX.PyMaterialXGenShader.UnitTransform, arg0: str, arg1: str, arg2: MaterialX.PyMaterialXGenShader.TypeDesc, arg3: str) -> None"""

class VariableBlock:
    def __init__(self, arg0: str, arg1: str) -> None:
        """__init__(self: MaterialX.PyMaterialXGenShader.VariableBlock, arg0: str, arg1: str) -> None"""
    def empty(self) -> bool:
        """empty(self: MaterialX.PyMaterialXGenShader.VariableBlock) -> bool

        Return true if the block has no variables.
        """
    @overload
    def find(self, arg0: str) -> ShaderPort:
        """find(*args, **kwargs)
        Overloaded function.

        1. find(self: MaterialX.PyMaterialXGenShader.VariableBlock, arg0: str) -> MaterialX.PyMaterialXGenShader.ShaderPort

        Given an input filename, iterate through each path in this sequence, returning the first combined path found on the file system.

        On success, the combined path is returned; otherwise the original filename is returned unmodified.

        2. find(self: MaterialX.PyMaterialXGenShader.VariableBlock, arg0: Callable[[MaterialX.PyMaterialXGenShader.ShaderPort], bool]) -> MaterialX.PyMaterialXGenShader.ShaderPort

        Given an input filename, iterate through each path in this sequence, returning the first combined path found on the file system.

        On success, the combined path is returned; otherwise the original filename is returned unmodified.
        """
    @overload
    def find(self, arg0: Callable[[ShaderPort], bool]) -> ShaderPort:
        """find(*args, **kwargs)
        Overloaded function.

        1. find(self: MaterialX.PyMaterialXGenShader.VariableBlock, arg0: str) -> MaterialX.PyMaterialXGenShader.ShaderPort

        Given an input filename, iterate through each path in this sequence, returning the first combined path found on the file system.

        On success, the combined path is returned; otherwise the original filename is returned unmodified.

        2. find(self: MaterialX.PyMaterialXGenShader.VariableBlock, arg0: Callable[[MaterialX.PyMaterialXGenShader.ShaderPort], bool]) -> MaterialX.PyMaterialXGenShader.ShaderPort

        Given an input filename, iterate through each path in this sequence, returning the first combined path found on the file system.

        On success, the combined path is returned; otherwise the original filename is returned unmodified.
        """
    def getInstance(self) -> str:
        """getInstance(self: MaterialX.PyMaterialXGenShader.VariableBlock) -> str

        Get the instance name of this block.
        """
    def getName(self) -> str:
        """getName(self: MaterialX.PyMaterialXGenShader.VariableBlock) -> str

        Return the ColorManagementSystem name.
        """
    def size(self) -> int:
        """size(self: MaterialX.PyMaterialXGenShader.VariableBlock) -> int

        Return the number of strings in the path.
        """
    def __getitem__(self, arg0: int) -> ShaderPort:
        """__getitem__(self: MaterialX.PyMaterialXGenShader.VariableBlock, arg0: int) -> MaterialX.PyMaterialXGenShader.ShaderPort

        Return the number of strings in the path.
        """
    def __iter__(self) -> typing.Iterator[ShaderPort]:
        """def __iter__(self) -> typing.Iterator[ShaderPort]"""
    def __len__(self) -> int:
        """__len__(self: MaterialX.PyMaterialXGenShader.VariableBlock) -> int

        Return the number of strings in the path.
        """

def connectsToWorldSpaceNode(arg0: MaterialX.PyMaterialXCore.Output) -> MaterialX.PyMaterialXCore.Node:
    """connectsToWorldSpaceNode(arg0: MaterialX.PyMaterialXCore.Output) -> MaterialX.PyMaterialXCore.Node"""
def elementRequiresShading(arg0: MaterialX.PyMaterialXCore.TypedElement) -> bool:
    """elementRequiresShading(arg0: MaterialX.PyMaterialXCore.TypedElement) -> bool"""
def findRenderableElements(doc: MaterialX.PyMaterialXCore.Document, includeReferencedGraphs: bool = ...) -> list[MaterialX.PyMaterialXCore.TypedElement]:
    """findRenderableElements(doc: MaterialX.PyMaterialXCore.Document, includeReferencedGraphs: bool = False) -> list[MaterialX.PyMaterialXCore.TypedElement]"""
def findRenderableMaterialNodes(arg0: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.TypedElement]:
    """findRenderableMaterialNodes(arg0: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.TypedElement]"""
def getNodeDefInput(arg0: MaterialX.PyMaterialXCore.Input, arg1: str) -> MaterialX.PyMaterialXCore.Input:
    """getNodeDefInput(arg0: MaterialX.PyMaterialXCore.Input, arg1: str) -> MaterialX.PyMaterialXCore.Input"""
def getUdimCoordinates(arg0: list[str]) -> list[MaterialX.PyMaterialXCore.Vector2]:
    """getUdimCoordinates(arg0: list[str]) -> list[MaterialX.PyMaterialXCore.Vector2]"""
def getUdimScaleAndOffset(arg0: list[MaterialX.PyMaterialXCore.Vector2], arg1: MaterialX.PyMaterialXCore.Vector2, arg2: MaterialX.PyMaterialXCore.Vector2) -> None:
    """getUdimScaleAndOffset(arg0: list[MaterialX.PyMaterialXCore.Vector2], arg1: MaterialX.PyMaterialXCore.Vector2, arg2: MaterialX.PyMaterialXCore.Vector2) -> None"""
def hasElementAttributes(arg0: MaterialX.PyMaterialXCore.Output, arg1: list[str]) -> bool:
    """hasElementAttributes(arg0: MaterialX.PyMaterialXCore.Output, arg1: list[str]) -> bool"""
def isTransparentSurface(arg0: MaterialX.PyMaterialXCore.Element, arg1: str) -> bool:
    """isTransparentSurface(arg0: MaterialX.PyMaterialXCore.Element, arg1: str) -> bool"""
def mapValueToColor(arg0: MaterialX.PyMaterialXCore.Value, arg1: MaterialX.PyMaterialXCore.Color4) -> None:
    """mapValueToColor(arg0: MaterialX.PyMaterialXCore.Value, arg1: MaterialX.PyMaterialXCore.Color4) -> None"""
def requiresImplementation(arg0: MaterialX.PyMaterialXCore.NodeDef) -> bool:
    """requiresImplementation(arg0: MaterialX.PyMaterialXCore.NodeDef) -> bool"""
def tokenSubstitution(arg0: dict[str, str], arg1: str) -> None:
    """tokenSubstitution(arg0: dict[str, str], arg1: str) -> None"""
