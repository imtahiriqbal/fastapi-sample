from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

    
app = FastAPI()

@app.get("/")
async def hello():
    return {"msg": "Hello World!"}

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "Tahir"}

@app.get("/users/{user_id}")
async def read_user_by_id(user_id: str):
    return {"user_id": user_id}


class Item(BaseModel):
    name: str
    description: Optional[str] = "Add item description (optional)"
    price: float
    tax: Optional[float] = None
    

@app.get("/items/{item_id}")
async def read_item(item_id:int):
    return {"item_id": item_id}

@app.post("/items/", response_model=Item) # response_model will show a sample success response in endpoint
async def create_item(item: Item):
    return item

@app.post("/items_with_tax/")
async def create_item_with_tax(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

@app.put("/items/{item_id}")
async def update_item_with_id(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}
