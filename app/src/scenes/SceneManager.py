from src.scenes.Scene import Scene

class SceneManager:
    """
    The SceneManager provides functionalities to change Scenes.
    """

    activeScene: Scene
    previousScene: Scene
    menuScene: Scene
    newScene: Scene
    menu: bool

    def __init__(self, startScene: Scene) -> None:
        """
        Creates a SceneManager Object and sets the starting Scene.
        """
        self.activeScene = startScene
        self.previousScene = None
        self.newScene = None
        self.menu = False

    def setNewScene(self, scene: Scene) -> None:
        """
        Takes a Scene to set as the new Scene. If there is a  new Scene,
        the Scene will be changed in the next update of the SceneManager.
        """
        self.newScene = scene

    def startMenu(self) -> None:
        """
        Stores the active Scene in the previous Scene variable
        and sets the menu Scene as the active Scene.
        Once the menu is left, the previous scene will be set
        as active again.
        """
        self.previousScene = self.activeScene
        self.activeScene = self.menuScene

    def endMenu(self) -> None:
        """
        Sets the previous Scene (active Scene when the menu was started)
        to the active Scene and set the previousScene
        variable to None to indicate, that the menu is closed.
        """
        self.activeScene = self.previousScene
        self.previousScene = None

    def update(self) -> None:
        """
        If the new Scene flag is active, the next Scene will be set
        to the active Scene and then, together with the new Scene flag,
        be cleared.
        Checks, if the menu should be started or ended.
        """
        if self.newScene:
            self.activeScene = self.newScene
            self.newScene = None

        if self.menu and not self.previousScene:
            self.startMenu()

        elif not self.menu and self.previousScene:
            self.endMenu()