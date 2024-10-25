import pygame

from src.resources.components.Component import Component
from src.core.Configuration import Fonts, TAG

class Textfield(Component):
    """
    This class provides functionalities to create and manage Textfields.
    """
    __text: str
    __font: pygame.font.Font
    __color: pygame.Color

    def __init__(
            self,
            id: str,
            x: int,
            y: int,
            text: str = None,
            font: str = Fonts.STANDARDFONT,
            fontsize: int = Fonts.STANDARDSIZE,
            color: str = Fonts.STANDARDCOLOR
        ) -> None:
        """
        Creates a Textfield object. This object can display any text.

        Args:
            id (str): Identifier for the Textfield.
            x (int): x coordinate of the top left corner
            y (int): y coordinate of the top left corner
            text (str): text that will be displayed, if no text is provided, 
            the Textfield ID will be used.
            font (str): if no font is provided, the standardfont from
            the configuration will be used
            size (int): size of the letters - if no size is provided, 
            the standardsize from the configuration will be used
            color (str): if no colot is provided, black will be used
        """
        super().__init__(id, x, y)
        if not text:
            text = id
        self.__text = text
        self.__color = pygame.Color(color)
        self.__fontsize = fontsize
        self.font = font
        self._tag = TAG.TEXTFIELDS

    @property
    def text(self) -> str:
        """Returns the text of the associated Textfield object."""
        return self.__text
    
    @text.setter
    def text(self, text: str) -> None:
        """
        Checks, if the provided text is of type str and sets it to
        the text attribute.\n
        Recreates the objects image with the new text.

        Args:
            text (str): new text to be displayed
        """
        if not isinstance(text, str):
            raise TypeError("> variable must be str type!")
        self.__text = text
        self.__create_image()

    @property
    def font(self) -> pygame.font.Font:
        """Returns the font of the associated Textfield object."""
        return self.__font

    @font.setter
    def font(self, font: str) -> None:
        """
        Checks, if the provided font is of type str and sets it to
        the text attribute.\n
        Recreates the objects image with the new text.

        Args:
            text (str): new text to be displayed
        """
        try:
            self.__font = pygame.font.SysFont(font, self.fontsize)
        except ValueError as e:
            print(e)
        self.__create_image()

    @property
    def fontsize(self) -> int:
        """Returns the letter size associated with the Textfield object."""
        return self.__fontsize
    
    @fontsize.setter
    def fontsize(self, size: int) -> None:
        """
        Checks, if the provided size is of type int and sets it to
        the size attribute.\n
        Recreates the objects image with the new size.

        Args:
            size (int): new size for the letters to be displayed with
        """
        if not isinstance(size, int):
            raise TypeError("> Variable must be int!")
        self.__fontsize = size
        self.__font = pygame.font.SysFont(self.__font, size)
        self.__create_image()

    @property
    def color(self) -> pygame.Color:

        return self.__color
    
    @color.setter
    def color(self, color: str) -> None:
        """
        Checks, if the provided color is a valid value for pygame.Color()
        and stores the new Color in the color attribute.\n
        Recreates the objects image with the new Color.

        Args:
            color (str): new color to displayed the text with
        """
        try:
            self.__color = pygame.Color(color)
        except ValueError as e:
            print(e)
        self.__create_image()
    
    def __create_image(self) -> None:
        """
        Uses the font to create an image of the string stored in the text
        attribute.\n
        The color attribute of the Textfield object will be used for the 
        color parameter. 
        """
        self._image = self.__font.render(self.__text, True, self.__color)
        image_size = self._image.get_size()
        self.size = image_size[0], image_size[1]
        self._set_update()
