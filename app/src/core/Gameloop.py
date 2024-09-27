import pygame
from src.core.Eventhandler import Eventhandler
from src.core.Renderer import Renderer
from src.core.Configuration import Configuration as CFG
from src.scenes.Cardgame import Cardgame
from src.scenes.Scene import Scene

class Gameloop:

    eventhandler: Eventhandler
    renderer: Renderer
    running: bool
    clock: pygame.time.Clock
    scene: Scene

    def __init__(self) -> None:
        self.clock = pygame.time.Clock()
        self.eventhandler = Eventhandler()
        self.renderer = Renderer()
        self.running = True
        self.scene = Cardgame()

    def run(self) -> None:

        self.clock.tick(CFG.FPS)

        self.running = self.eventhandler.run(pygame.event.get())

        self.renderer.run(self.scene)

    def stop(self):
        self.running = False