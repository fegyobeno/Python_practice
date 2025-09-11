# FastAPI Kód Magyarázat

## Mi az az API?

Az API (Application Programming Interface) egy olyan interfész, amely lehetővé teszi különböző szoftveralkalmazások számára, hogy kommunikáljanak egymással. Az API meghatározza a szabályokat és protokollokat, amelyeket a programoknak követniük kell az adatok cseréjéhez és a funkciók eléréséhez. Az API-k lehetnek nyilvánosak vagy privátak, és különböző típusúak, például RESTful, SOAP, GraphQL stb.

Az API-k használatának előnyei közé tartozik a modularitás, az újrafelhasználhatóság és a rugalmasság, mivel lehetővé teszik a különböző rendszerek és szolgáltatások integrációját anélkül, hogy azok belső működését ismerni kellene.

Ez a dokumentum egy FastAPI alkalmazás kódját magyarázza el.

```python
from fastapi import FastAPI, HTTPException, Request
from typing import Optional
import uvicorn
from pydantic import BaseModel

app = FastAPI()
```

## Pydantic Modell

A `BaseModel` osztály segítségével definiálunk egy modellt, amely validálja a bejövő adatokat.

```python
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
```

## Gyökér Útvonal

A gyökér útvonal egy egyszerű "Hello World" üzenetet ad vissza.

```python
@app.get("/")
def read_root():
    return {"Hello": "World"}
```

## Üdvözlő Üzenet

Egy opcionális névvel ellátott üdvözlő üzenetet ad vissza.

```python
@app.get("/welcome")
def welcome_with_name(name: Optional[str] = None):
    return {f"Welcome {name}" if name else "Welcome unknown user"}
```

## Elemlista

Egy előre definiált elemlistát ad vissza.

```python
items = {1: {"name": "Item 1", "price": 9.99}, 2: {"name": "Item 2", "price": 19.99}}

@app.get("/items/")
def read_items():
    return items
```

## Elem Lekérdezése

Egy adott azonosítójú elemet kérdez le, és opcionálisan egy query paramétert is kezel.

```python
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id, "q": q, "item": items.get(item_id)}
```

## Adat Fogadása

Aszinkron módon fogad JSON adatokat egy POST kérésben.

```python
@app.post("/adat_fogadása")
async def adat_fogadása(request: Request):
    json_adat = await request.json()
    return {"kapott_adat": json_adat}
```

## Új Elem Létrehozása

Új elemet hoz létre a megadott adatok alapján.

```python
@app.post("/items/")
async def create_item(item: Item):
    item_id = max(items.keys()) + 1
    items[item_id] = item.model_dump()
    return item
```

## Elem Frissítése

Egy meglévő elemet frissít a megadott adatok alapján.

```python
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    items[item_id] = item.model_dump()
    return item
```

## Elem Törlése

Egy adott azonosítójú elemet töröl.

```python
@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    item = items.pop(item_id)
    return item
```

## Alkalmazás Futtatása

Az alkalmazás futtatása a megadott host és port beállításokkal.

az if __name__=="__main__" biztosítja hogy a file csak akkor fusson le ha közvetlenül futtatják de akkor nem ha importálják

```python
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=10000)
```