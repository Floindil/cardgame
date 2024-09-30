import pygame
from src.core.Eventhandler import Eventhandler
from src.core.Renderer import Renderer
from src.core.Configuration import Configuration as CFG
from src.scenes.SceneManager import SceneManager

class Gameloop:
    """
    The Gameloop manages all other managers and updates them at every tick.
    """

    def __init__(self) -> None:
        """
        Creates a Gameloop Object and initializes all other
        managers and the clock.
        """
        self.__clock = pygame.time.Clock()
        self.__eventhandler = Eventhandler()
        self.__renderer = Renderer()
        self.__running = True
        self.__sceneManager = SceneManager()

    def update(self) -> None:
        """
        Manages the game flow and quits the game, when asked to.
        """
        self.__clock.tick(CFG.FPS)
        self.__running = self.__eventhandler.run(pygame.event.get())
        self.__sceneManager.update()
        self.__renderer.run(self.rendering_context)

    def stop(self):
        self.__running = False

    @property
    def rendering_context(self) -> list[tuple[pygame.Surface, tuple[int, int]]]:
        return self.__sceneManager.get_rendering_context()

    @property
    def running(self) -> bool:
        """Public getter for the running attribute."""
        return self.__running

    @running.setter
    def running(self, value: bool) -> None:
        """Public setter for the running attribute."""
        self.__running = value
