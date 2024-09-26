import pygame
from core.eventhandler import Eventhandler
from core.rendering import Renderer
from core.configuration import Configuration as CFG

class Gameloop:

    eventhandler: Eventhandler
    renderer: Renderer
    running: bool
    clock: pygame.time.Clock

    def __init__(self) -> None:
        self.clock = pygame.time.Clock()
        self.eventhandler = Eventhandler()
        self.renderer = Renderer()
        self.running = True

    def run(self) -> None:

        self.clock.tick(CFG.FPS)

        self.running = self.eventhandler.run(pygame.event.get())

        self.renderer.run()

    def stop(self):
        self.running = False