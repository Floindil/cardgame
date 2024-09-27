from resources.assets.AssetManager import AssetManager
from resources.components.Zone import Zone
from scenes.Scene import Scene

class Cardgame(Scene):

    def __init__(self) -> None:
        super().__init__()

        zone1 = Zone(100, 100)
        self.addComponent(zone1)