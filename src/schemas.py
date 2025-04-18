from pydantic import BaseModel
from typing import Optional
class Item(BaseModel):
    itemid: int
    description: str
    owner: Optional[str] = None

