from src.resources.components.Component import Component
from src.resources.components.Zone import Zone

class Dragable(Component):
    """
    The Dragable class represents a draggable component in the game,
    inheriting from Component. It can be picked up, moved, and dropped
    into specified zones.
    """

    __drag: bool                # indicates, if the object is currently beeing dragged
    __static: bool              # indicates, if the object can be dragged
    __ancor: tuple[int, int]    # location to which the object returnes, when dropped
    __zones: list[Zone]         # zones, where the object can be dropped

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
        self.__zones = []

    @property
    def static(self) -> bool:
        """Indicates whether the dragable component is static and cannot be moved."""
        return self.__static

    @property
    def drag(self) -> bool:
        """Indicates whether the dragable component is currently being dragged."""
        return self.__drag

    def register_zone(self, zone: Zone) -> None:
        """
        Registers a zone that the dragable component can be dropped into.

        Args:
            zone (Zone): The zone to be registered.
        """
        if zone not in self.__zones:
            self.__zones.append(zone)

    def unregister_zone(self, zone: Zone) -> None:
        """
        Unregisters a zone from the list of zones the dragable component can be dropped into.

        Args:
            zone (Zone): The zone to be unregistered.
        """
        if zone in self.__zones:
            self.__zones.remove(zone)

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
        the component is centered within that zone. Resets the render priority.

        Args:
            x (int): The x-coordinate of the drop location.
            y (int): The y-coordinate of the drop location.
        """
        for zone in self.__zones:
            if zone.collide_point(x, y):
                location = (
                    zone.location.x + (zone.size[0] - self.size[0]) / 2,
                    zone.location.y + (zone.size[1] - self.size[1]) / 2
                )
                self.__ancor = location
                zone.add__occupant(self)
                break
        self.location = self.__ancor
        self.__drag = False
        self.RENDERPRIORITY -= 1
