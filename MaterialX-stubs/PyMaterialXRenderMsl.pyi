import MaterialX.PyMaterialXCore
import MaterialX.PyMaterialXFormat
import MaterialX.PyMaterialXGenShader
import MaterialX.PyMaterialXRender
from typing import overload

class Input:
    isConstant: bool
    location: int
    path: str
    size: int
    typeString: str
    value: MaterialX.PyMaterialXCore.Value
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: str) -> None:
        """__init__(self: MaterialX.PyMaterialXRenderMsl.Input, arg0: int, arg1: int, arg2: int, arg3: str) -> None"""

class MetalTextureHandler(MaterialX.PyMaterialXRender.ImageHandler):
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def bindImage(self, arg0: MaterialX.PyMaterialXRender.Image) -> bool:
        """bindImage(self: MaterialX.PyMaterialXRenderMsl.MetalTextureHandler, arg0: MaterialX.PyMaterialXRender.Image) -> bool"""
    @staticmethod
    def create(arg0, arg1: MaterialX.PyMaterialXRender.ImageLoader) -> MetalTextureHandler:
        """create(arg0: objc_object<MTLDevice>, arg1: MaterialX.PyMaterialXRender.ImageLoader) -> MaterialX.PyMaterialXRenderMsl.MetalTextureHandler"""
    def createRenderResources(self, arg0: MaterialX.PyMaterialXRender.Image, arg1: bool, arg2: bool) -> bool:
        """createRenderResources(self: MaterialX.PyMaterialXRenderMsl.MetalTextureHandler, arg0: MaterialX.PyMaterialXRender.Image, arg1: bool, arg2: bool) -> bool"""
    def releaseRenderResources(self, image: MaterialX.PyMaterialXRender.Image = ...) -> None:
        """releaseRenderResources(self: MaterialX.PyMaterialXRenderMsl.MetalTextureHandler, image: MaterialX.PyMaterialXRender.Image = None) -> None"""
    def unbindImage(self, arg0: MaterialX.PyMaterialXRender.Image) -> bool:
        """unbindImage(self: MaterialX.PyMaterialXRenderMsl.MetalTextureHandler, arg0: MaterialX.PyMaterialXRender.Image) -> bool"""

