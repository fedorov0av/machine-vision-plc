import cv2
import numpy as np
from typing import List


class ImageProcessor:
    def __init__(self, image: np.ndarray):
        if image is None:
            raise ValueError("Изображение не может быть пустым.")
        self.image = image

    async def remove_artifacts(self) -> np.ndarray:
        kernel = np.ones((5, 5), np.uint8)
        cleaned_image = cv2.morphologyEx(self.image, cv2.MORPH_CLOSE, kernel)
        self.image = cleaned_image
        return self.image
    
    async def harris_corner_detection(self) -> np.ndarray:
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        gray_float32 = np.float32(gray)
        dst = cv2.cornerHarris(gray_float32, 2, 3, 0.04)
        dst = cv2.dilate(dst, None)
        self.image[dst > 0.01 * dst.max()] = [0, 0, 255]
        return self.image

    async def line_intersection_corner_detection(self) -> List[tuple]:
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        edges = cv2.Canny(blurred, 50, 150, apertureSize=3)
        lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength=50, maxLineGap=10)
        corners = []
        if lines is not None:
            for line in lines:
                x1, y1, x2, y2 = line[0]
                if 0 in (x1, y1, x2, y2):
                    angle = np.arctan2(y2 - y1, x2 - x1) * 180 / np.pi
                    if 10 < angle < 80:
                        corners.append((x1, y1))
                        corners.append((x2, y2))
                        continue
                    continue
                corners.append((x1, y1))
                corners.append((x2, y2))
            corners = list(set(corners))
        return corners

    async def save_image(self, filename: str = "images/output/output.png"):
        cv2.imwrite(filename, self.image)
