import pygame

from src.resources.components.Component import Component
from src.core.Configuration import Fonts, TAG

class Textfield(Component):
    """
    This class provides functionalities to create and manage Textfields.
    """
    __textlines: list[str]
    __font: pygame.font.Font
    __color: pygame.Color
    __bgcolor: pygame.Color

    def __init__(
            self,
            id: str,
            x: int,
            y: int,
            textlines: list[str] = None,
            font: str = Fonts.STANDARDFONT,
            fontsize: int = Fonts.STANDARDSIZE,
            fontcolor: str = Fonts.STANDARDCOLOR,
            bgcolor: str = None
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
        self.__bgcolor = None
        if bgcolor:
            self.__bgcolor = pygame.Color(bgcolor)
        if not textlines:
            self.__textlines = [id]
        else:
            self.__textlines = textlines
        self.__color = pygame.Color(fontcolor)
        self.__fontsize = fontsize
        self.font = font
        self._tag = TAG.TEXTFIELDS
            

    @property
    def textlines(self) -> str:
        """Returns the text of the associated Textfield object."""
        return self.__textlines
    
    @textlines.setter
    def textlines(self, textlines: list[str]) -> None:
        """
        Checks, if the provided text is of type str and sets it to
        the text attribute.\n
        Recreates the objects image with the new text.

        Args:
            textlines (list[str]): new text to be displayed
        """
        for line in textlines:
            if not isinstance(line, str):
                raise TypeError("> variable must be str type!")
        self.__textlines = textlines
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
        parts = []
        width = 0
        height = 0

        for i, line in enumerate(self.__textlines):
            image = self.__font.render(line, True, self.__color, self.__bgcolor)
            parts.append((image, height))

            size = image.get_size()

            if size[0] > width:
                width = size[0]

            height += size[1]
            if i+1 < len(self.textlines):
                height += Fonts.LINEBUFFER

        self.size = width, height
        self._image = pygame.Surface(self.size, pygame.SRCALPHA)
        if self.__bgcolor:
            self._image.fill(self.__bgcolor)
        for part in parts:
            self.image.blit(part[0], (0, part[1]))
        self._set_update()
