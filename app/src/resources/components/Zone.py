from src.core.Configuration import Card as CS
from src.resources.components.Card import Card
from src.resources.components.Component import Component

class Zone(Component):
    """
    The Zone class represents a specific area in the game and inherits from Component.
    """

    TAG = "ZONE"

    def __init__(self, width: int, height: int, x: int, y: int) -> None:
        """
        Initializes a Zone with the given position.
        
        Args:
            x (int): The x-coordinate of the zone's position.
            y (int): The y-coordinate of the zone's position.
        """
        super().__init__(width, height, x, y)
        self._card = None

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
