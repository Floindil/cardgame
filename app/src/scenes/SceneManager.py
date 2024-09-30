from src.scenes.Scene import Scene
from src.scenes.Menu import Menu
from src.resources.components.Component import Component

class SceneManager:
    """
    The SceneManager provides functionalities to change Scenes.
    """
    _active_scene: Scene
    _previous_scene: Scene
    _menu_scene: Scene
    _new_scene: Scene
    _menu: bool

    def __init__(self) -> None:
        """
        Creates a SceneManager Object and sets the starting Scene.
        """
        self._menu_scene = Menu()
        self._active_scene = self._menu_scene
        self._previous_scene = None
        self._new_scene = None
        self._menu = False

    def set_new_scene(self, scene: Scene) -> None:
        """
        Takes a Scene to set as the new Scene. If there is a  new Scene,
        the Scene will be changed in the next update of the SceneManager.

        Args:
            scene (Scene): New Scene to be displayed
        """
        self._new_scene = scene

    def start_menu(self) -> None:
        """
        Stores the active Scene in the previous Scene variable
        and sets the menu Scene as the active Scene.
        Once the menu is left, the previous scene will be set
        as active again.
        """
        self._previous_scene = self._active_scene
        self._active_scene = self._menu_scene

    def end_menu(self) -> None:
        """
        Sets the previous Scene (active Scene when the menu was started)
        to the active Scene and set the _previous_scene
        variable to None to indicate, that the menu is closed.
        """
        self._active_scene = self._previous_scene
        self._previous_scene = None

    def update(self) -> None:
        """
        If the new Scene flag is active, the next Scene will be set
        to the active Scene and then, together with the new Scene flag,
        be cleared.
        Checks, if the menu should be started or ended.
        """
        if self._new_scene:
            self._active_scene = self._new_scene
            self._new_scene = None

        if self._menu and not self._previous_scene:
            self.start_menu()

        elif not self._menu and self._previous_scene:
            self.end_menu()
    
    def get_rendering_context(self) -> list[Component]:
        """
        Gets all the components, that should be rendered, 
        from the active Scene.

        Returns:
            Components to be rendered to the screen
        """
        return self._active_scene.get_rendering_context()