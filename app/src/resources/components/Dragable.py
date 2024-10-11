from src.resources.components.Component import Component

class Dragable(Component):

    __drag: bool                # indicates, if the object is currently beeing dragged
    __static: bool              # indicates, if the object can be dragged
    __ancor: tuple[int, int]    # location to which the object returnes, when dropped

    def __init__(self, id: str, x: int, y: int, width: int = 1, height: int = 1) -> None:
        super().__init__(id, x, y, width, height)
        self._tag = "dragable"
        self.__drag = False
        self.__static = False

    def flip_drag(self) -> None:
        if not self.__static:
            if self.__drag:
                self.__drag = False
            else:
                self.__drag = True