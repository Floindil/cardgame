import pygame
from src.core.Configuration import Game as CFG

class Renderer:
    """
    The Renderer class is responsible for handling all rendering operations in the game.
    It manages the display surface and renders components based on the provided rendering context.
    """
    
    __display: pygame.Surface
    __surface: pygame.Surface

    def __init__(self) -> None:
        """
        Initializes the Renderer class by setting up the display and surface.
        The display is set to the configured size and title, and the surface is filled with black.
        """
        self.__display = pygame.display.set_mode(CFG.DISPLAYSIZE)
        pygame.display.set_caption(CFG.TITLE)
        self.__surface = pygame.Surface(CFG.DISPLAYSIZE)
        self.__surface.fill("black")

    def run(self, rendering_context: list[tuple[pygame.Surface, tuple[int, int]]]) -> None:
        """
        Executes the rendering process. Clears the surface, then draws each component
        from the rendering context onto the surface. Finally, updates the display with
        the rendered content.

        Args:
            rendering_context (list[tuple[pygame.Surface, tuple[int, int]]]): 
                A list of tuples containing surfaces and their respective positions.
        """
        # Clear the surface by filling it
        self.__surface.fill("black")

        # Render each component in the rendering context
        if rendering_context:
            for component in rendering_context:
                image = component[0]
                location = component[1]
                if image:
                    self.__surface.blit(image, location)

        # Blit the surface onto the display
        self.__display.blit(self.__surface, (0, 0))

        # Update the display with the new frame
        pygame.display.update()

        # Ensure everything is properly drawn
        pygame.display.flip()
