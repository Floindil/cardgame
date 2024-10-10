from src.resources.components.Component import Component
from src.resources.components.Button import Button

class ComponentManager:
    """
    Provides functionalities to store and manage Components.
    """

    __components: dict

    def __init__(self) -> None:
        """
        Initializes the components dictionary.
        """
        self.__components = {}

    def register(self, component: Component) -> None:
        """
        Adds a component to the components dict and uses the ID of the 
        component as key.
        
        Args:
            component (Component): component to add to the components dict
        """
        self.__components.update({component.ID: component})

    def get(self, ID: str) -> Component:
        """
        Returns a component associated with the provided ID from the components dict.
        
        Args:
            ID (str): ID of the component, that should be returned

        Returns:
            component (Component): component associated with the provided ID
        """
        return self.__components.get(ID)

    @property
    def rendering_context(self) -> list:
        """
        Iterates through the components dict and gathers all the information needed
        for rendering from all components, where the RENDER flag is set to true.

        Returns:
            context (list): list of information needed to render the component
        """
        context = []
        for entity in self.__components:
            c: Component = self.__components.get(entity)
            if c.RENDER:
                context.append((c.image_id, c.location, c.RENDERPRIORITY))
        return context

    @property
    def components(self) -> dict:
        """Returns all registered components as dict."""
        return self.__components
    
    @property
    def buttons(self) -> list[Button]:
        """Returns all registered button components."""
        b = []
        for entity in self.__components:
            c = self.__components.get(entity)
            if isinstance(c, Component) and c.TAG == "button":
                b.append(c)
        return b
