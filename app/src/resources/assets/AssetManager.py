import pygame
from src.core.Configuration import Paths, Assets

class AssetManager:
    """
    The AssetManager class provides functionalities to load
    and store assets like images and sounds.

    Loaded assets will be stored in dictionaries and can be
    returned for use when needed.
    """
    __images: dict
    __sounds: dict
    __path: str
    __mixer: pygame.mixer

    def __init__(self) -> None:
        """
        Initializes the AssetManager object and initializes the
        images and sounds dictionaries.
        """
        self.__path = Paths.ASSETS
        self.__mixer = pygame.mixer
        self.__images = {}
        self.__sounds = {}

    @property
    def images(self) -> dict:
        """
        Returns the dictionary of loaded images.

        Returns:
            dict: A dictionary where keys are image names and values are pygame.Surface objects.
        """
        return self.__images

    def update_image(self, image_name: str, image: pygame.Surface) -> None:
        """
        Updates the images dictionary with a new image.

        Args:
            image_name (str): The name to register the image under.
            image (pygame.Surface): The image surface to store.
        """
        if isinstance(image, pygame.Surface):
            self.__images.update({image_name: image})
        else:
            raise TypeError("image must be a pygame.Surface object")

    def load_image(self, asset: Assets) -> None:
        """
        Loads a .png file from the assets/images folder and registers it in the images dictionary.

        Args:
            image_name (str): The name of the image file to load.
        
        Raises:
            TypeError: If the file is not a .png file.
        """
        if asset.NAME.endswith(".png"):
            file_path = f"{self.__path}images/{asset.NAME}"
            new_image = pygame.image.load(file_path)
            self.__images.update({asset.ID: new_image})
        else:
            raise TypeError("file must be a .png file")

    def get_image(self, image_name: str) -> pygame.Surface:
        """
        Returns a specific image from the images dictionary.

        Args:
            image_name (str): The name of the image to retrieve.

        Returns:
            pygame.Surface: The requested image surface.
        """
        return self.__images.get(image_name)

    @property
    def sounds(self) -> dict:
        """
        Returns the dictionary of loaded sounds.

        Returns:
            dict: A dictionary where keys are sound names and values are pygame.mixer.Sound objects.
        """
        return self.__sounds

    def load_sound(self, asset: Assets) -> None:
        """
        Loads a .mp3 file from the assets/sounds folder and registers it in the sounds dictionary.

        Args:
            audio_name (str): The name of the audio file to load.
        
        Raises:
            TypeError: If the file is not a .mp3 file.
        """
        if asset.NAME.endswith(".mp3"):
            file_path = f"{self.__path}sounds/{asset.NAME}"
            new_audio = self.__mixer.Sound(file_path)
            self.__sounds.update({asset.ID: new_audio})
        else:
            raise TypeError("file must be a .mp3 file")

    def get_sound(self, sound_name: str) -> pygame.mixer.Sound:
        """
        Returns a specific sound from the sounds dictionary.

        Args:
            sound_name (str): The name of the sound to retrieve.

        Returns:
            pygame.mixer.Sound: The requested sound.
        """
        return self.__sounds.get(sound_name)
