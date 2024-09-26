import pygame
from core.statics import Card as CS
from assets.card.card import Card
from assets.asset import Asset

class Zone(Asset):

    TAG = "ZONE"

    surface: pygame.Surface
    position: pygame.Vector2
    cards: list[Card]


    def __init__(self, capability: int, position: pygame.Vector2) -> None:
        self.capability = capability
        self.position = position
        size = CS.SIZE.x*capability, CS.SIZE.y
        self.surface = pygame.Surface(size)
        self.surface.fill("yellow")
        self.cards = []

    def add_card(self, card: Card) -> bool:
        if len(self.cards) < self.capability:
            self.cards.append(card)
            return True
        return False

    def remove_card(self, card: Card) -> None:
        self.cards.remove(card)