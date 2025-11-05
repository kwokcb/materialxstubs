import MaterialX.PyMaterialXCore
import MaterialX.PyMaterialXGenShader

class MslResourceBindingContext(MaterialX.PyMaterialXGenShader.HwResourceBindingContext):
    def __init__(self, arg0: int, arg1: int) -> None:
        """__init__(self: MaterialX.PyMaterialXGenMsl.MslResourceBindingContext, arg0: int, arg1: int) -> None"""
    @staticmethod
    def create(arg0: int, arg1: int) -> MslResourceBindingContext:
        """create(arg0: int, arg1: int) -> MaterialX.PyMaterialXGenMsl.MslResourceBindingContext"""
    def emitDirectives(self, arg0: MaterialX.PyMaterialXGenShader.GenContext, arg1: MaterialX.PyMaterialXGenShader.ShaderStage) -> None:
        """emitDirectives(self: MaterialX.PyMaterialXGenMsl.MslResourceBindingContext, arg0: MaterialX.PyMaterialXGenShader.GenContext, arg1: MaterialX.PyMaterialXGenShader.ShaderStage) -> None"""
    def emitResourceBindings(self, arg0: MaterialX.PyMaterialXGenShader.GenContext, arg1: MaterialX.PyMaterialXGenShader.VariableBlock, arg2: MaterialX.PyMaterialXGenShader.ShaderStage) -> None:
        """emitResourceBindings(self: MaterialX.PyMaterialXGenMsl.MslResourceBindingContext, arg0: MaterialX.PyMaterialXGenShader.GenContext, arg1: MaterialX.PyMaterialXGenShader.VariableBlock, arg2: MaterialX.PyMaterialXGenShader.ShaderStage) -> None"""

class MslShaderGenerator(MaterialX.PyMaterialXGenShader.HwShaderGenerator):
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def create() -> MaterialX.PyMaterialXGenShader.ShaderGenerator:
        """create() -> MaterialX.PyMaterialXGenShader.ShaderGenerator"""
    def generate(self, arg0: str, arg1: MaterialX.PyMaterialXCore.Element, arg2: MaterialX.PyMaterialXGenShader.GenContext) -> MaterialX.PyMaterialXGenShader.Shader:
        """generate(self: MaterialX.PyMaterialXGenMsl.MslShaderGenerator, arg0: str, arg1: MaterialX.PyMaterialXCore.Element, arg2: MaterialX.PyMaterialXGenShader.GenContext) -> MaterialX.PyMaterialXGenShader.Shader"""
    def getTarget(self) -> str:
        """getTarget(self: MaterialX.PyMaterialXGenMsl.MslShaderGenerator) -> str"""
    def getVersion(self) -> str:
        """getVersion(self: MaterialX.PyMaterialXGenMsl.MslShaderGenerator) -> str"""
