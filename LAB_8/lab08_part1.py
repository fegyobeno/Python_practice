#Fájlok megnyitása olvasása írása
# Beépített open() függvény ami lehetővé teszi a fájlok olvasását és írását

# r - read mode
with open('data.txt', 'r') as f:
    data = f.read()
    print(data)

with open('data.txt', 'r') as f:
    for line in f:
        print(line)

#alternatívan
with open('data.txt', 'r') as f:
    data = f.readline()
    print(data)

# Fölösleges enterek eltávolításay
with open('data.txt', 'r') as f:
    data = f.readline()
    data = [i.rstrip('\n') for i in data]
    print(data)

# w - write mode
with open('data.txt', 'w') as f:
    f.write('first line\n')
    f.write('second line\n')

# a - append mode
with open('data.txt', 'a') as f:
    f.write('third line\n')

import struct

# b - binary mode
with open('binary_data.bin', "wb") as f:
    packer = struct.Struct('10s 10s')
    packed_data = packer.pack('Hello'.encode(), 'World'.encode())
    f.write(packed_data)

with open('binary_data.bin', "rb") as f:
    data = f.read()
    unpacker = struct.Struct('10s 10s')
    unpacked_data = unpacker.unpack(data)
    unpacked_data = [i.decode().strip('\x00') for i in unpacked_data]
    print(unpacked_data)

# 'r': Open for reading (default).

# 'w': Open for writing, truncating the file first.

# 'x': Open for exclusive creation; fails if the file already exists.

# 'a': Open for writing, appending to the end of the file if it exists.

# 'b': Binary mode.

# 't': Text mode (default).

# '+': Open for updating (reading and writing).

# Egyszerre több file olvasása
with open('data.txt', "rb") as f, open('data.json', "r+") as j_f:
    pass

# CSV fájlok olvasása
import csv
with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# CSV fájlok írása
with open('data.csv', 'w', newline="") as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'age'])
    writer.writerow(['Alice', 24])
    writer.writerow(['Bob', 25])
# a newline automatikusan hozzáad egy üres sort a sorok közé, amit ha nem szeretnénk akkor newline=""-t kell használni

# CSV fájlok írása listával
data = [
    ['name', 'age'],
    ['Alice', 24],
    ['Bob', 25]
]

with open('output.csv', 'w', newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)

# JSON fájlok olvasása
import json
with open('data.json', 'r') as f:
    data = json.load(f)
    print(data)

# JSON fájlok írása
data = {
    'name': 'Alice',
    'age': 24
}

with open('output.json', 'w') as f:
    json.dump(data, f, indent=4)

#Fájlműveletek hibakezelése
try:
    with open("nonexistent.randomformat", "rw") as f:
        data = f.read()
except FileNotFoundError:
    print("The file you are trying to reach cannot be found")
except PermissionError:
    print("Nope")
except IsADirectoryError:
    print("THe file you are trying to open is a directory")
except Exception as e:
    print(f"Error: {e}")

# Try-except-finally, ha a művelet végén nem akarunk autómatikusan felszabadítani egy forrást
try:
    f = open("inexistent.txt", "r")
    content = f.read()
except FileNotFoundError:
    print("The file cannot be found")
finally:
    if f:
       f.close() 