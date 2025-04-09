import cv2
import os
import numpy as np

class Camera:
    def __init__(
            self,
            image_directory: str = "images/input/",
            ):
        self.image_directory = image_directory

    async def capture(self) -> np.ndarray:
        image_files = [f for f in os.listdir(self.image_directory) if f.endswith(('.png'))]
        if not image_files:
            raise FileNotFoundError(f"В директории {self.image_directory} нет изображений")
        image_name = image_files[0]
        image_path = os.path.join(self.image_directory, image_name)
        if os.path.exists(image_path):
            image = cv2.imread(image_path)
            if image is None:
                raise ValueError(f"Не удалось загрузить изображение: {image_name}")
            return image
        else:
            raise FileNotFoundError(f"Файл {image_name} не найден в директории {self.image_directory}")
