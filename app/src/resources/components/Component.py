import pygame

class Component:
    """
    The Component class is used as a base for every
    object that might be displayed on the screen.
    """

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
        self._rect = pygame.Rect(x, y, width, height)
        self._image_name = ""

    @property
    def image_name(self) -> str:
        """Returns the name of the image associated with this component."""
        return self._image_name

    @image_name.setter
    def image_name(self, name: str) -> None:
        """Sets the name of the image associated with this component."""
        self._image_name = name

    @property
    def location(self) -> pygame.Vector2:
        """Returns the top-left position of the component."""
        return pygame.Vector2(self._rect.topleft)

    @property
    def size(self) -> tuple[int, int]:
        return (self._rect.width, self._rect.height)
    
    @property
    def center(self) -> tuple[int, int]:
        return (self._rect.centerx, self._rect.centery)

    @size.setter
    def size(self, width: int, height: int) -> None:
        """
        Sets the size of the component.

        Args:
            width (int): The new width of the component.
            height (int): The new height of the component.
        """
        self._rect.size = (width, height)

    def get_top_left(self) -> pygame.Vector2:
        """
        Gets the top-left position of the component as a pygame.Vector2.

        Returns:
            pygame.Vector2: The top-left position of the component.
        """
        return pygame.Vector2(self._rect.topleft)
