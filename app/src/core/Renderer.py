import pygame
from src.core.Configuration import Configuration as CFG
from src.resources.components.Component import Component
from src.scenes.Scene import Scene


class Renderer:
    
    display: pygame.Surface

    def __init__(self) -> None:
        self.display = pygame.display.set_mode(CFG.DISPLAYSIZE)
        pygame.display.set_caption(CFG.TITLE)
        self.surface = pygame.Surface(CFG.DISPLAYSIZE)
        self.surface.fill("green")

    def run(self, scene: Scene):
        ctr: list[Component] = scene.getComponentsToRender()
        if ctr:
            for c in ctr:
                if c.imageName:
                    image = scene.assetManager.getImage(c.imageName)
                else:
                    image = c.image
                if image:
                    self.surface.blit(image, c.location)

        self.display.blit(self.surface, (0,0))
        
        pygame.display.flip()