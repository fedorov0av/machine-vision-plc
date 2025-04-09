import cv2
import numpy as np
from typing import List


class ImageProcessor:
    def __init__(self, images: List[np.ndarray]):
        if images is None:
            raise ValueError("Изображение не может быть пустым.")
        self.images = images

    async def remove_artifacts(self) -> List[np.ndarray]:
        kernel = np.ones((5, 5), np.uint8)
        cleaned_images = []
        for image in self.images:
            cleaned_image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
            cleaned_images.append(cleaned_image)
        self.images = cleaned_images
        return cleaned_images
    
    async def harris_corner_detection(self) -> List[np.ndarray]:
        processed_images = []
        for image in self.images:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            gray_float32 = np.float32(gray)
            dst = cv2.cornerHarris(gray_float32, 2, 3, 0.04)
            dst = cv2.dilate(dst, None)
            image[dst > 0.01 * dst.max()] = [0, 0, 255]
            processed_images.append(image)
        self.images = processed_images
        return processed_images

    async def save_images(self, filenames: List[str] = None):
        if filenames is None:
            filenames = [f"images/output/output_{i}.png" for i in range(len(self.images))]
        for idx, image in enumerate(self.images):
            filename = filenames[idx] if idx < len(filenames) else f"images/output/output_{idx}.png"
            cv2.imwrite(filename, image)