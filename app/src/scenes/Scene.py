import pygame
from src.core.Configuration import Configuration as CFG
from src.resources.assets.AssetManager import AssetManager
from src.resources.components.ComponentManager import ComponentManager
from src.resources.components.Textfield import Textfield
from src.resources.components.Component import Component
from src.resources.components.Button import Button

class Scene:
    """
    The Scene class is used as a base for other Scene Objects
    like menus and game screens.
    """
    __assetManager: AssetManager
    __componentManager: ComponentManager
    __counter: int
    __stop: bool
    __event: str

    def __init__(self) -> None:
        """
        Creates a Scene object and initializes the surface,
        assetManager, componentManager, counter and stop variables.
        """
        self.__assetManager = AssetManager()
        self.__componentManager = ComponentManager()
        self.__counter = 0
        self.__stop = False
        self.__event = ""

    @property
    def counter(self) -> int:
        """
        Returns the counter of the Scene object. The counter is increased 
        by 1 with every tick.
        """
        return self.__counter
    
    @property
    def last_event(self) -> str:
        return self.__event

    @property
    def stop(self) -> bool:
        """Indicates, if the Game should be stopped."""
        return self.__stop
    
    def end(self) -> None:
        """Sets the stop variable to True to indicate, that the Game should end."""
        self.__stop = True

    def update(self, event: str, mouselocation: tuple[int, int]) -> None:
        """
        Checks the Component for updates and provides them to the managers.\n
        Increments the counter of the Scene by 1 to allow timed Scene events.
        """
        if event:
            self.__event = event

        self.__counter += 1

        for entity in self.__componentManager.components:
            c: Component = self.__componentManager.components.get(entity)
            if c.update:
                if c.ID in self.__assetManager.images:
                    self.__assetManager.update_image(c.ID, c.image)
                    c.resetUpdate()

        if "//d" in event:
            for button in self.__componentManager.buttons:
                if button.collide_point(mouselocation[0], mouselocation[1]):
                    button.flag = True
                print(f"flag state down {button.flag}")

        if "//u" in event:
            for button in self.__componentManager.buttons:
                if button.collide_point(mouselocation[0], mouselocation[1]) and button.flag:
                    button.action()
                button.flag = False
                print(f"flag state up {button.flag}")

    def register_image(self, image_name: str, image: pygame.Surface) -> None:
        """
        Registers an image with the asset manager.

        Args:
            image_name (str): The name of the image.
            image (pygame.Surface): The image surface.
        """
        self.__assetManager.update_image(image_name, image)

    def get_image_size(self, image_id: str):
        image = self.__assetManager.get_image(image_id)
        return image.get_size()

    def register_button(self, button: Button):
        self.register_component(button)
        self.register_textfield(button.textfield)

    def register_textfield(self, textfield: Textfield) -> None:
        self.register_component(textfield)
        self.register_image(textfield.ID, textfield.image)

    def load_asset(self, asset_name: str) -> None:
        """
        Loads an asset (either an image or sound) using the asset manager.\n
        Directly registers the asset in the AssetManager.

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

    def register_component(self, component: Component) -> None:
        """
        Adds a Component object to the components list of the Scene.

        Args:
            component (Component): The component to add.

        Raises:
            TypeError: If the component is not an instance of Component.
        """
        if isinstance(component, Component):
            self.__componentManager.register(component)
        else:
            raise TypeError("Can only add instances of Component")
        
    def get_component(self, ID: str) -> Component:
        """
        Uses the ID of a component to return it from the componentManager.
        
        Args:
            ID (str): component ID
            
        Returns:
            component (Component): the component associated with the ID
        """
        return self.__componentManager.get(ID)

    def get_rendering_context(self) -> list[tuple[pygame.Surface, tuple[int, int]]]:
        """
        Gets the components to render from the componentManager and prepares
        them for rendering based on their render priority.

        Returns:
            list[tuple[pygame.Surface, tuple[int, int]]]: A list of tuples containing
            the image surface and its location for rendering.
        """
        render_context: list[tuple[pygame.Surface, tuple[int, int]]] = []

        # Iterate through all the Scene's components that will be rendered
        for information in self.__componentManager.rendering_context:

            component_ID = information[0]
            location = information[1]
            priority = information[2]

            image = self.__assetManager.get_image(component_ID)
            render_information = (image, location, priority)

            # Insert the component into the list based on render priority
            inserted = False
            for i, context in enumerate(render_context):
                c_priority = context[2]
                if priority <= c_priority:
                    render_context.insert(i + 1, render_information)
                    inserted = True
                    break

            if not inserted:
                render_context.append(render_information)

        return render_context
