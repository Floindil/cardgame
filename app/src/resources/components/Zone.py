import pygame
from src.core.Configuration import Card as CS
from src.resources.components.Card import Card
from src.resources.components.Component import Component

class Zone(Component):

    TAG = "ZONE"

    card: Card

    def __init__(self, x: int, y:int) -> None:
        super().__init__(x, y)
        size = CS.SIZE.x, CS.SIZE.y
        self.image = pygame.Surface(size)
        self.image.fill("yellow")
        self.card = None

    def addCard(self, card: Card) -> None:
        self.card = card

    def removeCard(self) -> None:
        self.card = None