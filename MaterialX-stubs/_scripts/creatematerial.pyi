import MaterialX as mx
from _typeshed import Incomplete

UDIM_TOKEN: str
UDIM_REGEX: str
TEXTURE_EXTENSIONS: Incomplete
INPUT_ALIASES: Incomplete

class UdimFilePath(mx.FilePath):
    def __init__(self, pathString) -> None: ...
    def asPattern(self): ...
    def isUdim(self): ...
    def getUdimFiles(self): ...
    def getUdimNumbers(self): ...
    def getNameWithoutExtension(self): ...

def listTextures(textureDir, texturePrefix=None):
    """
    Return a list of texture filenames matching known extensions.
    """
def findBestMatch(textureName, shadingModel):
    """
    Given a texture name and shading model, return the shader input that is the closest match.
    """
def buildDocument(textureFiles, mtlxFile, shadingModel, colorspace, useTiledImage):
    """
    Build a MaterialX document from the given textures and shading model.
    """
def main() -> None: ...
