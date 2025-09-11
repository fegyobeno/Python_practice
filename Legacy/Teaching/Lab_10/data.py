import random
import string
import csv

def generate_random_name(length=6):
    return ''.join(random.choices(string.ascii_letters, k=length))

def generate_random_age(min_age=18, max_age=99):
    return random.randint(min_age, max_age)

def generate_random_email(name):
    domains = ["example.com", "test.com", "sample.org"]
    return f"{name.lower()}@{random.choice(domains)}"

def generate_sample_data(num_records=1000):
    data = []
    for _ in range(num_records):
        name = generate_random_name()
        age = generate_random_age()
        email = generate_random_email(name)
        data.append({"name": name, "age": age, "email": email})
    return data

if __name__ == "__main__":
    sample_data = generate_sample_data()
    with open('data.csv', mode='w', newline='') as file:
        for record in sample_data:
            print(record)
            writer = csv.DictWriter(file, fieldnames=["name", "age", "email"])
            writer.writeheader()
            writer.writerows(sample_data)