from scenes.Scene import Scene

class SceneManager:

    _active_scene: Scene
    _previous_scene: Scene
    _main_menu: Scene

    def __init__(self) -> None:
        pass

    def startNewScene(self, scene: Scene) -> None:
        self._previous_scene = self._active_scene
        self._active_scene = scene

        self._active_scene.start()

    def startPreviousScene(self) -> None:
        previous_scene = self._active_scene
        self._active_scene = self._previous_scene
        self._previous_scene = previous_scene

        self._active_scene.start()

    def startMainMenu(self) -> None:
        self._previous_scene = self._active_scene
        self._active_scene = self._main_menu

        self._active_scene.start()