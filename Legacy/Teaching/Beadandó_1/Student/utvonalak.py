from fastapi import APIRouter, HTTPException
from typing import List
from .modellek import Kurzus, Valasz
from .fajl_kezeles import KurzusFajlKezelo

utvonal = APIRouter()

fajl_kezelo = KurzusFajlKezelo()

# 1. GET Az összes kurzus lekérdezése, 1 pont
@utvonal.get("/kurzusok", response_model=List[Kurzus])
async def get_osszes_kurzus():
    k = fajl_kezelo.kurzusok_olvasas()
    return k
    #return fajl_kezelo.kurzusok_olvasas()



# 2. POST Új kurzus hozzáadása, 2 pont
@utvonal.post("/kurzusok", response_model=Valasz)
async def uj_kurzus(kurzus: Kurzus):

    kurzusok = fajl_kezelo.kurzusok_olvasas()
    
    #A Következő két sor nem része a feladatnak (lásd a kiírást), de ha máshol vesztett pontot a hallgató, akkor 0,25 pont adható rá bónuszként.
    '''if not isinstance(kurzus.id, int) or kurzus.id < 1:
       raise HTTPException(status_code=400, detail="A kurzus id mezője kötelező pozitív egész szám")    '''

    for elem in kurzusok:
        if elem["id"] == kurzus.id:
            raise HTTPException(status_code=400, detail="Ez a kurzus id már foglalt")

    kurzusok.append(kurzus.model_dump())  

    fajl_kezelo.kurzusok_iras(kurzusok)
    return Valasz(uzenet = "Sikeres felvétel")



# 3. GET Kurzusok szűrése pontosan egy kiválasztott tulajdonság alapján, 2 pont (több szűrési lehetőség is megadható, de csak a sorrendben elsőt vesszük figyelembe)
@utvonal.get("/kurzusok/filter", response_model=List[Kurzus])
async def get_kurzusok_filter(nap_idopont: str = None, oktato_email: str = None, tipus: str = None, evfolyam: int = None, helyszin: str = None, max_letszam: int = None):
    k = fajl_kezelo.kurzusok_olvasas()

    filt_lista = [nap_idopont, oktato_email, tipus, evfolyam, helyszin, max_letszam]
    db = len([x for x in filt_lista if x is not None])
    if db != 1:
        raise HTTPException(status_code=400, detail="Pontosan egy szűrési feltételt kell megadni")

    kurzusok = []
    for elem in k:
        if nap_idopont is not None and elem["nap_idopont"] == nap_idopont:
            kurzusok.append(elem)
        elif oktato_email is not None and elem["oktato"]["email"] == oktato_email:
            kurzusok.append(elem)
        elif tipus is not None and elem["tipus"] == tipus:
            kurzusok.append(elem)
        elif evfolyam is not None and elem["evfolyam"] == evfolyam:
            kurzusok.append(elem)
        elif helyszin is not None and elem["helyszin"] == helyszin:
            kurzusok.append(elem)
        elif max_letszam is not None and elem["max_letszam"] == max_letszam:
            kurzusok.append(elem)
    return kurzusok



# 4. GET Kurzusok szűrése pontosan két tulajdonság alapján, 3 pont (A pontosan két feltételt ellenőrizzük)
@utvonal.get("/kurzusok/filters", response_model=List[Kurzus])
async def get_kurzusok_filters(nap_idopont: str = None, oktato_email: str = None, tipus: str = None, evfolyam: int = None, helyszin: str = None, max_letszam: int = None):
    k = fajl_kezelo.kurzusok_olvasas()

    filterek = {"nap_idopont": nap_idopont, "oktato_email": oktato_email, "tipus": tipus, "evfolyam": evfolyam, "helyszin": helyszin, "max_letszam": max_letszam}
    db = len([x for x in filterek.values() if x is not None])
    if db != 2:
        raise HTTPException(status_code=400, detail="Pontosan két szűrési feltételt kell megadni")
    
    felt = [x for x in filterek if filterek[x] is not None]   #ez a két kiválasztott feltétel neveinek listája 
    kurzusok = []
    for elem in k:
        if oktato_email is not None:
            if elem["oktato"]["email"] == oktato_email:
                if (felt[0] == "oktato_email" and elem[felt[1]] == filterek[felt[1]]) or (felt[1] == "oktato_email" and elem[felt[0]] == filterek[felt[0]]):
                    kurzusok.append(elem)   
    return kurzusok



