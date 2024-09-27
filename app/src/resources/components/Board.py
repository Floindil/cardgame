import pygame
from src.resources.components.Zone import Zone
from src.resources.components.Component import Component

class Board(Component):

    surface: pygame.Surface
    zones: list[Zone]

    def __init__(self, size: tuple[int, int], position: tuple[int, int]) -> None:
        super().__init__(size, position)
        self.zones = []

    def register_zone(self, zone: Zone):
        self.zones.append(zone)
        self.surface.blit(zone.surface, zone.position)