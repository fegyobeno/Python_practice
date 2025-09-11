#A következő feleadatokat old meg ciklusok használata nélkül a LAB_1/lab_1_exercises.py alapján:

#1. Hozz létre egy listát, populáld fel általad választott elemekkel, majd írd ki a lista első és utolsó elemét.
l = [1, True, f"Alamafa{123*3}"]

print("Első elem:", l[0])
print("Utolsó elem:", l[-1])

#2. Írj egy függvényt, amely bemeneti paraméterként kap egy számot, és visszaadja annak a négyzetét.
def square(num : int) -> int:
    return num ** 2

#3. Hozz létre egy komplex számot, majd írd ki a valós és képzetes részét külön-külön.
complex_num = 3 + 4j
print("Valós rész:", complex_num.real)
print("Képzetes rész:", complex_num.imag)

#4. Írj egy függvényt ami kap egy szót és egy szótárat. Amenniyben a szó nem szerepel a kulcsok között, 
#   akkor add hozzá a szót a szótárhoz és rendelj hozzá egy értéket (pl. 1). Ha már szerepel, akkor növeld meg az értékét eggyel.
def update_word_count(word: str, word_dict: dict) -> None:
    if word not in word_dict:
        word_dict[word] = 1
    else:
        word_dict[word] += 1