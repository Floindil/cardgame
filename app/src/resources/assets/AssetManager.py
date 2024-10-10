import pygame
from src.core.Configuration import Paths

class AssetManager:
    """
    The AssetManager class provides functionalities to load
    and store assets like images and sounds.

    Loaded assets will be stored in a dictionary and can be
    returned to use them.
    """
    __images: dict
    __sounds: dict
    __path: str 
    __mixer: pygame.mixer

    def __init__(self) -> None:
        """
        Creates a AssetManager Object and initializes the
        images and sounds dictionaries.
        """
        self.__path = Paths.ASSETS
        self.__mixer = pygame.mixer
        self.__images = {}
        self.__sounds = {}

    @property
    def images(self) -> dict:
        return self.__images

    def update_image(self, image_name: str, image: pygame.Surface) -> None:
        if isinstance(image, pygame.Surface):
            self.__images.update({image_name: image})

    def load_image(self, image_name: str) -> None:
        """
        Loads a .png file from your images/assets folder.\n
        registers the image in the images dictionary.
        """
        if image_name.endswith(".png"):
            fileArg = f"{self.__path}images/{image_name}"
            newImage = pygame.image.load(fileArg)
            self.__images.update({image_name.replace(".png", ""): newImage})
        else:
            raise TypeError("must be png file!")

    def get_image(self, imageName: str) -> pygame.Surface:
        """
        Returns a specific image from the images dictionary.
        """
        image = self.__images.get(imageName)
        return image

    @property
    def sounds(self) -> dict:
        return self.__sounds

    def load_sound(self, audio_name: str) -> None:
        """
        Loads a .mp3 file from your images/sounds folder.\n
        registers the sound in the sounds dictionary.
        """
        if audio_name.endswith(".mp3"):
            fileArg = f"{self.__path}sounds/{audio_name}"
            newAudio = self.__mixer.Sound(fileArg)
            self.__sounds.update({audio_name.replace(".mp3", ""): newAudio})
        else:
            raise TypeError("must be mp3 file!")
    
    def get_sound(self, soundName: str) -> pygame.mixer.Sound:
        """
        Returns a specific sound from the sounds dictionary.
        """
        sound = self.__sounds.get(soundName)
        return sound
