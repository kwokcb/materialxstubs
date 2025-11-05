import MaterialX.PyMaterialXCore
import MaterialX.PyMaterialXFormat
import MaterialX.PyMaterialXGenShader
import MaterialX.PyMaterialXRender
from typing import ClassVar, overload

class GLTextureHandler(MaterialX.PyMaterialXRender.ImageHandler):
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def bindImage(self, arg0: MaterialX.PyMaterialXRender.Image, arg1: MaterialX.PyMaterialXRender.ImageSamplingProperties) -> bool:
        """bindImage(self: MaterialX.PyMaterialXRenderGlsl.GLTextureHandler, arg0: MaterialX.PyMaterialXRender.Image, arg1: MaterialX.PyMaterialXRender.ImageSamplingProperties) -> bool

        Bind a single image.
        """
    @staticmethod
    def create(arg0: MaterialX.PyMaterialXRender.ImageLoader) -> MaterialX.PyMaterialXRender.ImageHandler:
        """create(arg0: MaterialX.PyMaterialXRender.ImageLoader) -> MaterialX.PyMaterialXRender.ImageHandler"""
    def createRenderResources(self, arg0: MaterialX.PyMaterialXRender.Image, arg1: bool, arg2: bool) -> bool:
        """createRenderResources(self: MaterialX.PyMaterialXRenderGlsl.GLTextureHandler, arg0: MaterialX.PyMaterialXRender.Image, arg1: bool, arg2: bool) -> bool

        Create rendering resources for the given image.
        """
    def releaseRenderResources(self, image: MaterialX.PyMaterialXRender.Image = ...) -> None:
        """releaseRenderResources(self: MaterialX.PyMaterialXRenderGlsl.GLTextureHandler, image: MaterialX.PyMaterialXRender.Image = None) -> None

        Release rendering resources for the given image, or for all cached images if no image pointer is specified.
        """
    def unbindImage(self, arg0: MaterialX.PyMaterialXRender.Image) -> bool:
        """unbindImage(self: MaterialX.PyMaterialXRenderGlsl.GLTextureHandler, arg0: MaterialX.PyMaterialXRender.Image) -> bool

        Unbind an image.
        """

