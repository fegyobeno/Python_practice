# Struktúrált adatok: táblázatok, adatbázisok
# Struktúrálatlan adatok: szöveges fájlok, képek, videók

# Az adatok exponenciálian nőnek, PL: indiaiak jó reggelt üzenetei

# BIG Data: olyan adathalmaz amely túl nagy ahhoz, hogy hagyományos módszerekkel vagy belátható időn belül fel lehessen dolgozni
# Az 5V jellemzője:
# Volume: mennyiség
# Velocity: sebesség
# Variety: változatosság
# Veracity: hitelesség
# Value: érték

#Open Data: mindenki számára hozzáférhető
#Private Data: csak bizonyos személyek számára hozzáférhető

# Az adatelemzési folyamat:
# 1. Adatgyűjtés
# 2. Adattisztítás
# 3. Adatmodellezés
# 4. Adatvizualizáció
# 5. Értelmezés
# 6. Döntéshozatal

# Python adatelemzési könyvtárak: numpy, pandas, matplotlib, seaborn, scikit-learn, tensorflow, keras

#Az amelyikeket a gyakorlaton használunk:
# Numpy: Numerical Python, tömbökkel és mátrixokkal dolgozik
# Pandas: adatok kezelésére, manipulálására és elemzésére használják

import numpy as np
import pandas as pd


# Numpy - tömbök x dimenziósak lehetnek, hatékony linalhoz
array = np.array([1, 2, 3, 4, 5])
print(f"Array: {array}")

matrix = np.array([[1,2,3],[4,5,6]], ndmin=2)
print(f"Matrix:\n{matrix}")

# Alapvető műveletek
print(f"Összeg: {np.sum(array)}")

print(f"Átlag: {np.mean(array)}")

print(f"Legnagyobb elem: {np.max(array)}")

print(f"Legkisebb elem: {np.min(array)}")

print(f"Elemek szorzata: {np.prod(array)}")

#Mártrixra

print(f"Összeg: {np.sum(matrix)}")

print(f"Átlag: {np.mean(matrix)}")

print(f"Legnagyobb elem: {np.max(matrix)}")

print(f"Legkisebb elem: {np.min(matrix)}")

print(f"Elemek szorzata: {np.prod(matrix)}")


# Pandas - egydimenziós adatsorok
series = pd.Series([1, 2, 3, 4, 5])

print(series)

indexes = ['a', 'b', 'c', 'd', 'e']
series = pd.Series([1, 2, 3, 4, 5], index=indexes) # nem feltétlen kell nullától indexelni

print(series)

# Pandas - kétdimenziós adatsorok
df = pd.DataFrame({
    'numbers': series,
    'letters': indexes
})

print(df)

data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [24, 25, 26],
    'city': ['Budapest', 'Debrecen', 'Szeged']
}


df = pd.DataFrame(data)
print(df)

#első sor adatai
print(df.iloc[0])

# age oszlop
print(df['age'])
print('---------------------------------------------------------')

jegyek = pd.Series([5, 4, 3, 5, 2, 3, 4, 5], index=['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Helen'])

print(jegyek['Alice'])

print(f"Név: {jegyek.index[0]}, Jegy: {jegyek.values[0]}")

# Itt jön a part2 pandas ipynb

#----->
# folytatás
