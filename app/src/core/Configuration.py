import pygame

class Configuration:
    """
    Holds configuration constants for the game.
    """
    DISPLAYSIZE = (1200, 750)
    TITLE = "Cardgame"
    FPS = 60

class Paths:
    """
    Holds paths used in the game.
    """
    ASSETS = "resources/assets/"

class Card:
    """
    Holds constants related to Cards.
    """
    SIZE = pygame.Vector2(100, 150)

class Fonts:
    STANDARDFONT = 'Trebuchet MS'
    STANDARDSIZE = 40
    TREBUCHET = 'Trebuchet MS'
    ARIAL = 'Arial'
    COURIER = 'Courier New'
    COMICSANS = 'Comic Sans MS'
    TREBUCHET = 'Trebuchet MS'
    IMPACT = 'Impact'
    LUCIDACONSOLE = 'Lucida Console'
    CHILLER = 'Chiller'
    INKFREE = 'Ink Free'

    @classmethod
    def font_exists(cls, font_name):
        # Collect all font values in the class
        font_values = [value for key, value in cls.__dict__.items() if not key.startswith("__") and isinstance(value, str)]
        # Check if the font_name exists in the font_values
        return font_name in font_values