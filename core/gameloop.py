import pygame
from core.eventhandler import Eventhandler
from core.rendering import Render
from core.configuration import Configuration as CFG

class Gameloop:

    eventhandler: Eventhandler
    render: Render
    running: bool
    display: pygame.display
    clock: pygame.time.Clock

    def __init__(self) -> None:
        self.display = pygame.display.set_mode(CFG.DISPLAYSIZE)
        pygame.display.set_caption(CFG.TITLE)
        self.clock = pygame.time.Clock()
        self.eventhandler = Eventhandler()
        self.render = Render()
        self.running = True

    def run(self) -> None:

        self.clock.tick(CFG.FPS)

        self.running = self.eventhandler.run(pygame.event.get())

        self.render.run(self.display)

        pygame.display.flip()

    def stop(self):
        self.running = False