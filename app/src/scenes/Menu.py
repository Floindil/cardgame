from src.resources.components.Textfield import Textfield
from src.scenes.Scene import Scene

class Menu(Scene):

    def __init__(self) -> None:
        super().__init__()

        self.textfield = Textfield("Main Menu", 100, 100, color = "white")
        self.textfield.image_name = "text1"
        self.register_image("text1", self.textfield.image)
        self.add_component(self.textfield)

    def update(self) -> None:
        super().update()
        if self.counter == 60:
            self.textfield.text = "Changed Text"
            self.textfield.location = (200, 200)
        if self.counter == 120:
            self.textfield.text = "F*** this is Wild!"
            self.textfield.location = (300, 300)
        if self.counter == 180:
            self.textfield.text = "TIME TO END THIS!"
            self.textfield.location = (400, 400)
        if self.counter == 240:
            self.end()