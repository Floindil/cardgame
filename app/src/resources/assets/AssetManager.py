import pygame
from core.statics import Paths

class AssetManager:
    """
    The AssetManager class provides functionalities to load
    and store assets like images and sounds.

    Loaded assets will be stored in a dictionary and can be
    returned to use them.
    """
    assets: dict
    path: str

    def __init__(self) -> None:
        """
        Creates a AssetManager Object and initializes the
        assets dictionary.
        """
        self.path = Paths.ASSETS
        self.mixer = pygame.mixer
        self.assets = {
            "images": {},
            "sounds": {}
        }

    def loadImage(self, imageName: str) -> None:
        """
        Loads a .png file from your images/assets folder.
        """
        fileArg = f"{self.path}images/{imageName}.png"
        newImage = pygame.image.load(fileArg)
        self.assets.update({"images": {imageName: newImage}})

    def getImage(self, imageName: str) -> pygame.Surface:
        """
        Returns a specific image from the asset dictionary.
        """
        image = self.assets["images"].get(imageName)
        return image

    def loadAudio(self, audioName: str) -> None:
        """
        Loads a .mp3 file from your images/sounds folder.
        """
        fileArg = f"{self.path}sounds/{audioName}.mp3"
        newAudio = self.mixer.Sound(fileArg)
        self.assets.update({"sounds": {audioName: newAudio}})
    
    def getSound(self, soundName: str) -> pygame.mixer.Sound:
        """
        Returns a specific sound from the asset dictionary.
        """
        sound = self.assets["sounds"].get(soundName)
        return sound