# 5. PUT Kurzus módosítása azonosító alapján (1.mo.), 2 pont
@utvonal.put("/kurzusok/{kurzus_id}", response_model=Kurzus)
async def update_kurzus(kurzus_id: int, kurzus: Kurzus):
    k = fajl_kezelo.kurzusok_olvasas()   
    for i, elem in enumerate(k):
        if elem["id"] == kurzus_id:
            kurzus.id = kurzus_id
            k[i] = kurzus.model_dump()
            fajl_kezelo.kurzusok_iras(k)
            return kurzus
    raise HTTPException(status_code=404, detail="A kurzus nem létezik")


'''
# 5. PUT Kurzus módosítása azonosító alapján (2.mo.), 2 pont
@utvonal.put("/kurzusok/{kurzus_id}", response_model=Kurzus)
async def update_kurzus(kurzus_id: int, kurzus: Kurzus):
    k = fajl_kezelo.kurzusok_olvasas()
    for elem in k:
        if elem["id"] == kurzus_id:
            elem["nev"] = kurzus.nev
            elem["tipus"] = kurzus.tipus
            elem["evfolyam"] = kurzus.evfolyam
            elem["nap_idopont"] = kurzus.nap_idopont
            elem["helyszin"] = kurzus.helyszin
            elem["oktato"]["nev"] = kurzus.oktato.nev
            elem["oktato"]["email"] = kurzus.oktato.email
            for i in range(len(kurzus.hallgatok)):
                if i < len(elem["hallgatok"]):
                    elem["hallgatok"][i]["id"] = kurzus.hallgatok[i].id
                    elem["hallgatok"][i]["nev"] = kurzus.hallgatok[i].nev
                    elem["hallgatok"][i]["email"] = kurzus.hallgatok[i].email
                else:
                    elem["hallgatok"].append({
                        "id": kurzus.hallgatok[i].id,
                        "nev": kurzus.hallgatok[i].nev,
                        "email": kurzus.hallgatok[i].email
                    })
            elem["max_letszam"] = kurzus.max_letszam
            fajl_kezelo.kurzusok_iras(k)
            return elem
    raise HTTPException(status_code=404, detail="Kurzus nem létezik")
'''


# 6. GET Hallgató kurzusainak lekérdezése hallgató azonosító alapján, 2 pont
@utvonal.get("/kurzusok/hallgatok/{hallgato_id}", response_model=List[Kurzus])
async def get_hallgato_kurzusai(hallgato_id: int):
    k = fajl_kezelo.kurzusok_olvasas()
    kurzusok = []
    for elem in k:
        for hallgato in elem["hallgatok"]:
            if hallgato["id"] == hallgato_id:
                kurzusok.append(elem)
    if len(kurzusok) == 0:
        raise HTTPException(status_code=404, detail="A hallgató id nem létezik")
    return kurzusok
    


# 7. DELETE Adott azonosítójú kurzus törlése, 1 pont
@utvonal.delete("/kurzusok/{kurzus_id}")
async def delete_kurzus(kurzus_id: int):
    k = fajl_kezelo.kurzusok_olvasas()
    van_kurzus = False
    for elem in k:
        if elem["id"] == kurzus_id:
            van_kurzus = True
            k.remove(elem)
            fajl_kezelo.kurzusok_iras(k)
    if not van_kurzus:
        raise HTTPException(status_code=404, detail="A kurzus nem létezik")
    return



# 8. GET Hallgató kurzuson való részvételének ellenőrzése, 2 pont
@utvonal.get("/kurzusok/{kurzus_id}/hallgatok/{hallgato_id}", response_model=Valasz)
async def get_hallgato_kurzuson(kurzus_id: int, hallgato_id: int):
    k = fajl_kezelo.kurzusok_olvasas()
    van_kurzus = False
    for elem in k:
        if elem["id"] == kurzus_id:
            van_kurzus = True
            for hallgato in elem["hallgatok"]:
                if hallgato["id"] == hallgato_id:
                    Valasz.uzenet = "Igen"
                    return Valasz
    if not van_kurzus:
        raise HTTPException(status_code=404, detail="A kurzus nem létezik")
    return Valasz(uzenet="Nem")
