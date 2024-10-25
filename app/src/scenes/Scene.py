import pygame
from typing import Type, Optional

from src.core.Configuration import Assets, Game as C
from src.resources.assets.AssetManager import AssetManager
from src.resources.components.ComponentManager import ComponentManager
from src.resources.components.Textfield import Textfield
from src.resources.components.Component import Component
from src.resources.components.Button import Button

class Scene:
    """
    The Scene class serves as a base for other scene objects such as menus and game screens.
    It manages assets, components, and transitions between scenes.
    """

    __assetManager: AssetManager
    __componentManager: ComponentManager
    __next_scene: Optional[Type['Scene']]
    __counter: int
    __event: str
    __stop: bool
    __interaction: bool
    _menuacces: bool

    def __init__(self) -> None:
        """
        Initializes a Scene object and its core attributes, including asset and component managers,
        event handling, scene transition, and control variables.
        """
        self.__assetManager = AssetManager()
        self.__componentManager = ComponentManager()
        self.__counter = 0
        self.__stop = False
        self.__event = ""
        self.__next_scene = None
        self.__interaction = True
        self._menuacces = True

    def start(self):
        """
        Placeholder for starting behavior and component creation.
        Should be overridden in subclasses to define specific start behavior.
        """
        pass

    @property
    def interaction(self) -> bool:
        """
        Indicates whether the Scene Object can be interacted with or not.

        Returns:
            bool: True if interaction is allowed, False otherwise.
        """
        return self.__interaction
    
    @interaction.setter
    def interaction(self, state: bool):
        """
        Sets the next interaction to True or False.

        Args:
            state (bool): True if interaction should be allowed allowed, False otherwise.
        """
        self.__interaction = state

    @property
    def assets(self) -> Assets:
        """
        Returns the Assets class which holds asset names and IDs.

        Returns:
            Assets: The class containing asset constants.
        """
        return Assets

    @property
    def counter(self) -> int:
        """
        Returns the counter of the Scene object, which increments with every tick.

        Returns:
            int: The current counter value.
        """
        return self.__counter

    @property
    def last_event(self) -> str:
        """
        Returns the last event that occurred in the Scene.

        Returns:
            str: The last event.
        """
        return self.__event

    @property
    def stop(self) -> bool:
        """
        Indicates whether the game should be stopped.

        Returns:
            bool: True if the game should stop, False otherwise.
        """
        return self.__stop

    @property
    def next_scene(self) -> Optional[Type['Scene']]:
        """
        Returns the next scene to transition to.

        Returns:
            Optional[Type['Scene']]: The next scene or None if no transition is set.
        """
        return self.__next_scene

    @next_scene.setter
    def next_scene(self, new_scene: Optional[Type['Scene']]) -> None:
        """
        Sets the next scene to transition to.

        Args:
            new_scene (Optional[Type['Scene']]): The next scene.
        """
        self.__next_scene = new_scene

    def end(self) -> None:
        """
        Sets the stop flag to True to indicate that the game should end.
        """
        self.__stop = True

    def update(self, event: str, mouselocation: tuple[int, int]) -> None:
        """
        Updates the Scene based on events and mouse location, manages component updates,
        and handles button actions.

        Args:
            event (str): The event string.
            mouselocation (tuple[int, int]): The mouse location as an (x, y) tuple.
        """
        if event:
            self.__event = event

        self.__counter += 1

        # Update all components and get the resulting asset updates
        asset_updates = self.__componentManager.update(self.interaction, event, mouselocation)

        if asset_updates:
            for update in asset_updates:
                self.__assetManager.update_image(update[0], update[1])


    def register_image(self, image_name: str, image: pygame.Surface) -> None:
        """
        Registers an image with the asset manager.

        Args:
            image_name (str): The name of the image.
            image (pygame.Surface): The image surface.
        """
        self.__assetManager.update_image(image_name, image)

    def get_image_size(self, image_id: str) -> tuple[int, int]:
        """
        Gets the size of an image by its ID.

        Args:
            image_id (str): The ID of the image.

        Returns:
            tuple[int, int]: The size of the image as (width, height).
        """
        image = self.__assetManager.get_image(image_id)
        return image.get_size()

    def register_button(self, button: Button) -> None:
        """
        Registers a button component and its associated textfield.

        Args:
            button (Button): The button to register.
        """
        self.register_component(button)
        self.register_textfield(button.textfield)

    def register_textfield(self, textfield: Textfield) -> None:
        """
        Registers a textfield component and its associated image.

        Args:
            textfield (Textfield): The textfield to register.
        """
        self.register_component(textfield)
        self.register_image(textfield.ID, textfield.image)

    def register_component(self, component: Component) -> None:
        """
        Adds a component object to the component list of the Scene.

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
        Retrieves a component by its ID from the component manager.

        Args:
            ID (str): The ID of the component.

        Returns:
            Component: The component associated with the ID.
        """
        return self.__componentManager.get(ID)

    def get_rendering_context(self) -> list[tuple[pygame.Surface, tuple[int, int]]]:
        """
        Retrieves the components to be rendered from the component manager.

        Returns:
            list[tuple[pygame.Surface, tuple[int, int]]]: A list of tuples containing
            the image surface and its location for rendering.
        """
        render_context: list[tuple[pygame.Surface, tuple[int, int]]] = []

        for information in self.__componentManager.rendering_context:
            component_ID = information[0]
            location = information[1]
            priority = information[2]

            image = self.__assetManager.get_image(component_ID)
            render_information = (image, location, priority)

            render_context.append(render_information)

        return render_context

    def load_asset(self, asset: Assets) -> None:
        """
        Loads an asset (either an image or sound) using the asset manager
        and directly registers it in the AssetManager.

        Args:
            asset_name (str): The name of the asset to load.

        Raises:
            TypeError: If the asset is not a .png or .mp3 file.
        """
        if asset.NAME.endswith(".png"):
            self.__assetManager.load_image(asset)
        elif asset.NAME.endswith(".mp3"):
            self.__assetManager.load_sound(asset)
        else:
            raise TypeError("Asset must be either a .png or .mp3 file!")

    def create_component_highlight(
        self,
        component: Component,
        color: str = C.HIGHLIGHT_COLOR,
        border_width: int = C.HIGHLIGHT_BORDER_WIDTH
    ) -> None:
        """
        Adds a highlight to the specified component.

        Args:
            component (Component): The component to which the highlight will be added.
            color (str): The color of the highlight border. Defaults to highlight color from configuration.
            border_width (int): The width of the highlight border. Defaults to highlight border width from configuration.
        """
        # Create the highlight image for the component
        highlight, image = component.create_highlight_image(color, border_width)
        
        # Register the highlight component within the system
        self.register_component(highlight)
        
        # Register the highlight image with the corresponding highlight ID
        self.register_image(component.highlight_id, image)
    
    def add_component_highlight(self, component: Component, asset: Assets) -> None:

        self.load_asset(asset)
        image = self.__assetManager.get_image(asset.ID)
        delta_x = (component.size[0] - image.get_width()) / 2
        delta_y = (component.size[1] - image.get_height()) / 2

        location = (component.location.x + delta_x, component.location.y + delta_y)
        
        highlight = component.create_highlight(asset.ID, location, image.get_size())
        self.register_component(highlight)