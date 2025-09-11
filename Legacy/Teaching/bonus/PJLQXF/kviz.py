import random
from typing import List, Tuple
from colored import fg, attr

class Question:
    def __init__(self, text: str, answers: List[Tuple[str, bool]]):
        self.text = text
        self.answers = answers

class Quiz:
    def __init__(self):
        self.questions = []

    def add_question(self, question: Question):
        self.questions.append(question)

    def shuffle_questions(self):
        random.shuffle(self.questions)

def read_questions_from_file(filename: str) -> List[Question]:
    questions = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            print(f"Észleltük a(z) {filename} fájlt. Ha szeretnél manuálisan megadni kérdéseket, akkor töröld ki a fájlt, és futtasd újra a programot!")
            lines = file.readlines()
            current_question = None
            answers = []
            for line in lines:
                line = line.strip()
                if line.startswith('*'):
                    answer_text, is_correct = line[1:].split('|')
                    answers.append((answer_text.strip(), is_correct.strip() == 'True'))
                else:
                    if current_question:
                        questions.append(Question(current_question, answers))
                    current_question = line
                    answers = []
            if current_question:
                questions.append(Question(current_question, answers))
    except FileNotFoundError:
        print(f"A(z) {filename} fájl nem található. Kérjük, add meg a kérdéseket manuálisan!")
        while True:
            num_questions = input("Hány kérdésből álljon a kvíz? ")
            if num_questions.isdigit():
                num_questions = int(num_questions)
                break
            else:
                print("Érvénytelen szám. Kérjük, adj meg egy pozitív egész számot!")
        
        manual_questions = []
        for i in range(1, num_questions + 1):
            question_input = input(f"Add meg a(z) {i}. kérdést és a válaszokat a következő formátumban: ['Kérdés?|Válaszok száma', 'Válasz1|True/False', 'Válasz2|True/False', ...]:\n")
            question_data = eval(question_input)
            question_text = f"{i}, {question_data[0].split('|')[0]}"
            answers = [(ans.split('|')[0], ans.split('|')[1] == 'True') for ans in question_data[1:]]
            questions.append(Question(question_text, answers))
            manual_questions.append(question_text)
            for ans in answers:
                manual_questions.append(f"*{ans[0]}|{ans[1]}")
        
        with open("manual_questions.txt", "w", encoding="utf-8") as file:
            for item in manual_questions:
                file.write(f"{item}\n")
        
        print(f"\nA megadott kérdéseket és válaszokat elmentettük a manual_questions.txt fájlba.\nHa a következő futtatáskor szeretnéd ezeket a kérdéseket betölteni, akkor nevezd át az alábbira: {filename}")
    
    return questions

def ask_question(question: Question):
    print(f"\n{question.text[3:]}")
    for i, (answer, _) in enumerate(question.answers):
        print(f"{i + 1}. {answer}")
    
    while True:
        user_answer = input("Válasz: ")
        if user_answer.isdigit() and 1 <= int(user_answer) <= len(question.answers):
            return [int(user_answer) - 1]
        else:
            print("Érvénytelen válasz. Adj meg egy számot a megadott lehetőségek közül!")

def check_answer(question: Question, user_answers: List[int]):
    correct_answers = [i for i, (_, correct) in enumerate(question.answers) if correct]
    return any(answer in correct_answers for answer in user_answers), correct_answers

def provide_feedback(is_correct: bool, correct_answers: List[int], question: Question):
    if is_correct:
        print(f"{fg('green')}Helyes!{attr('reset')}")
    else:
        print(f"{fg('red')}Helytelen!{attr('reset')}")

def evaluate_quiz(quiz: Quiz):
    correct_count = 0
    for question in quiz.questions:
        user_answers = ask_question(question)
        is_correct, correct_answers = check_answer(question, user_answers)
        provide_feedback(is_correct, correct_answers, question)
        if is_correct:
            correct_count += 1
    print(f"\nVégső pontszám: {len(quiz.questions)}/{correct_count}")
    if correct_count == len(quiz.questions):
        print(f"{fg('green')}Hibátlan!{attr('reset')}")

def main():
    quiz = Quiz()
    quiz.questions = read_questions_from_file('questions.txt')
    quiz.shuffle_questions()
    evaluate_quiz(quiz)

if __name__ == "__main__":
    main()