import colored
import random

RED = colored.Fore.red
BLUE = colored.Fore.blue
BLACK = colored.Fore.black
GREEN = colored.Fore.green
WHITE = colored.Fore.white

class Question:
    def __init__(self, number, question, answers, correct_answers):
        self.number = number
        self.question = question
        self.answers = answers
        self.correct_answers = correct_answers

class Quiz:
    def __init__(self, questions, name):
        self.questions = questions
        self.name = name
    def useQuiz(self):
        randomized_questions = self.questions[:]
        random.shuffle(randomized_questions)
        return randomized_questions

def readQuizFromFile(filePath):
    questions = []
    with open(filePath, "r", encoding="utf-8") as file:
                lines = file.readlines()
                for i in range(0, len(lines), 5):
                    block = lines[i:i+5]
                    question_line = block[0].strip()
                    question_number = question_line.split(',')[0]
                    question_text = question_line.split(',')[1]

                    answers = [line.strip() for line in block[1:5]]
                    parsed_answers = []
                    correct_answers = []

                    for idx, answer in enumerate(answers, 1):
                        answer_text, is_correct = answer.split('|')
                        is_correct = is_correct.lower() == 'true'
                        parsed_answers.append(answer_text)
                        if is_correct:
                            correct_answers.append(answer_text)
                    question = Question(question_number, question_text, parsed_answers, correct_answers)
                    questions.append(question)
    quiz = Quiz(questions, filePath.split(".")[0])
    quizes.append(quiz)

def makeQuizManually():
    questions = []
    counter = 1
    adding = 1
    while adding == 1:
        print(f"{GREEN}{counter}. Kérdés{BLACK}")
        question_text = input("Kérdés szövege: ")
        answers = []
        correct_ans = []
        for i in range(4):
            ans_text = input(f"{i + 1}. Válasz: ")
            answers.append(ans_text)
            print(f"{RED}Helytelen válasz -> {BLUE}0")
            print(f"{GREEN}Helyes válasz -> {BLUE}1{BLACK}")
            correct = int(input(f"{RED}0/{GREEN}1: {BLACK}"))
            if correct == 1:
                correct_ans.append(ans_text)
        question = Question(counter, question_text, answers, correct_ans)
        questions.append(question)
        counter+= 1
        print(f"{BLUE}Szeretnél hozzáadni újabb kérdést?{BLACK}")
        print(f"{RED}0 -> NEM")
        print(f"{GREEN}1 -> IGEN{BLACK}")
        adding = int(input())
    quiz_name = input("Mi legyen a kvíz neve?: ")
    quiz = Quiz(questions, quiz_name)
    quizes.append(quiz)
    print(f"{BLACK}El szeretnéd menteni a Kvízt?")
    print(f"{RED}0 -> Nem {BLACK}/ {GREEN}1 -> Igen{BLACK}")
    save = int(input())
    if save == 1:
        saveQuiz(quiz)

def takeQuiz(quiz):
    tempQuiz = quiz.useQuiz() 
    score = 0
    for question in tempQuiz:
        numOfCorrect = len(question.correct_answers)
        correctness = 0
        local_correct_answers = question.correct_answers[:]
        print(f"{BLUE}({question.number}.) {question.question} [{len(question.correct_answers)}]")
        for ind, ans in enumerate(question.answers):
            print(f"{BLACK}{ind + 1} -> {ans}")
        for i in range(len(question.correct_answers)):
            inputAnswer = int(input(f"{GREEN}Válasz: ")) - 1
            if question.answers[inputAnswer] in local_correct_answers:
                local_correct_answers.remove(question.answers[inputAnswer])
                correctness+=1
                print(f"{GREEN}Jó válasz.{BLACK}")
            else:
                print(f"{RED}Rossz válasz.{BLACK}")
        if correctness == numOfCorrect:
            score += 1
    if score > len(quiz.questions) * 0.5:
        print(f"{GREEN}Ügyes vagy, {score}/{len(quiz.questions)} pontod lett!")
    else:
        print(f"{RED}Sajnos csak {score}/{len(quiz.questions)} pontod lett, legközelebb jobb lesz!")


def saveQuiz(quiz):
    name = input(f"{BLUE}Mi legyen a file neve?: {BLACK}")
    fileName = name + ".txt"
    with open(fileName, "w", encoding="utf-8") as file:
        for question in quiz.questions:
            file.write(f"{question.number}, {question.question}\n")
            for ans in question.answers:
                correct = False
                if ans in question.correct_answers:
                    correct = True
                if correct:
                    file.write(f"*{ans}|True\n")
                else:
                    file.write(f"*{ans}|False\n")

quizes = []
running = True

while running:
    print(f"{BLACK}Mit szeretnél csinálni?")
    print(f"{BLUE}1 -> Kvíz kitöltése")
    print(f"{BLUE}2 -> Új kvíz készítése")
    print(f"{RED}0 -> Kilépés{BLACK}")

    menu = int(input())
    
    if menu == 0:
        running = False
    elif menu == 1:
        print(f"{BLUE}Melyik Kvízt szeretnéd kitölteni?{BLACK}")
        quizCounter = 1
        for quiz in quizes:
            print(f"{quizCounter}. {quiz.name}")
            quizCounter+=1
        chosenQuizNum = int(input()) - 1
        chosenQuiz = quizes[chosenQuizNum]
        takeQuiz(chosenQuiz)
        menu = -1
    elif menu == 2:
        print(f"{BLACK}Milyen módon szeretnél quizt hozzáadni?")
        print(f"{BLUE}1 -> Kvíz betöltése fileból")
        print(f"{BLUE}2 -> Kérdések hozzáadása manuálisan")
        print(f"{RED}0 -> Visszalépés{BLACK}")
        newSubMenu = int(input())
        if newSubMenu == 1:
            print(f"{BLUE}Add meg a fájl nevét.")
            newFileName = input()
            readQuizFromFile(newFileName)
        elif newSubMenu == 2:
            makeQuizManually()
        elif newSubMenu == 0:
            menu = -1
        

print(f"{WHITE}Köszi, hogy a programot használtad!{colored.Style.reset}")