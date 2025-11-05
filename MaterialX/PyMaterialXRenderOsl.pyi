import MaterialX.PyMaterialXFormat
import MaterialX.PyMaterialXGenShader
import MaterialX.PyMaterialXRender
from typing import ClassVar, overload

class OslRenderer(MaterialX.PyMaterialXRender.ShaderRenderer):
    OSL_CLOSURE_COLOR_STRING: ClassVar[str] = ...
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def captureImage(self, arg0: MaterialX.PyMaterialXRender.Image) -> MaterialX.PyMaterialXRender.Image:
        """captureImage(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: MaterialX.PyMaterialXRender.Image) -> MaterialX.PyMaterialXRender.Image"""
    def compileOSL(self, arg0: MaterialX.PyMaterialXFormat.FilePath) -> None:
        """compileOSL(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: MaterialX.PyMaterialXFormat.FilePath) -> None"""
    @staticmethod
    def create(arg0: int, arg1: int, arg2: MaterialX.PyMaterialXRender.BaseType) -> OslRenderer:
        """create(arg0: int, arg1: int, arg2: MaterialX.PyMaterialXRender.BaseType) -> MaterialX.PyMaterialXRenderOsl.OslRenderer"""
    @overload
    def createProgram(self, arg0: MaterialX.PyMaterialXGenShader.Shader) -> None:
        """createProgram(*args, **kwargs)
        Overloaded function.

        1. createProgram(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: MaterialX.PyMaterialXGenShader.Shader) -> None

        2. createProgram(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: dict[str, str]) -> None
        """
    @overload
    def createProgram(self, arg0: dict[str, str]) -> None:
        """createProgram(*args, **kwargs)
        Overloaded function.

        1. createProgram(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: MaterialX.PyMaterialXGenShader.Shader) -> None

        2. createProgram(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: dict[str, str]) -> None
        """
    def initialize(self, renderContextHandle: capsule = ...) -> None:
        """initialize(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, renderContextHandle: capsule = None) -> None"""
    def render(self) -> None:
        """render(self: MaterialX.PyMaterialXRenderOsl.OslRenderer) -> None"""
    def setOslCompilerExecutable(self, arg0: MaterialX.PyMaterialXFormat.FilePath) -> None:
        """setOslCompilerExecutable(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: MaterialX.PyMaterialXFormat.FilePath) -> None"""
    def setOslIncludePath(self, arg0: MaterialX.PyMaterialXFormat.FileSearchPath) -> None:
        """setOslIncludePath(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: MaterialX.PyMaterialXFormat.FileSearchPath) -> None"""
    def setOslOutputFilePath(self, arg0: MaterialX.PyMaterialXFormat.FilePath) -> None:
        """setOslOutputFilePath(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: MaterialX.PyMaterialXFormat.FilePath) -> None"""
    def setOslShaderName(self, arg0: str) -> None:
        """setOslShaderName(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: str) -> None"""
    def setOslShaderOutput(self, arg0: str, arg1: str) -> None:
        """setOslShaderOutput(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: str, arg1: str) -> None"""
    def setOslTestRenderExecutable(self, arg0: MaterialX.PyMaterialXFormat.FilePath) -> None:
        """setOslTestRenderExecutable(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: MaterialX.PyMaterialXFormat.FilePath) -> None"""
    def setOslTestRenderSceneTemplateFile(self, arg0: MaterialX.PyMaterialXFormat.FilePath) -> None:
        """setOslTestRenderSceneTemplateFile(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: MaterialX.PyMaterialXFormat.FilePath) -> None"""
    def setOslTestShadeExecutable(self, arg0: MaterialX.PyMaterialXFormat.FilePath) -> None:
        """setOslTestShadeExecutable(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: MaterialX.PyMaterialXFormat.FilePath) -> None"""
    def setOslUtilityOSOPath(self, arg0: MaterialX.PyMaterialXFormat.FilePath) -> None:
        """setOslUtilityOSOPath(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: MaterialX.PyMaterialXFormat.FilePath) -> None"""
    def setShaderParameterOverrides(self, arg0: list[str]) -> None:
        """setShaderParameterOverrides(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: list[str]) -> None"""
    def useTestRender(self, arg0: bool) -> None:
        """useTestRender(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: bool) -> None"""
    def validateInputs(self) -> None:
        """validateInputs(self: MaterialX.PyMaterialXRenderOsl.OslRenderer) -> None"""
