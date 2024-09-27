import pygame
from src.core.Eventhandler import Eventhandler
from src.core.Renderer import Renderer
from src.core.Configuration import Configuration as CFG
from src.scenes.Cardgame import Cardgame
from src.scenes.Scene import Scene
from src.scenes.SceneManager import SceneManager

class Gameloop:
    """
    The Gameloop manages all other managers and updates them at every tick.
    """

    eventhandler: Eventhandler
    renderer: Renderer
    running: bool
    clock: pygame.time.Clock
    sceneManager: SceneManager

    def __init__(self) -> None:
        """
        Creates a Gameloop Object and initializes all other
        managers and the clock.
        """
        self.clock = pygame.time.Clock()
        self.eventhandler = Eventhandler()
        self.renderer = Renderer()
        self.running = True
        scene = Cardgame()
        self.sceneManager = SceneManager(scene)

    def update(self) -> None:
        """
        Manages the game flow and quits the game, when asked to.
        """

        self.clock.tick(CFG.FPS)

        self.running = self.eventhandler.run(pygame.event.get())

        self.sceneManager.update()

        self.renderer.run(self.sceneManager.activeScene)

    def stop(self):
        self.running = False