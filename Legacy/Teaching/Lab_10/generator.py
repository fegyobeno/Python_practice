class Worker:
    def __init__(self, name, salary, birth_date, position, department):
        self.name = name
        self.salary = salary
        self.birth_date = birth_date
        self.position = position
        self.department = department

import csv
import random
def generate_workers(n):
    names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Heidi', 'Ivan', 'Judy']
    positions = ['manager', 'developer', 'designer', 'tester', 'HR', 'accountant', 'secretary','cleaner', 'driver', 'courier', 'cook']
    departments = ['IT', 'HR', 'Finance', 'Marketing', 'Logistics', 'Sales', 'Production', 'Cleaning', 'Catering', 'Transport']
    
    with open('company_data.csv', 'w', newline="") as f:
        writer = csv.writer(f)
        writer.writerow(['name', 'salary', 'birth_date', 'position', 'department'])
        for i in range(n):
            name = random.choice(names)
            position = random.choice(positions)
            if position == 'manager':
                salary = random.randint(500, 1000)
            elif position == 'developer':
                salary = random.randint(400, 800)
            elif position == 'designer':
                salary = random.randint(300, 600)
            elif position == 'tester':
                salary = random.randint(300, 500)
            elif position == 'HR':
                salary = random.randint(200, 400)
            elif position == 'accountant':
                salary = random.randint(300, 600)
            elif position == 'secretary':
                salary = random.randint(200, 300)
            elif position == 'cleaner':
                salary = random.randint(100, 200)
            elif position == 'driver':
                salary = random.randint(200, 400)
            elif position == 'courier':
                salary = random.randint(150, 300)
            elif position == 'cook':
                salary = random.randint(200, 400)
            birth_date = f"{random.randint(1950, 2000)}-{random.randint(1, 12)}-{random.randint(1, 28)}"
            
            department = random.choice(departments)
            if department == 'IT':
                salary += 1000
            elif department == 'HR':
                salary += 500
            elif department == 'Finance':
                salary += 1500
            elif department == 'Marketing':
                salary += 700
            elif department == 'Logistics':
                salary += 600
            elif department == 'Sales':
                salary += 800
            elif department == 'Production':
                salary += 400
            elif department == 'Cleaning':
                salary += 200
            elif department == 'Catering':
                salary += 300
            elif department == 'Transport':
                salary += 500

            writer.writerow([name, salary, birth_date, position, department])

if __name__ == "__main__":
    generate_workers(10000)