import random
import os
from colored import fg, attr


def load_quiz_from_file(filepath):
    questions = []
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            lines = file.readlines()
            question = None
            answers = []
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                if not line.startswith("*"):
                    # A kérdést és a válaszokat akkor adjuk hozzá, mikor új kérédést találunk
                    if question:
                        questions.append((question, answers))
                    question = line.split(",", 1)[
                        1
                    ].strip()  # Csak a kérdést hagyjuk meg, a számot "kidobjuk"
                    answers = []
                elif line.startswith("*"):
                    answer_text, is_correct = line[1:].rsplit("|", 1)
                    answers.append((answer_text.strip(), is_correct.strip() == "True"))
            if question:  # Utolsó kérdés hozzáadása
                questions.append((question, answers))
    except FileNotFoundError as e:
        return None
    return questions


def create_quiz_manually():
    questions = []
    while True:
        question = input("Add meg a kérdést (vagy 'q' a kilépéshez): ")
        if question.lower() == "q":
            break
        answers = []
        while True:
            answer = input("Add meg egy választ (vagy 'q' a következő kérdés megadásához): ")
            if answer.lower() == "q":
                break
            is_correct = input("Ez a válasz helyes? (igen/nem): ").lower() == "igen"
            answers.append((answer, is_correct))
        questions.append((question, answers))
    return questions


def save_quiz_to_file(questions, filepath):
    try:
        with open(filepath, "w", encoding="utf-8") as file:
            for i, (question, answers) in enumerate(questions, 1):
                file.write(f"{i}, {question}\n")
                for answer, is_correct in answers:
                    file.write(f"*{answer}|{'True' if is_correct else 'False'}\n")
        print("Kvíz sikeresen elmentve")
    except Exception as e:
        print("Hiba történt mentés közben: " + e)


def run(questions):
    score = 0
    random.shuffle(questions)
    for question, answers in questions:
        print(f"\nKérdés: {question}")
        random.shuffle(answers)
        for idx, (answer, _) in enumerate(answers, 1):
            print(f"  {idx}. {answer}")
        user_input = input("Válaszaid számokkal (pl. 1,2): ")
        user_choices = [
            int(x.strip()) - 1 for x in user_input.split(",") if x.strip().isdigit()
        ]

        correct_indices = [i for i, (_, is_correct) in enumerate(answers) if is_correct]
        if sorted(user_choices) == sorted(correct_indices):
            print(f"{fg('green')}Helyes!{attr('reset')}")
            score += 1
        else:
            print(f"{fg('red')}Helytelen!{attr('reset')}")
    print(
        f"\nVége! Eredmény: {score}/{len(questions)} pont"
    )


def main():
    questions = []
    while True:
        print("\nKvíz Alkalmazás Menü:")
        print("1. Kvíz betöltése fájlból")
        print("2. Kvíz létrehozása manuálisan")
        print("3. Kvíz elmentése fájlba")
        print("4. Kvíz indítása")
        print("5. Kilépés")
        choice = input("Válaszd ki a művelet számát: ")
        
        if choice == '1':
            filepath = input("Add meg a fájl elrési útját: ")
            questions = load_quiz_from_file(filepath)
            if questions is None:
                print("Couldn't open file")
                continue
            else:
                print("Kvíz sikeresen betöltve, elindíthatod")
        elif choice == '2':
            questions = create_quiz_manually()
        elif choice == '3':
            if questions:
                filepath = input("Add meg a mentési fájl elérési útját: ")
                save_quiz_to_file(questions, filepath)
            else:
                print("Nincsenek menthető kérdések!")
        elif choice == '4':
            if questions:
                run(questions)
            else:
                print("Nincsenek betöltött kérdések!")
        elif choice == '5':
            break
        else:
            print("Érvénytelen választás!")

if __name__ == "__main__":
    main()