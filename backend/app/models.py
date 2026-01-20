from pydantic import BaseModel
from typing import List, Optional


class UserProfile(BaseModel):
    age: int
    sex: str
    height_cm: Optional[float]
    weight_kg: Optional[float]
    goal: str
    experience: str
    equipment: List[str]
    injuries: List[str] = []
    days_per_week: int = 3


class ExerciseOut(BaseModel):
    name: str
    description: Optional[str]
    type: Optional[str]
    primary_muscle: Optional[str]
    required_equipment: Optional[List[str]]
    unsafe_for: Optional[List[str]]
    required_experience: Optional[str]


class PlanResponse(BaseModel):
    summary: str
    week: dict
