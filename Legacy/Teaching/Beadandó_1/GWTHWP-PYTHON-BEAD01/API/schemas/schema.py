from pydantic import BaseModel, Field, EmailStr

ShopName = "Bolt"


class User(BaseModel):
    id: int = Field(..., ge=0, description="Az ID nem lehet negatív szám")
    name: str
    email: EmailStr


class Basket(BaseModel):
    id: int = Field(..., ge=0, description="Az ID nem lehet negatív szám")
    user_id: int = Field(
        ..., ge=0, description="A felhasználó ID nem lehet negatív szám"
    )
    items: list


class Item(BaseModel):
    item_id: int = Field(..., ge=0, description="Az ID nem lehet negatív szám")
    name: str
    brand: str
    price: float = Field(..., ge=0, description="Az ár nem lehet negatív")
    quantity: int = Field(..., ge=0, description="A mennyiség nem lehet negatív")
