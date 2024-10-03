import pygame

class Eventhandler:
    """
    Handles events for the game.
    """

    __pressed_buttons: list
    __mouse_location: tuple[int, int]

    def __init__(self) -> None:
        """
        Initializes the Eventhandler.
        """
        self.__pressed_buttons = []
        self.__mouse_location = (0,0)

    @property
    def mouse_location(self) -> tuple[int, int]:
        return self.__mouse_location

    @property
    def pressed_buttons(self) -> list:
        return self.__pressed_buttons

    def run(self, events: list[pygame.event.Event]) -> bool:
        """
        Processes a list of events.

        Args:
            events (list[pygame.event.Event]): A list of pygame events.

        Returns:
            bool: False if a QUIT event is detected, True otherwise.
        """
        running = True
        typed_string = ""

        self.__mouse_location = pygame.mouse.get_pos()

        for event in events:

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.__pressed_buttons = pygame.mouse.get_pressed()

            if event.type == pygame.MOUSEBUTTONUP:
                self.__pressed_buttons = pygame.mouse.get_pressed()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    typed_string += "//<"
                elif event.key == pygame.K_DELETE:
                    typed_string += "//>"
                elif event.key == pygame.K_RETURN:
                    typed_string += "//!"
                elif event.key == pygame.K_ESCAPE:
                    typed_string += "//?"
                else:
                    typed_string += event.unicode

        return running, typed_string