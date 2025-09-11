import json
import os
from typing import Dict, Any, List


'''
Útmutató a fájl függvényeinek a használatához

Új felhasználó hozzáadása:

new_user = {
    "id": 4,  # Egyedi felhasználó azonosító
    "name": "Szilvás Szabolcs",
    "email": "szabolcs@plumworld.com"
}

Felhasználó hozzáadása a JSON fájlhoz:

add_user(new_user)

Hozzáadunk egy új kosarat egy meglévő felhasználóhoz:

new_basket = {
    "id": 104,  # Egyedi kosár azonosító
    "user_id": 2,  # Az a felhasználó, akihez a kosár tartozik
    "items": []  # Kezdetben üres kosár
}

add_basket(new_basket)

Új termék hozzáadása egy felhasználó kosarához:

user_id = 2
new_item = {
    "item_id": 205,
    "name": "Szilva",
    "brand": "Stanley",
    "price": 7.99,
    "quantity": 3
}

Termék hozzáadása a kosárhoz:

add_item_to_basket(user_id, new_item)

Hogyan használd a fájlt?

Importáld a függvényeket a filehandler.py modulból:

from filehandler import (
    add_user,
    add_basket,
    add_item_to_basket,
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

def save_json(data: Dict[str, Any]) -> None:
    with open(JSON_FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    return

def add_user(user: Dict[str, Any]) -> None:
    data = load_json()
    if "Users" not in data:
        data["Users"] = []
    for curr_user in data["Users"]:
        if curr_user["id"] == user["id"]:
            raise ValueError("User ID already exists! This value must be unique!")
    data["Users"].append(user)
    save_json(data)

def add_basket(basket: Dict[str, Any]) -> None:
    data = load_json()
    if "Users" not in data:
        raise ValueError("Basket cannot be added")
    if "Baskets" not in data:
        data["Baskets"] = []
    for existing_basket in data["Baskets"]:
        if existing_basket["user_id"] == basket["user_id"]:
            raise ValueError("Basket cannot be added, as this user already has a basket!")
    for user in data["Users"]:
        if user["id"] == basket["user_id"]:
            data["Baskets"].append(basket)
            save_json(data)
            return
    raise ValueError("Basket cannot be added, as corresponding user id not found in database!")

def add_item_to_basket(user_id: int, item: Dict[str, Any]) -> None:
    data = load_json()
    for basket in data["Baskets"]:
        if basket["user_id"] == user_id:
            basket["items"].append(item)
            save_json(data)
            return
    raise ValueError("No valid basket exists to add item to!")

def delete_item_from_basket(user_id: int, item_id: int) -> None:
    data = load_json()
    for basket in data["Baskets"]:
        if basket["user_id"] == user_id:
            items: List[Dict[str, Any]] = basket["items"]
            for item in items:
                if item["item_id"] == item_id:
                    items.remove(item)
                    save_json(data)
                    return
    raise ValueError("Item not found!")

def modify_item_in_basket(user_id: int, update_item: Dict[str,Any]) -> None:
    data = load_json()
    basket_found = False
    for basket in data["Baskets"]:
        if basket["user_id"] == user_id:
            basket_found = True
            for item in basket["items"]:
                if (item["item_id"]) == update_item["item_id"]:
                    item.update(update_item) # type: ignore
                    save_json(data)
                    return
    # if we found basket we did not find item, so we raise error on that. otherwise we state basket was not found
    if (basket_found):
        raise ValueError("Item was not found based on item id indicated! Nothing to update.")
    else:
        raise ValueError("No valid basket exists to modify item in!")
    