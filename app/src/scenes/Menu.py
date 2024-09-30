import pygame

from src.resources.components.Zone import Zone
from src.scenes.Scene import Scene

class Menu(Scene):

    def __init__(self) -> None:
        super().__init__()

        zonesize = pygame.Vector2(120, 170)

        zone_image = pygame.Surface(zonesize.xy)
        zone_image.fill("white")
        image_name = "zone"
        self.register_image(image_name, zone_image)

        zone1 = Zone(zonesize.x, zonesize.y, 100, 100)
        zone1.image_name = image_name
        self.add_component(zone1)

        zone2 = Zone(zonesize.x, zonesize.y, 240, 100)
        zone2.image_name = image_name
        self.add_component(zone2)
        
        