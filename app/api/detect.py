from fastapi import APIRouter, HTTPException

from app.schemas.responses import CornerResponse
from app.utils.image_processor import ImageProcessor
from app.utils.camera import Camera


router = APIRouter(prefix="/api", tags=["detect"])

@router.get("/detect_corners/", response_model=CornerResponse)
async def detect_corners():
    camera = Camera()
    try:
        image = await camera.capture()
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    image_processor = ImageProcessor(image)
    await image_processor.remove_artifacts()
    corners = await image_processor.line_intersection_corner_detection()
    await image_processor.harris_corner_detection()
    await image_processor.save_image()
    corner_1 = corners[0]
    corner_2 = corners[1]
    return CornerResponse(
        corner_1=corner_1,
        corner_2=corner_2,
    )
