import dis

# Demonstráció: változó létrehozása és azonosítója.
# A `id()` függvény visszaadja egy objektum egyedi azonosítóját (memória címét).
a = 10
print(id(a))

def add(a: int, b: int) -> int:
    """Egyszerű példa függvény: két egész összeadása.

    Tipikus anotációkat használunk: bemenetek egész számok (int),
    visszatérés is egész szám (int).
    """
    return a + b


# Közvetlen függvényhívás — eredmény kiírása.
# A print(add(3, 5)) meghívja az add függvényt és kiírja a visszatérési értéket (8).
print(add(3, 5))


# dis.dis() — a Python bytecode disassembler-e.
# dis.dis(add) kiírja az `add` függvény Python bytecode-át a terminálra.
# Fontos: a dis.dis függvény maga None-t ad vissza (visszatérési értéke None),
# ezért ha `print(dis.dis(add))`-ot írunk, előbb a disassembler kinyomtatja a
# bytecode-ot, majd a print kiírja a dis.dis visszatérési értékét (ami None lesz),
# így a kimeneten először látjuk a bytecode-ot, majd egy üres sorban `None`-t.
print(dis.dis(add))


print("----------------------------------------------")


# dis.dis("{}") — ha stringet adunk a dis.dis-nek, akkor a disassembler
# megpróbálja disassemblálni a string objektumot (azaz annak belső kódját),
# de általában nem hasznos értelmezhető bytecode-ot kapunk egy sima stringből.
# Itt csak demonstráljuk, hogy dis.dis elfogad más típusokat is, de eredménye
# nem ugyanaz, mint egy függvény vagy kódobjektum disassemblálásánál.
print(dis.dis("{}"))


print("----------------------------------------------")


# Példa a compile() és exec() használatára különböző módokban.
# compile(source, filename, mode) visszaad egy kódobjektumot.
# mode lehet: 'exec' (több utasítás), 'eval' (kifejezés), vagy 'single' (interaktív sor).
# A következő sor létrehoz egy kódobjektumot, ami egy print hívást tartalmaz,
# majd az exec lefuttatja azt — tehát a "Hello, world!" kiírásra kerül.
code = compile('print("Hello, world!")', '', 'exec')
exec(code)


print("----------------------------------------------")


# Ha mode='eval', a compile egy kifejezést vár (például `2+2` vagy `print(2+2)`).
# Az eval mód visszaad egy kifejezés eredményét, de fontos megjegyezni, hogy a
# `exec` függvény nem ad vissza értéket — itt azonban a kódobjektum egy `print`
# hívást tartalmaz, így a `print(2+2)` kiírja az eredményt (4) mielőtt az exec véget ér.
code = compile('print(2+2)', '', 'eval')
exec(code)


print("----------------------------------------------")


# mode='single' általában interaktív sorokra használatos: kifejezéseket és
# utasításokat is elfogad. Itt a forrás csak `2+2`, ami kifejezés; exec-hez
# átadva általában nincs közvetlen visszatérés, de a kódobjektum futtatása
# esetleg nem ír ki semmit, ha nincs print. (Ezt itt demonstráljuk: nincs print.)
code = compile('2+2', '', 'single')
exec(code)