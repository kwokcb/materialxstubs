import MaterialX.PyMaterialXCore
import MaterialX.PyMaterialXGenShader

OSL_INPUTS: str
OSL_OUTPUTS: str
OSL_UNIFORMS: str

class OslShaderGenerator(MaterialX.PyMaterialXGenShader.ShaderGenerator):
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def create() -> MaterialX.PyMaterialXGenShader.ShaderGenerator:
        """create() -> MaterialX.PyMaterialXGenShader.ShaderGenerator"""
    def generate(self, arg0: str, arg1: MaterialX.PyMaterialXCore.Element, arg2: MaterialX.PyMaterialXGenShader.GenContext) -> MaterialX.PyMaterialXGenShader.Shader:
        """generate(self: MaterialX.PyMaterialXGenOsl.OslShaderGenerator, arg0: str, arg1: MaterialX.PyMaterialXCore.Element, arg2: MaterialX.PyMaterialXGenShader.GenContext) -> MaterialX.PyMaterialXGenShader.Shader

        Generate a shader starting from the given element, translating the element and all dependencies upstream into shader code.
        """
    def getTarget(self) -> str:
        """getTarget(self: MaterialX.PyMaterialXGenOsl.OslShaderGenerator) -> str

        Return a unique identifier for the target this generator is for.
        """
