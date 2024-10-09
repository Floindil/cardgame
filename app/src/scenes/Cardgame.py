from src.resources.assets.AssetManager import AssetManager
from src.resources.components.Zone import Zone
from src.scenes.Scene import Scene

class Cardgame(Scene):

    def __init__(self) -> None:
        super().__init__()

        zone1 = Zone(100, 100)
        self.register_component(zone1)