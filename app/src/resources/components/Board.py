import pygame
from src.resources.components.Zone import Zone
from src.resources.components.Component import Component

class Board(Component):

    __zones: list[Zone]

    def __init__(self, size: tuple[int, int], position: tuple[int, int]) -> None:
        super().__init__(size, position)
        self.__zones = []

    def register_zone(self, zone: Zone):
        self.__zones.append(zone)