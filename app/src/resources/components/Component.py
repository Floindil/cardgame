import pygame

class Component:
    """
    The Component class serves as a base for any object that can be displayed on the screen.
    It includes properties and methods for managing the object's position, size, and rendering attributes.
    """

    def __init__(self, id: str, x: int, y: int, width: int = 1, height: int = 1) -> None:
        """
        Initializes a Component with the given dimensions and position.

        Args:
            id (str): ID for the component, used to identify the component and associated assets.
            x (int): The x-coordinate of the component's position.
            y (int): The y-coordinate of the component's position.
            width (int, optional): The width of the component. Defaults to 1.
            height (int, optional): The height of the component. Defaults to 1.
        """
        self.RENDER = True
        self.RENDERPRIORITY = 0
        self.__rect = pygame.Rect(x, y, width, height)
        self.__id = id
        self.__image_id = id
        self.__update = False
        self._image = pygame.Surface((1, 1))
        self._tag = ""

    @property
    def image_id(self) -> str:
        """Returns the image ID associated with the component."""
        return self.__image_id

    @image_id.setter
    def image_id(self, id: str) -> None:
        """Sets the image ID for the component."""
        self.__image_id = id

    @property
    def update(self) -> bool:
        """Indicates whether the component has been changed."""
        return self.__update

    @property
    def TAG(self) -> str:
        """Returns the tag of the component."""
        return self._tag

    def _set_update(self) -> None:
        """Sets the update flag to True."""
        self.__update = True

    def reset_update(self) -> None:
        """Sets the update flag to False."""
        self.__update = False

    @property
    def ID(self) -> str:
        """Returns the ID of the component."""
        return self.__id

    @ID.setter
    def ID(self, name: str) -> None:
        """Sets the ID of the component."""
        self.__id = name

    @property
    def image(self) -> pygame.Surface:
        """Returns the image of the component."""
        return self._image

    @property
    def location(self) -> pygame.Vector2:
        """Returns the top-left position of the component."""
        return pygame.Vector2(self.__rect.topleft)

    @location.setter
    def location(self, location: tuple[int, int]) -> None:
        """Sets a new top-left position for the component."""
        self.__rect.topleft = location

    @property
    def size(self) -> tuple[int, int]:
        """Returns the width and height of the component."""
        return self.__rect.size

    @size.setter
    def size(self, size: tuple[int, int]) -> None:
        """Sets the size of the component.

        Args:
            size (tuple[int, int]): The new size of the component (width, height).
        """
        self.__rect.size = size

    @property
    def center(self) -> tuple[int, int]:
        """Returns the center coordinates of the component."""
        return self.__rect.center

    def collide_point(self, x: int, y: int) -> bool:
        """Checks if a point collides with the component's rectangle.

        Args:
            x (int): The x-coordinate of the point.
            y (int): The y-coordinate of the point.

        Returns:
            bool: True if the point collides with the component's rectangle, False otherwise.
        """
        return self.__rect.collidepoint(x, y)

    def get_top_left(self) -> pygame.Vector2:
        """Gets the top-left position of the component as a pygame.Vector2.

        Returns:
            pygame.Vector2: The top-left position of the component.
        """
        return pygame.Vector2(self.__rect.topleft)
