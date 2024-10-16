from src.resources.components.Component import Component
from src.resources.components.Zone import Zone

class Dragable(Component):
    """
    The Dragable class represents a draggable component in the game,
    inheriting from Component. It can be picked up, moved, and dropped
    into specified zones.
    """

    __drag: bool                # Indicates if the object is currently being dragged
    __static: bool              # Indicates if the object can be dragged
    __ancor: tuple[int, int]    # Location to which the object returns when dropped
    __static_zone: list[bool]   # Indicates if the object can be moved from the corresponding zone
    __zones: list[Zone]         # Zones where the object can be dropped (same indexes as __static_zone)

    def __init__(self, id: str, x: int, y: int, width: int = 1, height: int = 1) -> None:
        """
        Initializes a Dragable object with the given dimensions and position.

        Args:
            id (str): ID for the dragable component.
            x (int): The x-coordinate of the component's initial position.
            y (int): The y-coordinate of the component's initial position.
            width (int, optional): The width of the component. Defaults to 1.
            height (int, optional): The height of the component. Defaults to 1.
        """
        super().__init__(id, x, y, width, height)
        self._tag = "dragable"
        self.__drag = False
        self.__static = False
        self.__ancor = self.location
        self.__static_zone = []
        self.__zones = []

    @property
    def static(self) -> bool:
        """
        Indicates whether the dragable component is static and cannot be moved.

        Returns:
            bool: True if the component is static, False otherwise.
        """
        return self.__static

    @property
    def drag(self) -> bool:
        """
        Indicates whether the dragable component is currently being dragged.

        Returns:
            bool: True if the component is being dragged, False otherwise.
        """
        return self.__drag

    def register_zone(self, zone: Zone, static: bool = False) -> None:
        """
        Registers a zone that the dragable component can be dropped into.

        Args:
            zone (Zone): The zone to be registered.
            static (bool, optional): Indicates if the component should become static when dropped in this zone. Defaults to False.
        """
        if zone not in self.__zones:
            self.__zones.append(zone)
            self.__static_zone.append(static)

    def unregister_zone(self, zone: Zone) -> None:
        """
        Unregisters a zone from the list of zones the dragable component can be dropped into.

        Args:
            zone (Zone): The zone to be unregistered.
        """
        if zone in self.__zones:
            index = self.__zones.index(zone)
            self.__zones.pop(index)
            self.__static_zone.pop(index)

    def pick_up(self) -> None:
        """
        Marks the dragable component as being picked up and increases its render priority.
        """
        if not self.__static:
            self.__drag = True
            self.RENDERPRIORITY += 1

    def drop(self, x: int, y: int) -> None:
        """
        Drops the dragable component at the specified coordinates. If it collides with a registered zone,
        the component is centered within that zone. Sets the object to static, if the collided zone is 
        marked as static. Resets the render priority.

        Args:
            x (int): The x-coordinate of the drop location.
            y (int): The y-coordinate of the drop location.
        """
        for i, zone in enumerate(self.__zones):
            if zone.collide_point(x, y):
                location = (
                    zone.location.x + (zone.size[0] - self.size[0]) / 2,
                    zone.location.y + (zone.size[1] - self.size[1]) / 2
                )
                if self.__static_zone[i]:
                    self.__static = True
                self.__ancor = location
                zone.add__occupant(self)
                break
        self.location = self.__ancor
        self.__drag = False
        self.RENDERPRIORITY -= 1
