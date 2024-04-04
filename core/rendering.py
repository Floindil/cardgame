import pygame
from core.configuration import Configuration as CFG

class Render:
    def __init__(self) -> None:
        self.surface = pygame.Surface(CFG.DISPLAYSIZE)
        self.surface.fill("green")

    def run(self, display: pygame.Surface):
        display.blit(self.surface, (0,0))