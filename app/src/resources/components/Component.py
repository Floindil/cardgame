import pygame

class Component:
    """
    The Component class is used as a base for every
    object that might be displayed on the screen.
    """
    RENDER: bool
    RENDERPRIORITY: int
    _image: pygame.Surface
    __rect: pygame.Rect
    __image_name: str
    __update: bool

    def __init__(self, x: int, y: int, width: int = 1, height: int = 1) -> None:
        """
        Initializes a Component with the given dimensions and position.

        Args:
            width (int): The width of the component.
            height (int): The height of the component.
            x (int): The x-coordinate of the component's position.
            y (int): The y-coordinate of the component's position.
        """
        self.RENDER = True
        self.RENDERPRIORITY = 0
        self.__rect = pygame.Rect(x, y, width, height)
        self.__image_name = ""
        self._image = pygame.Surface((1,1))
        self.__update = False

    @property
    def update(self) -> bool:
        """The update flag indicates, that the Component has been changed."""
        return self.__update
    
    def _set_update(self) -> None:
        """Sets the update variable to True"""
        self.__update = True
    
    def resetUpdate(self) -> None:
        """Sets the update variable to False"""
        self.__update = False

    @property
    def image_name(self) -> str:
        """Returns the name of the image associated with this component."""
        return self.__image_name

    @image_name.setter
    def image_name(self, name: str) -> None:
        """Sets the name of the image associated with this component."""
        self.__image_name = name

    @property
    def image(self) -> pygame.Surface:
        """Returns the image of the associated Textfield object."""
        return self._image

    @property
    def location(self) -> pygame.Vector2:
        """Returns the top-left position of the component."""
        return pygame.Vector2(self.__rect.topleft)

    @property
    def size(self) -> tuple[int, int]:
        return (self.__rect.width, self.__rect.height)
    
    @property
    def center(self) -> tuple[int, int]:
        return (self.__rect.centerx, self.__rect.centery)

    @size.setter
    def size(self, width: int, height: int) -> None:
        """
        Sets the size of the component.

        Args:
            width (int): The new width of the component.
            height (int): The new height of the component.
        """
        self.__rect.size = (width, height)

    def get_top_left(self) -> pygame.Vector2:
        """
        Gets the top-left position of the component as a pygame.Vector2.

        Returns:
            pygame.Vector2: The top-left position of the component.
        """
        return pygame.Vector2(self.__rect.topleft)
