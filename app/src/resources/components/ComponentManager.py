from src.resources.components.Component import Component
from src.resources.components.Dragable import Dragable
from src.resources.components.Button import Button
from src.resources.components.Zone import Zone
from src.core.Configuration import TAG

class ComponentManager:
    """
    Manages and stores various components for the game, including buttons, dragables, and other components.
    
    Attributes:
        __buttons (dict[str, Button]): A dictionary to store Button components with their IDs as keys.
        __dragables (dict[str, Dragable]): A dictionary to store Dragable components with their IDs as keys.
        __other (dict[str, Component]): A dictionary to store other types of components with their IDs as keys.
        __dragable_priority (int): The priority value used to manage render priorities of dragable components.
    """
    __components: dict[str, Component]
    __dragable_priority: int

    def __init__(self) -> None:
        """
        Initializes the ComponentManager with empty dictionaries for buttons, dragables, and other components.
        """
        self.__components = {}
        self.__dragable_priority = 0

    def register(self, component: Component) -> None:
        """
        Registers a component by adding it to the appropriate dictionary based on its type.

        Args:
            component (Component): The component to register. It can be of type Button, Dragable, or any other type that inherits from Component.
        """
        if not self.__components.get(component.TAG):
            self.__components.update({component.TAG: {}})
        if component.TAG == TAG.DRAGABLES:
            component.render_priority = self.__dragable_priority
        self.__components.get(component.TAG).update({component.ID:component})
        self.update_dragable_priority(component.render_priority)
    
    def unregister(self, component: Component) -> None:
        """
        Unregisters a component by removing it from the appropriate dictionary based on its type.

        Args:
            component (Component): The component to unregister. It can be of type Button, Dragable, or any other type that inherits from Component.
        """
        self.__components[component.TAG].pop(component.ID)

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

        for id in self.components:
            c: Component = self.components.get(id)
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

            buttons: list[Button] = self.get_by_tag(TAG.BUTTONS)
            dragables: list[Dragable] = self.get_by_tag(TAG.DRAGABLES)

            # Handle mouse button down event
            if "//m1d" in event:
                # Check for button interactions
                for button in buttons:
                    if button.collide_point(mouselocation[0], mouselocation[1]) and button.active:
                        button.flag = True
                        break

                # Check for draggable interactions
                for dragable in dragables:
                    if not dragable.static \
                    and dragable.collide_point(mouselocation[0], mouselocation[1]) \
                    and dragable.active:
                        self.__pick_up_dragable(dragable)
                        break

            # Handle mouse button up event
            if "//m1u" in event:
                # Trigger button actions
                for button in buttons:
                    if button.collide_point(mouselocation[0], mouselocation[1]) and button.flag:
                        button.action()
                    button.flag = False

                # Drop draggable components
                for dragable in dragables:
                    if not dragable.static and dragable.collide_point(mouselocation[0], mouselocation[1]):
                        self.__drop_dragable(dragable)

        return asset_updates

    def update_dragable_priority(self, priority: int) -> None:
        """
        Updates the dragable priority if the given priority matches the current dragable priority.

        Args:
            priority (int): The priority value to be checked and potentially updated.
        """
        if priority >= self.__dragable_priority:
            self.__dragable_priority = priority + 1

            dragables = self.get_by_tag(TAG.DRAGABLES)
            if dragables:
                for dragable in dragables:
                    dragable.render_priority = self.__dragable_priority

    def get(self, ID: str) -> Component:
        """
        Retrieves a component from the stored dictionary using its ID.

        Args:
            ID (str): The ID of the component to retrieve.

        Returns:
            Component: The component associated with the provided ID. Returns None if no component with the given ID is found.
        """
        for tag in self.__components:
            if self.__components[tag].get(ID):
                return self.__components[tag].get(ID)
        return None

    @property
    def rendering_context(self) -> list[tuple[str, tuple[int, int], int]]:
        """
        Gathers rendering information from all components that have the RENDER flag set to True and orders them by
        render_priority.

        Returns:
            list[tuple[str, tuple[int, int], int]]: A list of tuples containing the image_id, location, and render priority of each component to be rendered.
        """
        components_to_render = []

        for c in self.components.values():
            if c.render:

                render_information = (c.image_id, c.location, c.render_priority)
                inserted = False

                if components_to_render:
                    for i, values in enumerate(components_to_render):
                        if c.render_priority <= values[2]:
                            components_to_render.insert(i, render_information)
                            inserted = True
                            break
                    if not inserted:
                        components_to_render.append(render_information)
                else:    
                    components_to_render.append(render_information)

        return components_to_render

    @property
    def components(self) -> dict[str, Component]:
        """
        Retrieves all registered components as a dictionary.

        Returns:
            dict[str, Component]: A dictionary of all registered components, including buttons, dragables, and others.
        """
        components = {}
        for component in self.__components.values():
            components.update(component)
        return components
    
    def get_by_tag(self, tag: TAG) -> list[Component]:
        """
        Retrieves all registered components with the provided Tag.

        Returns:
            list[Component]: A list of all components with the provided Tag.
        """
        tagged_components = self.__components.get(tag)
        if tagged_components:
            return list(tagged_components.values())
        return {}
    
    def __pick_up_dragable(self, dragable: Dragable):
        if not dragable.static:
            dragable.drag = True
            dragable.render_priority += 1

            for zone_id in dragable.zone_ids:
                zone: Zone = self.get(zone_id)
                zone.set_highlight(True)

    def __drop_dragable(self, dragable: Dragable) -> None:
        """
        Drops the dragable component at the specified coordinates. If it collides with a registered zone,
        the component is centered within that zone. Sets the object to static, if the collided zone is 
        marked as static. Resets the render priority. Deactivates all the highlights of zones.

        Args:
            x (int): The x-coordinate of the drop location.
            y (int): The y-coordinate of the drop location.
        """
        for id in dragable.zone_ids:
            zone: Zone = self.__components[TAG.ZONES].get(id)

            # Activate the zones highlight, if it has one
            if zone.highlight:
                zone.set_highlight(False)

            # Update the zone and component, if the component can be dropped
            if zone.collide_point(dragable.location.x, dragable.location.y):
                location = (
                    zone.location.x + (zone.size[0] - dragable.size[0]) / 2,
                    zone.location.y + (zone.size[1] - dragable.size[1]) / 2
                )
                # Set self to static, if the zone is indicated as static
                if dragable.get_zone_static_state(id):
                    dragable.static = True

                dragable.ancor = location
                zone.add__occupant(dragable)
                break

        dragable.location = dragable.ancor
        dragable.drag = False
        dragable.render_priority -= 1