class GlslProgram:
    UNDEFINED_OPENGL_PROGRAM_LOCATION: ClassVar[int] = ...
    UNDEFINED_OPENGL_RESOURCE_ID: ClassVar[int] = ...
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def addStage(self, arg0: str, arg1: str) -> None:
        """addStage(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram, arg0: str, arg1: str) -> None

        Set the code stages based on a list of stage strings.

        Args:
            stage: Name of the shader stage.
            sourceCode: Source code of the shader stage.
        """
    def bind(self) -> bool:
        """bind(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram) -> bool

        Bind the program.

        Returns:
            False if failed
        """
    def bindAttribute(self, arg0, arg1: MaterialX.PyMaterialXRender.Mesh) -> None:
        """bindAttribute(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram, arg0: dict[str, MaterialX_v1_39_5::GlslProgram::Input], arg1: MaterialX.PyMaterialXRender.Mesh) -> None

        Bind attribute buffers to attribute inputs.

        Args:
            inputs: Attribute inputs to bind to
            mesh: Mesh containing streams to bind
        """
    def bindLighting(self, arg0: MaterialX.PyMaterialXRender.LightHandler, arg1: MaterialX.PyMaterialXRender.ImageHandler) -> None:
        """bindLighting(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram, arg0: MaterialX.PyMaterialXRender.LightHandler, arg1: MaterialX.PyMaterialXRender.ImageHandler) -> None

        Bind lights to shader.
        """
    def bindMesh(self, arg0: MaterialX.PyMaterialXRender.Mesh) -> None:
        """bindMesh(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram, arg0: MaterialX.PyMaterialXRender.Mesh) -> None

        Bind the given mesh to this material.
        """
    def bindPartition(self, arg0: MaterialX.PyMaterialXRender.MeshPartition) -> None:
        """bindPartition(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram, arg0: MaterialX.PyMaterialXRender.MeshPartition) -> None

        Bind a mesh partition to this material.
        """
    def bindTextures(self, arg0: MaterialX.PyMaterialXRender.ImageHandler) -> None:
        """bindTextures(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram, arg0: MaterialX.PyMaterialXRender.ImageHandler) -> None

        Bind any input textures.
        """
    def bindTimeAndFrame(self, time: float = ..., frame: float = ...) -> None:
        """bindTimeAndFrame(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram, time: float = 0.0, frame: float = 1.0) -> None

        Bind time and frame.
        """
    def bindUniform(self, arg0: str, arg1: MaterialX.PyMaterialXCore.Value, arg2: bool) -> None:
        """bindUniform(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram, arg0: str, arg1: MaterialX.PyMaterialXCore.Value, arg2: bool) -> None

        Bind a value to the uniform with the given name.
        """
    def bindViewInformation(self, arg0: MaterialX.PyMaterialXRender.Camera) -> None:
        """bindViewInformation(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram, arg0: MaterialX.PyMaterialXRender.Camera) -> None

        Bind viewing information for this material.
        """
    def build(self) -> None:
        """build(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram) -> None

        Build shader program data from the source code set for each shader stage.

        An exception is thrown if the program cannot be built. The exception will contain a list of compilation errors.
        """
    def clearBuiltData(self) -> None:
        """clearBuiltData(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram) -> None"""
    @staticmethod
    def create() -> GlslProgram:
        """create() -> MaterialX.PyMaterialXRenderGlsl.GlslProgram"""
    def findInputs(self, arg0: str, arg1, arg2, arg3: bool) -> None:
        """findInputs(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram, arg0: str, arg1: dict[str, MaterialX_v1_39_5::GlslProgram::Input], arg2: dict[str, MaterialX_v1_39_5::GlslProgram::Input], arg3: bool) -> None

        Find the locations in the program which starts with a given variable name.

        Args:
            variable: Variable to search for
            variableList: List of program inputs to search
            foundList: Returned list of found program inputs. Empty if none found.
            exactMatch: Search for exact variable name match.
        """
    def getAttributesList(self, *args, **kwargs):
        """getAttributesList(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram) -> dict[str, MaterialX_v1_39_5::GlslProgram::Input]

        Get list of program input attributes.

        Returns:
            Program attributes list.
        """
    def getShader(self) -> MaterialX.PyMaterialXGenShader.Shader:
        """getShader(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram) -> MaterialX.PyMaterialXGenShader.Shader

        Return the shader, if any, used to generate this program.
        """
    def getStageSourceCode(self, arg0: str) -> str:
        """getStageSourceCode(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram, arg0: str) -> str

        Get source code string for a given stage.

        Returns:
            Shader stage string. String is empty if not found.
        """
    def getUniformsList(self, *args, **kwargs):
        """getUniformsList(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram) -> dict[str, MaterialX_v1_39_5::GlslProgram::Input]

        Get list of program input uniforms.

        Returns:
            Program uniforms list.
        """
    def hasActiveAttributes(self) -> bool:
        """hasActiveAttributes(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram) -> bool

        Return true if the program has active attributes.
        """
    def hasBuiltData(self) -> bool:
        """hasBuiltData(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram) -> bool

        Return true if built shader program data is present.
        """
    def setStages(self, arg0: MaterialX.PyMaterialXGenShader.Shader) -> None:
        """setStages(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram, arg0: MaterialX.PyMaterialXGenShader.Shader) -> None

        Set up code stages to validate based on an input hardware shader.

        Args:
            shader: Hardware shader to use
        """
    def unbind(self) -> None:
        """unbind(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram) -> None

        Unbind the program. Equivalent to binding no program.
        """
    def unbindGeometry(self) -> None:
        """unbindGeometry(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram) -> None

        Unbind all geometry from this material.
        """

