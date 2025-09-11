import pandas as pd
import matplotlib.pyplot as plt
import random

data = pd.read_csv('eladas.csv')

days = data['date']
data['amount_of_sales'] = [random.randint(0, 1000) for i in range(len(data))]
sales = data['amount_of_sales']

#pyplottal
plt.plot(days, sales, marker='o', linestyle='-', color='purple') 
plt.title('Napi eladások')
plt.xlabel('Napok')
plt.ylabel('Eladások (db)')
plt.show()
print(data.head())

#pandas beépített plot függvényével
data.plot(x='date', y='amount_of_sales', kind='line', marker='o', color='green', title='Napi eladások') 
# kind = 'line' -> vonaldiagramm 
plt.xlabel('Napok')
plt.ylabel('Eladások (db)')
plt.grid(True)
plt.show()
# A beolvasott adatok megtekintése 
print(data.head())

# Oszlopdiagram készítése az eladások ábrázolására
data.plot(x='date', y='amount_of_sales', kind='bar', color='coral', title='Napi eladások oszlopdiagramon') 
# kind = 'bar' -> oszlopdiagramm
plt.xlabel('Napok')
plt.ylabel('Eladások (db)')
plt.show()

# Hisztogram készítése
data['amount_of_sales'].plot(kind='hist', bins=6, color='skyblue', title='Eladások eloszlása', edgecolor='black') 
plt.xlabel('Eladások száma')
plt.ylabel('Gyakoriság') 
plt.show()

data['visitors'] = [x - random.randint(int(x/10),int(x/5)) for x in data['amount_of_sales']]

# Scatter plot készítése a látogatók száma és eladások közötti kapcsolat ábrázolására 
data.plot(kind='scatter', x='visitors', y='amount_of_sales', color='red', title='Látogatók és eladások közötti kapcsolat') 
plt.xlabel('Látogatók száma')
plt.ylabel('Eladások (db)')
plt.show()

#kombinált adatok
# Kombinált diagram készítése
fig, ax1 = plt.subplots() # egy ábra és egy tengely létrehozása
# Első Y tengely: bevételek
ax1.plot(data['date'], data['amount_of_sales'], color='blue', marker='o', label='Bevétel') 
ax1.set_xlabel('Hónapok')
ax1.set_ylabel('Bevétel (ezer Ft)', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')
# Második Y tengely: látogatók száma
ax2 = ax1.twinx()
ax2.plot(data['date'], data['visitors'], color='red', marker='s', linestyle='--', label='Látogatók száma') 
ax2.set_ylabel('Látogatók száma', color='red')
ax2.tick_params(axis='y', labelcolor='red')
plt.title('Havi bevételek és látogatók száma')
fig.tight_layout()
plt.show()

# A plt.subplots() és a twinx() 
# metódusok segítségével két y 
# tengelyt hozhatunk létre, így 
# egy diagramon egyszerre két 
# különböző adatot 
# ábrázolhatunk.

data.to_csv('eladas_modositott.csv', index=False) # adatok mentése fájlba