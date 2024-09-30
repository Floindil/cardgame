import pygame
from src.core.Configuration import Configuration as CFG
from src.resources.assets.AssetManager import AssetManager
from src.resources.components.Component import Component

class Scene:
    """
    The Scene class is used as a base for other Scene Objects
    like menus and game screens.
    """
    _components: list[Component]
    __assetManager: AssetManager

    def __init__(self) -> None:
        """
        Creates a Scene object and initializes the surface,
        assetManager, and components variables.
        """
        self.__assetManager = AssetManager()
        self._components = []

    def register_image(self, image_name: str, image: pygame.Surface) -> None:
        """
        Registers an image with the asset manager.

        Args:
            image_name (str): The name of the image.
            image (pygame.Surface): The image surface.
        """
        self.__assetManager.add_image(image_name, image)

    def load_asset(self, asset_name: str) -> None:
        """
        Loads an asset (either an image or sound) using the asset manager.

        Args:
            asset_name (str): The name of the asset to load.

        Raises:
            TypeError: If the asset is not a .png or .mp3 file.
        """
        if asset_name.endswith(".png"):
            self.__assetManager.load_image(asset_name)
        elif asset_name.endswith(".mp3"):
            self.__assetManager.load_sound(asset_name)
        else:
            raise TypeError("Asset must be either a .png or .mp3 file!")

    def start(self) -> None:
        """
        Defines the behaviour of the Scene when it is started.
        This method should be overridden by subclasses.
        """
        pass

    def add_component(self, component: Component) -> None:
        """
        Adds a Component object to the components list of the Scene.

        Args:
            component (Component): The component to add.

        Raises:
            TypeError: If the component is not an instance of Component.
        """
        if isinstance(component, Component):
            self._components.append(component)
        else:
            raise TypeError("Can only add instances of Component")

    def get_rendering_context(self) -> list[tuple[pygame.Surface, tuple[int, int]]]:
        """
        Checks all components in the Scene's components list and prepares
        them for rendering based on their render priority.

        Returns:
            list[tuple[pygame.Surface, tuple[int, int]]]: A list of tuples containing
            the image surface and its location for rendering.
        """
        render_context: list[tuple[pygame.Surface, tuple[int, int]]] = []

        # Iterate through all the Scene's components
        for component in self._components:
            # Check if the component should be rendered
            if component.RENDER:
                image = self.__assetManager.get_image(component.image_name)
                render_information = (image, component.location, component.RENDERPRIORITY)

                # Insert the component into the list based on render priority
                inserted = False
                for i, context in enumerate(render_context):
                    priority = context[2]
                    if component.RENDERPRIORITY <= priority:
                        render_context.insert(i + 1, render_information)
                        inserted = True
                        break

                if not inserted:
                    render_context.append(render_information)

        return render_context
