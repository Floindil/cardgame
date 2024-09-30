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