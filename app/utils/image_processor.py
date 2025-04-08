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
    
    async def harris_corner_detection(self, image: np.ndarray = None) -> np.ndarray:
        if image is not None:
            self.image = image
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        gray_float32 = np.float32(gray)
        dst = cv2.cornerHarris(gray_float32, 2, 3, 0.04)
        dst = cv2.dilate(dst, None)
        self.image[dst > 0.01 * dst.max()] = [0, 0, 255]
        return dst

    async def save_image(self, image: np.ndarray = None, filename: str = "images/output.png"):
        if image is not None:
            self.image = image
        cv2.imwrite(filename, self.image)