class GlslRenderer(MaterialX.PyMaterialXRender.ShaderRenderer):
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def captureImage(self, arg0: MaterialX.PyMaterialXRender.Image) -> MaterialX.PyMaterialXRender.Image:
        """captureImage(self: MaterialX.PyMaterialXRenderGlsl.GlslRenderer, arg0: MaterialX.PyMaterialXRender.Image) -> MaterialX.PyMaterialXRender.Image

        Capture the current contents of the off-screen hardware buffer as an image.
        """
    @staticmethod
    def create(arg0: int, arg1: int, arg2: MaterialX.PyMaterialXRender.BaseType) -> GlslRenderer:
        """create(arg0: int, arg1: int, arg2: MaterialX.PyMaterialXRender.BaseType) -> MaterialX.PyMaterialXRenderGlsl.GlslRenderer"""
    @overload
    def createProgram(self, arg0: MaterialX.PyMaterialXGenShader.Shader) -> None:
        """createProgram(*args, **kwargs)
        Overloaded function.

        1. createProgram(self: MaterialX.PyMaterialXRenderGlsl.GlslRenderer, arg0: MaterialX.PyMaterialXGenShader.Shader) -> None

        Create GLSL program based on shader stage source code.

        Args:
            stages: Map of name and source code for the shader stages.

        2. createProgram(self: MaterialX.PyMaterialXRenderGlsl.GlslRenderer, arg0: dict[str, str]) -> None

        Create GLSL program based on shader stage source code.

        Args:
            stages: Map of name and source code for the shader stages.
        """
    @overload
    def createProgram(self, arg0: dict[str, str]) -> None:
        """createProgram(*args, **kwargs)
        Overloaded function.

        1. createProgram(self: MaterialX.PyMaterialXRenderGlsl.GlslRenderer, arg0: MaterialX.PyMaterialXGenShader.Shader) -> None

        Create GLSL program based on shader stage source code.

        Args:
            stages: Map of name and source code for the shader stages.

        2. createProgram(self: MaterialX.PyMaterialXRenderGlsl.GlslRenderer, arg0: dict[str, str]) -> None

        Create GLSL program based on shader stage source code.

        Args:
            stages: Map of name and source code for the shader stages.
        """
    def getProgram(self) -> GlslProgram:
        """getProgram(self: MaterialX.PyMaterialXRenderGlsl.GlslRenderer) -> MaterialX.PyMaterialXRenderGlsl.GlslProgram

        Return the underlying GLSL program.
        """
    def initialize(self, renderContextHandle: capsule = ...) -> None:
        """initialize(self: MaterialX.PyMaterialXRenderGlsl.GlslRenderer, renderContextHandle: capsule = None) -> None

        Initialize with the given implementation element.

        Initialization must set the name and hash for the implementation, as well as any other data needed to emit code for the node.
        """
    def render(self) -> None:
        """render(self: MaterialX.PyMaterialXRenderGlsl.GlslRenderer) -> None

        Render the current program to an offscreen buffer.
        """
    def renderTextureSpace(self, arg0: MaterialX.PyMaterialXCore.Vector2, arg1: MaterialX.PyMaterialXCore.Vector2) -> None:
        """renderTextureSpace(self: MaterialX.PyMaterialXRenderGlsl.GlslRenderer, arg0: MaterialX.PyMaterialXCore.Vector2, arg1: MaterialX.PyMaterialXCore.Vector2) -> None

        Render the current program in texture space to an off-screen buffer.
        """
    def validateInputs(self) -> None:
        """validateInputs(self: MaterialX.PyMaterialXRenderGlsl.GlslRenderer) -> None

        Validate inputs for the program.
        """

class Input:
    INVALID_OPENGL_TYPE: ClassVar[int] = ...
    gltype: int
    isConstant: bool
    location: int
    path: str
    size: int
    typeString: str
    value: MaterialX.PyMaterialXCore.Value
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: str) -> None:
        """__init__(self: MaterialX.PyMaterialXRenderGlsl.Input, arg0: int, arg1: int, arg2: int, arg3: str) -> None"""

