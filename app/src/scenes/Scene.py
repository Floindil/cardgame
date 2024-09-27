import pygame
from core.Configuration import Configuration as CFG
from resources.assets.AssetManager import AssetManager
from resources.components.Component import Component

class Scene:

    components: list[Component]

    def __init__(self) -> None:
        self.surface = pygame.Surface(CFG.DISPLAYSIZE)
        self.assetManager = AssetManager()
        self.components = []

    def addComponent(self, component: Component) -> None:
        self.components.append(component)

    def getComponentsToRender(self) -> list[Component]:
        """
        Checks all Components in the Scenes components List.
        If the component has the RENDER flag set to true, it will
        be added to the componentsToRender list right behind the first
        Components with a lower RENDERPRIORITY number. Components with
        a lower RENDERPRIORITY will be rendered last.
        """
        componentsToRender: list[Component] = []
        # iterate through all the Scenes components
        for c in self.components:
            # check, if the components should be rendered
            if c.RENDER:
                if len(componentsToRender) != 0:
                    # sort the components by RENDERPRIORITY
                    for i, ctr in enumerate(componentsToRender):
                        if c.RENDERPRIORITY <= ctr.RENDERPRIORITY:
                            componentsToRender.insert(i+1, c)
                            break
                else:
                    componentsToRender.append(c)
        return componentsToRender
