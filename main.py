import pygame
from core.gameloop import Gameloop

gameloop = Gameloop()
pygame.init()

while gameloop.running:
    gameloop.run()

pygame.quit()