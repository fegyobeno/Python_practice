from pydantic import BaseModel, EmailStr, Field
from typing import List

'''

Útmutató a fájl használatához:

Az osztályokat a schema alapján ki kell dolgozni.

A schema.py az adatok küldésére és fogadására készített osztályokat tartalmazza.
Az osztályokban az adatok legyenek validálva.
 - az int adatok nem lehetnek negatívak.
 - az email mező csak e-mail formátumot fogadhat el.
 - Hiba esetén ValuErrort kell dobni, lehetőség szerint ezt a 
   kliens oldalon is jelezni kell.

'''

ShopName='Bolt'

class User(BaseModel):
    id: int = Field(gt=0)
    name: str
    email: EmailStr

class Item(BaseModel):
    item_id: int = Field(gt=0)
    name: str
    brand: str
    price: float = Field(ge=0)
    quantity: int = Field(ge=0)

class Basket(BaseModel):
    id: int = Field(gt=0)
    user_id: int = Field(gt=0)
    items: List[Item]


