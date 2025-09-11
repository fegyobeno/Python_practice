import json
from typing import Dict, Any
import os
import math

JSON_FILE_PATH = os.path.join(os.path.dirname(__file__), "data.json")


def load_json() -> Dict[str, Any]:
    with open(JSON_FILE_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


def save_json(data: Dict[str, Any]) -> None:
    with open(JSON_FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def add_user(newUser: Dict[str, Any]) -> None:
    data = load_json()
    if isItemExistsWithThisId(newUser["id"], data, "Users"):
        raise ValueError(f"Ezzel az id-val: {newUser['id']} már létezik felhasználó")
    save("Users", newUser, data)


def add_basket(newBasket: Dict[str, Any]) -> None:
    data = load_json()
    if not isItemExistsWithThisId(newBasket["user_id"], data, "Users"):
        raise ValueError(
            f"Nincs ezzel az id-val: {newBasket['user_id']} felhasználó létrehozva"
        )
    if isItemExistsWithThisId(newBasket["id"], data, "Baskets"):
        raise ValueError(f"Ezzel az id-val rendelkező usernek: {math.floor(newBasket['id'] / 100)} már létezik kosara")
    save("Baskets", newBasket, data)


def add_item_to_basket(user_id: int, item: Dict[str, Any]) -> None:
    data = load_json()
    basket = next(
        (basket for basket in data["Baskets"] if basket["user_id"] == user_id), None
    )
    if not basket:
        raise ValueError(
            f"Ezzel az id-val: {user_id} rendelkező felhasználónak nincsen kosara"
        )
    basket["items"].append(item)
    save_json(data)


def isItemExistsWithThisId(id: int, data: Dict[str, Any], key: str) -> bool:
    return any(item["id"] == id for item in data[key])


def save(key: str, newItem: Dict[str, Any], data: Dict[str, Any]) -> None:
    data[key].append(newItem)
    save_json(data)