class TextureBaker(GlslRenderer):
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def bakeAllMaterials(self, arg0: MaterialX.PyMaterialXCore.Document, arg1: MaterialX.PyMaterialXFormat.FileSearchPath, arg2: MaterialX.PyMaterialXFormat.FilePath) -> None:
        """bakeAllMaterials(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker, arg0: MaterialX.PyMaterialXCore.Document, arg1: MaterialX.PyMaterialXFormat.FileSearchPath, arg2: MaterialX.PyMaterialXFormat.FilePath) -> None

        Bake materials in the given document and write them to disk.

        If multiple documents are written, then the given output filename will be used as a template.
        """
    def bakeMaterialToDoc(self, arg0: MaterialX.PyMaterialXCore.Document, arg1: MaterialX.PyMaterialXFormat.FileSearchPath, arg2: str, arg3: list[str], arg4: str) -> MaterialX.PyMaterialXCore.Document:
        """bakeMaterialToDoc(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker, arg0: MaterialX.PyMaterialXCore.Document, arg1: MaterialX.PyMaterialXFormat.FileSearchPath, arg2: str, arg3: list[str], arg4: str) -> MaterialX.PyMaterialXCore.Document

        Bake material to document in memory and write baked textures to disk.
        """
    @staticmethod
    def create(arg0: int, arg1: int, arg2: MaterialX.PyMaterialXRender.BaseType) -> TextureBaker:
        """create(arg0: int, arg1: int, arg2: MaterialX.PyMaterialXRender.BaseType) -> MaterialX.PyMaterialXRenderGlsl.TextureBaker"""
    def getAverageImages(self) -> bool:
        """getAverageImages(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker) -> bool

        Return whether images should be averaged to generate constants.
        """
    def getBakedGeomInfoName(self) -> str:
        """getBakedGeomInfoName(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker) -> str

        Return the name of the baked geometry info element.
        """
    def getBakedGraphName(self) -> str:
        """getBakedGraphName(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker) -> str

        Return the name of the baked graph element.
        """
    def getColorSpace(self) -> str:
        """getColorSpace(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker) -> str

        Return the element's color space string.
        """
    def getDistanceUnit(self) -> str:
        """getDistanceUnit(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker) -> str

        Return the distance unit to which textures are baked.
        """
    def getExtension(self) -> str:
        """getExtension(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker) -> str

        Return the file extension of the given path.
        """
    def getHashImageNames(self) -> bool:
        """getHashImageNames(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker) -> bool

        Return whether automatic baked texture resolution is set.
        """
    def getOptimizeConstants(self) -> bool:
        """getOptimizeConstants(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker) -> bool

        Return whether uniform textures should be stored as constants.
        """
    def getOutputImagePath(self) -> MaterialX.PyMaterialXFormat.FilePath:
        """getOutputImagePath(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker) -> MaterialX.PyMaterialXFormat.FilePath

        Get the current output location for baked texture images.
        """
    def getTextureFilenameTemplate(self) -> str:
        """getTextureFilenameTemplate(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker) -> str

        Get the texture filename template.
        """
    def getTextureSpaceMax(self) -> MaterialX.PyMaterialXCore.Vector2:
        """getTextureSpaceMax(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker) -> MaterialX.PyMaterialXCore.Vector2

        Return the maximum texcoords used in texture baking.
        """
    def getTextureSpaceMin(self) -> MaterialX.PyMaterialXCore.Vector2:
        """getTextureSpaceMin(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker) -> MaterialX.PyMaterialXCore.Vector2

        Return the minimum texcoords used in texture baking.
        """
    def setAverageImages(self, arg0: bool) -> None:
        """setAverageImages(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker, arg0: bool) -> None

        Set whether images should be averaged to generate constants. Defaults to false.
        """
    def setBakedGeomInfoName(self, arg0: str) -> None:
        """setBakedGeomInfoName(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker, arg0: str) -> None

        Set the name of the baked geometry info element.
        """
    def setBakedGraphName(self, arg0: str) -> None:
        """setBakedGraphName(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker, arg0: str) -> None

        Set the name of the baked graph element.
        """
    def setColorSpace(self, arg0: str) -> None:
        """setColorSpace(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker, arg0: str) -> None

        Set the element's color space string.
        """
    def setDistanceUnit(self, arg0: str) -> None:
        """setDistanceUnit(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker, arg0: str) -> None

        Set the distance unit to which textures are baked. Defaults to meters.
        """
    def setExtension(self, arg0: str) -> None:
        """setExtension(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker, arg0: str) -> None

        Set the file extension for baked textures.
        """
    def setFilenameTemplateVarOverride(self, arg0: str, arg1: str) -> None:
        """setFilenameTemplateVarOverride(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker, arg0: str, arg1: str) -> None

        Set texFilenameOverrides if template variable exists.
        """
    def setHashImageNames(self, arg0: bool) -> None:
        """setHashImageNames(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker, arg0: bool) -> None

        Set whether to create a short name for baked images by hashing the baked image filenames This is useful for file systems which may have a maximum limit on filename size.

        By default names are not hashed.
        """
    def setOptimizeConstants(self, arg0: bool) -> None:
        """setOptimizeConstants(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker, arg0: bool) -> None

        Set whether uniform textures should be stored as constants. Defaults to true.
        """
    def setOutputImagePath(self, arg0: MaterialX.PyMaterialXFormat.FilePath) -> None:
        """setOutputImagePath(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker, arg0: MaterialX.PyMaterialXFormat.FilePath) -> None

        Set the output location for baked texture images.

        Defaults to the root folder of the destination material.
        """
    def setTextureFilenameTemplate(self, arg0: str) -> None:
        """setTextureFilenameTemplate(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker, arg0: str) -> None

        Set the texture filename template.
        """
    def setTextureSpaceMax(self, arg0: MaterialX.PyMaterialXCore.Vector2) -> None:
        """setTextureSpaceMax(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker, arg0: MaterialX.PyMaterialXCore.Vector2) -> None

        Set the maximum texcoords used in texture baking. Defaults to 1, 1.
        """
    def setTextureSpaceMin(self, arg0: MaterialX.PyMaterialXCore.Vector2) -> None:
        """setTextureSpaceMin(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker, arg0: MaterialX.PyMaterialXCore.Vector2) -> None

        Set the minimum texcoords used in texture baking. Defaults to 0, 0.
        """
    def setupUnitSystem(self, arg0: MaterialX.PyMaterialXCore.Document) -> None:
        """setupUnitSystem(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker, arg0: MaterialX.PyMaterialXCore.Document) -> None

        Set up the unit definitions to be used in baking.
        """
    def writeDocumentPerMaterial(self, arg0: bool) -> None:
        """writeDocumentPerMaterial(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker, arg0: bool) -> None

        Set whether to write a separate document per material when calling bakeAllMaterials.

        By default separate documents are written.
        """
