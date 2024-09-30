import pygame

class Eventhandler:
    """
    Handles events for the game.
    """

    def __init__(self) -> None:
        """
        Initializes the Eventhandler.
        """
        # Any initialization for Eventhandler would go here
        pass

    def run(self, events: list[pygame.event.Event]) -> bool:
        """
        Processes a list of events.

        Args:
            events (list[pygame.event.Event]): A list of pygame events.

        Returns:
            bool: False if a QUIT event is detected, True otherwise.
        """
        for event in events:
            if event.type == pygame.QUIT:
                return False
        return True
