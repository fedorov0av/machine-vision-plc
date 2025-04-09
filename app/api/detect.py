from fastapi import APIRouter

from app.schemas.responses import CornerResponse
from app.utils.image_processor import ImageProcessor
from app.utils.camera import Camera


router = APIRouter(prefix="/api", tags=["detect"])

@router.post("/detect_corners/", response_model=CornerResponse)
async def detect_corners():
    camera = Camera()
    images = await camera.capture()
    image_processor = ImageProcessor(images)
    await image_processor.remove_artifacts()
    await image_processor.harris_corner_detection()
    await image_processor.save_images()
    return CornerResponse(
        corner_1=(0, 0),
        corner_2=(0, 0),
    ) # temp response