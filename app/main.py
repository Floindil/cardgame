import pygame
from src.core.Gameloop import Gameloop

gameloop = Gameloop()
pygame.init()

while gameloop.running:
    gameloop.run()

pygame.quit()