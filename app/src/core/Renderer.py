import pygame
from src.core.Configuration import Configuration as CFG
from src.resources.components.Component import Component
from src.scenes.Scene import Scene


class Renderer:
    
    __display: pygame.Surface
    __surface: pygame.Surface

    def __init__(self) -> None:
        self.__display = pygame.display.set_mode(CFG.DISPLAYSIZE)
        pygame.display.set_caption(CFG.TITLE)
        self.__surface = pygame.Surface(CFG.DISPLAYSIZE)
        self.__surface.fill("black")

    def run(self, rendering_context: list[tuple[pygame.Surface, tuple[int, int]]]) -> None:
        self.__surface.fill("black")
        if rendering_context:
            for c in rendering_context:
                image = c[0]
                location = c[1]
                if image:
                    self.__surface.blit(image, location)

        self.__display.blit(self.__surface, (0,0))

        pygame.display.update()
        
        pygame.display.flip()