from fastapi import FastAPI, HTTPException, Request
from typing import Optional
import uvicorn
from pydantic import BaseModel

# python3 -m pip install -r resources.txt


app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to the API!"}

# /welcome?name=YourName
# /welcome?name=YourName&password=secret
@app.get("/welcome")
def welcome_message(name: Optional[str] = None, password: Optional[str] = None):
    if name and password == "secret":
        return {"message": f"Welcome, {name}!"}
    return {"message": "Welcome, guest!"}

# /items/{item_id}?q=somequery
items = { 1: {"name": "Item 1", "price": 9.99}, 2: {"name": "Item 2", "price": 19.99} }
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id, "q": q, "item": items.get(item_id)}

# BaseModel --> adatmodell
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

items_db = {}
items_db[0] = {"name": "Sample Item", "description": "This is a sample item", "price": 10.0, "tax": 1.0}
items_db[1] = {"name": "Another Item", "description": "This is another item", "price": 20.0, "tax": 2.0}
@app.get("/items_v2/{item_id}", response_model=Item)
def get_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return items_db[item_id]

# Post it on an endpoint
@app.post("/items_v2/", response_model=Item)
def create_item(item: Item):
    item_id = len(items_db)
    items_db[item_id] = item.dict()
    return items_db[item_id]

@app.put("/items_v2/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    items_db[item_id] = item.dict()
    return items_db[item_id]

@app.delete("/items_v2/{item_id}")
def delete_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    del items_db[item_id]
    return {"message": "Item deleted successfully"}

# http://127.0.0.1:8000/docs

# async endpoint --> lehetővé teszi a párhuzamos feldolgozást
# egyszerre több kérést képes kiszolgálni
@app.get("/async-endpoint")
async def async_endpoint():
    return {"message": "This is an async endpoint"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

