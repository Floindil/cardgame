import pygame
from assets.board.zone import Zone
from assets.board.statics import Board as B
from assets.asset import Asset

class Board(Asset):

    surface: pygame.Surface
    zones: list[Zone]

    def __init__(self, size: tuple[int, int], position: tuple[int, int]) -> None:
        super().__init__(size, position)
        self.zones = []

    def register_zone(self, zone: Zone):
        self.zones.append(zone)
        self.surface.blit(zone.surface, zone.position)