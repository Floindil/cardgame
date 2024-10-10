from src.resources.components.Textfield import Textfield
from src.resources.components.Button import Button
from src.scenes.Scene import Scene

class Menu(Scene):

    def __init__(self) -> None:
        super().__init__()
        self._menuacces = False

        textfield = Textfield("MAIN MENU", 100, 100, color = "white", fontsize = 40)
        self.register_textfield(textfield)

        textfield = Textfield("inputcontrol", 100, 300, color = "white")
        self.register_textfield(textfield)

    def update(self, event: str, mouselocation: list[int, int]) -> None:
        super().update(event, mouselocation)
        textfield: Textfield = self.get_component("inputcontrol")
        textfield.text = self.last_event