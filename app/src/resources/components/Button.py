from src.resources.components.Component import Component
from src.resources.components.Textfield import Textfield
from src.core.Configuration import Fonts, TAG

class Button(Component):
    """
    Extends the Component class to create a Button with an action.\n
    The button has a flag, that can be set on the mousedown event 
    to control, that the mouse still points at the Button when the
    mouseup event occurs.
    """

    __textfield: Textfield
    __action: callable
    __flag: bool

    def __init__(
            self,
            id: str,
            x: int,
            y: int,
            width: int,
            height: int,
            action: callable = None,
            text_color: str = Fonts.BUTTONCOLOR,
            text: str = None,
            image_id: str = None
        ) -> None:
        """
        Initializes the attributes of the Button Object.

        Args:
            id (str): ID for the component, used to identify the 
            component and associated assets.
            x (int): The x-coordinate of the component's position.
            y (int): The y-coordinate of the component's position.
            width (int): The width of the component.
            height (int): The height of the component.
            action (callable): Action that will be called, when the 
            Button is pressed.
            text (str): Text displayed on the Button. If no text is
            provided, the Button ID will be used as text.
            image_id (str): ID of the associated image. If no ID is
            provided, the Button ID will be used as image ID.
        """
        super().__init__(id, x, y, width, height)
        if not text:
            text = self.ID
        self.__textfield = Textfield(f"{id}_tf", 0, 0, text = text, color = text_color)
        self.__textfield.render_priority = self.render_priority + 1
        self.__textfield.location = self.__location_tf

        if image_id:
            self.image_id = image_id
        else:
            self.image_id = self.ID

        if action:
            self.__action = action
        else:
            self.__action = self.__default_action

        self.__flag = False
        self._tag = TAG.BUTTONS

    @property
    def __location_tf(self) -> tuple[int, int]:
        """Returns the current location of the Textfield associated with the Button."""
        x = self.location.x + (self.size[0] - self.__textfield.size[0])/2
        y = self.location.y + (self.size[1] - self.__textfield.size[1])/2
        return (x, y)
    
    @property
    def textfield(self) -> Textfield:
        return self.__textfield

    @property
    def flag(self) -> tuple[bool, bool]:
        """Returns the flag boolean."""
        return self.__flag
    
    @flag.setter
    def flag(self, bool: bool):
        """Sets the flag boolean."""
        self.__flag = bool
    
    def action(self) -> None:
        """Calls the action set in the action attribute."""
        self.__action()

    def __default_action(self) -> None:
        print(f"pressed Button {self.ID}")