import pygame

class Component:
    """
    The Component class is used as a base for every
    Object that might be displayed on the screen.
    """

    RENDER: bool
    RENDERPRIORITY: int

    location: pygame.Vector2
    image: pygame.Surface
    imageName: str

    def __init__(self, x: int, y: int) -> None:
        self.RENDER = True
        self.RENDERPRIORITY = 0
        self.location = pygame.Vector2(x, y)
        self.image = None
        self.imageName = None