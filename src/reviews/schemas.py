from pydantic import BaseModel, Field
from src.db.models import Review
import uuid
from typing import Optional, List
from datetime import datetime



class ReviewModel(BaseModel):
    uid: uuid.UUID
    rating: int = Field(lt=5)
    review_text: str
    user_uid: Optional[uuid.UUID]
    book_uid: Optional[uuid.UUID]
    created_at: datetime
    updated_at: datetime



class ReviewCreateModel(BaseModel):
    rating: int = Field(lt=5)
    review_text: str