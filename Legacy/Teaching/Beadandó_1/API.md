Szerver

1 Kérj be a felhasználótól ellenőrzötten egy számot, és a localhost azon a portján indíts el egy FastAPI szervert.
  Ha rossz az input legyen lekezelve a hiba és addig kérje be a számokat amíg nem kap egy valódi értéket.

2 Definiáld a gyökér végpontot ami ha kap paramétert, üdvözli a felhasználót, különben üdvözli az ismeretlen felhasználót

3 Hozz létre egy temprature osztályt amit a pydantic validál
 {temp float, unit string, location string, time datetime}

4 Hozz létre egy listát a hőmérsékletek tárolására

5 Hozz létre egy GET végpontot a hőmérséklet objektumok visszaadására, ami HTTPE hiblval tér vissza, ha nincs adat

6 Hozz létre egy POST végpontot egy új hőmérséklet objektum aszinkron hozzáadására

Kliens_1..n

1 Írj egy python szkriptet ami 2 másodpercenként küld egy Post kérést a FastAPI szervernek egy véletlenszerűen generált hőmérséklet   objektummal

ControlNode

2 Írj egy python scriptet ami egy get requesttel lekéri az összes eddigi mérést és matplotlibbel vizualizálja