#Hozzátok létre az Employee osztályt aminek két adattagja van a Név és a Fizetés

#Írjatok egy generátor függvényt ami véletlenszerűen generál dolgozókat, olyan módon, 
# hogy a fizetésük 70 százalékban 1875 és 5000 között legyen, a maradék 30%-ban pedig None

#Írjatok egy függvényt, ami egy employees.txt szöveges fájlban eltárol 100 véletlenszerűen generált dolgozót

#Írjatok egy függvényt ami beolvassa az employees.txt fájlt kiszűri az összes None fizetésű dolgozót és kiírja egy employees_no_none.csv fájlba
# Name, Salary fejléccel

# Olvassátok be az employees_no_none.csv fájlt, minden dolgozóhoz rendeljetek hozzá egy véletlenszerű pozíciót a következők közül:
# ['Manager', 'Developer', 'QA', 'DevOps', 'HR', 'Sales', 'Marketing', 'Finance', 'Support', 'Intern'] -majd az így kapott dolgozókat
# írjátok ki egy employees_with_position.json fájlba