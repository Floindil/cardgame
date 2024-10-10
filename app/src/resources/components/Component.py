import pygame

class Component:
    """
    The Component class is used as a base for every
    object that might be displayed on the screen.
    """
    RENDER: bool
    RENDERPRIORITY: int
    _tag: str
    _image: pygame.Surface
    __rect: pygame.Rect
    __id: str
    __update: bool

    def __init__(self,id: str, x: int, y: int, width: int = 1, height: int = 1) -> None:
        """
        Initializes a Component with the given dimensions and position.

        Args:
            id (str): ID for the component, used to identify the 
            component and associated assets.
            x (int): The x-coordinate of the component's position.
            y (int): The y-coordinate of the component's position.
            width (int): The width of the component.
            height (int): The height of the component.
        """
        self.RENDER = True
        self.RENDERPRIORITY = 0
        self.__rect = pygame.Rect(x, y, width, height)
        self.__id = id
        self.__image_id = id
        self.__update = False
        self._image = pygame.Surface((1,1))
        self._tag = ""

    @property
    def image_id(self) -> str:
        return self.__image_id
    
    @image_id.setter
    def image_id(self, id: str):
        self.__image_id = id

    @property
    def update(self) -> bool:
        """The update flag indicates, that the Component has been changed."""
        return self.__update
    
    @property
    def TAG(self) -> str:
        """Returns the TAG of the component"""
        return self._tag
    
    def _set_update(self) -> None:
        """Sets the update variable to True"""
        self.__update = True
    
    def resetUpdate(self) -> None:
        """Sets the update variable to False"""
        self.__update = False

    @property
    def ID(self) -> str:
        """Returns the ID of the the component."""
        return self.__id

    @ID.setter
    def ID(self, name: str) -> None:
        """Sets the name of the ID of the component."""
        self.__id = name

    @property
    def image(self) -> pygame.Surface:
        """Returns the image of the associated Textfield object."""
        return self._image

    @property
    def location(self) -> pygame.Vector2:
        """Returns the top-left position of the component."""
        return pygame.Vector2(self.__rect.topleft)
    
    @location.setter
    def location(self, location: tuple[int, int]):
        """Sets a new x and y for the Components top-left location"""
        self.__rect.topleft = (location)

    @property
    def size(self) -> tuple[int, int]:
        return (self.__rect.width, self.__rect.height)
    
    @property
    def center(self) -> tuple[int, int]:
        return (self.__rect.centerx, self.__rect.centery)
    
    def collide_point(self, x: int, y: int) -> bool:
        if self.__rect.collidepoint(x, y):
            return True
        else:
            return False

    @size.setter
    def size(self, size: tuple[int, int]) -> None:
        """
        Sets the size of the component.

        Args:
            width (int): The new width of the component.
            height (int): The new height of the component.
        """
        self.__rect.size = size

    def get_top_left(self) -> pygame.Vector2:
        """
        Gets the top-left position of the component as a pygame.Vector2.

        Returns:
            pygame.Vector2: The top-left position of the component.
        """
        return pygame.Vector2(self.__rect.topleft)
