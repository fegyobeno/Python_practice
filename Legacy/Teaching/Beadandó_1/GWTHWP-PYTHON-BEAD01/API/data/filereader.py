import json
from typing import Dict, Any, List
import os

JSON_FILE_PATH = os.path.join(os.path.dirname(__file__), "data.json")


def load_json() -> Dict[str, Any]:
    try:
        with open(JSON_FILE_PATH, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        raise ValueError("Nincs ilyen fájl")


def get_user_by_id(user_id: int) -> Dict[str, Any]:
    data = load_json()
    user = findItemById(data, user_id, "Users", "id", True)
    if not user:
        raise ValueError(f"Ezzel az id-val: {user_id} nem létezik felhasználó")
    return user


def get_basket_by_user_id(user_id: int) -> List[Dict[str, Any]]:
    data = load_json()
    basket = findItemById(data, user_id, "Baskets", "user_id", True)
    if not basket:
        raise ValueError(
            f"Ezzel az id-val rendelkező felhasználónak {user_id} nincs kosara"
        )
    return basket["items"]


def get_all_users() -> List[Dict[str, Any]]:
    return load_json()["Users"]


def get_total_price_of_basket(user_id: int) -> float:
    basketItems = get_basket_by_user_id(user_id)
    totalPriceOfBasketItems = sum(
        item["price"] * item["quantity"] for item in basketItems
    )
    return totalPriceOfBasketItems


def findItemById(data: Dict[str, Any],id: int, key: str, itemKey: str, raiseError: bool) -> Dict[str, Any]:
    item = next((item for item in data[key] if item[itemKey] == id), None)
    if not item and raiseError:
        raise ValueError(f"Ezzel az id-val: {id} nem létezik elem")
    return item
