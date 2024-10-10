import pygame

class Eventhandler:
    """
    Handles events for the game.
    """

    __pressed_buttons: list

    def __init__(self) -> None:
        """
        Initializes the Eventhandler.
        """
        self.__pressed_buttons = []

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
        event_string = ""

        mouselocation = pygame.mouse.get_pos()

        for event in events:

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.__pressed_buttons = pygame.mouse.get_pressed()
                event_string += "//d"

            if event.type == pygame.MOUSEBUTTONUP:
                self.__pressed_buttons = pygame.mouse.get_pressed()
                event_string += "//u"

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    event_string += "//<"
                elif event.key == pygame.K_DELETE:
                    event_string += "//>"
                elif event.key == pygame.K_RETURN:
                    event_string += "//!"
                elif event.key == pygame.K_ESCAPE:
                    event_string += "//?"
                else:
                    event_string += event.unicode

        return (running, event_string, mouselocation)