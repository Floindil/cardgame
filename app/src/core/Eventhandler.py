import pygame

class Eventhandler:
    """
    Handles events for the game.
    """

    __pressed_keys: list

    def __init__(self) -> None:
        """
        Initializes the Eventhandler.
        """
        self.__pressed_keys = []
        # Any initialization for Eventhandler would go here
        pass

    @property
    def pressed_keys(self) -> list:
        return self.__pressed_keys

    def run(self, events: list[pygame.event.Event]) -> bool:
        """
        Processes a list of events.

        Args:
            events (list[pygame.event.Event]): A list of pygame events.

        Returns:
            bool: False if a QUIT event is detected, True otherwise.
        """
        running = True
        for event in events:
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                key_name = f"MB{event.button}"
                self.__pressed_keys.append(key_name)

            if event.type == pygame.MOUSEBUTTONUP:
                key_name = f"MB{event.button}"
                self.__pressed_keys.remove(key_name)

            if event.type == pygame.KEYDOWN:
                key_name = pygame.key.name(event.key)
                self.__pressed_keys.append(key_name)

            if event.type == pygame.KEYUP:
                key_name = pygame.key.name(event.key)
                self.__pressed_keys.remove(key_name)

        return running

