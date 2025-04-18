from fastapi import FastAPI
from typing import Optional
api = FastAPI()



@api.get('/addition')
def get_addition(a: int, b: Optional[int]=None):
    if b:
        result = a + b
    else:
        result = a + 1
    return {
        'addition_result': result
    }


class Item(BaseModel):
    itemid: int
    description: str
    owner: Optional[str] = None
