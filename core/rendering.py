import pygame
from core.configuration import Configuration as CFG


class Renderer:
    
    display: pygame.Surface

    def __init__(self) -> None:
        self.display = pygame.display.set_mode(CFG.DISPLAYSIZE)
        pygame.display.set_caption(CFG.TITLE)
        self.surface = pygame.Surface(CFG.DISPLAYSIZE)
        self.surface.fill("green")

    def run(self):
        self.display.blit(self.surface, (0,0))
        
        pygame.display.flip()