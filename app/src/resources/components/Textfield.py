import pygame

from src.resources.components.Component import Component
from src.core.Configuration import Fonts

class Textfield(Component):
    """
    This class provides functionalities to create and manage Textfields.
    """

    __text: str
    __image: pygame.Surface
    __font: pygame.font.Font
    __color: pygame.Color
    __size: int

    def __init__(
            self,
            text: str,
            x: int,
            y: int,
            font: str = Fonts.STANDARDFONT,
            size: int = Fonts.STANDARDSIZE,
            color: str = 'black'
        ) -> None:
        super().__init__(x, y)
        self.__text = text
        self.__font = pygame.font.SysFont(font, size)
        self.__size = size
        try:
            self.__color = pygame.Color(color)
        except ValueError as e:
            print(e)
        self.__create_image()

    @property
    def text(self) -> str:
        return self.__text
    
    @text.setter
    def text(self, text: str) -> None:
        if not isinstance(text, str):
            raise TypeError("> variable must be str type!")
        self.__text = text
        self.__create_image()

    @property
    def image(self) -> pygame.Surface:
        return self.__image

    @property
    def font(self) -> pygame.font.Font:
        return self.__font

    @font.setter
    def font(self, font: str) -> None:
        if not Fonts.font_exists(font):
            raise TypeError("> Variable must be from Fonts dataclass!")
        self.__font = pygame.font.SysFont(font, self.__size)
        self.__create_image()

    @property
    def size(self) -> int:
        return self.__size
    
    @size.setter
    def size(self, size: int) -> None:
        if not isinstance(size, int):
            raise TypeError("> Variable must be int!")
        self.__size = size
        self.__font = pygame.font.SysFont(self.__font, size)
        self.__create_image()

    @property
    def color(self) -> pygame.Color:
        return self.__color
    
    @color.setter
    def color(self, color: str) -> None:
        try:
            self.__color = pygame.Color(color)
        except ValueError as e:
            print(e)
        self.__create_image()
    
    def __create_image(self) -> None:
        self.__image = self.__font.render(self.__text, True, self.__color)
