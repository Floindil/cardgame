from src.resources.components.Component import Component
from src.resources.components.Dragable import Dragable
from src.resources.components.Button import Button

class ComponentManager:
    """
    Manages and stores various components for the game, including buttons, dragables, and other components.
    
    Attributes:
        __buttons (dict[str, Button]): A dictionary to store Button components with their IDs as keys.
        __dragables (dict[str, Dragable]): A dictionary to store Dragable components with their IDs as keys.
        __other (dict[str, Component]): A dictionary to store other types of components with their IDs as keys.
        __dragable_priority (int): The priority value used to manage render priorities of dragable components.
    """

    __buttons: dict[str, Button]
    __dragables: dict[str, Dragable]
    __other: dict[str, Component]
    __dragable_priority: int

    def __init__(self) -> None:
        """
        Initializes the ComponentManager with empty dictionaries for buttons, dragables, and other components.
        """
        self.__buttons = {}
        self.__dragables = {}
        self.__other = {}
        self.__dragable_priority = 0

    def register(self, component: Component) -> None:
        """
        Registers a component by adding it to the appropriate dictionary based on its type.

        Args:
            component (Component): The component to register. It can be of type Button, Dragable, or any other type that inherits from Component.
        """
        if isinstance(component, Button):
            self.__buttons[component.ID] = component
            self.update_dragable_priority(component.render_priority)

        elif isinstance(component, Dragable):
            component.render_priority = self.__dragable_priority
            self.__dragables[component.ID] = component

        else:
            self.__other[component.ID] = component
            self.update_dragable_priority(component.render_priority)
    
    def unregister(self, component: Component) -> None:
        """
        Unregisters a component by removing it from the appropriate dictionary based on its type.

        Args:
            component (Component): The component to unregister. It can be of type Button, Dragable, or any other type that inherits from Component.
        """
        if isinstance(component, Button):
            self.__buttons.pop(component.ID)

        elif isinstance(component, Dragable):
            self.__dragables.pop(component.ID)

        else:
            self.__other.pop(component.ID)

    def update(self, interaction: bool, event: str, mouselocation: tuple[int, int]) -> list[tuple]:
        """
        Update the state of components, handle interactions, and return asset updates.

        Args:
            interaction (bool): Flag indicating if there is user interaction.
            event (str): Description of the event (e.g., mouse button down/up).
            mouselocation (tuple[int, int]): Current mouse cursor location (x, y).

        Returns:
            list[tuple]: A list of tuples containing component IDs and updated images.
        """

        asset_updates = []

        for entity in self.components:
            c: Component = self.components.get(entity)

            # Unregister the component if it's marked for removal
            if c.remove:
                self.unregister(c)

            # Add component image to asset update list if it has been changed
            if c.update:
                asset_updates.append((c.ID, c.image))
                c.reset_update()

            # Update location of draggable components
            if isinstance(c, Dragable) and c.drag:
                c.location = (mouselocation[0] - c.size[0] / 2, mouselocation[1] - c.size[1] / 2)

        if interaction:
            # Handle mouse button down event
            if "//m1d" in event:
                # Check for button interactions
                for button in self.buttons:
                    if button.collide_point(mouselocation[0], mouselocation[1]) and button.active:
                        button.flag = True
                        break

                # Check for draggable interactions
                for dragable in self.dragables:
                    if not dragable.static \
                    and dragable.collide_point(mouselocation[0], mouselocation[1]) \
                    and dragable.active:
                        dragable.pick_up()
                        break

            # Handle mouse button up event
            if "//m1u" in event:
                # Trigger button actions
                for button in self.buttons:
                    if button.collide_point(mouselocation[0], mouselocation[1]) and button.flag:
                        button.action()
                    button.flag = False

                # Drop draggable components
                for dragable in self.dragables:
                    if not dragable.static and dragable.collide_point(mouselocation[0], mouselocation[1]):
                        dragable.drop(mouselocation[0], mouselocation[1])

        return asset_updates

    def update_dragable_priority(self, priority: int) -> None:
        """
        Updates the dragable priority if the given priority matches the current dragable priority.

        Args:
            priority (int): The priority value to be checked and potentially updated.
        """
        if priority == self.__dragable_priority:
            self.__dragable_priority = priority + 1

            for dragable in self.dragables:
                dragable.RENDERPRIORITY = self.__dragable_priority

    def get(self, ID: str) -> Component:
        """
        Retrieves a component from the stored dictionaries using its ID.

        Args:
            ID (str): The ID of the component to retrieve.

        Returns:
            Component: The component associated with the provided ID. Returns None if no component with the given ID is found.
        """
        if ID in self.__buttons:
            return self.__buttons.get(ID)

        elif ID in self.__dragables:
            return self.__dragables.get(ID)

        else:
            return self.__other.get(ID)

    @property
    def rendering_context(self) -> list[tuple[str, tuple[int, int], int]]:
        """
        Gathers rendering information from all components that have the RENDER flag set to True.

        Returns:
            list[tuple[str, tuple[int, int], int]]: A list of tuples containing the image_id, location, and render priority of each component to be rendered.
        """
        return [
            (c.image_id, c.location, c.render_priority)
            for c in self.components.values()
            if c.render
        ]

    @property
    def components(self) -> dict[str, Component]:
        """
        Retrieves all registered components as a dictionary.

        Returns:
            dict[str, Component]: A dictionary of all registered components, including buttons, dragables, and others.
        """
        components = {}
        components.update(self.__buttons)
        components.update(self.__dragables)
        components.update(self.__other)
        return components
    
    @property
    def buttons(self) -> list[Button]:
        """
        Retrieves all registered Button components.

        Returns:
            list[Button]: A list of all Button components.
        """
        return list(self.__buttons.values())
    
    @property
    def dragables(self) -> list[Dragable]:
        """
        Retrieves all registered Dragable components.

        Returns:
            list[Dragable]: A list of all Dragable components.
        """
        return list(self.__dragables.values())
