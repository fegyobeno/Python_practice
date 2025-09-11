import random
import csv
import json

#Hozzátok létre az Employee osztályt aminek két adattagja van a Név és a Fizetés

#Írjatok egy generátor függvényt ami véletlenszerűen generál dolgozókat, olyan módon, 
# hogy a fizetésük 70 százalékban 1875 és 5000 között legyen, a maradék 30%-ban pedig None

#Írjatok egy függvényt, ami egy employees.txt szöveges fájlban eltárol 100 véletlenszerűen generált dolgozót

#Írjatok egy függvényt ami beolvassa az employees.txt fájlt kiszűri az összes None fizetésű dolgozót és kiírja egy employees_no_none.csv fájlba
# Name, Salary fejléccel

# Olvassátok be az employees_no_none.csv fájlt, minden dolgozóhoz rendeljetek hozzá egy véletlenszerű pozíciót a következők közül:
# ['Manager', 'Developer', 'QA', 'DevOps', 'HR', 'Sales', 'Marketing', 'Finance', 'Support', 'Intern'] -majd az így kapott dolgozókat
# írjátok ki egy employees_with_position.json fájlba
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

def employee_generator():
    names = ["John", "Jane", "Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Hank"]
    while True:
        name = random.choice(names)
        salary = random.choice([random.randint(1875, 5000) if random.random() < 0.7 else None for _ in range(1)])
        yield Employee(name, salary)

def generate_employees_file():
    employees = [next(employee_generator()) for _ in range(100)]
    with open('employees.txt', 'w') as file:
        for emp in employees:
            file.write(f"{emp.name},{emp.salary}\n")

def filter_and_save_employees():
    with open('employees.txt', 'r') as file:
        employees = [line.strip().split(',') for line in file.readlines()]
    filtered_employees = [emp for emp in employees if emp[1] != 'None']
    with open('employees_no_none.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Salary'])
        writer.writerows(filtered_employees)

def assign_positions_and_save():
    positions = ['Manager', 'Developer', 'QA', 'DevOps', 'HR', 'Sales', 'Marketing', 'Finance', 'Support', 'Intern']
    with open('employees_no_none.csv', 'r') as file:
        reader = csv.DictReader(file)
        employees = [row for row in reader]
    for emp in employees:
        emp['Position'] = random.choice(positions)
    with open('employees_with_position.json', 'w') as file:
        json.dump(employees, file, indent=4)

if __name__ == "__main__":
# Generate employees file
    generate_employees_file()

# Filter and save employees without None salary
    filter_and_save_employees()

# Assign positions and save to JSON
    assign_positions_and_save()