from src.scenes.Scene import Scene
from src.scenes.Start import Start
from src.scenes.Menu import Menu
from src.resources.components.Component import Component

class SceneManager:
    """
    The SceneManager class handles the transitions between different Scenes
    in the game, including starting, stopping, and managing a menu Scene.
    """
    __active_scene: Scene
    __previous_scene: Scene
    __menu_scene: Scene
    __menu: bool

    def __init__(self) -> None:
        """
        Initializes the SceneManager with the starting Scene and menu Scene.
        Sets the initial active Scene to the starting Scene and initializes
        the previous Scene and menu flag.
        """
        self.__menu_scene = Menu()
        self.__active_scene = Start()
        self.__previous_scene = None
        self.__menu = False
        self.__active_scene.start()

    @property
    def stop(self) -> bool:
        """
        Returns a boolean indicating if the game should be ended based on
        the active Scene's stop flag.
        
        Returns:
            bool: True if the game should be stopped, False otherwise.
        """
        return self.__active_scene.stop

    def __start_menu(self) -> None:
        """
        Activates the menu Scene by storing the current active Scene in the
        previous Scene variable and setting the menu Scene as the active Scene.
        """
        self.__previous_scene = self.__active_scene
        self.__active_scene = self.__menu_scene

    def __end_menu(self) -> None:
        """
        Deactivates the menu Scene by restoring the previous Scene as the
        active Scene and setting the previous Scene variable to None.
        """
        self.__active_scene = self.__previous_scene
        self.__previous_scene = None

    def update(self, event: str, mouselocation: tuple[int, int]) -> None:
        """
        Updates the active Scene based on the provided event and mouse location.
        Handles the transition to and from the menu Scene if the menu access
        event is triggered. Switches to the next Scene if the new Scene flag
        is set in the active Scene.

        Args:
            event (str): The event to process.
            mouselocation (tuple[int, int]): The current mouse location.
        """
        if "//?" in event:
            if not isinstance(self.__active_scene, Start):
                if self.__menu:
                    self.__menu = False
                    self.__end_menu()
                elif self.__active_scene._menuacces:
                    self.__menu = True
                    self.__start_menu()
                self.__active_scene.start()

        new_scene = self.__active_scene.next_scene

        if new_scene:
            self.__active_scene.next_scene = None
            self.__active_scene = new_scene
            self.__active_scene.start()

        self.__active_scene.update(event, mouselocation)
    
    def get_rendering_context(self) -> list[Component]:
        """
        Retrieves the components to be rendered from the active Scene.

        Returns:
            list[Component]: A list of components to be rendered on the screen.
        """
        return self.__active_scene.get_rendering_context()
