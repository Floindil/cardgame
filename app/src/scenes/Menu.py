from src.resources.components.Textfield import Textfield
from src.resources.components.Button import Button
from src.scenes.Scene import Scene

class Menu(Scene):

    def __init__(self) -> None:
        super().__init__()

        textfield = Textfield("text1", "Main Menu", 100, 100, color = "white")
        self.register_image(textfield.ID, textfield.image)
        self.register_component(textfield)

        self.load_asset("button.png")
        buttonsize = self.get_image_size("button")

        button = Button("START", 100, 300, buttonsize[0], buttonsize[1], image_id = "button")
        self.register_button(button)

    def update(self, event: str, mouselocation: list[int, int]) -> None:
        super().update(event, mouselocation)
        textfield: Textfield = self.get_component("text1")
        textfield.text = self.last_event