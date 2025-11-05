import MaterialX.PyMaterialXCore
import MaterialX.PyMaterialXFormat
import MaterialX.PyMaterialXGenShader
from _typeshed import Incomplete
from typing import Callable, ClassVar, overload

FLOAT: BaseType
HALF: BaseType
UINT16: BaseType
UINT8: BaseType

class BaseType:
    __members__: ClassVar[dict] = ...  # read-only
    FLOAT: ClassVar[BaseType] = ...
    HALF: ClassVar[BaseType] = ...
    UINT16: ClassVar[BaseType] = ...
    UINT8: ClassVar[BaseType] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None:
        """__init__(self: MaterialX.PyMaterialXRender.BaseType, value: int) -> None"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: MaterialX.PyMaterialXRender.BaseType) -> int"""
    def __int__(self) -> int:
        """__int__(self: MaterialX.PyMaterialXRender.BaseType) -> int"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class Camera:
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def create() -> Camera:
        """create() -> MaterialX.PyMaterialXRender.Camera"""
    @staticmethod
    def createOrthographicMatrix(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> MaterialX.PyMaterialXCore.Matrix44:
        """createOrthographicMatrix(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> MaterialX.PyMaterialXCore.Matrix44"""
    @staticmethod
    def createPerspectiveMatrix(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> MaterialX.PyMaterialXCore.Matrix44:
        """createPerspectiveMatrix(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> MaterialX.PyMaterialXCore.Matrix44"""
    @staticmethod
    def createViewMatrix(arg0: MaterialX.PyMaterialXCore.Vector3, arg1: MaterialX.PyMaterialXCore.Vector3, arg2: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Matrix44:
        """createViewMatrix(arg0: MaterialX.PyMaterialXCore.Vector3, arg1: MaterialX.PyMaterialXCore.Vector3, arg2: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Matrix44"""
    def getProjectionMatrix(self) -> MaterialX.PyMaterialXCore.Matrix44:
        """getProjectionMatrix(self: MaterialX.PyMaterialXRender.Camera) -> MaterialX.PyMaterialXCore.Matrix44

        Return the projection matrix.
        """
    def getViewDirection(self) -> MaterialX.PyMaterialXCore.Vector3:
        """getViewDirection(self: MaterialX.PyMaterialXRender.Camera) -> MaterialX.PyMaterialXCore.Vector3

        Derive viewer direction from the view matrix.
        """
    def getViewMatrix(self) -> MaterialX.PyMaterialXCore.Matrix44:
        """getViewMatrix(self: MaterialX.PyMaterialXRender.Camera) -> MaterialX.PyMaterialXCore.Matrix44

        Return the view matrix.
        """
    def getViewPosition(self) -> MaterialX.PyMaterialXCore.Vector3:
        """getViewPosition(self: MaterialX.PyMaterialXRender.Camera) -> MaterialX.PyMaterialXCore.Vector3

        Derive viewer position from the view matrix.
        """
    def getViewportSize(self) -> MaterialX.PyMaterialXCore.Vector2:
        """getViewportSize(self: MaterialX.PyMaterialXRender.Camera) -> MaterialX.PyMaterialXCore.Vector2

        Return the size of the viewport window.
        """
    def getWorldMatrix(self) -> MaterialX.PyMaterialXCore.Matrix44:
        """getWorldMatrix(self: MaterialX.PyMaterialXRender.Camera) -> MaterialX.PyMaterialXCore.Matrix44

        Return the world matrix.
        """
    def getWorldViewProjMatrix(self) -> MaterialX.PyMaterialXCore.Matrix44:
        """getWorldViewProjMatrix(self: MaterialX.PyMaterialXRender.Camera) -> MaterialX.PyMaterialXCore.Matrix44

        Compute our full model-view-projection matrix.
        """
    def projectToViewport(self, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3:
        """projectToViewport(self: MaterialX.PyMaterialXRender.Camera, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3

        Project a position from object to viewport space.
        """
    def setProjectionMatrix(self, arg0: MaterialX.PyMaterialXCore.Matrix44) -> None:
        """setProjectionMatrix(self: MaterialX.PyMaterialXRender.Camera, arg0: MaterialX.PyMaterialXCore.Matrix44) -> None

        Set the projection matrix.
        """
    def setViewMatrix(self, arg0: MaterialX.PyMaterialXCore.Matrix44) -> None:
        """setViewMatrix(self: MaterialX.PyMaterialXRender.Camera, arg0: MaterialX.PyMaterialXCore.Matrix44) -> None

        Set the view matrix.
        """
    def setViewportSize(self, arg0: MaterialX.PyMaterialXCore.Vector2) -> None:
        """setViewportSize(self: MaterialX.PyMaterialXRender.Camera, arg0: MaterialX.PyMaterialXCore.Vector2) -> None

        Set the size of the viewport window.
        """
    def setWorldMatrix(self, arg0: MaterialX.PyMaterialXCore.Matrix44) -> None:
        """setWorldMatrix(self: MaterialX.PyMaterialXRender.Camera, arg0: MaterialX.PyMaterialXCore.Matrix44) -> None

        Set the world matrix.
        """
    @staticmethod
    def transformPointPerspective(arg0: MaterialX.PyMaterialXCore.Matrix44, arg1: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3:
        """transformPointPerspective(arg0: MaterialX.PyMaterialXCore.Matrix44, arg1: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3"""
    def unprojectFromViewport(self, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3:
        """unprojectFromViewport(self: MaterialX.PyMaterialXRender.Camera, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3

        Unproject a position from viewport to object space.
        """

class CgltfLoader(GeometryLoader):
    def __init__(self) -> None:
        """__init__(self: MaterialX.PyMaterialXRender.CgltfLoader) -> None"""
    @staticmethod
    def create() -> CgltfLoader:
        """create() -> MaterialX.PyMaterialXRender.CgltfLoader"""
    def load(self, arg0: MaterialX.PyMaterialXFormat.FilePath, arg1: list[Mesh], arg2: bool) -> bool:
        """load(self: MaterialX.PyMaterialXRender.CgltfLoader, arg0: MaterialX.PyMaterialXFormat.FilePath, arg1: list[MaterialX.PyMaterialXRender.Mesh], arg2: bool) -> bool

        Load geometry from file path.
        """

class ExceptionRenderError(Exception): ...

class GeometryHandler:
    def __init__(self) -> None:
        """__init__(self: MaterialX.PyMaterialXRender.GeometryHandler) -> None"""
    def addLoader(self, arg0: GeometryLoader) -> None:
        """addLoader(self: MaterialX.PyMaterialXRender.GeometryHandler, arg0: MaterialX.PyMaterialXRender.GeometryLoader) -> None

        Add a geometry loader.

        Args:
            loader: Loader to add to list of available loaders.
        """
    def clearGeometry(self) -> None:
        """clearGeometry(self: MaterialX.PyMaterialXRender.GeometryHandler) -> None

        Clear all loaded geometry.
        """
    @staticmethod
    def create() -> GeometryHandler:
        """create() -> MaterialX.PyMaterialXRender.GeometryHandler"""
    def findParentMesh(self, arg0: MeshPartition) -> Mesh:
        """findParentMesh(self: MaterialX.PyMaterialXRender.GeometryHandler, arg0: MaterialX.PyMaterialXRender.MeshPartition) -> MaterialX.PyMaterialXRender.Mesh

        Return the first mesh in our list containing the given partition.

        If no matching mesh is found, then nullptr is returned.
        """
    def getGeometry(self, arg0: list[Mesh], arg1: str) -> None:
        """getGeometry(self: MaterialX.PyMaterialXRender.GeometryHandler, arg0: list[MaterialX.PyMaterialXRender.Mesh], arg1: str) -> None"""
    def getMaximumBounds(self) -> MaterialX.PyMaterialXCore.Vector3:
        """getMaximumBounds(self: MaterialX.PyMaterialXRender.GeometryHandler) -> MaterialX.PyMaterialXCore.Vector3

        Return the minimum bounds for all meshes.
        """
    def getMeshes(self) -> list[Mesh]:
        """getMeshes(self: MaterialX.PyMaterialXRender.GeometryHandler) -> list[MaterialX.PyMaterialXRender.Mesh]

        Get list of meshes.
        """
    def getMinimumBounds(self) -> MaterialX.PyMaterialXCore.Vector3:
        """getMinimumBounds(self: MaterialX.PyMaterialXRender.GeometryHandler) -> MaterialX.PyMaterialXCore.Vector3

        Return the minimum bounds for all meshes.
        """
    def hasGeometry(self, arg0: str) -> bool:
        """hasGeometry(self: MaterialX.PyMaterialXRender.GeometryHandler, arg0: str) -> bool"""
    def loadGeometry(self, arg0: MaterialX.PyMaterialXFormat.FilePath, arg1: bool) -> bool:
        """loadGeometry(self: MaterialX.PyMaterialXRender.GeometryHandler, arg0: MaterialX.PyMaterialXFormat.FilePath, arg1: bool) -> bool

        Load geometry from a given location.

        Args:
            filePath: Path to geometry
            texcoordVerticalFlip: Flip texture coordinates in V. Default is to not flip.
        """

class GeometryLoader:
    def __init__(self) -> None:
        """__init__(self: MaterialX.PyMaterialXRender.GeometryLoader) -> None"""
    def load(self, arg0: MaterialX.PyMaterialXFormat.FilePath, arg1: list[Mesh], arg2: bool) -> bool:
        """load(self: MaterialX.PyMaterialXRender.GeometryLoader, arg0: MaterialX.PyMaterialXFormat.FilePath, arg1: list[MaterialX.PyMaterialXRender.Mesh], arg2: bool) -> bool

        Load geometry from file path.
        """
    def supportedExtensions(self) -> set[str]:
        """supportedExtensions(self: MaterialX.PyMaterialXRender.GeometryLoader) -> set[str]

        Get a list of extensions supported by the handler.
        """

class Image:
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def applyBoxBlur(self) -> Image:
        """applyBoxBlur(self: MaterialX.PyMaterialXRender.Image) -> MaterialX.PyMaterialXRender.Image

        Apply a 3x3 box blur to this image, returning a new blurred image.
        """
    def applyBoxDownsample(self, arg0: int) -> Image:
        """applyBoxDownsample(self: MaterialX.PyMaterialXRender.Image, arg0: int) -> MaterialX.PyMaterialXRender.Image

        Downsample this image by an integer factor using a box filter, returning the new reduced image.
        """
    def applyGammaTransform(self, arg0: float) -> None:
        """applyGammaTransform(self: MaterialX.PyMaterialXRender.Image, arg0: float) -> None

        Apply the given gamma transform to all texels of this image.
        """
    def applyGaussianBlur(self) -> Image:
        """applyGaussianBlur(self: MaterialX.PyMaterialXRender.Image) -> MaterialX.PyMaterialXRender.Image

        Apply a 7x7 Gaussian blur to this image, returning a new blurred image.
        """
    def applyMatrixTransform(self, arg0: MaterialX.PyMaterialXCore.Matrix33) -> None:
        """applyMatrixTransform(self: MaterialX.PyMaterialXRender.Image, arg0: MaterialX.PyMaterialXCore.Matrix33) -> None

        Apply the given matrix transform to all texels of this image.
        """
    def copy(self, arg0: int, arg1: BaseType) -> Image:
        """copy(self: MaterialX.PyMaterialXRender.Image, arg0: int, arg1: MaterialX.PyMaterialXRender.BaseType) -> MaterialX.PyMaterialXRender.Image

        Create a deep copy of the value.
        """
    @staticmethod
    def create(arg0: int, arg1: int, arg2: int, arg3: BaseType) -> Image:
        """create(arg0: int, arg1: int, arg2: int, arg3: MaterialX.PyMaterialXRender.BaseType) -> MaterialX.PyMaterialXRender.Image"""
    def createResourceBuffer(self) -> None:
        """createResourceBuffer(self: MaterialX.PyMaterialXRender.Image) -> None

        Allocate a resource buffer for this image that matches its properties.
        """
    def getBaseStride(self) -> int:
        """getBaseStride(self: MaterialX.PyMaterialXRender.Image) -> int

        Return the stride of our base type in bytes.
        """
    def getBaseType(self) -> BaseType:
        """getBaseType(self: MaterialX.PyMaterialXRender.Image) -> MaterialX.PyMaterialXRender.BaseType

        Return the base type of the image.
        """
    def getChannelCount(self) -> int:
        """getChannelCount(self: MaterialX.PyMaterialXRender.Image) -> int

        Return the channel count of the image.
        """
    def getHeight(self) -> int:
        """getHeight(self: MaterialX.PyMaterialXRender.Image) -> int

        Return the height attribute of the backdrop.
        """
    def getMaxMipCount(self) -> int:
        """getMaxMipCount(self: MaterialX.PyMaterialXRender.Image) -> int

        Return the maximum number of mipmaps for this image.
        """
    def getResourceBuffer(self) -> capsule:
        """getResourceBuffer(self: MaterialX.PyMaterialXRender.Image) -> capsule

        Return the resource buffer for this image.
        """
    def getResourceBufferDeallocator(self) -> Callable[[capsule], None]:
        """getResourceBufferDeallocator(self: MaterialX.PyMaterialXRender.Image) -> Callable[[capsule], None]

        Return the resource buffer deallocator for this image.
        """
    def getTexelColor(self, arg0: int, arg1: int) -> MaterialX.PyMaterialXCore.Color4:
        """getTexelColor(self: MaterialX.PyMaterialXRender.Image, arg0: int, arg1: int) -> MaterialX.PyMaterialXCore.Color4

        Return the texel color at the given coordinates.

        If the coordinates or image resource buffer are invalid, then an exception is thrown.
        """
    def getWidth(self) -> int:
        """getWidth(self: MaterialX.PyMaterialXRender.Image) -> int

        Return the width attribute of the backdrop.
        """
    def isUniformColor(self, arg0: MaterialX.PyMaterialXCore.Color4) -> bool:
        """isUniformColor(self: MaterialX.PyMaterialXRender.Image, arg0: MaterialX.PyMaterialXCore.Color4) -> bool

        Return true if all texels of this image are identical in color.

        Args:
            uniformColor: Return the uniform color of the image, if any.
        """
    def releaseResourceBuffer(self) -> None:
        """releaseResourceBuffer(self: MaterialX.PyMaterialXRender.Image) -> None

        Release the resource buffer for this image.
        """
    def setResourceBuffer(self, arg0: capsule) -> None:
        """setResourceBuffer(self: MaterialX.PyMaterialXRender.Image, arg0: capsule) -> None

        Set the resource buffer for this image.
        """
    def setResourceBufferDeallocator(self, arg0: Callable[[capsule], None]) -> None:
        """setResourceBufferDeallocator(self: MaterialX.PyMaterialXRender.Image, arg0: Callable[[capsule], None]) -> None

        Set the resource buffer deallocator for this image.
        """
    def setTexelColor(self, arg0: int, arg1: int, arg2: MaterialX.PyMaterialXCore.Color4) -> None:
        """setTexelColor(self: MaterialX.PyMaterialXRender.Image, arg0: int, arg1: int, arg2: MaterialX.PyMaterialXCore.Color4) -> None

        Set the texel color at the given coordinates.

        If the coordinates or image resource buffer are invalid, then an exception is thrown.
        """
    def setUniformColor(self, arg0: MaterialX.PyMaterialXCore.Color4) -> None:
        """setUniformColor(self: MaterialX.PyMaterialXRender.Image, arg0: MaterialX.PyMaterialXCore.Color4) -> None

        Set all texels of this image to a uniform color.
        """
    def splitByLuminance(self, arg0: float) -> tuple[Image, Image]:
        """splitByLuminance(self: MaterialX.PyMaterialXRender.Image, arg0: float) -> tuple[MaterialX.PyMaterialXRender.Image, MaterialX.PyMaterialXRender.Image]

        Split this image by the given luminance threshold, returning the resulting underflow and overflow images.
        """

class ImageBufferDeallocator:
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class ImageHandler:
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def acquireImage(self, filePath: MaterialX.PyMaterialXFormat.FilePath, defaultColor: MaterialX.PyMaterialXCore.Color4 = ...) -> Image:
        """acquireImage(self: MaterialX.PyMaterialXRender.ImageHandler, filePath: MaterialX.PyMaterialXFormat.FilePath, defaultColor: MaterialX.PyMaterialXCore.Color4 = <MaterialX.PyMaterialXCore.Color4 object at 0x000001807D2921B0>) -> MaterialX.PyMaterialXRender.Image

        Acquire an image from the cache or file system.

        Args:
            filePath: File path of the image.
            defaultColor: Default color to use as a fallback for missing images.

        Returns:
            On success, a shared pointer to the acquired image.
        """
    def addLoader(self, arg0: ImageLoader) -> None:
        """addLoader(self: MaterialX.PyMaterialXRender.ImageHandler, arg0: MaterialX.PyMaterialXRender.ImageLoader) -> None

        Add a geometry loader.

        Args:
            loader: Loader to add to list of available loaders.
        """
    def bindImage(self, arg0: Image, arg1: ImageSamplingProperties) -> bool:
        """bindImage(self: MaterialX.PyMaterialXRender.ImageHandler, arg0: MaterialX.PyMaterialXRender.Image, arg1: MaterialX.PyMaterialXRender.ImageSamplingProperties) -> bool

        Bind a single image.
        """
    def clearImageCache(self) -> None:
        """clearImageCache(self: MaterialX.PyMaterialXRender.ImageHandler) -> None

        Clear the contents of the image cache, first releasing any render resources associated with cached images.
        """
    @staticmethod
    def create(arg0: ImageLoader) -> ImageHandler:
        """create(arg0: MaterialX.PyMaterialXRender.ImageLoader) -> MaterialX.PyMaterialXRender.ImageHandler"""
    def createRenderResources(self, arg0: Image, arg1: bool, arg2: bool) -> bool:
        """createRenderResources(self: MaterialX.PyMaterialXRender.ImageHandler, arg0: MaterialX.PyMaterialXRender.Image, arg1: bool, arg2: bool) -> bool

        Create rendering resources for the given image.
        """
    def getFilenameResolver(self) -> MaterialX.PyMaterialXCore.StringResolver:
        """getFilenameResolver(self: MaterialX.PyMaterialXRender.ImageHandler) -> MaterialX.PyMaterialXCore.StringResolver

        Return the filename resolver for images.
        """
    def getReferencedImages(self, arg0: MaterialX.PyMaterialXCore.Document) -> list[Image]:
        """getReferencedImages(self: MaterialX.PyMaterialXRender.ImageHandler, arg0: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXRender.Image]

        Acquire all images referenced by the given document, and return the images in a vector.
        """
    def getSearchPath(self) -> MaterialX.PyMaterialXFormat.FileSearchPath:
        """getSearchPath(self: MaterialX.PyMaterialXRender.ImageHandler) -> MaterialX.PyMaterialXFormat.FileSearchPath

        Return the image search path.
        """
    def getZeroImage(self) -> Image:
        """getZeroImage(self: MaterialX.PyMaterialXRender.ImageHandler) -> MaterialX.PyMaterialXRender.Image

        Return a fallback image with zeroes in all channels.
        """
    def releaseRenderResources(self, image: Image = ...) -> None:
        """releaseRenderResources(self: MaterialX.PyMaterialXRender.ImageHandler, image: MaterialX.PyMaterialXRender.Image = None) -> None

        Release rendering resources for the given image, or for all cached images if no image pointer is specified.
        """
    def saveImage(self, filePath: MaterialX.PyMaterialXFormat.FilePath, image: Image, verticalFlip: bool = ...) -> bool:
        """saveImage(self: MaterialX.PyMaterialXRender.ImageHandler, filePath: MaterialX.PyMaterialXFormat.FilePath, image: MaterialX.PyMaterialXRender.Image, verticalFlip: bool = False) -> bool

        Save image to disk.

        Args:
            filePath: File path to be written
            image: The image to be saved
            verticalFlip: Whether the image should be flipped in Y during save

        Returns:
            if save succeeded
        """
    def setFilenameResolver(self, arg0: MaterialX.PyMaterialXCore.StringResolver) -> None:
        """setFilenameResolver(self: MaterialX.PyMaterialXRender.ImageHandler, arg0: MaterialX.PyMaterialXCore.StringResolver) -> None

        Set the filename resolver for images.
        """
    def setSearchPath(self, arg0: MaterialX.PyMaterialXFormat.FileSearchPath) -> None:
        """setSearchPath(self: MaterialX.PyMaterialXRender.ImageHandler, arg0: MaterialX.PyMaterialXFormat.FileSearchPath) -> None

        Set the search path to be used for finding images on the file system.
        """
    def unbindImage(self, arg0: Image) -> bool:
        """unbindImage(self: MaterialX.PyMaterialXRender.ImageHandler, arg0: MaterialX.PyMaterialXRender.Image) -> bool

        Unbind an image.
        """
    def unbindImages(self) -> None:
        """unbindImages(self: MaterialX.PyMaterialXRender.ImageHandler) -> None

        Unbbind all images for this material.
        """

class ImageLoader:
    BMP_EXTENSION: ClassVar[str] = ...  # read-only
    EXR_EXTENSION: ClassVar[str] = ...  # read-only
    GIF_EXTENSION: ClassVar[str] = ...  # read-only
    HDR_EXTENSION: ClassVar[str] = ...  # read-only
    JPEG_EXTENSION: ClassVar[str] = ...  # read-only
    JPG_EXTENSION: ClassVar[str] = ...  # read-only
    PIC_EXTENSION: ClassVar[str] = ...  # read-only
    PNG_EXTENSION: ClassVar[str] = ...  # read-only
    PSD_EXTENSION: ClassVar[str] = ...  # read-only
    TGA_EXTENSION: ClassVar[str] = ...  # read-only
    TIFF_EXTENSION: ClassVar[str] = ...  # read-only
    TIF_EXTENSION: ClassVar[str] = ...  # read-only
    TXT_EXTENSION: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def loadImage(self, arg0: MaterialX.PyMaterialXFormat.FilePath) -> Image:
        """loadImage(self: MaterialX.PyMaterialXRender.ImageLoader, arg0: MaterialX.PyMaterialXFormat.FilePath) -> MaterialX.PyMaterialXRender.Image"""
    def saveImage(self, arg0: MaterialX.PyMaterialXFormat.FilePath, arg1: Image, arg2: bool) -> bool:
        """saveImage(self: MaterialX.PyMaterialXRender.ImageLoader, arg0: MaterialX.PyMaterialXFormat.FilePath, arg1: MaterialX.PyMaterialXRender.Image, arg2: bool) -> bool

        Save image to disk.

        Args:
            filePath: File path to be written
            image: The image to be saved
            verticalFlip: Whether the image should be flipped in Y during save

        Returns:
            if save succeeded
        """
    def supportedExtensions(self) -> set[str]:
        """supportedExtensions(self: MaterialX.PyMaterialXRender.ImageLoader) -> set[str]

        Get a list of extensions supported by the handler.
        """

class ImageSamplingProperties:
    defaultColor: MaterialX.PyMaterialXCore.Color4
    filterType: Incomplete
    uaddressMode: Incomplete
    vaddressMode: Incomplete
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class LightHandler:
    def __init__(self) -> None:
        """__init__(self: MaterialX.PyMaterialXRender.LightHandler) -> None"""
    def addLightSource(self, arg0: MaterialX.PyMaterialXCore.Node) -> None:
        """addLightSource(self: MaterialX.PyMaterialXRender.LightHandler, arg0: MaterialX.PyMaterialXCore.Node) -> None

        Add a light source.
        """
    def computeLightIdMap(self, arg0: list[MaterialX.PyMaterialXCore.Node]) -> dict[str, int]:
        """computeLightIdMap(self: MaterialX.PyMaterialXRender.LightHandler, arg0: list[MaterialX.PyMaterialXCore.Node]) -> dict[str, int]

        From a set of nodes, create a mapping of corresponding nodedef identifiers to numbers.
        """
    @staticmethod
    def create() -> LightHandler:
        """create() -> MaterialX.PyMaterialXRender.LightHandler"""
    def findLights(self, arg0: MaterialX.PyMaterialXCore.Document, arg1: list[MaterialX.PyMaterialXCore.Node]) -> None:
        """findLights(self: MaterialX.PyMaterialXRender.LightHandler, arg0: MaterialX.PyMaterialXCore.Document, arg1: list[MaterialX.PyMaterialXCore.Node]) -> None

        Find lights to use based on an input document.

        Args:
            doc: Document to scan for lights
            lights: List of lights found in document
        """
    def getAlbedoTable(self, *args, **kwargs):
        """getAlbedoTable(self: MaterialX.PyMaterialXRender.LightHandler) -> MaterialX_v1_39_5::Image

        Return the directional albedo table.
        """
    def getDirectLighting(self) -> bool:
        """getDirectLighting(self: MaterialX.PyMaterialXRender.LightHandler) -> bool

        Return whether direct lighting is enabled.
        """
    def getEnvIrradianceMap(self, *args, **kwargs):
        """getEnvIrradianceMap(self: MaterialX.PyMaterialXRender.LightHandler) -> MaterialX_v1_39_5::Image

        Return the environment irradiance map.
        """
    def getEnvRadianceMap(self, *args, **kwargs):
        """getEnvRadianceMap(self: MaterialX.PyMaterialXRender.LightHandler) -> MaterialX_v1_39_5::Image

        Return the environment radiance map.
        """
    def getEnvSampleCount(self) -> int:
        """getEnvSampleCount(self: MaterialX.PyMaterialXRender.LightHandler) -> int

        Return the environment lighting sample count.
        """
    def getFirstLightOfCategory(self, arg0: str) -> MaterialX.PyMaterialXCore.Node:
        """getFirstLightOfCategory(self: MaterialX.PyMaterialXRender.LightHandler, arg0: str) -> MaterialX.PyMaterialXCore.Node

        Return the first light source, if any, of the given category.
        """
    def getIndirectLighting(self) -> bool:
        """getIndirectLighting(self: MaterialX.PyMaterialXRender.LightHandler) -> bool

        Return whether indirect lighting is enabled.
        """
    def getLightIdMap(self) -> dict[str, int]:
        """getLightIdMap(self: MaterialX.PyMaterialXRender.LightHandler) -> dict[str, int]

        Get a list of identifiers associated with a given light nodedef.
        """
    def getLightSources(self) -> list[MaterialX.PyMaterialXCore.Node]:
        """getLightSources(self: MaterialX.PyMaterialXRender.LightHandler) -> list[MaterialX.PyMaterialXCore.Node]

        Return the vector of light sources.
        """
    def getLightTransform(self) -> MaterialX.PyMaterialXCore.Matrix44:
        """getLightTransform(self: MaterialX.PyMaterialXRender.LightHandler) -> MaterialX.PyMaterialXCore.Matrix44

        Return the light transform.
        """
    def getRefractionTwoSided(self) -> int:
        """getRefractionTwoSided(self: MaterialX.PyMaterialXRender.LightHandler) -> int

        Return the two-sided refraction property.
        """
    def registerLights(self, arg0: MaterialX.PyMaterialXCore.Document, arg1: list[MaterialX.PyMaterialXCore.Node], arg2: MaterialX.PyMaterialXGenShader.GenContext) -> None:
        """registerLights(self: MaterialX.PyMaterialXRender.LightHandler, arg0: MaterialX.PyMaterialXCore.Document, arg1: list[MaterialX.PyMaterialXCore.Node], arg2: MaterialX.PyMaterialXGenShader.GenContext) -> None

        Register light node definitions and light count with a given generation context.

        Args:
            doc: Document containing light nodes and definitions
            lights: Lights to register
            context: Context to update
        """
    def setAlbedoTable(self, arg0) -> None:
        """setAlbedoTable(self: MaterialX.PyMaterialXRender.LightHandler, arg0: MaterialX_v1_39_5::Image) -> None

        Set the directional albedo table.
        """
    def setDirectLighting(self, arg0: bool) -> None:
        """setDirectLighting(self: MaterialX.PyMaterialXRender.LightHandler, arg0: bool) -> None

        Set whether direct lighting is enabled.
        """
    def setEnvIrradianceMap(self, arg0) -> None:
        """setEnvIrradianceMap(self: MaterialX.PyMaterialXRender.LightHandler, arg0: MaterialX_v1_39_5::Image) -> None

        Set the environment irradiance map.
        """
    def setEnvRadianceMap(self, arg0) -> None:
        """setEnvRadianceMap(self: MaterialX.PyMaterialXRender.LightHandler, arg0: MaterialX_v1_39_5::Image) -> None

        Set the environment radiance map.
        """
    def setEnvSampleCount(self, arg0: int) -> None:
        """setEnvSampleCount(self: MaterialX.PyMaterialXRender.LightHandler, arg0: int) -> None

        Set the environment lighting sample count.
        """
    def setIndirectLighting(self, arg0: bool) -> None:
        """setIndirectLighting(self: MaterialX.PyMaterialXRender.LightHandler, arg0: bool) -> None

        Set whether indirect lighting is enabled.
        """
    def setLightSources(self, arg0: list[MaterialX.PyMaterialXCore.Node]) -> None:
        """setLightSources(self: MaterialX.PyMaterialXRender.LightHandler, arg0: list[MaterialX.PyMaterialXCore.Node]) -> None

        Set the vector of light sources.
        """
    def setLightTransform(self, arg0: MaterialX.PyMaterialXCore.Matrix44) -> None:
        """setLightTransform(self: MaterialX.PyMaterialXRender.LightHandler, arg0: MaterialX.PyMaterialXCore.Matrix44) -> None

        Set the light transform.
        """
    def setRefractionTwoSided(self, arg0: bool) -> None:
        """setRefractionTwoSided(self: MaterialX.PyMaterialXRender.LightHandler, arg0: bool) -> None

        Set the two-sided refraction property.
        """

class Mesh:
    def __init__(self, arg0: str) -> None:
        """__init__(self: MaterialX.PyMaterialXRender.Mesh, arg0: str) -> None"""
    def addPartition(self, arg0: MeshPartition) -> None:
        """addPartition(self: MaterialX.PyMaterialXRender.Mesh, arg0: MaterialX.PyMaterialXRender.MeshPartition) -> None

        Add a partition.
        """
    def addStream(self, arg0: MeshStream) -> None:
        """addStream(self: MaterialX.PyMaterialXRender.Mesh, arg0: MaterialX.PyMaterialXRender.MeshStream) -> None

        Add a mesh stream.
        """
    @staticmethod
    def create(arg0: str) -> Mesh:
        """create(arg0: str) -> MaterialX.PyMaterialXRender.Mesh"""
    def generateBitangents(self, arg0: MeshStream, arg1: MeshStream) -> MeshStream:
        """generateBitangents(self: MaterialX.PyMaterialXRender.Mesh, arg0: MaterialX.PyMaterialXRender.MeshStream, arg1: MaterialX.PyMaterialXRender.MeshStream) -> MaterialX.PyMaterialXRender.MeshStream

        Generate bitangents from the given normals and tangents.

        Args:
            normalStream: Input normal stream
            tangentStream: Input tangent stream

        Returns:
            The generated bitangent stream, on success; otherwise, a null pointer.
        """
    def generateNormals(self, arg0: MeshStream) -> MeshStream:
        """generateNormals(self: MaterialX.PyMaterialXRender.Mesh, arg0: MaterialX.PyMaterialXRender.MeshStream) -> MaterialX.PyMaterialXRender.MeshStream

        Generate face normals from the given positions.

        Args:
            positionStream: Input position stream

        Returns:
            The generated normal stream
        """
    def generateTangents(self, arg0: MeshStream, arg1: MeshStream, arg2: MeshStream) -> MeshStream:
        """generateTangents(self: MaterialX.PyMaterialXRender.Mesh, arg0: MaterialX.PyMaterialXRender.MeshStream, arg1: MaterialX.PyMaterialXRender.MeshStream, arg2: MaterialX.PyMaterialXRender.MeshStream) -> MaterialX.PyMaterialXRender.MeshStream

        Generate tangents from the given positions, normals, and texture coordinates.

        Args:
            positionStream: Input position stream
            normalStream: Input normal stream
            texcoordStream: Input texcoord stream

        Returns:
            The generated tangent stream, on success; otherwise, a null pointer.
        """
    def generateTextureCoordinates(self, arg0: MeshStream) -> MeshStream:
        """generateTextureCoordinates(self: MaterialX.PyMaterialXRender.Mesh, arg0: MaterialX.PyMaterialXRender.MeshStream) -> MaterialX.PyMaterialXRender.MeshStream

        Create texture coordinates from the given positions.

        Args:
            positionStream: Input position stream

        Returns:
            The generated texture coordinate stream
        """
    def getMaximumBounds(self) -> MaterialX.PyMaterialXCore.Vector3:
        """getMaximumBounds(self: MaterialX.PyMaterialXRender.Mesh) -> MaterialX.PyMaterialXCore.Vector3

        Return the minimum bounds for all meshes.
        """
    def getMinimumBounds(self) -> MaterialX.PyMaterialXCore.Vector3:
        """getMinimumBounds(self: MaterialX.PyMaterialXRender.Mesh) -> MaterialX.PyMaterialXCore.Vector3

        Return the minimum bounds for all meshes.
        """
    def getName(self) -> str:
        """getName(self: MaterialX.PyMaterialXRender.Mesh) -> str

        Return the ColorManagementSystem name.
        """
    def getPartition(self, arg0: int) -> MeshPartition:
        """getPartition(self: MaterialX.PyMaterialXRender.Mesh, arg0: int) -> MaterialX.PyMaterialXRender.MeshPartition

        Return a reference to a mesh partition.
        """
    def getPartitionCount(self) -> int:
        """getPartitionCount(self: MaterialX.PyMaterialXRender.Mesh) -> int

        Return the number of mesh partitions.
        """
    def getSourceUri(self) -> str:
        """getSourceUri(self: MaterialX.PyMaterialXRender.Mesh) -> str

        Return the element's source URI.
        """
    def getSphereCenter(self) -> MaterialX.PyMaterialXCore.Vector3:
        """getSphereCenter(self: MaterialX.PyMaterialXRender.Mesh) -> MaterialX.PyMaterialXCore.Vector3

        Return center of the bounding sphere.
        """
    def getSphereRadius(self) -> float:
        """getSphereRadius(self: MaterialX.PyMaterialXRender.Mesh) -> float

        Return radius of the bounding sphere.
        """
    @overload
    def getStream(self, arg0: str) -> MeshStream:
        """getStream(*args, **kwargs)
        Overloaded function.

        1. getStream(self: MaterialX.PyMaterialXRender.Mesh, arg0: str) -> MaterialX.PyMaterialXRender.MeshStream

        Get a mesh stream by type and index.

        Args:
            type: Type of stream
            index: Index of stream

        Returns:
            Reference to a mesh stream if found

        2. getStream(self: MaterialX.PyMaterialXRender.Mesh, arg0: str, arg1: int) -> MaterialX.PyMaterialXRender.MeshStream

        Get a mesh stream by type and index.

        Args:
            type: Type of stream
            index: Index of stream

        Returns:
            Reference to a mesh stream if found
        """
    @overload
    def getStream(self, arg0: str, arg1: int) -> MeshStream:
        """getStream(*args, **kwargs)
        Overloaded function.

        1. getStream(self: MaterialX.PyMaterialXRender.Mesh, arg0: str) -> MaterialX.PyMaterialXRender.MeshStream

        Get a mesh stream by type and index.

        Args:
            type: Type of stream
            index: Index of stream

        Returns:
            Reference to a mesh stream if found

        2. getStream(self: MaterialX.PyMaterialXRender.Mesh, arg0: str, arg1: int) -> MaterialX.PyMaterialXRender.MeshStream

        Get a mesh stream by type and index.

        Args:
            type: Type of stream
            index: Index of stream

        Returns:
            Reference to a mesh stream if found
        """
    def getVertexCount(self) -> int:
        """getVertexCount(self: MaterialX.PyMaterialXRender.Mesh) -> int

        Get vertex count.
        """
    def hasSourceUri(self) -> bool:
        """hasSourceUri(self: MaterialX.PyMaterialXRender.Mesh) -> bool

        Return true if this element has a source URI.
        """
    def mergePartitions(self) -> None:
        """mergePartitions(self: MaterialX.PyMaterialXRender.Mesh) -> None

        Merge all mesh partitions into one.
        """
    def setMaximumBounds(self, arg0: MaterialX.PyMaterialXCore.Vector3) -> None:
        """setMaximumBounds(self: MaterialX.PyMaterialXRender.Mesh, arg0: MaterialX.PyMaterialXCore.Vector3) -> None

        Set the minimum bounds for the geometry.
        """
    def setMinimumBounds(self, arg0: MaterialX.PyMaterialXCore.Vector3) -> None:
        """setMinimumBounds(self: MaterialX.PyMaterialXRender.Mesh, arg0: MaterialX.PyMaterialXCore.Vector3) -> None

        Set the minimum bounds for the geometry.
        """
    def setSourceUri(self, arg0: str) -> None:
        """setSourceUri(self: MaterialX.PyMaterialXRender.Mesh, arg0: str) -> None

        Set the element's source URI.

        Args:
            sourceUri: A URI string representing the resource from which this element originates. This string may be used by serialization and deserialization routines to maintain hierarchies of include references.
        """
    def setSphereCenter(self, arg0: MaterialX.PyMaterialXCore.Vector3) -> None:
        """setSphereCenter(self: MaterialX.PyMaterialXRender.Mesh, arg0: MaterialX.PyMaterialXCore.Vector3) -> None

        Set center of the bounding sphere.
        """
    def setSphereRadius(self, arg0: float) -> None:
        """setSphereRadius(self: MaterialX.PyMaterialXRender.Mesh, arg0: float) -> None

        Set radius of the bounding sphere.
        """
    def setVertexCount(self, arg0: int) -> None:
        """setVertexCount(self: MaterialX.PyMaterialXRender.Mesh, arg0: int) -> None

        Set vertex count.
        """
    def splitByUdims(self) -> None:
        """splitByUdims(self: MaterialX.PyMaterialXRender.Mesh) -> None

        Split the mesh into a single partition per UDIM.
        """

class MeshPartition:
    def __init__(self) -> None:
        """__init__(self: MaterialX.PyMaterialXRender.MeshPartition) -> None"""
    def addSourceName(self, arg0: str) -> None:
        """addSourceName(self: MaterialX.PyMaterialXRender.MeshPartition, arg0: str) -> None

        Add a source name, representing a partition that was processed to generate this one.
        """
    @staticmethod
    def create() -> MeshPartition:
        """create() -> MaterialX.PyMaterialXRender.MeshPartition"""
    def getFaceCount(self) -> int:
        """getFaceCount(self: MaterialX.PyMaterialXRender.MeshPartition) -> int

        Return number of faces.
        """
    def getIndices(self) -> list[int]:
        """getIndices(self: MaterialX.PyMaterialXRender.MeshPartition) -> list[int]

        Return indexing.
        """
    def getName(self) -> str:
        """getName(self: MaterialX.PyMaterialXRender.MeshPartition) -> str

        Return the ColorManagementSystem name.
        """
    def getSourceNames(self) -> set[str]:
        """getSourceNames(self: MaterialX.PyMaterialXRender.MeshPartition) -> set[str]

        Return the vector of source names, representing all partitions that were processed to generate this one.
        """
    def resize(self, arg0: int) -> None:
        """resize(self: MaterialX.PyMaterialXRender.MeshPartition, arg0: int) -> None

        Resize data to the given number of indices.
        """
    def setFaceCount(self, arg0: int) -> None:
        """setFaceCount(self: MaterialX.PyMaterialXRender.MeshPartition, arg0: int) -> None

        Set face count.
        """
    def setName(self, arg0: str) -> None:
        """setName(self: MaterialX.PyMaterialXRender.MeshPartition, arg0: str) -> None

        Set the element's name string.
        """

class MeshStream:
    BITANGENT_ATTRIBUTE: ClassVar[str] = ...  # read-only
    COLOR_ATTRIBUTE: ClassVar[str] = ...  # read-only
    GEOMETRY_PROPERTY_ATTRIBUTE: ClassVar[str] = ...  # read-only
    NORMAL_ATTRIBUTE: ClassVar[str] = ...  # read-only
    POSITION_ATTRIBUTE: ClassVar[str] = ...  # read-only
    TANGENT_ATTRIBUTE: ClassVar[str] = ...  # read-only
    TEXCOORD_ATTRIBUTE: ClassVar[str] = ...  # read-only
    def __init__(self, arg0: str, arg1: str, arg2: int) -> None:
        """__init__(self: MaterialX.PyMaterialXRender.MeshStream, arg0: str, arg1: str, arg2: int) -> None"""
    @staticmethod
    def create(arg0: str, arg1: str, arg2: int) -> MeshStream:
        """create(arg0: str, arg1: str, arg2: int) -> MaterialX.PyMaterialXRender.MeshStream"""
    def getData(self) -> list[float]:
        """getData(self: MaterialX.PyMaterialXRender.MeshStream) -> list[float]

        Return the raw float vector.
        """
    def getIndex(self) -> int:
        """getIndex(self: MaterialX.PyMaterialXRender.MeshStream) -> int

        Return the index string of this element.
        """
    def getName(self) -> str:
        """getName(self: MaterialX.PyMaterialXRender.MeshStream) -> str

        Return the ColorManagementSystem name.
        """
    def getSize(self) -> int:
        """getSize(self: MaterialX.PyMaterialXRender.MeshStream) -> int

        Get the number of elements.
        """
    def getStride(self) -> int:
        """getStride(self: MaterialX.PyMaterialXRender.MeshStream) -> int

        Get stride between elements.
        """
    def getType(self) -> str:
        """getType(self: MaterialX.PyMaterialXRender.MeshStream) -> str

        Get stream attribute name.
        """
    def reserve(self, arg0: int) -> None:
        """reserve(self: MaterialX.PyMaterialXRender.MeshStream, arg0: int) -> None

        Reserve memory for a given number of elements.
        """
    def resize(self, arg0: int) -> None:
        """resize(self: MaterialX.PyMaterialXRender.MeshStream, arg0: int) -> None

        Resize data to the given number of indices.
        """
    def setStride(self, arg0: int) -> None:
        """setStride(self: MaterialX.PyMaterialXRender.MeshStream, arg0: int) -> None

        Set stride between elements.
        """
    def transform(self, arg0: MaterialX.PyMaterialXCore.Matrix44) -> None:
        """transform(self: MaterialX.PyMaterialXRender.MeshStream, arg0: MaterialX.PyMaterialXCore.Matrix44) -> None

        Transform elements by a matrix.
        """

class ShaderRenderer:
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @overload
    def createProgram(self, arg0: MaterialX.PyMaterialXGenShader.Shader) -> None:
        """createProgram(*args, **kwargs)
        Overloaded function.

        1. createProgram(self: MaterialX.PyMaterialXRender.ShaderRenderer, arg0: MaterialX.PyMaterialXGenShader.Shader) -> None

        Create GLSL program based on shader stage source code.

        Args:
            stages: Map of name and source code for the shader stages.

        2. createProgram(self: MaterialX.PyMaterialXRender.ShaderRenderer, arg0: dict[str, str]) -> None

        Create GLSL program based on shader stage source code.

        Args:
            stages: Map of name and source code for the shader stages.
        """
    @overload
    def createProgram(self, arg0: dict[str, str]) -> None:
        """createProgram(*args, **kwargs)
        Overloaded function.

        1. createProgram(self: MaterialX.PyMaterialXRender.ShaderRenderer, arg0: MaterialX.PyMaterialXGenShader.Shader) -> None

        Create GLSL program based on shader stage source code.

        Args:
            stages: Map of name and source code for the shader stages.

        2. createProgram(self: MaterialX.PyMaterialXRender.ShaderRenderer, arg0: dict[str, str]) -> None

        Create GLSL program based on shader stage source code.

        Args:
            stages: Map of name and source code for the shader stages.
        """
    def getCamera(self) -> Camera:
        """getCamera(self: MaterialX.PyMaterialXRender.ShaderRenderer) -> MaterialX.PyMaterialXRender.Camera

        Return the camera.
        """
    def getGeometryHandler(self) -> GeometryHandler:
        """getGeometryHandler(self: MaterialX.PyMaterialXRender.ShaderRenderer) -> MaterialX.PyMaterialXRender.GeometryHandler

        Return the geometry handler.
        """
    def getImageHandler(self) -> ImageHandler:
        """getImageHandler(self: MaterialX.PyMaterialXRender.ShaderRenderer) -> MaterialX.PyMaterialXRender.ImageHandler

        Return the image handler.
        """
    def getLightHandler(self) -> LightHandler:
        """getLightHandler(self: MaterialX.PyMaterialXRender.ShaderRenderer) -> MaterialX.PyMaterialXRender.LightHandler

        Return the light handler.
        """
    def initialize(self, renderContextHandle: capsule = ...) -> None:
        """initialize(self: MaterialX.PyMaterialXRender.ShaderRenderer, renderContextHandle: capsule = None) -> None

        Initialize with the given implementation element.

        Initialization must set the name and hash for the implementation, as well as any other data needed to emit code for the node.
        """
    def render(self) -> None:
        """render(self: MaterialX.PyMaterialXRender.ShaderRenderer) -> None

        Render the current program to an offscreen buffer.
        """
    def setCamera(self, arg0: Camera) -> None:
        """setCamera(self: MaterialX.PyMaterialXRender.ShaderRenderer, arg0: MaterialX.PyMaterialXRender.Camera) -> None

        Set the camera.
        """
    def setGeometryHandler(self, arg0: GeometryHandler) -> None:
        """setGeometryHandler(self: MaterialX.PyMaterialXRender.ShaderRenderer, arg0: MaterialX.PyMaterialXRender.GeometryHandler) -> None

        Set the geometry handler.
        """
    def setImageHandler(self, arg0: ImageHandler) -> None:
        """setImageHandler(self: MaterialX.PyMaterialXRender.ShaderRenderer, arg0: MaterialX.PyMaterialXRender.ImageHandler) -> None

        Set the image handler used by this renderer for image I/O.
        """
    def setLightHandler(self, arg0: LightHandler) -> None:
        """setLightHandler(self: MaterialX.PyMaterialXRender.ShaderRenderer, arg0: MaterialX.PyMaterialXRender.LightHandler) -> None

        Set the light handler used by this renderer for light bindings.
        """
    def setSize(self, arg0: int, arg1: int) -> None:
        """setSize(self: MaterialX.PyMaterialXRender.ShaderRenderer, arg0: int, arg1: int) -> None

        Set the size of the rendered image.
        """
    def updateUniform(self, arg0: str, arg1: MaterialX.PyMaterialXCore.Value) -> None:
        """updateUniform(self: MaterialX.PyMaterialXRender.ShaderRenderer, arg0: str, arg1: MaterialX.PyMaterialXCore.Value) -> None

        Update the program with value of the uniform.
        """
    def validateInputs(self) -> None:
        """validateInputs(self: MaterialX.PyMaterialXRender.ShaderRenderer) -> None

        Validate inputs for the program.
        """

class StbImageLoader(ImageLoader):
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def create() -> StbImageLoader:
        """create() -> MaterialX.PyMaterialXRender.StbImageLoader"""
    def loadImage(self, arg0: MaterialX.PyMaterialXFormat.FilePath) -> Image:
        """loadImage(self: MaterialX.PyMaterialXRender.StbImageLoader, arg0: MaterialX.PyMaterialXFormat.FilePath) -> MaterialX.PyMaterialXRender.Image"""
    def saveImage(self, arg0: MaterialX.PyMaterialXFormat.FilePath, arg1: Image, arg2: bool) -> bool:
        """saveImage(self: MaterialX.PyMaterialXRender.StbImageLoader, arg0: MaterialX.PyMaterialXFormat.FilePath, arg1: MaterialX.PyMaterialXRender.Image, arg2: bool) -> bool

        Save image to disk.

        Args:
            filePath: File path to be written
            image: The image to be saved
            verticalFlip: Whether the image should be flipped in Y during save

        Returns:
            if save succeeded
        """

class TinyObjLoader(GeometryLoader):
    def __init__(self) -> None:
        """__init__(self: MaterialX.PyMaterialXRender.TinyObjLoader) -> None"""
    @staticmethod
    def create() -> TinyObjLoader:
        """create() -> MaterialX.PyMaterialXRender.TinyObjLoader"""
    def load(self, arg0: MaterialX.PyMaterialXFormat.FilePath, arg1: list[Mesh], arg2: bool) -> bool:
        """load(self: MaterialX.PyMaterialXRender.TinyObjLoader, arg0: MaterialX.PyMaterialXFormat.FilePath, arg1: list[MaterialX.PyMaterialXRender.Mesh], arg2: bool) -> bool

        Load geometry from file path.
        """

def createImageStrip(arg0: list[Image]) -> Image:
    """createImageStrip(arg0: list[MaterialX.PyMaterialXRender.Image]) -> MaterialX.PyMaterialXRender.Image"""
def createUniformImage(arg0: int, arg1: int, arg2: int, arg3: BaseType, arg4: MaterialX.PyMaterialXCore.Color4) -> Image:
    """createUniformImage(arg0: int, arg1: int, arg2: int, arg3: MaterialX.PyMaterialXRender.BaseType, arg4: MaterialX.PyMaterialXCore.Color4) -> MaterialX.PyMaterialXRender.Image"""
def getMaxDimensions(arg0: list[Image]) -> tuple[int, int]:
    """getMaxDimensions(arg0: list[MaterialX.PyMaterialXRender.Image]) -> tuple[int, int]"""
