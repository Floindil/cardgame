import pygame

from src.resources.components.Zone import Zone
from src.resources.components.Dragable import Dragable
from src.resources.components.Textfield import Textfield
from src.scenes.Scene import Scene

class Cardgame(Scene):
    """
    Cardgame class extends the Scene class and represents the main 
    logic for the card game. It handles the initialization and 
    updating of various components like text fields and zones.
    """

    def __init__(self) -> None:
        """
        Initializes the Cardgame class. Calls the initializer of the 
        parent Scene class.
        """
        super().__init__()

    def start(self) -> None:
        """
        Starts the card game by setting up initial components such as
        text fields and zones. Loads assets and registers components 
        for the game.
        """
        # Create and register a title text field
        textfield = Textfield("CARDGAME", 100, 100, fontsize=40)
        self.register_textfield(textfield)

        # Create and register an input control text field
        textfield = Textfield("inputcontrol", 100, 150)
        self.register_textfield(textfield)

        # Load and register the field zone component
        self.load_asset(self.assets.FIELDZONE)
        fieldzone_size = self.get_image_size(self.assets.FIELDZONE.ID)
        fieldzone = Zone(self.assets.FIELDZONE.ID, 200, 200, fieldzone_size[0], fieldzone_size[1])
        self.register_component(fieldzone)

        # Load and register the grave zone component
        self.load_asset(self.assets.GRAVEZONE)
        gravezone_size = self.get_image_size(self.assets.GRAVEZONE.ID)
        gravezone = Zone(self.assets.GRAVEZONE.ID, 400, 200, gravezone_size[0], gravezone_size[1])
        self.register_component(gravezone)

        # Create and register a blank card image for testing
        card_image = pygame.Surface((50, 75))
        card_image.fill(pygame.Color('white'))
        self.register_image("card", card_image)

        # Create and register a draggable object and register zones, where it can be dropped
        card = Dragable("card", 200, 400, card_image.get_width(), card_image.get_height())
        card.register_zone(fieldzone)
        card.register_zone(gravezone)
        self.register_component(card)

    def update(self, event: str, mouselocation: list[int, int]) -> None:
        """
        Updates the game state based on events and mouse location.
        
        Args:
            event (str): The latest event to process.
            mouselocation (list[int, int]): The current mouse location.
        """
        super().update(event, mouselocation)

        # Update the text of the input control text field with the last event
        textfield: Textfield = self.get_component("inputcontrol")
        textfield.text = self.last_event
