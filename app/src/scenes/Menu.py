from src.resources.components.Textfield import Textfield
from src.resources.components.Button import Button
from src.scenes.Start import Start
from src.scenes.Scene import Scene

class Menu(Scene):

    def __init__(self) -> None:
        super().__init__()
        self._menuacces = False

    def start(self) -> None:

        textfield = Textfield("MAIN MENU", 100, 100, color = "white", fontsize = 40)
        self.register_textfield(textfield)

        textfield = Textfield("inputcontrol", 100, 300, color = "white")
        self.register_textfield(textfield)

        self.load_asset("button.png")
        buttonsize = self.get_image_size("button")

        button = Button(
            "EXIT",
            100,
            500,
            buttonsize[0],
            buttonsize[1],
            image_id = "button",
            action = self.startmenu
        )
        self.register_button(button)

    def update(self, event: str, mouselocation: list[int, int]) -> None:
        super().update(event, mouselocation)
        textfield: Textfield = self.get_component("inputcontrol")
        textfield.text = self.last_event

    def startmenu(self) -> None:
        self.next_scene = Start()