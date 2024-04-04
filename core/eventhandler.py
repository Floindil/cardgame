import pygame

class Eventhandler:
    def __init__(self) -> None:
        pass

    def run(self, events: list[pygame.event.Event]):
        for event in events:
            if event.type == pygame.QUIT:
                return False
        return True