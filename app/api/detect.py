from fastapi import APIRouter

from app.schemas.responses import CornerResponse


router = APIRouter(prefix="/api", tags=["detect"])

@router.post("/detect_corners/", response_model=CornerResponse)
async def detect_corners():
    pass