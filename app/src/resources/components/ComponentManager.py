from src.resources.components.Component import Component
from src.resources.components.Button import Button

class ComponentManager:
    """
    Manages and stores components for the game.
    """
    __components: dict[str, Component]

    def __init__(self) -> None:
        """
        Initializes the ComponentManager with an empty dictionary for components.
        """
        self.__components = {}

    def register(self, component: Component) -> None:
        """
        Registers a component by adding it to the components dictionary using the component's ID as the key.
        
        Args:
            component (Component): The component to add to the components dictionary.
        """
        self.__components[component.ID] = component

    def get(self, ID: str) -> Component:
        """
        Retrieves a component from the components dictionary using its ID.
        
        Args:
            ID (str): The ID of the component to retrieve.

        Returns:
            Component: The component associated with the provided ID.
        """
        return self.__components.get(ID)

    @property
    def rendering_context(self) -> list[tuple[str, tuple[int, int], int]]:
        """
        Gathers rendering information from all components that have the RENDER flag set to True.

        Returns:
            list: A list of tuples containing the image_id, location, and render priority of each component to be rendered.
        """
        context = [
            (c.image_id, c.location, c.RENDERPRIORITY)
            for c in self.__components.values()
            if c.RENDER
        ]
        return context

    @property
    def components(self) -> dict[str, Component]:
        """
        Returns all registered components as a dictionary.

        Returns:
            dict: A dictionary of all registered components.
        """
        return self.__components
    
    @property
    def buttons(self) -> list[Button]:
        """
        Returns all registered button components.

        Returns:
            list[Button]: A list of all button components.
        """
        return [c for c in self.__components.values() if isinstance(c, Button)]
