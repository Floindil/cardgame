from src.scenes.Scene import Scene
from src.scenes.Cardgame import Cardgame
from src.resources.components.Button import Button
from src.resources.components.Textfield import Textfield

class Start(Scene):
    """
    The Start class represents the initial scene of the game, typically used
    as the main menu where the player can start the game or exit.
    """

    def __init__(self) -> None:
        """
        Initializes the Start scene by calling the parent Scene's initializer
        and setting the menu access flag to False.
        """
        super().__init__()
        self._menuacces = False

    def start(self) -> None:
        """
        Sets up the Start scene by creating and registering a title textfield
        and two buttons: one to start the card game and one to exit the game.
        """
        # Create and register a title textfield
        textfield = Textfield("START MENU", 100, 100, fontsize=40)
        self.register_textfield(textfield)

        # Create and register an input control text field
        textfield = Textfield("inputcontrol", 100, 150)
        self.register_textfield(textfield)
        
        # Load the button asset and get its size
        self.load_asset(self.assets.BUTTON)
        buttonsize = self.get_image_size(self.assets.BUTTON.ID)

        # Create and register the start button
        start_button = Button(
            "START",
            100,
            300,
            buttonsize[0],
            buttonsize[1],
            image_id="button",
            action=self.start_cardgame
        )
        self.register_button(start_button)

        # Create and register the exit button
        exit_button = Button(
            "EXIT",
            100,
            400,
            buttonsize[0],
            buttonsize[1],
            image_id="button",
            action=self.end
        )
        self.register_button(exit_button)

    def start_cardgame(self) -> None:
        """
        Sets the next scene to be the Cardgame scene, initiating the transition
        from the Start menu to the card game.
        """
        self.next_scene = Cardgame()

    def update(self, event: str, mouselocation: list[int, int]) -> None:
        """
        Updates the game state based on events and mouse location.
        
        Args:
            event (str): The latest event to process.
            mouselocation (list[int, int]): The current mouse location.
        """
        super().update(event, mouselocation)

        # Update the text of the input control text field with the last event
        textfield: Textfield = self.get_component("inputcontrol")
        textfield.text = self.last_event
