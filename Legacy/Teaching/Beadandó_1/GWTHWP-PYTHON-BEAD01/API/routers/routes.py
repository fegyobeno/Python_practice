from schemas.schema import User, Basket, Item
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi import FastAPI, HTTPException, Request, Response, Cookie
from fastapi import APIRouter
from data.filereader import (
    get_user_by_id,
    get_basket_by_user_id,
    get_all_users,
    get_total_price_of_basket,
    findItemById,
)
from data.filehandler import (
    add_user,
    add_basket,
    add_item_to_basket,
    save_json,
    load_json,
)
from domain.HttpExceptionMessage import HttpExceptionMessage


routers = APIRouter()


@routers.post("/adduser", response_model=User)
def adduser(user: User) -> User:
    try:
        add_user(user.model_dump())
        return JSONResponse(content=user.model_dump(), status_code=200)
    except ValueError as e:
        HttpExceptionMessage.VALUE.raise_exception()


@routers.post("/addshoppingbag", response_model=str)
def addshoppingbag(userid: int) -> str:
    try:
        newBasket = {"id": userid * 100, "user_id": userid, "items": []}
        add_basket(newBasket)
        return JSONResponse(content="Sikeres kosár hozzárendelés.", status_code=200)
    except ValueError as e:
        HttpExceptionMessage.VALUE.raise_exception()


@routers.post("/additem", response_model=Basket)
def additem(userid: int, item: Item) -> Basket:
    try:
        add_item_to_basket(userid, item.model_dump())
        basketItems = get_basket_by_user_id(userid)
        return JSONResponse(
            content={"user_id": userid, "items": basketItems}, status_code=200
        )
    except ValueError as e:
        HttpExceptionMessage.VALUE.raise_exception()


@routers.put("/updateitem", response_model=Basket)
def updateitem(userid: int, itemid: int, updateItem: Item) -> Basket:
    try:
        data = load_json()
        basket = findItemById(data, userid, "Baskets", "user_id", False)
        if not basket:
            HttpExceptionMessage.BASKET.raise_exception()
        item = next(
            (item for item in basket["items"] if item["item_id"] == itemid), None
        )
        if not item:
            HttpExceptionMessage.ITEM.raise_exception()
        item.update(updateItem.model_dump())
        save_json(data)
        return JSONResponse(
            content={"user_id": userid, "items": basket["items"]}, status_code=200
        )
    except ValueError as e:
        HttpExceptionMessage.VALUE.raise_exception()


@routers.delete("/deleteitem", response_model=Basket)
def deleteitem(userid: int, itemid: int) -> Basket:
    try:
        data = load_json()
        basket = findItemById(data, userid, "Baskets", "user_id", False)
        if not basket:
            HttpExceptionMessage.BASKET.raise_exception()
        basket["items"] = [
            item for item in basket["items"] if item["item_id"] != itemid
        ]
        save_json(data)
        return JSONResponse(
            content={"user_id": userid, "items": basket["items"]}, status_code=200
        )
    except ValueError as e:
        HttpExceptionMessage.VALUE.raise_exception()


@routers.get("/user", response_model=User)
def user(userid: int) -> User:
    try:
        userData = get_user_by_id(userid)
        return JSONResponse(content=userData, status_code=200)
    except ValueError as e:
        HttpExceptionMessage.VALUE.raise_exception()


@routers.get("/users", response_model=list[User])
def users() -> list[User]:
    try:
        allUsers = get_all_users()
        return JSONResponse(content=allUsers, status_code=200)
    except ValueError as e:
        HttpExceptionMessage.VALUE.raise_exception()


@routers.get("/shoppingbag", response_model=list[Item])
def shoppingbag(userid: int) -> list[Item]:
    try:
        basketItems = get_basket_by_user_id(userid)
        return JSONResponse(content=basketItems, status_code=200)
    except ValueError as e:
        HttpExceptionMessage.VALUE.raise_exception()


@routers.get("/getusertotal", response_model=float)
def getusertotal(userid: int) -> float:
    try:
        totalPrice = get_total_price_of_basket(userid)
        return JSONResponse(content=totalPrice, status_code=200)
    except ValueError as e:
        HttpExceptionMessage.VALUE.raise_exception()
