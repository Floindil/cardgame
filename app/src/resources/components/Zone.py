from src.core.Configuration import Card as CS
from src.resources.components.Dragable import Dragable
from src.resources.components.Component import Component

class Zone(Component):
    """
    The Zone class represents a specific area in the game and inherits from Component.
    It can hold a card and has a tag identifying it as a zone.
    """
    __occupant: Dragable

    def __init__(self, id: str, x: int, y: int, width: int, height: int) -> None:
        """
        Initializes a Zone with the given position and dimensions.
        
        Args:
            id (str): The identifier for the zone.
            x (int): The x-coordinate of the zone's position.
            y (int): The y-coordinate of the zone's position.
            width (int): The width of the zone.
            height (int): The height of the zone.
        """
        super().__init__(id, x, y, width, height)
        self.__occupant = None
        self._tag = "zone"

    def add__occupant(self, object: Dragable) -> None:
        """
        Adds a card to the zone.
        
        Args:
            card (Card): The card to be added.
        """
        self.__occupant = object

    def remove__occupant(self) -> None:
        """
        Removes the card from the zone.
        """
        self.__occupant = None

    @property
    def card(self) -> Dragable:
        """
        Gets the card currently in the zone.
        
        Returns:
            Card: The card in the zone, or None if no card is present.
        """
        return self.__occupant