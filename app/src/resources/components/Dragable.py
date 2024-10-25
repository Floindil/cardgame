from pygame import Vector2

from src.resources.components.Component import Component
from src.core.Configuration import TAG

class Dragable(Component):
    """
    The Dragable class represents a draggable component in the game,
    inheriting from Component. It can be picked up, moved, and dropped
    into specified zones.

    Atributes:
        __drag (bool): Indicates if the object is currently being dragged
        __static (bool): Indicates if the object can be dragged
        __ancor (tuple[int, int]): Location to which the object returns when dropped
        __zones (list[list[str,bool]]): Indicates where the object can be dropped and if it can be moved afterwards
    """

    __drag: bool
    __static: bool
    __ancor: tuple[int, int]
    __zones: list[list[str,bool]]

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
        self._tag = TAG.DRAGABLES
        self.__drag = False
        self.__static = False
        self.__ancor = self.location
        self.__zones = []

    @property
    def ancor(self) -> Vector2:
        """Retunrs the ancor location of the dragable object."""
        return self.__ancor
    
    @ancor.setter
    def ancor(self, location: Vector2):
        self.__ancor = location

    @property
    def static(self) -> bool:
        """
        Indicates whether the dragable component is static and cannot be moved.

        Returns:
            bool: True if the component is static, False otherwise.
        """
        return self.__static
    
    @static.setter
    def static(self, state: bool) -> None:
        self.__static = state

    @property
    def drag(self) -> bool:
        """
        Indicates whether the dragable component is currently being dragged.

        Returns:
            bool: True if the component is being dragged, False otherwise.
        """
        return self.__drag
    
    @drag.setter
    def drag(self, state: bool) -> None:
        self.__drag = state
    
    @property
    def zone_ids(self) -> list[str]:
        """Returns a list of all registered zone ids."""
        ids = []
        for zone in self.__zones:
            ids.append(zone[0])
        return ids
    
    def get_zone_static_state(self, zone_id: str) -> bool:
        """Returns the static flag of the zone to indicate, if the dragable can
        be moved out of that zone. Returns None if the id is not registered"""
        for zone in self.__zones:
            if zone[0] == zone_id:
                return zone[1]
        return None

    def register_zone(self, zone_id: str, static: bool = False) -> None:
        """
        Registers a zone that the dragable component can be dropped into.

        Args:
            zone (Zone): The zone to be registered.
            static (bool, optional): Indicates if the component should become static when dropped in this zone. Defaults to False.
        """
        if zone_id not in self.__zones:
            self.__zones.append([zone_id, static])

    def unregister_zone(self, zone_id: str) -> None:
        """
        Unregisters a zone from the list of zones the dragable component can be dropped into.

        Args:
            zone (Zone): The zone to be unregistered.
        """
        if zone_id in self.zone_ids:
            index = self.zone_ids.index(zone_id)
            self.__zones.pop(index)
