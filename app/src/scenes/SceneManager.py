from src.scenes.Scene import Scene
from src.scenes.Menu import Menu
from src.resources.components.Component import Component

class SceneManager:
    """
    The SceneManager provides functionalities to change Scenes.
    """
    __active_scene: Scene
    __previous_scene: Scene
    __menu_scene: Scene
    __new_scene: Scene
    __menu: bool

    @property
    def stop(self) -> bool:
        """Returns True, if the Game should be ended from the Scene"""
        return self.__active_scene.stop

    def __init__(self) -> None:
        """
        Creates a SceneManager Object and sets the starting Scene.
        """
        self.__menu_scene = Menu()
        self.__active_scene = self.__menu_scene
        self.__previous_scene = None
        self.__new_scene = None
        self.__menu = False

    def set__new_scene(self, scene: Scene) -> None:
        """
        Takes a Scene to set as the new Scene. If there is a  new Scene,
        the Scene will be changed in the next update of the SceneManager.

        Args:
            scene (Scene): New Scene to be displayed
        """
        self.__new_scene = scene

    def start__menu(self) -> None:
        """
        Stores the active Scene in the previous Scene variable
        and sets the menu Scene as the active Scene.
        Once the menu is left, the previous scene will be set
        as active again.
        """
        self.__previous_scene = self.__active_scene
        self.__active_scene = self.__menu_scene

    def end__menu(self) -> None:
        """
        Sets the previous Scene (active Scene when the menu was started)
        to the active Scene and set the __previous_scene
        variable to None to indicate, that the menu is closed.
        """
        self.__active_scene = self.__previous_scene
        self.__previous_scene = None

    def update(self) -> None:
        """
        If the new Scene flag is active, the next Scene will be set
        to the active Scene and then, together with the new Scene flag,
        be cleared.
        Checks, if the menu should be started or ended.
        """
        if self.__new_scene:
            self.__active_scene = self.__new_scene
            self.__new_scene = None

        if self.__menu and not self.__previous_scene:
            self.start__menu()

        elif not self.__menu and self.__previous_scene:
            self.end__menu()

        self.__active_scene.update()
    
    def get_rendering_context(self) -> list[Component]:
        """
        Gets all the components, that should be rendered, 
        from the active Scene.

        Returns:
            Components to be rendered to the screen
        """
        return self.__active_scene.get_rendering_context()