class MslProgram:
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def addStage(self, arg0: str, arg1: str) -> None:
        """addStage(self: MaterialX.PyMaterialXRenderMsl.MslProgram, arg0: str, arg1: str) -> None"""
    def bind(self, arg0) -> bool:
        """bind(self: MaterialX.PyMaterialXRenderMsl.MslProgram, arg0: objc_object<MTLRenderCommandEncoder>) -> bool"""
    def bindAttribute(self, arg0, arg1, arg2: MaterialX.PyMaterialXRender.Mesh) -> None:
        """bindAttribute(self: MaterialX.PyMaterialXRenderMsl.MslProgram, arg0: objc_object<MTLRenderCommandEncoder>, arg1: dict[str, MaterialX_v1_39_4::MslProgram::Input], arg2: MaterialX.PyMaterialXRender.Mesh) -> None"""
    def bindLighting(self, arg0: MaterialX.PyMaterialXRender.LightHandler, arg1: MaterialX.PyMaterialXRender.ImageHandler) -> None:
        """bindLighting(self: MaterialX.PyMaterialXRenderMsl.MslProgram, arg0: MaterialX.PyMaterialXRender.LightHandler, arg1: MaterialX.PyMaterialXRender.ImageHandler) -> None"""
    def bindMesh(self, arg0, arg1: MaterialX.PyMaterialXRender.Mesh) -> None:
        """bindMesh(self: MaterialX.PyMaterialXRenderMsl.MslProgram, arg0: objc_object<MTLRenderCommandEncoder>, arg1: MaterialX.PyMaterialXRender.Mesh) -> None"""
    def bindPartition(self, arg0: MaterialX.PyMaterialXRender.MeshPartition) -> None:
        """bindPartition(self: MaterialX.PyMaterialXRenderMsl.MslProgram, arg0: MaterialX.PyMaterialXRender.MeshPartition) -> None"""
    def bindTextures(self, arg0, arg1: MaterialX.PyMaterialXRender.LightHandler, arg2: MaterialX.PyMaterialXRender.ImageHandler) -> None:
        """bindTextures(self: MaterialX.PyMaterialXRenderMsl.MslProgram, arg0: objc_object<MTLRenderCommandEncoder>, arg1: MaterialX.PyMaterialXRender.LightHandler, arg2: MaterialX.PyMaterialXRender.ImageHandler) -> None"""
    def bindTimeAndFrame(self, time: float = ..., frame: float = ...) -> None:
        """bindTimeAndFrame(self: MaterialX.PyMaterialXRenderMsl.MslProgram, time: float = 0.0, frame: float = 1.0) -> None"""
    def bindUniform(self, arg0: str, arg1: MaterialX.PyMaterialXCore.Value, arg2: bool) -> None:
        """bindUniform(self: MaterialX.PyMaterialXRenderMsl.MslProgram, arg0: str, arg1: MaterialX.PyMaterialXCore.Value, arg2: bool) -> None"""
    def bindViewInformation(self, arg0: MaterialX.PyMaterialXRender.Camera) -> None:
        """bindViewInformation(self: MaterialX.PyMaterialXRenderMsl.MslProgram, arg0: MaterialX.PyMaterialXRender.Camera) -> None"""
    def build(self, *args, **kwargs):
        """build(self: MaterialX.PyMaterialXRenderMsl.MslProgram, arg0: objc_object<MTLDevice>, arg1: MaterialX_v1_39_4::MetalFramebuffer) -> objc_object<MTLRenderPipelineState>"""
    @staticmethod
    def create() -> MslProgram:
        """create() -> MaterialX.PyMaterialXRenderMsl.MslProgram"""
    def findInputs(self, arg0: str, arg1, arg2, arg3: bool) -> None:
        """findInputs(self: MaterialX.PyMaterialXRenderMsl.MslProgram, arg0: str, arg1: dict[str, MaterialX_v1_39_4::MslProgram::Input], arg2: dict[str, MaterialX_v1_39_4::MslProgram::Input], arg3: bool) -> None"""
    def getAttributesList(self, *args, **kwargs):
        """getAttributesList(self: MaterialX.PyMaterialXRenderMsl.MslProgram) -> dict[str, MaterialX_v1_39_4::MslProgram::Input]"""
    def getShader(self) -> MaterialX.PyMaterialXGenShader.Shader:
        """getShader(self: MaterialX.PyMaterialXRenderMsl.MslProgram) -> MaterialX.PyMaterialXGenShader.Shader"""
    def getStageSourceCode(self, arg0: str) -> str:
        """getStageSourceCode(self: MaterialX.PyMaterialXRenderMsl.MslProgram, arg0: str) -> str"""
    def getUniformsList(self, *args, **kwargs):
        """getUniformsList(self: MaterialX.PyMaterialXRenderMsl.MslProgram) -> dict[str, MaterialX_v1_39_4::MslProgram::Input]"""
    def prepareUsedResources(self, arg0, arg1: MaterialX.PyMaterialXRender.Camera, arg2: MaterialX.PyMaterialXRender.GeometryHandler, arg3: MaterialX.PyMaterialXRender.ImageHandler, arg4: MaterialX.PyMaterialXRender.LightHandler) -> None:
        """prepareUsedResources(self: MaterialX.PyMaterialXRenderMsl.MslProgram, arg0: objc_object<MTLRenderCommandEncoder>, arg1: MaterialX.PyMaterialXRender.Camera, arg2: MaterialX.PyMaterialXRender.GeometryHandler, arg3: MaterialX.PyMaterialXRender.ImageHandler, arg4: MaterialX.PyMaterialXRender.LightHandler) -> None"""
    def setStages(self, arg0: MaterialX.PyMaterialXGenShader.Shader) -> None:
        """setStages(self: MaterialX.PyMaterialXRenderMsl.MslProgram, arg0: MaterialX.PyMaterialXGenShader.Shader) -> None"""
    def unbindGeometry(self) -> None:
        """unbindGeometry(self: MaterialX.PyMaterialXRenderMsl.MslProgram) -> None"""

