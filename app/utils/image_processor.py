import cv2
import numpy as np

class ImageProcessor:
    def __init__(self, image: np.ndarray):
        if image is None:
            raise ValueError("Изображение не может быть пустым.")
        self.image = image

    async def remove_artifacts(self) -> np.ndarray:
        kernel = np.ones((5, 5), np.uint8)
        cleaned_image = cv2.morphologyEx(self.image, cv2.MORPH_CLOSE, kernel)
        self.image = cleaned_image
        return cleaned_image

    async def save_image(self, image: np.ndarray = None, filename: str = "output.png"):
        if image is not None:
            self.image = image
        cv2.imwrite(filename, self.image)