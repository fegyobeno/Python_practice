from colored import fg, attr
import random

class Kerdes:
    def __init__(self, kerdes, valaszok, helyes_valaszok):
        self.kerdes = kerdes
        self.valaszok = valaszok
        self.helyes_valaszok = helyes_valaszok

def print_kerdes(kerdesek):
    osszes_kerdes = list_to_quiz(kerdesek)
    num_of_q = len(osszes_kerdes)
    num_of_helyes_valasz = 0
    while osszes_kerdes != []:
        random.shuffle(osszes_kerdes)
        jelenlegi_kerdes = osszes_kerdes[-1]

        print(jelenlegi_kerdes.kerdes)
        for i in range(len(jelenlegi_kerdes.valaszok)):
            print(f"{i+1}. {jelenlegi_kerdes.valaszok[i][1:]}")

        tipp = input("Tipp: ")
        if jelenlegi_kerdes.helyes_valaszok[int(tipp)-1]:
            print(f"{fg("green")}Helyes valasz!\n{attr('reset')}")
            num_of_helyes_valasz += 1
        else:
            print(f"{fg("red")}Helytelen valasz!\n{attr('reset')}")
        osszes_kerdes.pop()

    print(f"Eredmény: {num_of_helyes_valasz}/{num_of_q}")

def create_quiz(file_name):
    kerdesek = []
    q_sum = input("Hány kérdést szeretne a kvízbe?: ")
    for i in range(int(q_sum)):
        num_of_q,num_of_a = 1,0
        question = input(f"Adja meg az {num_of_q}. kérdését: ")
        kerdesek.append(f"{num_of_q}, {question}")
        while num_of_a < 4:
            print(f"Adja meg az {num_of_q}. kérdés {num_of_a+1}. válaszát (*valasz|False formátumban): ")
            valasz = input()
            kerdesek.append(valasz)
            num_of_a += 1
    with open(file_name, "w") as f:
        for k in kerdesek:
            f.write(f"{k}\n")
    print(f"Kviz sikeresen mentve {file_name}.txt néven!")

def list_to_quiz(kerdesek):
    valaszok,helyes_valaszok,num_of_q,osszes_kerdes = [], [], 1, []
    num_of_q = 1
    for k in range(len(kerdesek)):
        if kerdesek[k][0] == str(num_of_q):
            for i in range(1,5):
                valaszok.append(kerdesek[k+i].split("|")[0])
                helyes_valaszok.append(True if kerdesek[k+i].split("|")[1].strip() == "True" else False)
            osszes_kerdes.append(Kerdes(kerdesek[k], valaszok, helyes_valaszok))
            valaszok, helyes_valaszok = [], []
            num_of_q += 1
    return osszes_kerdes

option = 9
while option != "0":
    print("1 - Kviz létrehozása")
    print("2- Kvíz betöltése:")
    print("0. Kilepés")
    option = input("Válasszon a menüpontok közül:  ")

    if(option == "1"):
        q_name = input("Adja meg a kviz file kívánt nevét: ")
        create_quiz(q_name + ".txt")
        break
    elif(option == "2"):
        file = input("Adja meg a file nevét/helyét: (pl.: kerdesek, csak txt file lehet):  ")
        try:
            with open(file+".txt", "r") as f:
                kerdesek = f.readlines()
            print_kerdes(kerdesek)
        except:
            print("Helytelen file!")
        break
    

    
