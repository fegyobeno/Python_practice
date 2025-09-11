Kvíz alkalmazás

A feladat egy olyan Kvíz alkalmazás létrehozása, ami parancssorban fut. 
Egy kvíz kérdésekből áll amelyekre egy vagy több jó válasz adható. A kérdéseket a program véletlenszerű sorrendben teszi fel, majd a válaszadás után színes (colored library) visszajelzést ad a válasz helyességéről. A válaszokat felhasználó az adott válaszlehetőség számának megnyomásával tudja kiválasztani. 
A kvíz kitöltése után az alkalmazás értékelje a felhasználó teljesítményét.

Kvízt két féle módon lehet létrehozni, manuálisan kérdések és válaszok megadásával, vagy szöveges fájlból beolvasva. 
Olyan szöveges fájlból kell tudnia kérdés-válasz halmazokat beolvasni amelyek a következő formátumúak:
1, kérdés
*válasz1|True
*válasz2|False
*válasz3|True
*válasz4|False

A True-k száma meghatározza kérdésre adható helyes válaszok számát. 

Legyen lehetőség a létrehozott Kvízek mentésére és a már mentett kvízek betöltésére. 