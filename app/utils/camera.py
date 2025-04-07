import cv2
import os
import numpy as np

class Camera:
    def __init__(
            self,
            image_directory: str = "app/assets/images/",
            image_name: str = "test.png"
            ):
        self.image_directory = image_directory
        self.image_name = image_name

    async def capture(self) -> np.ndarray:
        image_path = os.path.join(self.image_directory, self.image_name)
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Файл {self.image_name} не найден в директории {self.image_directory}")
        image = cv2.imread(image_path)
        if image is None:
            raise ValueError(f"Не удалось загрузить изображение: {self.image_name}")
        return image
