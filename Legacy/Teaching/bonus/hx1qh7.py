import random
import json
from colored import fg, bg, attr

class QuizApp:
    def __init__(self):
        self.quizzes = []

    def load_quiz_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                quiz = []
                lines = file.readlines()
                for i in range(0, len(lines), 5):
                    question = lines[i].strip().split(',', 1)[1]
                    options = []
                    for j in range(1, 5):
                        text, correctness = lines[i+j].strip().split('|')
                        options.append((text.strip('*'), correctness == 'True'))
                    quiz.append({'question': question, 'options': options})
                self.quizzes.append(quiz)
                print(f"{fg('green')}Kvíz betöltve: {filename}{attr('reset')}")
        except Exception as e:
            print(f"{fg('red')}Hiba történt a fájl betöltésekor: {e}{attr('reset')}")

    def create_quiz_manually(self):
        quiz = []
        print("Kérdések hozzáadása. Írd be a kérdést, majd a válaszlehetőségeket.")
        while True:
            question = input("Kérdés (üres befejezéshez): ").strip()
            if not question:
                break

            options = []
            for i in range(4):
                answer = input(f"Válasz {i+1}: ").strip()
                correctness = input(f"Ez helyes? (i/n): ").strip().lower() == 'i'
                options.append((answer, correctness))

            quiz.append({'question': question, 'options': options})
        
        self.quizzes.append(quiz)

    def save_quiz(self, filename):
        try:
            with open(filename, 'w') as file:
                for quiz in self.quizzes:
                    for item in quiz:
                        file.write(f"1, {item['question']}\n")
                        for text, correctness in item['options']:
                            file.write(f"*{text}|{'True' if correctness else 'False'}\n")
                print(f"{fg('green')}Kvíz mentve: {filename}{attr('reset')}")
        except Exception as e:
            print(f"{fg('red')}Hiba történt a mentés során: {e}{attr('reset')}")

    def run_quiz(self):
        if not self.quizzes:
            print(f"{fg('red')}Nincsenek elérhető kvízek!{attr('reset')}")
            return

        quiz = random.choice(self.quizzes)
        random.shuffle(quiz)

        score = 0
        for item in quiz:
            print(f"{fg('blue')}{item['question']}{attr('reset')}")
            for i, (option, _) in enumerate(item['options'], 1):
                print(f"  {i}. {option}")

            try:
                user_answers = list(map(int, input("Válasz(ok) számai vesszővel elválasztva: ").split(',')))
                correct_answers = [i+1 for i, (_, correct) in enumerate(item['options']) if correct]

                if sorted(user_answers) == sorted(correct_answers):
                    print(f"{fg('green')}Helyes!{attr('reset')}")
                    score += 1
                else:
                    print(f"{fg('red')}Helytelen! A helyes válasz(ok): {', '.join(map(str, correct_answers))}{attr('reset')}")
            except ValueError:
                print(f"{fg('red')}Érvénytelen válasz!{attr('reset')}")

        print(f"{fg('yellow')}Kvíz vége! Eredmény: {score}/{len(quiz)}{attr('reset')}")


def main():
    app = QuizApp()

    while True:
        print("\nFőmenü:")
        print("1. Kvíz létrehozása manuálisan")
        print("2. Kvíz betöltése fájlból")
        print("3. Kvíz mentése fájlba")
        print("4. Kvíz futtatása")
        print("5. Kilépés")

        choice = input("Választás: ").strip()

        if choice == '1':
            app.create_quiz_manually()
        elif choice == '2':
            filename = input("Fájl neve: ").strip()
            app.load_quiz_from_file(filename)
        elif choice == '3':
            filename = input("Fájl neve: ").strip()
            app.save_quiz(filename)
        elif choice == '4':
            app.run_quiz()
        elif choice == '5':
            print("Viszlát!")
            break
        else:
            print(f"{fg('red')}Érvénytelen választás!{attr('reset')}")

if __name__ == "__main__":
    main()
