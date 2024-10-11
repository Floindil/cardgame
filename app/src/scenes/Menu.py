from src.resources.components.Textfield import Textfield
from src.resources.components.Button import Button
from src.scenes.Start import Start
from src.scenes.Scene import Scene

class Menu(Scene):
    """
    Menu class extends the Scene class and represents the main menu of the game.
    It handles the initialization and updating of various components like text 
    fields and buttons.
    """

    def __init__(self) -> None:
        """
        Initializes the Menu class. Calls the initializer of the parent Scene class 
        and sets the menu access flag.
        """
        super().__init__()
        self._menuacces = False

    def start(self) -> None:
        """
        Starts the menu by setting up initial components such as text fields and 
        buttons. Loads assets and registers components for the menu.
        """
        # Create and register a title text field for the main menu
        textfield = Textfield("MAIN MENU", 100, 100, fontsize=40)
        self.register_textfield(textfield)

        # Create and register an input control text field
        textfield = Textfield("inputcontrol", 100, 150)
        self.register_textfield(textfield)

        # Load and register the exit button component
        self.load_asset(self.assets.BUTTON)
        buttonsize = self.get_image_size(self.assets.BUTTON.ID)

        button = Button(
            "EXIT",
            100,
            500,
            buttonsize[0],
            buttonsize[1],
            image_id="button",
            action=self.startmenu
        )
        self.register_button(button)

    def update(self, event: str, mouselocation: list[int, int]) -> None:
        """
        Updates the menu state based on events and mouse location.
        
        Args:
            event (str): The latest event to process.
            mouselocation (list[int, int]): The current mouse location.
        """
        super().update(event, mouselocation)

        # Update the text of the input control text field with the last event
        textfield: Textfield = self.get_component("inputcontrol")
        textfield.text = self.last_event

    def startmenu(self) -> None:
        """
        Transitions to the start scene when the exit button is pressed.
        """
        self.next_scene = Start()
