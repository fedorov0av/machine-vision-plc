from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/api", tags=["detect"])

class CornerRequest(BaseModel):
    method: str

@router.post("/detect_corners")
async def detect_corners(request: CornerRequest):
    pass