from fastapi import APIRouter
import json

router = APIRouter()

with open("data/benefits.json", "r") as f:
    benefit_data = json.load(f)

@router.get("/benefits/{state}")
def get_benefits_by_state(state: str):
    state_data = benefit_data.get(state.upper(), [])
    return {"state": state.upper(), "programs": state_data}
