from src.resources.components.Zone import Zone
from src.resources.components.Button import Button
from src.resources.components.Textfield import Textfield
from src.scenes.Scene import Scene

class Cardgame(Scene):

    def __init__(self) -> None:
        super().__init__()

    def start(self) -> None:

        textfield = Textfield("CARDGAME", 100, 100, color = "white", fontsize = 40)
        self.register_textfield(textfield)

        self.load_asset("fieldzone.png")
        fieldzone_size = self.get_image_size("fieldzone")
        fieldzone = Zone("fieldzone", 200, 200, fieldzone_size[0], fieldzone_size[1])
        self.register_component(fieldzone)

        self.load_asset("gravezone.png")
        gravezone_size = self.get_image_size("gravezone")
        gravezone = Zone("gravezone", 400, 200, gravezone_size[0], gravezone_size[1])
        self.register_component(gravezone)

        textfield = Textfield("inputcontrol", 100, 300, color = "white")
        self.register_textfield(textfield)

    def update(self, event: str, mouselocation: list[int, int]) -> None:
        super().update(event, mouselocation)
        textfield: Textfield = self.get_component("inputcontrol")
        textfield.text = self.last_event