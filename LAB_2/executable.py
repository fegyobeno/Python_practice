# pip install pyinstaller
# py -m pip install pyinstaller
# pyinstaller --onefile executable.py
# dist/executable.exe

def print_hello():
    print("Hello, executable!")

def waitkey():
    input("Press Enter to continue...")

if __name__ == "__main__":
    print_hello()
    waitkey()