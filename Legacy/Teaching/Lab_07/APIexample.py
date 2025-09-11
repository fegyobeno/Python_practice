from fastapi import FastAPI, HTTPException, Request
from typing import Optional
import uvicorn
from pydantic import BaseModel

app = FastAPI()

#pydantic modell a Base javítására, validálja a bejövő adatokat
class Item(BaseModel):
        name :str
        description :str = None
        price :float
        tax :float = None

# definiálja a gyökeret
@app.get("/")
def read_root():
    return {"Hello": "World"}

#üdvözlő üzenet
@app.get("/welcome")
def welcome_with_name(name: Optional[str] = None):
    return {f"Welcome {name}" if name else "Welcome unknown user"}

#curl -X GET "http://127.0.0.1:20000/welcome?name=Benedek"
#http://127.0.0.1:20000/welcome?name=Benedek

items = { 1: {"name": "Item 1", "price": 9.99}, 2: {"name": "Item 2", "price": 19.99} }

@app.get("/items/")
def read_items():
    return items

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id, "q": q, "item": items.get(item_id)}

#http://127.0.0.1:10000/items/1?q=alma

# asyinc --> aszinkron működés
# az aszinkron működés lehetővé teszi, hogy a szerver több kérést is kezeljen egyszerre

@app.post("/adat_fogadása")
async def adat_fogadása(request: Request):
    json_adat = await request.json()
    return {"kapott_adat": json_adat}

@app.post("/items/")
async def create_item(item: Item):
    item_id = max(items.keys()) + 1
    items[item_id] = item.model_dump()
    return item

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    items[item_id] = item.model_dump()
    return item

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    item = items.pop(item_id)
    return item

#items/5?q=alma

#curl -X POST "http://127.0.0.1:10000 /items/" -H "Content-Type: application/json" -d '{"name": "Sample Item", "description": "This is a sample item", "price": 10.99, "tax": 1.99}'

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=10000)