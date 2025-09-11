# Feladat 7: Definiálj egy generátort ami a fibonacci sorozat következő elemét generálja     

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fibonacci_generator = fibonacci_generator()
for _ in range(10):
    print(next(fibonacci_generator))

#----------------------------------------------

# Feladat 8: Készíts egy függvényt ami ismeretlen számú számot vár paraméterként, és visszaadja a számok összegét
def sum_numbers(*args):
    return sum(args)

# Feladat 9: Készíts egy függvényt ami ismeretlen számú név szerinti paramétert vár, kiírja azokat, majd visszaadja a paraméterek számát

def print_and_return_number_of_parameters(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    return len(kwargs)

print(f"Paraméterek száma: {print_and_return_number_of_parameters(a=1, b=2, c=3)}")

# Készítsd el a "játékos" osztályt egy új file-ban, ami a következő metódusokkal rendelkezik:
# - __init__: inicializálja a játékos nevét, pontszámát és életét
# - add_points: adott pontszámot ad a játékoshoz
# - remove_points: adott pontszámot vesz el a játékostól
# - add_life: életet ad a játékoshoz
# - remove_life: életet vesz el a játékostól
# - get_score: visszaadja a játékos pontszámát
# - get_lives: visszaadja a játékos életét
# - get_name: visszaadja a játékos nevét
# - is_dead: visszaadja, hogy a játékos élete >= 0-e
# - __str__: visszaadja a játékos nevét és pontszámát
# - __del__: kiírja, hogy a játékos objektumot törölték
# - __eq__: összehasonlítja két játékos pontszámát
# - attack_other_player: egy statikus metódus ami két játékost kap paraméterül és meghívja az egyik játékos remove_life metódusát a másik játékos pontszáma alapján
# - bónusz feladat, kezeld az esetlegesen adódó hibákat; pl: rossz típusú paraméterek, negatív pontszámok, stb.

class Jatekos:
    def __init__(self, nev, pontszam=0, elet=3):
        self.nev = nev
        self.pontszam = pontszam
        self.elet = elet

    def add_points(self, points):
        if not isinstance(points, int) or points < 0:
            raise ValueError("A pontszámnak pozitív egész számnak kell lennie.")
        self.pontszam += points

    def remove_points(self, points):
        if not isinstance(points, int) or points < 0:
            raise ValueError("A pontszámnak pozitív egész számnak kell lennie.")
        self.pontszam -= points

    def add_life(self):
        self.elet += 1

    def remove_life(self):
        if self.elet > 0:
            self.elet -= 1
        else:
            raise ValueError("A játékosnak nincs több élete.")

    def get_score(self):
        return self.pontszam

    def get_lives(self):
        return self.elet

    def get_name(self):
        return self.nev

    def is_dead(self):
        return self.elet <= 0

    def __str__(self):
        return f"{self.nev}: {self.pontszam} pont"

    def __del__(self):
        print(f"A(z) {self.nev} játékos objektumot törölték")

    def __eq__(self, other):
        if isinstance(other, Jatekos):
            return self.pontszam == other.pontszam
        return False
    
    def __lt__(self, other):
        if isinstance(other, Jatekos):
            return self.pontszam < other.pontszam
        return False

    @staticmethod
    def attack_other_player(player1, player2):
        if not isinstance(player1, Jatekos) or not isinstance(player2, Jatekos):
            raise ValueError("Mindkét paraméternek Jatekos típusúnak kell lennie.")
        player2.remove_life()


a = Jatekos("A", pontszam=5)
b = Jatekos("B", pontszam=10)

print(a == b)
print(a < b)
print(list(sorted([a,b])))