class MslRenderer(MaterialX.PyMaterialXRender.ShaderRenderer):
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def captureImage(self, arg0: MaterialX.PyMaterialXRender.Image) -> MaterialX.PyMaterialXRender.Image:
        """captureImage(self: MaterialX.PyMaterialXRenderMsl.MslRenderer, arg0: MaterialX.PyMaterialXRender.Image) -> MaterialX.PyMaterialXRender.Image"""
    @staticmethod
    def create(arg0: int, arg1: int, arg2: MaterialX.PyMaterialXRender.BaseType) -> MslRenderer:
        """create(arg0: int, arg1: int, arg2: MaterialX.PyMaterialXRender.BaseType) -> MaterialX.PyMaterialXRenderMsl.MslRenderer"""
    @overload
    def createProgram(self, arg0: MaterialX.PyMaterialXGenShader.Shader) -> None:
        """createProgram(*args, **kwargs)
        Overloaded function.

        1. createProgram(self: MaterialX.PyMaterialXRenderMsl.MslRenderer, arg0: MaterialX.PyMaterialXGenShader.Shader) -> None

        2. createProgram(self: MaterialX.PyMaterialXRenderMsl.MslRenderer, arg0: dict[str, str]) -> None
        """
    @overload
    def createProgram(self, arg0: dict[str, str]) -> None:
        """createProgram(*args, **kwargs)
        Overloaded function.

        1. createProgram(self: MaterialX.PyMaterialXRenderMsl.MslRenderer, arg0: MaterialX.PyMaterialXGenShader.Shader) -> None

        2. createProgram(self: MaterialX.PyMaterialXRenderMsl.MslRenderer, arg0: dict[str, str]) -> None
        """
    def getProgram(self) -> MslProgram:
        """getProgram(self: MaterialX.PyMaterialXRenderMsl.MslRenderer) -> MaterialX.PyMaterialXRenderMsl.MslProgram"""
    def initialize(self, renderContextHandle: capsule = ...) -> None:
        """initialize(self: MaterialX.PyMaterialXRenderMsl.MslRenderer, renderContextHandle: capsule = None) -> None"""
    def render(self) -> None:
        """render(self: MaterialX.PyMaterialXRenderMsl.MslRenderer) -> None"""
    def renderTextureSpace(self, arg0: MaterialX.PyMaterialXCore.Vector2, arg1: MaterialX.PyMaterialXCore.Vector2) -> None:
        """renderTextureSpace(self: MaterialX.PyMaterialXRenderMsl.MslRenderer, arg0: MaterialX.PyMaterialXCore.Vector2, arg1: MaterialX.PyMaterialXCore.Vector2) -> None"""
    def validateInputs(self) -> None:
        """validateInputs(self: MaterialX.PyMaterialXRenderMsl.MslRenderer) -> None"""

