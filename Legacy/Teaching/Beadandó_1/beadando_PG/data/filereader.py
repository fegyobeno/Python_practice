import json
import os
from typing import Dict, Any, List

'''
Útmutató a féjl használatához:

Felhasználó adatainak lekérdezése:

user_id = 1
user = get_user_by_id(user_id)
print(f"Felhasználó adatai: {user}")

Felhasználó kosarának tartalmának lekérdezése:

user_id = 1
basket = get_basket_by_user_id(user_id)
print(f"Felhasználó kosarának tartalma: {basket}")

Összes felhasználó lekérdezése:

users = get_all_users()
print(f"Összes felhasználó: {users}")

Felhasználó kosarában lévő termékek összárának lekérdezése:

user_id = 1
total_price = get_total_price_of_basket(user_id)
print(f"A felhasználó kosarának összára: {total_price}")

Hogyan futtasd?

Importáld a függvényeket a filehandler.py modulból:

from filereader import (
    get_user_by_id,
    get_basket_by_user_id,
    get_all_users,
    get_total_price_of_basket
)

 - Hiba esetén ValuErrort kell dobni, lehetőség szerint ezt a 
   kliens oldalon is jelezni kell.

'''

# A JSON fájl elérési útja
JSON_FILE_PATH = os.path.join(os.path.dirname(__file__), "data.json")

def load_json() -> Dict[str, Any]:
    with open(JSON_FILE_PATH, "r", encoding="utf-8") as f:
        ## Dict[str, List[Dict[str, Any]]]
        data = json.load(f)
    return data

def get_user_by_id(user_id: int) -> Dict[str, Any]:
    data = load_json()
    for user in data["Users"]:
        if user["id"] == user_id:
            return user
    raise ValueError("User not found!")

# name is confusing, we return a list of items here actually
def get_basket_by_user_id(user_id: int) -> List[Dict[str, Any]]:
    data = load_json()    
    for basket in data["Baskets"]:
        if basket["user_id"] == user_id:
            return basket["items"]
    raise ValueError("No basket found for user, or no user found!")

def get_basket_id_by_user_id(user_id: int) -> int:
    data = load_json()
    for basket in data["Baskets"]:
        if basket["user_id"] == user_id:
            return basket["id"]
    raise ValueError("no basket id found based on this user id")


def get_all_users() -> List[Dict[str, Any]]:
    data = load_json()
    return data["Users"]

def get_total_price_of_basket(user_id: int) -> float:
    data = load_json()
    result = 0
    found = False

    for basket in data["Baskets"]:
        if basket["user_id"] == user_id:
            found = True
            for item in basket["items"]:
                result += (item["price"] * item["quantity"])

    if not found:
        raise ValueError("No basket found for user or no user with that id exists!")

    return result

def get_current_highest_ids() -> List[int]:
    data = load_json()
    result = [100,200] # item ids start at 200, basket ids at 100, so these work as good min values
    for basket in data["Baskets"]:
        if (result[0] < basket["id"]): 
            result[0] = basket["id"]
        for item in basket["items"]:
            if (result[1] < item["item_id"]):
                result[1] = item["item_id"]
    return result    



