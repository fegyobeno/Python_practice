from schemas.schema import User, Basket, Item
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi import FastAPI, HTTPException, Request, Response, Cookie
from fastapi import APIRouter
from typing import Dict, Any, List

from data.filereader import (
    get_user_by_id,
    get_basket_by_user_id,
    get_all_users,
    get_total_price_of_basket,
    get_current_highest_ids,
    get_basket_id_by_user_id
)

from data.filehandler import (
    add_user,
    add_basket,
    add_item_to_basket,
    delete_item_from_basket,
    modify_item_in_basket
)

'''

Útmutató a fájl használatához:

- Minden route esetén adjuk meg a response_modell értékét (típus)
- Ügyeljünk a típusok megadására
- A függvények visszatérési értéke JSONResponse() legyen
- Minden függvény tartalmazzon hibakezelést, hiba esetén dobjon egy HTTPException-t
- Az adatokat a data.json fájlba kell menteni.
- A HTTP válaszok minden esetben tartalmazzák a 
  megfelelő Státus Code-ot, pl 404 - Not found, vagy 200 - OK

Code	Meaning	                When to use
200	    OK	                    Generic success
201	    Created	                New resource created
204	    No Content	            Success, but no return body
400	    Bad Request	            Client sent invalid data
404	    Not Found	            Resource doesn’t exist
422	    Unprocessable Entity	Validation failed (Pydantic)
500	    Internal Server Error	Code error or crash
'''

routers = APIRouter()

@routers.post('/adduser', response_model=User)
def adduser(user: User) -> JSONResponse:
    user_dict: Dict[str, Any] = user.model_dump()
    try:
        add_user(user_dict) # unique ID check is handled in add_user
        return JSONResponse(content=user_dict, status_code=201)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) # propagate filehandler add_user Value error as http exception if it occurs
    

@routers.post('/addshoppingbag')
def addshoppingbag(userid: int) -> JSONResponse:
    # since add_basket in filehandler requires a basket dictionary, we need to create it here. we use a helper method called get_current_highest_ids from filereader
    basket = {
        "id": get_current_highest_ids()[0]+1,
        "user_id": userid,
        "items": []
    }
    try:
        add_basket(basket)
        return JSONResponse(content="Sikeres kosár hozzárendelés.", status_code=200)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@routers.post('/additem', response_model=Basket)
def additem(userid: int, item: Item) -> JSONResponse:
    try:
        item_data = item.model_dump()
        add_item_to_basket(userid, item_data)
        basket = {
            "id": get_basket_id_by_user_id(userid),
            "user_id": userid,
            "items": get_basket_by_user_id(userid)
        }
        return JSONResponse(content=basket, status_code=200)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

#itemid not needed in signature (the Item struct already contains it), so this was removed
# we return the updated basket in a JSONResponse as per original signature + task requirement
@routers.put('/updateitem', response_model=Basket)
def updateitem(userid: int, update_item: Item) -> JSONResponse:
    try:
        modify_item_in_basket(userid, update_item.model_dump())
        basket = {
            "id": get_basket_id_by_user_id(userid),
            "user_id": userid,
            "items": get_basket_by_user_id(userid)
        }
        return JSONResponse(content = basket, status_code=200)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

# returning basket in the message
@routers.delete('/deleteitem', response_model=Basket)
def deleteitem(userid: int, itemid: int) -> JSONResponse:
    try:
        delete_item_from_basket(userid, itemid)  
        basket = {
            "id": get_basket_id_by_user_id(userid),
            "user_id": userid,
            "items": get_basket_by_user_id(userid)
        }     
        return JSONResponse(content = basket, status_code=200)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@routers.get('/user', response_model=User)
def user(userid: int) -> JSONResponse:
    try:
        user_data = get_user_by_id(userid)
        return JSONResponse(content = user_data, status_code=200)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@routers.get('/users', response_model = List[User])
def users() -> JSONResponse:
    all_users = get_all_users()
    return JSONResponse(content = all_users, status_code=200)


@routers.get('/shoppingbag', response_model=List[Item])
def shoppingbag(userid: int) -> JSONResponse:
    try:
        items = get_basket_by_user_id(userid)
        return JSONResponse(content = items, status_code = 200)
    except ValueError as e:
        raise HTTPException(status_code=404, detail = str(e))

@routers.get('/getusertotal')
def getusertotal(userid: int) -> JSONResponse:
    try:
        total = get_total_price_of_basket(userid)
        return JSONResponse(content = total, status_code = 200)
    except ValueError as e:
        raise HTTPException(status_code=404, detail = str(e))



