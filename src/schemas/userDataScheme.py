from pydantic import BaseModel
from src.enums.repairLevelEnum import repairLevel




class UserData(BaseModel):
    totalArea: float
    rommsCount: int
    repairLevel: repairLevel