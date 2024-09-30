import pygame
from src.core.Configuration import Paths

class AssetManager:
    """
    The AssetManager class provides functionalities to load
    and store assets like images and sounds.

    Loaded assets will be stored in a dictionary and can be
    returned to use them.
    """
    _assets: dict
    __path: str 
    __mixer: pygame.mixer

    def __init__(self) -> None:
        """
        Creates a AssetManager Object and initializes the
        assets dictionary.
        """
        self.__path = Paths.ASSETS
        self.__mixer = pygame.mixer
        self._assets = {
            "images": {},
            "sounds": {}
        }

    def add_image(self, image_name: str, image: pygame.Surface) -> None:
        if isinstance(image, pygame.Surface):
            self._assets.update({"images": {image_name: image}})

    def load_image(self, image_name: str) -> None:
        """
        Loads a .png file from your images/assets folder.
        """
        if image_name.endswith(".png"):
            fileArg = f"{self.__path}images/{image_name}"
            newImage = pygame.image.load(fileArg)
            self._assets.update({"images": {image_name[:-3]: newImage}})
        else:
            raise TypeError("must be png file!")

    def get_image(self, imageName: str) -> pygame.Surface:
        """
        Returns a specific image from the asset dictionary.
        """
        image = self._assets["images"].get(imageName)
        return image

    def load_sound(self, audio_name: str) -> None:
        """
        Loads a .mp3 file from your images/sounds folder.
        """
        if audio_name.endswith(".mp3"):
            fileArg = f"{self.__path}sounds/{audio_name}"
            newAudio = self.__mixer.Sound(fileArg)
            self._assets.update({"sounds": {audio_name[:-3]: newAudio}})
        else:
            raise TypeError("must be mp3 file!")
    
    def get_sound(self, soundName: str) -> pygame.mixer.Sound:
        """
        Returns a specific sound from the asset dictionary.
        """
        sound = self._assets["sounds"].get(soundName)
        return sound