class TextureBaker(MslRenderer):
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def bakeAllMaterials(self, arg0: MaterialX.PyMaterialXCore.Document, arg1: MaterialX.PyMaterialXFormat.FileSearchPath, arg2: MaterialX.PyMaterialXFormat.FilePath) -> None:
        """bakeAllMaterials(self: MaterialX.PyMaterialXRenderMsl.TextureBaker, arg0: MaterialX.PyMaterialXCore.Document, arg1: MaterialX.PyMaterialXFormat.FileSearchPath, arg2: MaterialX.PyMaterialXFormat.FilePath) -> None"""
    def bakeMaterialToDoc(self, arg0: MaterialX.PyMaterialXCore.Document, arg1: MaterialX.PyMaterialXFormat.FileSearchPath, arg2: str, arg3: list[str], arg4: str) -> MaterialX.PyMaterialXCore.Document:
        """bakeMaterialToDoc(self: MaterialX.PyMaterialXRenderMsl.TextureBaker, arg0: MaterialX.PyMaterialXCore.Document, arg1: MaterialX.PyMaterialXFormat.FileSearchPath, arg2: str, arg3: list[str], arg4: str) -> MaterialX.PyMaterialXCore.Document"""
    @staticmethod
    def create(arg0: int, arg1: int, arg2: MaterialX.PyMaterialXRender.BaseType) -> TextureBaker:
        """create(arg0: int, arg1: int, arg2: MaterialX.PyMaterialXRender.BaseType) -> MaterialX.PyMaterialXRenderMsl.TextureBaker"""
    def getAverageImages(self) -> bool:
        """getAverageImages(self: MaterialX.PyMaterialXRenderMsl.TextureBaker) -> bool"""
    def getBakedGeomInfoName(self) -> str:
        """getBakedGeomInfoName(self: MaterialX.PyMaterialXRenderMsl.TextureBaker) -> str"""
    def getBakedGraphName(self) -> str:
        """getBakedGraphName(self: MaterialX.PyMaterialXRenderMsl.TextureBaker) -> str"""
    def getColorSpace(self) -> str:
        """getColorSpace(self: MaterialX.PyMaterialXRenderMsl.TextureBaker) -> str"""
    def getDistanceUnit(self) -> str:
        """getDistanceUnit(self: MaterialX.PyMaterialXRenderMsl.TextureBaker) -> str"""
    def getExtension(self) -> str:
        """getExtension(self: MaterialX.PyMaterialXRenderMsl.TextureBaker) -> str"""
    def getHashImageNames(self) -> bool:
        """getHashImageNames(self: MaterialX.PyMaterialXRenderMsl.TextureBaker) -> bool"""
    def getOptimizeConstants(self) -> bool:
        """getOptimizeConstants(self: MaterialX.PyMaterialXRenderMsl.TextureBaker) -> bool"""
    def getOutputImagePath(self) -> MaterialX.PyMaterialXFormat.FilePath:
        """getOutputImagePath(self: MaterialX.PyMaterialXRenderMsl.TextureBaker) -> MaterialX.PyMaterialXFormat.FilePath"""
    def getTextureFilenameTemplate(self) -> str:
        """getTextureFilenameTemplate(self: MaterialX.PyMaterialXRenderMsl.TextureBaker) -> str"""
    def getTextureSpaceMax(self) -> MaterialX.PyMaterialXCore.Vector2:
        """getTextureSpaceMax(self: MaterialX.PyMaterialXRenderMsl.TextureBaker) -> MaterialX.PyMaterialXCore.Vector2"""
    def getTextureSpaceMin(self) -> MaterialX.PyMaterialXCore.Vector2:
        """getTextureSpaceMin(self: MaterialX.PyMaterialXRenderMsl.TextureBaker) -> MaterialX.PyMaterialXCore.Vector2"""
    def setAverageImages(self, arg0: bool) -> None:
        """setAverageImages(self: MaterialX.PyMaterialXRenderMsl.TextureBaker, arg0: bool) -> None"""
    def setBakedGeomInfoName(self, arg0: str) -> None:
        """setBakedGeomInfoName(self: MaterialX.PyMaterialXRenderMsl.TextureBaker, arg0: str) -> None"""
    def setBakedGraphName(self, arg0: str) -> None:
        """setBakedGraphName(self: MaterialX.PyMaterialXRenderMsl.TextureBaker, arg0: str) -> None"""
    def setColorSpace(self, arg0: str) -> None:
        """setColorSpace(self: MaterialX.PyMaterialXRenderMsl.TextureBaker, arg0: str) -> None"""
    def setDistanceUnit(self, arg0: str) -> None:
        """setDistanceUnit(self: MaterialX.PyMaterialXRenderMsl.TextureBaker, arg0: str) -> None"""
    def setExtension(self, arg0: str) -> None:
        """setExtension(self: MaterialX.PyMaterialXRenderMsl.TextureBaker, arg0: str) -> None"""
    def setFilenameTemplateVarOverride(self, arg0: str, arg1: str) -> None:
        """setFilenameTemplateVarOverride(self: MaterialX.PyMaterialXRenderMsl.TextureBaker, arg0: str, arg1: str) -> None"""
    def setHashImageNames(self, arg0: bool) -> None:
        """setHashImageNames(self: MaterialX.PyMaterialXRenderMsl.TextureBaker, arg0: bool) -> None"""
    def setOptimizeConstants(self, arg0: bool) -> None:
        """setOptimizeConstants(self: MaterialX.PyMaterialXRenderMsl.TextureBaker, arg0: bool) -> None"""
    def setOutputImagePath(self, arg0: MaterialX.PyMaterialXFormat.FilePath) -> None:
        """setOutputImagePath(self: MaterialX.PyMaterialXRenderMsl.TextureBaker, arg0: MaterialX.PyMaterialXFormat.FilePath) -> None"""
    def setTextureFilenameTemplate(self, arg0: str) -> None:
        """setTextureFilenameTemplate(self: MaterialX.PyMaterialXRenderMsl.TextureBaker, arg0: str) -> None"""
    def setTextureSpaceMax(self, arg0: MaterialX.PyMaterialXCore.Vector2) -> None:
        """setTextureSpaceMax(self: MaterialX.PyMaterialXRenderMsl.TextureBaker, arg0: MaterialX.PyMaterialXCore.Vector2) -> None"""
    def setTextureSpaceMin(self, arg0: MaterialX.PyMaterialXCore.Vector2) -> None:
        """setTextureSpaceMin(self: MaterialX.PyMaterialXRenderMsl.TextureBaker, arg0: MaterialX.PyMaterialXCore.Vector2) -> None"""
    def setupUnitSystem(self, arg0: MaterialX.PyMaterialXCore.Document) -> None:
        """setupUnitSystem(self: MaterialX.PyMaterialXRenderMsl.TextureBaker, arg0: MaterialX.PyMaterialXCore.Document) -> None"""
    def writeDocumentPerMaterial(self, arg0: bool) -> None:
        """writeDocumentPerMaterial(self: MaterialX.PyMaterialXRenderMsl.TextureBaker, arg0: bool) -> None"""
