from pydantic import BaseModel, Field
from typing import List, Optional
from enum import Enum

class AgeGroup(str, Enum):
    CHILD = "child"
    TEEN = "teen"
    YOUNG_ADULT = "young_adult"
    ADULT = "adult"
    SENIOR = "senior"

class Interest(str, Enum):
    TECHNOLOGY = "technology"
    SPORTS = "sports"
    MUSIC = "music"
    MOVIES = "movies"
    BOOKS = "books"
    TRAVEL = "travel"
    FOOD = "food"
    FITNESS = "fitness"

class UserProfile(BaseModel):
    user_id: str = Field(..., description="Unique identifier for the user")
    age_group: AgeGroup
    interests: List[Interest] = Field(default_factory=list)
    preferred_languages: List[str] = Field(default_factory=list)
    location: Optional[str] = None
    
    class Config:
        schema_extra = {
            "example": {
                "user_id": "user123",
                "age_group": "young_adult",
                "interests": ["technology", "music"],
                "preferred_languages": ["en"],
                "location": "New York, NY"
            }
        }
