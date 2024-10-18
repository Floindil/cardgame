import pygame
from src.core.Configuration import Configuration as C

class Component:
    """
    The Component class serves as a base for any object that can be displayed on the screen.
    It includes properties and methods for managing the object's position, size, and rendering attributes.
    """
    __highlight: 'Component'
    __rect: pygame.Rect
    __id: str
    __image_id: str
    __update: bool
    __active: bool
    __render: bool
    __render_priority: int
    _image: pygame.Surface
    _tag: str
    _remove: bool

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
        self.__highlight = None
        self.__render = True
        self.__render_priority = 0
        self.__rect = pygame.Rect(x, y, width, height)
        self.__id = id
        self.__image_id = id
        self.__update = False
        self.__active = True
        self._image = pygame.Surface((1, 1))
        self._tag = ""
        self._remove = False

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
    def render(self) -> bool:
        """Indicates whether the component should be rendered or not."""
        return self.__render
    
    @render.setter
    def render(self, render: bool) -> None:
        """Defines whether the component should be rendered or not."""
        self.__render = render
        
    @property
    def render_priority(self) -> int:
        """
        Indicates with which priority the component should be rendered.
        Components with priority 0 will be rendered first (bottom layer).
        """
        return self.__render_priority
    
    @render_priority.setter
    def render_priority(self, priority: int) -> None:
        """
        Sets the priority with which the component should be rendered.
        Components with priority 0 will be rendered first (bottom layer).
        """
        self.__render_priority = priority
    
    @property
    def active(self) -> bool:
        """Indicates whether the component is active or not."""
        return self.__active
    
    @active.setter
    def active(self, active: bool) -> None:
        """Sets the component to active or inactive."""
        self.__active = active

    @property
    def remove(self) -> bool:
        """Indicates whether the component should be removed from the program or not."""
        return self._remove

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
        """
        Sets the size of the component.

        Args:
            size (tuple[int, int]): The new size of the component (width, height).
        """
        self.__rect.size = size

    @property
    def rect(self) -> pygame.Rect:
        """Returns the Rect object of the component."""
        return self.__rect

    @property
    def center(self) -> tuple[int, int]:
        """Returns the center coordinates of the component."""
        return self.__rect.center

    def collide_point(self, x: int, y: int) -> bool:
        """
        Checks if a point collides with the component's rectangle.

        Args:
            x (int): The x-coordinate of the point.
            y (int): The y-coordinate of the point.

        Returns:
            bool: True if the point collides with the component's rectangle, False otherwise.
        """
        return self.__rect.collidepoint(x, y)

    def get_top_left(self) -> pygame.Vector2:
        """
        Gets the top-left position of the component as a pygame.Vector2.

        Returns:
            pygame.Vector2: The top-left position of the component.
        """
        return pygame.Vector2(self.__rect.topleft)

    @property
    def highlight(self) -> 'Component':
        """Returns the highlight component associated with this component."""
        return self.__highlight

    def set_highlight(self, state: bool) -> None:
        """Sets the rendering state of the highlight component."""
        self.__highlight.render = state
    
    @property
    def highlight_id(self) -> str:
        """Returns the ID for the highlight component."""
        if self.highlight:
            return self.highlight.ID
        else:
            return f"{self.ID}_highlight"
    
    def create_highlight(self, id: str, location: tuple[int, int], size: tuple[int, int]) -> None:
        """
        Creates a highlight component for the component.

        Args:
            id (str): id for the highlight component
            location (tuple[int, int]): location of the highlight
            size (tuple[int, int]): size of the highlight
        """
        highlight = Component(id, location[0], location[1], size[0], size[1])
        highlight.render = False
        highlight.render_priority = self.render_priority + 1
        
        self.__highlight = highlight

    def create_highlight_image(
            self,
            color: str = C.HIGHLIGHT_COLOR,
            border_width: int = C.HIGHLIGHT_BORDER_WIDTH
        ) -> pygame.Surface:
        """
        Creates a highlight and image for the component.

        Args:
            color (str): The color of the highlight border.
            border_width (int): The width of the highlight border.

        Returns:
            pygame.Surface: The surface representing the highlight.
        """
        location = (self.location.x - border_width, self.location.y - border_width)
        size = (self.size[0] + 2 * border_width, self.size[1] + 2 * border_width)
        
        self.create_highlight(self.highlight_id, location, size)

        image = pygame.Surface(size, pygame.SRCALPHA)
        rect = pygame.Rect(0, 0, size[0], size[1])
        pygame.draw.rect(image, color, rect, border_width, 10)

        return image
