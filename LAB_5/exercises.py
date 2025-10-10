# készíts egy osztályt ami baki felhasználókat ír le
# valamint egyet ami banki felhasználókat tárol
class BankAccount:
    pass
# Feladat:
# legyenek privát módon tárolva a következő változók:
# név email cím telefonszám bankszámlaszám egyenleg jelszó hash kódja
# ---> opcionálisan legyenek validálva példányosításkor
# mindegyikhez legyen egy getter és setter
# definiáld felül a __str__, __eq__, __lt__, __hash__ és del metódusokat

class Users:
    pass

# Feladat:
# egy privát szótárban legyenek eltárolva a felhasználók ahol a kulcs a BankAccount példány
# a value pedig egy felhasználónév + jelszó hash rendezett páros
# transaction method, a helyes bankszámlaszám jelszó párossal lehet pénzt felvenni valamint pénzt utalni
# close account method, törli egy felhasználó adatát a szótárból
# hitel: egy felhasználó kérhet hitelt, ebben az esetben eltárolásra kerül egy külön hitelezettek objektumban a tartozott összeggel
# valamint a felvett összeg rákerül a számlájára. A hitel a kamat() metódussal kamatozik (generátor) és a törleszt() metódussal törleszthető