
"Szakácsképző Intézmény" FastAPI projektje

Ez egy FastAPi alkalmazás, amelyik egy Szakácsképző Intézmény kurzusait, oktatóit és hallgatóit tartja nyilván:
   Kurzusok: azonosítószám, név, típus (ea, gyak), évfolyam(1,2,3), oktató, terem száma, nap-időpont, hallgatók, max. létszám
   Kurzus név: Előételek, Levesek, Sülthúsok, Főzelékek, Köretek, Saláták, Desszertek, …
   Hallgatók: azonosítószám, név, email
   Oktató: név, email

A kurzusok.json fájlban jelenleg egy példa szerepel. 
A modellek.py fájl tartalmazza az osztályok atribútumait és azok típusait.
A fájl_kezelés.py fájlban a kurzusok.json fájl olvasása és írása szerepel. Ezeket a metódusokat kell felhasználni az útvonalak.py hiányzó metódusainak megírásakor.
(Részletesen le fogom írni az egyes metódusok szerepét.)

Az alkalmazás futtatása:
1. Nyisd meg a Beadandó_1 mappát 

2. Az uvicorn modul telepítése:
pip install uvicorn

3. Futtasd a kódot a terminálban a következő paranccsal:
python app_sz/main_próba.py

4. A böngésző címsorába írd be a következő URL-t:
http://127.0.0.1:8000/docs

5. A kapott interaktív felületen tudod tesztelni az egyes API végpontokat.

6. Az útvonalak.py fájlban a pass utasítások helyére implementáld a megfelelő metódusokat. Alkalmazz mindenhol kivételkezelést a felmerülő exeption-ok esetén: 
pl. raise HTTPException(status_code=404, detail="Hallgató nem található.")








