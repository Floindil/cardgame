from src.resources.components.Textfield import Textfield
from src.scenes.Scene import Scene

class Menu(Scene):

    def __init__(self) -> None:
        super().__init__()

        textfield = Textfield("text1", "Main Menu", 100, 100, color = "white")
        self.register_image(textfield.ID, textfield.image)
        self.register_component(textfield)

    def update(self) -> None:
        super().update()
        textfield: Textfield = self.get_component("text1")
        if self.counter == 60:
            textfield.text = "Changed Text"
            textfield.location = (200, 200)
        if self.counter == 120:
            textfield.text = "F*** this is Wild!"
            textfield.location = (300, 300)
        if self.counter == 180:
            textfield.text = "TIME TO END THIS!"
            textfield.location = (400, 400)
        if self.counter == 240:
            self.end()