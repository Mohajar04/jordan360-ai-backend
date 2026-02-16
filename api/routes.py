from fastapi import APIRouter
from models.user import encode_interests
from models.location import load_locations
from core.optimizer import build_route
from api.schemas import RecommendRequest,ReoptimizeRequest

router=APIRouter()

@router.post("/recommend")
def recommend(req:RecommendRequest):
    user_vector=encode_interests(req.interests)
    locations=load_locations("data/locations.json")
    route,explanations=build_route(
        user_vector,req.latitude,req.longitude,
        req.available_time,locations,req.crowd)
    return {"route":route,"explanations":explanations}

@router.post("/reoptimize")
def reoptimize(req:ReoptimizeRequest):
    user_vector=encode_interests(req.interests)
    locations=load_locations("data/locations.json")
    route,explanations=build_route(
        user_vector,req.latitude,req.longitude,
        req.remaining_time,locations,req.crowd)
    return {"route":route,"explanations":explanations}
