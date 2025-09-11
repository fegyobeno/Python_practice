#Adatvizalizáció
# komplex adatok egyszerűsítése, ábrázolása
# adatok megjelenítése diagramokban, grafikonokban
# adatok vizuális elemzése
# mintázatok felismerése
# Hatékony kommunikáció

# Alapvető diagramm típőusok
# * Trendek figyelése, időbeli változások bemutatása – vonaldiagram
# • Adatok eloszlása – hisztogram, eloszlásgrafikon
# • Kapcsolatok azonosítása – scatter plot
# • Kiugró értékek felismerése – box plot, scatter plot
# • Adatok csoportos különbségei – oszlopdiagram, sávdiagram
# • Összegzés és részek megoszlása – kördiagram, halmozott diagram

# pip install matplotlib
import matplotlib.pyplot as plt
# Adatok generálása
latogatok = [120, 150, 180, 200, 170, 160, 140, 180, 190, 210, 190, 200] 
eladasok = [150, 180, 220, 240, 200, 230, 170, 190, 210, 250, 230, 220]

plt.scatter(latogatok, eladasok, color='orange')
plt.title('Látogatók száma és eladások közötti kapcsolat') 
plt.xlabel('Látogatók száma')
plt.ylabel('Eladások száma')
plt.grid(True) # vezetővonalak
plt.show() # megjelenítés

#v2
latogatok = [120, 150, 180, 200, 170, 160, 140, 180, 190, 210, 190, 200] 
eladasok = [150, 180, 220, 240, 200, 230, 170, 190, 210, 250, 230, 220]
# Scatter plot készítése
plt.plot(latogatok, eladasok, color='orange', marker='x', linestyle='None') #line style none miatt lesz scatter plot
# marker = 'x' kereszt jelölés marker = 'o' kör jelölés marker = 's' négyzet jelölés
plt.title('Látogatók száma és eladások közötti kapcsolat') 
plt.xlabel('Látogatók száma')
plt.ylabel('Eladások száma')
plt.grid(True)
plt.show()

# Vonaldiagram
# bemutat egy folyamatos változást
# időbeli változásokat, trendeket, összefüggéseket

speed = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 70, 50, 30, 30, 30]
time = [x for x in range(len(speed))]

plt.plot(time, speed, marker='o', linestyle='-', color='r')
# color = 'r' piros vonal color = 'g' zöld vonal color = 'b' kék vonal 
plt.title('Sebesség-idő diagram')
plt.xlabel('idő (s)')
plt.ylabel('sebesség (km/h)')
plt.grid(True)
plt.show()

#v2
plt.plot(time, speed, marker='s', color='g')
plt.title('Sebesség-idő diagram', fontsize=16, fontweight='bold', color='navy') 
plt.xlabel('idő (s)', fontsize=12, color='darkgreen')
plt.ylabel('sebesség (km/h)', fontsize=12, color='darkgreen') 
plt.xticks(rotation=45) # x tengely értékek elforgatása 
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.show()


speed.append(40)
time.append(len(time)+1)
acceleration = [(speed[i+1] - speed[i]) / (time[i+1] - time[i]) if time[i+1] != time[i] else 0 for i in range(len(speed)-1)]
speed.pop()
time.pop()
plt.figure(figsize=(12, 5))
# Első subplot
plt.subplot(1, 2, 1)  # 1 sor, 2 oszlop, 1. subplot 
plt.plot(time, speed, color='blue', marker='o') 
plt.title('Sebesség-idő diagram')
plt.xlabel('idő (s)')
plt.ylabel('sebesség (km/h)')
# Második subplot
plt.subplot(1, 2, 2)  # 1 sor, 2 oszlop, 2. subplot 
plt.plot(time, acceleration, color='red', marker='d') 
plt.title('Gyorsulás-idő diagram')
plt.xlabel('idő (s)')
plt.ylabel('Gyorsulás (km/h^2)')
plt.tight_layout() # Igazítás a helyes megjelenítéshez 
plt.show()

# Három diagram egy ábrán
hónapok = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII']
bevételek = [1000, 1200, 1300, 900, 1100, 1500, 1100, 1200, 1000, 900, 800, 1400] 
kiadások = [800, 900, 950, 870, 1000, 1200, 500, 900, 650, 1050, 700, 1000]  
plt.figure(figsize=(12, 12))
plt.subplot(2, 2, 1) # 1. diagram
plt.plot(hónapok, bevételek, marker='o', linestyle='-', color='b') 
plt.title('Cég havi bevételei')
plt.xlabel('Hónapok')
plt.ylabel('Bevétel (ezer Ft)')
plt.grid(True)
plt.subplot(2, 2, 2) # 2. diagram
plt.plot(hónapok, kiadások, marker='o', linestyle='-', color='r') 
plt.title('Cég havi kiadásai')
plt.xlabel('Hónapok')
plt.ylabel('Kiadás (ezer Ft)')
plt.grid(True)
plt.subplot(2, 2, 3) # 3. diagram 
plt.scatter(kiadások, bevételek, marker='o', color='b') 
plt.title('Kiadások és bevételek összefüggése') 
plt.xlabel('Kiadások (ezer Ft)')
plt.ylabel('Bevétel (ezer Ft)')
plt.grid(True)
plt.tight_layout() 
plt.show()

# Oszlopdiagram, hisztogram
import matplotlib.pyplot as plt
import pandas as pd
# Adatok generálása
eladasok = [150, 180, 220, 240, 200, 230, 170, 190, 210, 250, 230, 220]
# Hisztogram készítése
plt.hist(eladasok, bins=6, color='lightblue', edgecolor='black')  # bins = 6 oszlopok száma
plt.title('Napi eladások eloszlása')
plt.xlabel('Eladások száma')
plt.ylabel('Gyakoriság')
plt.grid(axis='y', linestyle='--', linewidth=0.5)
plt.show()

#Box plotok az adatok szórásának és kiugró értékeinek bemutatására. 
# Heti eladások adatai
heti_eladasok = [150, 180, 220, 240, 200, 230, 
 170, 190, 210, 250, 230, 220, 180, 195, 205] 
# Box plot készítése
plt.boxplot(heti_eladasok, patch_artist=True, 
    boxprops=dict(facecolor='lightgreen')) # patch_artist = True színes doboz, boxprops = dict(facecolor='lightgreen') doboz színe
plt.title('Heti eladások dobozábrája') 
plt.ylabel('Eladások száma')
plt.grid(axis='y', linestyle='--', linewidth=0.5) 
plt.show()
