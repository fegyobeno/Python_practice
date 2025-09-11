import random
from colored import fg, attr

def betolt_fajlbol(fajlnev):
    kerdesek = []
    try:
        with open(fajlnev, 'r', encoding='utf-8') as fajl:
            sorok = fajl.readlines()
            kerdes = None
            valaszok = []

            for sor in sorok:
                sor = sor.strip()
                if sor.startswith('*'):
                    valasz, helyes = sor[1:].rsplit('|', 1)
                    valaszok.append((valasz.strip(), helyes.strip().lower() == 'true'))
                elif sor:
                    if kerdes:
                        kerdesek.append({"kerdes": kerdes, "valaszok": valaszok})
                    kerdes = sor.split(',', 1)[1].strip()
                    valaszok = []

            if kerdes:
                kerdesek.append({"kerdes": kerdes, "valaszok": valaszok})

    except FileNotFoundError:
        print(f"Hiba: A(z) '{fajlnev}' fajl nem talalhato.")
    return kerdesek

def mentes_fajlba(fajlnev, kerdesek):
    try:
        with open(fajlnev, 'w', encoding='utf-8') as fajl:
            for i, k in enumerate(kerdesek, start=1):
                fajl.write(f"{i}, {k['kerdes']}\n")
                for valasz, helyes in k['valaszok']:
                    fajl.write(f"*{valasz}|{'True' if helyes else 'False'}\n")
        print(f"Kviz elmentve a(z) '{fajlnev}' fajlba.")
    except Exception as e:
        print(f"Hiba: {e}")

def uj_kerdes_hozzaadasa(kerdesek):
    kerdes = input("Add meg a kerdest: ").strip()
    valaszok = []
    print("Add meg a valaszokat es jelold meg, hogy helyesek-e. Ird be, hogy 'kesz', ha vegeztel.")
    while True:
        valasz = input("Valasz: ").strip()
        if valasz.lower() == 'kesz':
            break
        helyes = input("Ez a valasz helyes? (igen/nem): ").strip().lower() == 'igen'
        valaszok.append((valasz, helyes))
    kerdesek.append({"kerdes": kerdes, "valaszok": valaszok})

def kviz_inditasa(kerdesek):
    if not kerdesek:
        print("Nincsenek kerdesek. Adj hozza vagy tolj be egy kvizt.")
        return

    pontszam = 0
    random.shuffle(kerdesek)
    for k in kerdesek:
        print(f"\n{k['kerdes']}")
        opciok = k['valaszok']
        for i, (valasz, _) in enumerate(opciok, start=1):
            print(f"  {i}. {valasz}")

        felhasznalo_valaszai = input("Valaszd ki a helyes valasz szamait (vesszovel elvalasztva): ").strip()
        felhasznalo_valaszai = set(int(x) for x in felhasznalo_valaszai.split(',') if x.isdigit())
        helyes_valaszok = {i + 1 for i, (_, helyes) in enumerate(opciok) if helyes}

        if felhasznalo_valaszai == helyes_valaszok:
            print(f"{fg('green')}Helyes!{attr('reset')}")
            pontszam += 1
        else:
            print(f"{fg('red')}Hibas! A helyes valaszok: {', '.join(map(str, helyes_valaszok))}.{attr('reset')}")

    print(f"\nPontszam: {pontszam}/{len(kerdesek)}")

def menu():
    kerdesek = []
    while True:
        print("\n1. Kviz betoltese fajlbol")
        print("2. Kviz mentese fajlba")
        print("3. Uj kerdes hozzaadasa")
        print("4. Kviz inditasa")
        print("5. Kilepes")
        valasztas = input("Valassz egy lehetoseget: ").strip()

        if valasztas == '1':
            fajlnev = input("Add meg a fajl nevet: ").strip()
            kerdesek = betolt_fajlbol(fajlnev)
        elif valasztas == '2':
            fajlnev = input("Add meg a menteni kivant fajl nevet: ").strip()
            mentes_fajlba(fajlnev, kerdesek)
        elif valasztas == '3':
            uj_kerdes_hozzaadasa(kerdesek)
        elif valasztas == '4':
            kviz_inditasa(kerdesek)
        elif valasztas == '5':
            print("Viszlat!")
            break
        else:
            print("Ervenytelen valasztas, probald ujra.")

menu()
