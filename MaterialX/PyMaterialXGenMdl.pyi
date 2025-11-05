import MaterialX.PyMaterialXGenShader

class MdlShaderGenerator(MaterialX.PyMaterialXGenShader.ShaderGenerator):
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def create() -> MaterialX.PyMaterialXGenShader.ShaderGenerator:
        """create() -> MaterialX.PyMaterialXGenShader.ShaderGenerator"""
    def getTarget(self) -> str:
        """getTarget(self: MaterialX.PyMaterialXGenMdl.MdlShaderGenerator) -> str

        Return a unique identifier for the target this generator is for.
        """
