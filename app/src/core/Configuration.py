import pygame

class Game:
    """
    Holds configuration constants for the game.
    """
    DISPLAYSIZE = (1200, 750)  # Screen size of the game window
    TITLE = "Cardgame"         # Title of the game window
    FPS = 60                   # Frames per second (frame rate) for the game
    HIGHLIGHT_COLOR = "yellow" # Standard color for Component highlights
    HIGHLIGHT_BORDER_WIDTH = 3 # Standard border width for Component highlights

class TAG:
    COMPONENTS = "components"
    BUTTONS = "buttons"
    DRAGABLES = "dragables"
    TEXTFIELDS = "textfields"
    ZONES = "zones"
    POPUP = "popup"

class Paths:
    """
    Holds paths used in the game.
    """
    ASSETS = "app/src/resources/assets/"  # Path to the assets directory

class Assets:
    """
    Holds asset names and IDs used in the game.
    """
    NAME: str
    ID: str

    class BUTTON:
        """
        Constants for the button asset.
        """
        NAME = "button.png"
        ID = NAME.replace(".png", "")

class PopupTypes:
    HOVER = 0
    CLICK = 1

class Card:
    """
    Holds constants related to Cards.
    """
    SIZE = pygame.Vector2(100, 150)  # Default size of a card

class Fonts:
    """
    Holds font constants used in the game.
    """
    STANDARDFONT = 'Lucida Console'
    STANDARDSIZE = 20
    LINEBUFFER = 3
    STANDARDCOLOR = "white"
    BUTTONCOLOR = "black"
    TREBUCHET = 'Trebuchet MS'
    ARIAL = 'Arial'
    COURIER = 'Courier New'
    COMICSANS = 'Comic Sans MS'
    IMPACT = 'Impact'
    LUCIDACONSOLE = 'Lucida Console'
    CHILLER = 'Chiller'
    INKFREE = 'Ink Free'

    @classmethod
    def font_exists(cls, font_name: str) -> bool:
        """
        Checks if a given font name exists in the Fonts class.

        Args:
            font_name (str): The name of the font to check.

        Returns:
            bool: True if the font exists, False otherwise.
        """
        # Collect all font values in the class
        font_values = [value for key, value in cls.__dict__.items() if not key.startswith("__") and isinstance(value, str)]
        # Check if the font_name exists in the font_values
        return font_name in font_values
