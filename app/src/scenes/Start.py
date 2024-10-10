from src.scenes.Scene import Scene
from src.scenes.Cardgame import Cardgame
from src.resources.components.Button import Button
from src.resources.components.Textfield import Textfield

class Start(Scene):

    def __init__(self) -> None:
        super().__init__()

        self._menuacces = False
        
        textfield = Textfield("START MENU", 100, 100, color = "white", fontsize = 40)
        self.register_textfield(textfield)
        
        self.load_asset("button.png")
        buttonsize = self.get_image_size("button")

        button = Button(
            "START",
            100,
            300,
            buttonsize[0],
            buttonsize[1],
            image_id = "button",
            action = self.start_cardgame
        )
        self.register_button(button)

    def start_cardgame(self):
        self.next_scene = Cardgame()