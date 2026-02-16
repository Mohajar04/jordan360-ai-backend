from pydantic import BaseModel
from typing import Dict

class RecommendRequest(BaseModel):
    interests: Dict[str,int]
    latitude: float
    longitude: float
    available_time: float
    crowd: Dict[str,float]={}

class ReoptimizeRequest(BaseModel):
    interests: Dict[str,int]
    latitude: float
    longitude: float
    remaining_time: float
    crowd: Dict[str,float]={}
