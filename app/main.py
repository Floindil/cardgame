import pygame
from src.core.Gameloop import Gameloop

pygame.init()

gameloop = Gameloop()

while gameloop.running:
    gameloop.update()

pygame.quit()