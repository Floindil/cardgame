import pygame
from board.statics import Boardstatics as BS

class Zone:

    surface: pygame.Surface
    available: bool = True


    def __init__(self) -> None:
        self.surface = pygame.Surface(BS.ZONESIZE)
        self.surface.fill("yellow")
        self.available = True