import pygame

class Asset:

    RENDER: bool = True
    TAG = "ASSET"

    size: tuple[int,int]
    position:  tuple[int,int]
    surface: pygame.Surface

    def __init__(self, size: tuple[int,int], position: tuple[int,int]) -> None:
        self.size = pygame.Vector2(size)
        self.position = pygame.Vector2(position)
        self.surface = pygame.Surface(self.size.xy)

    def render(self, display_surface: pygame.Surface):
        display_surface.blit(self.surface, self.position)