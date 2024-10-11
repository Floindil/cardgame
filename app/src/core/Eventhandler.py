import pygame

class Eventhandler:
    """
    The Eventhandler class is responsible for handling and processing all game events.
    It captures mouse and keyboard inputs and updates the internal state accordingly.
    """

    __pressed_buttons: list

    def __init__(self) -> None:
        """
        Initializes the Eventhandler by setting up the list to track pressed buttons.
        """
        self.__pressed_buttons = []

    @property
    def pressed_buttons(self) -> list:
        """
        Gets the list of currently pressed mouse buttons.

        Returns:
            list: A list indicating the state of mouse buttons.
        """
        return self.__pressed_buttons

    def run(self, events: list[pygame.event.Event]) -> tuple[bool, str, tuple[int, int]]:
        """
        Processes a list of events, updates the pressed buttons, and constructs an event string.

        Args:
            events (list[pygame.event.Event]): A list of pygame events.

        Returns:
            tuple[bool, str, tuple[int, int]]: A tuple containing:
                - bool: False if a QUIT event is detected, True otherwise.
                - str: A string representing the sequence of events.
                - tuple[int, int]: The current mouse position.
        """
        running = True
        event_string = ""
        mouselocation = pygame.mouse.get_pos()

        for event in events:
            if event.type == pygame.QUIT:
                running = False
                event_string += "//q"

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    event_string += "//m1d" # Left mouse button
                elif event.button == 2:
                    event_string += "//m2d" # Middle mouse button
                elif event.button == 3:
                    event_string += "//m3d" # Right mouse button
                elif event.button == 4:
                    event_string += "//m4d" # Wheel up
                elif event.button == 5:
                    event_string += "//m5d" # Wheel down

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    event_string += "//m1u" # Left mouse button
                elif event.button == 2:
                    event_string += "//m2u" # Middle mouse button
                elif event.button == 3:
                    event_string += "//m3u" # Right mouse button
                # The wheel up events trigger simultaniously with the wheel 
                # down events and therefore don't need extra tracking.

            elif event.type == pygame.KEYDOWN:
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

        return running, event_string, mouselocation
