import pygame

from src.resources.components.Textfield import Textfield
from src.scenes.Scene import Scene

class Menu(Scene):

    def __init__(self) -> None:
        super().__init__()

        textfield = Textfield("Main Menu", 100, 100, color = "white")
        textfield.image_name = "text1"
        self.register_image("text1", textfield.image)
        self.add_component(textfield)
        
        