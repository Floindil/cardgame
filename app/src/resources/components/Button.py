from src.resources.components.Component import Component
from src.resources.components.Textfield import Textfield

class Button(Component):
    """
    
    """

    __textfield: Textfield

    def __init__(self, id: str, x: int, y: int, text: str, width: int = 1, height: int = 1, action = None) -> None:
        super().__init__(id, x, y, width, height)
        self.__textfield = Textfield(f"{id}_tf", text, 0, 0)
        self.__textfield.location = self.__location_tf
        self.__action = action
        self.__flag = False

    @property
    def __location_tf(self) -> tuple[int, int]:
        x = self.location.x + (self.size[0] - self.__textfield.size[0])/2
        y = self.location.y + (self.size[1] - self.__textfield.size[1])/2
        return (x, y)
    
    @property
    def flag(self) -> tuple[bool, bool]:
        return self.__flag
    
    @flag.setter
    def flag(self, bool: bool):
        self.__flag = bool
    
    def action(self) -> None:
        self.__action()