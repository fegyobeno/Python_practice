from fastapi import APIRouter, HTTPException
from typing import List
from .modellek import Kurzus, Valasz
from .fajl_kezeles import KurzusFajlKezelo

utvonal = APIRouter()

fajl_kezelo = KurzusFajlKezelo()

@utvonal.get("/kurzusok", response_model=List[Kurzus])
async def get_osszes_kurzus():
    k = fajl_kezelo.kurzusok_olvasas()
    return k
    #return fajl_kezelo.kurzusok_olvasas()

@utvonal.get("/kurzusok/filter", response_model=List[Kurzus])
async def get_kurzusok_filter(nap_idopont: str = None, oktato: str = None, tipus: str = None, evfolyam: str = None, helyszin: str = None, max_letszam: int = None):
    pass

@utvonal.get("/kurzusok/{kurzus_id}", response_model=Kurzus)
async def get_kurzus_by_id(kurzus_id: int):
    pass

@utvonal.post("/kurzusok", response_model=Kurzus)
async def uj_kurzus(kurzus: Kurzus):

    kurzusok = fajl_kezelo.kurzusok_olvasas()
    
    if not kurzus.id:
        raise HTTPException(status_code=400, detail="A kurzus id mezője kötelező")

    for elem in kurzusok:
        if elem["id"] == kurzus.id:
            raise HTTPException(status_code=400, detail="Ez a kurzus id már foglalt")

    kurzusok.append(kurzus.dict())  # Convert Event object to dictionary before appending

    fajl_kezelo.kurzusok_iras(kurzusok)
    return kurzus
    
@utvonal.put("/kurzusok/{kurzus_id}", response_model=Kurzus)
async def update_kurzus(kurzus_id: int, kurzus: Kurzus):
    pass

@utvonal.delete("/kurzusok/{kurzus_id}")
async def delete_kurzus(kurzus_id: int):
    pass

@utvonal.get("/kurzusok/hallgatok/{hallgato_id}", response_model=Kurzus)
async def get_hallgato_kurzusai(hallgato_id: int):
    pass

@utvonal.get("/kurzusok/{kurzus_id}/hallgatok/{hallgato_id}", response_model=Valasz)
async def get_hallgato_kurzuson(kurzus_id: int, hallgato_id: int):
    pass
