from src.core.Configuration import Card as CS
from src.resources.components.Card import Card
from src.resources.components.Component import Component

class Zone(Component):
    """
    The Zone class represents a specific area in the game and inherits from Component.
    It can hold a card and has a tag identifying it as a zone.
    """

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
        self._card = None
        self._tag = "zone"

    def add_card(self, card: Card) -> None:
        """
        Adds a card to the zone.
        
        Args:
            card (Card): The card to be added.
        """
        self._card = card

    def remove_card(self) -> None:
        """
        Removes the card from the zone.
        """
        self._card = None

    @property
    def card(self) -> Card:
        """
        Gets the card currently in the zone.
        
        Returns:
            Card: The card in the zone, or None if no card is present.
        """
        return self._card