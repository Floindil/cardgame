from src.resources.components.Textfield import Textfield
from src.scenes.Scene import Scene

class Menu(Scene):

    def __init__(self) -> None:
        super().__init__()

        textfield = Textfield("text1", "Main Menu", 100, 100, color = "white")
        self.register_image(textfield.ID, textfield.image)
        self.register_component(textfield)

    def update(self, event: str, mouselocation: list[int, int]) -> None:
        super().update(event, mouselocation)
        textfield: Textfield = self.get_component("text1")
        textfield.text = self.last_event