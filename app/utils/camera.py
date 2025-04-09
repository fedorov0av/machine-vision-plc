import cv2
import os
import numpy as np
from typing import List

class Camera:
    def __init__(
            self,
            image_directory: str = "images/input/",
            image_name: str = "test.png"
            ):
        self.image_directory = image_directory
        self.image_name = image_name

    async def capture(self) -> List[np.ndarray]:
        image_files = [f for f in os.listdir(self.image_directory) if f.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff'))]
        if not image_files:
            raise FileNotFoundError(f"В директории {self.image_directory} нет изображений")
        images = []
        for image_name in image_files:
            image_path = os.path.join(self.image_directory, image_name)
            if os.path.exists(image_path):
                image = cv2.imread(image_path)
                if image is None:
                    raise ValueError(f"Не удалось загрузить изображение: {image_name}")
                images.append(image)
            else:
                raise FileNotFoundError(f"Файл {image_name} не найден в директории {self.image_directory}")
        return images
