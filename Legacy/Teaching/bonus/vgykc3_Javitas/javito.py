import json
import random
from termcolor import colored

class QuizApp:
    def __init__(self):
        self.questions = []

    def load_questions_from_file(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                self.questions = []
                lines = [line.strip() for line in file.readlines() if line.strip()]
                
                i = 0
                while i < len(lines):
                    try:
                       
                        if not lines[i].startswith("1, "):
                            raise ValueError("Hibás kérdés formátum a fájlban.")
                        question_text = lines[i].split(", ", 1)[1]

                        
                        options = []
                        for j in range(1, 5):
                            if i + j >= len(lines) or not lines[i + j].startswith("*"):
                                raise ValueError("Hibás válasz formátum a fájlban.")
                            text, is_correct = lines[i + j].rsplit('|', 1)
                            options.append({"text": text.strip('*'), "is_correct": is_correct == 'True'})

                        self.questions.append({"question": question_text, "options": options})
                        i += 5  
                    except ValueError as e:
                        print(colored(f"Hiba a fájl beolvasásakor: {e}", "red"))
                        break
            print(colored("A fájl sikeresen beolvasva!", "green"))
        except FileNotFoundError:
            print(colored("Hiba: A fájl nem található.", "red"))
        except Exception as e:
            print(colored(f"Hiba történt a fájl betöltésekor: {e}", "red"))

    def save_quiz(self, file_path):
        
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                for question in self.questions:
                    file.write(f"1, {question['question']}\n")
                    for option in question['options']:
                        is_correct = "True" if option['is_correct'] else "False"
                        file.write(f"*{option['text']}|{is_correct}\n")
        except Exception as e:
            print(colored(f"Hiba történt a fájl mentésekor: {e}", "red"))

    def add_question_manually(self):
        
        question_text = input("Kérdés szövege: ")
        options = []
        for i in range(4):
            option_text = input(f"{i + 1}. válasz szövege: ")
            is_correct = input(f"Ez egy helyes válasz? (i/n): ").lower() == 'i'
            options.append({"text": option_text, "is_correct": is_correct})
        self.questions.append({"question": question_text, "options": options})

    def start_quiz(self):
        
        if not self.questions:
            print(colored("Nincsenek kérdések a kvízben!", "red"))
            return

        random.shuffle(self.questions)
        score = 0

        for idx, question in enumerate(self.questions):
            print(colored(f"\n{idx + 1}. {question['question']}", "cyan"))
            randomized_options = question['options'][:]
            random.shuffle(randomized_options)

            for i, option in enumerate(randomized_options):
                print(f"  {i + 1}. {option['text']}")

            try:
                user_answers = input("Válaszd ki a helyes válasz(ok) számát vesszővel elválasztva: ").split(',')
                user_answers = [int(answer.strip()) - 1 for answer in user_answers]

                correct_answers = [i for i, opt in enumerate(randomized_options) if opt['is_correct']]

                if set(user_answers) == set(correct_answers):
                    print(colored("Helyes!", "green"))
                    score += 1
                else:
                    print(colored("Helytelen.", "red"))
                    print("A helyes válasz(ok):", ", ".join(str(i + 1) for i in correct_answers))
            except ValueError:
                print(colored("Érvénytelen válaszformátum!", "red"))

        print(colored(f"\nA kvíz véget ért! Eredmény: {score}/{len(self.questions)}", "yellow"))

    def menu(self):
        
        while True:
            print("\nKvíz Alkalmazás Menü:")
            print("1. Kérdések betöltése fájlból")
            print("2. Kérdések mentése fájlba")
            print("3. Új kérdés hozzáadása")
            print("4. Kvíz indítása")
            print("5. Kilépés")

            choice = input("Választás: ")

            if choice == '1':
                file_path = input("Add meg a fájl nevét: ")
                self.load_questions_from_file(file_path)
            elif choice == '2':
                file_path = input("Add meg a mentés fájl nevét: ")
                self.save_quiz(file_path)
            elif choice == '3':
                self.add_question_manually()
            elif choice == '4':
                self.start_quiz()
            elif choice == '5':
                print("Kilépés a programból.")
                break
            else:
                print(colored("Érvénytelen választás!", "red"))

if __name__ == "__main__":
    app = QuizApp()
    app.menu()
