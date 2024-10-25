import pygame
from src.core.InputHandler import InputHandler
from src.core.Renderer import Renderer
from src.core.Configuration import Game as CFG
from src.scenes.SceneManager import SceneManager

class Gameloop:
    """
    The Gameloop class manages all other managers and updates them at every tick.
    It handles the game clock, event processing, scene updates, and rendering.
    """

    def __init__(self) -> None:
        """
        Initializes a Gameloop object, all managers and the clock.
        """
        self.__clock = pygame.time.Clock()
        self.__inputhandler = InputHandler()
        self.__renderer = Renderer()
        self.__running = True
        self.__sceneManager = SceneManager()

    def update(self) -> None:
        """
        Manages the game flow, including processing events, updating scenes,
        and rendering graphics. Also handles quitting the game when requested.
        """
        # Tick the clock to manage the frame rate
        self.__clock.tick(CFG.FPS)

        # Run the event handler to process events
        eventcontext = self.__inputhandler.run(pygame.event.get())
        running = eventcontext[0]
        event_string = eventcontext[1]
        mouselocation = eventcontext[2]

        # Check if the scene manager has requested to stop the game
        if self.__sceneManager.stop:
            running = False

        # Stop the game loop if running is set to False
        if not running:
            self.stop()

        # Update the scene manager with the latest events and mouse location
        self.__sceneManager.update(event_string, mouselocation)

        # Render the current scene
        self.__renderer.run(self.rendering_context)

    def stop(self) -> None:
        """
        Stops the game loop by setting the running attribute to False.
        """
        self.__running = False

    @property
    def rendering_context(self) -> list[tuple[pygame.Surface, tuple[int, int]]]:
        """
        Retrieves the rendering context for the current scene.

        Returns:
            list[tuple[pygame.Surface, tuple[int, int]]]: A list of surfaces and their positions.
        """
        return self.__sceneManager.get_rendering_context()

    @property
    def running(self) -> bool:
        """
        Checks if the game loop is currently running.

        Returns:
            bool: True if the game loop is running, False otherwise.
        """
        return self.__running
