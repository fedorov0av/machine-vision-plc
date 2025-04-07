from pydantic import BaseModel
from typing import Tuple

class CornerResponse(BaseModel):
    corner_1: Tuple[int, int]
    corner_2: Tuple[int, int]