import random

from baseClass import Question, Answer, QuestionCheck

def clear_console():
    print("\033c", end="")

def error(num1: int, num2: int):
    print(f"Egy egesz szamot adj meg {num1} es {num2} kozott", end="")
    input()

def fileCreate():
    try:
        with open("saves.txt", "r", encoding="utf-8"):
            pass
    except FileNotFoundError:
        with open("saves.txt", "w", encoding="utf-8"):
            pass
    try:
        with open("questions.txt", "r", encoding="utf-8"):
            pass
    except FileNotFoundError:
        with open("questions.txt", "w", encoding="utf-8"):
            pass

def menu():
    fileCreate()
    menuBar = ["Jatek", "Eredmenyek", "Kerdes hozzaadasa", "Kilepes"]
    running = True
    while (running):
        clear_console()
        for i, item in enumerate(menuBar):
            print(f"\t{i+1}. {item}")
        returnInput = input("\nAdd meg a kivalasztott menupont szamat: ")
        try:
            num = int(returnInput)
            if (num < 1 or len(menuBar) < num):
                error(1, len(menuBar))
            else:
                if (num == 1):
                    game()
                elif (num == 2):
                    scorePanel()
                elif (num == 3):
                    questionCreatePanel()
                else:
                    running = False
        except:
            error(1, len(menuBar))

def setupscorePanelBar(scorePanelBar: list):
    try:
        with open("saves.txt", "r", encoding="utf-8") as file:
            for line in file:
                if (len(line) > 0 and line[0] == '*'):
                    scorePanelBar.append(line[1:].strip())
    except BaseException:
        pass
    scorePanelBar.append("Vissza a menure")

########

def game():
    clear_console()
    questions = getQuestions()
    if (len(questions) == 0):
        print("Hozz letre legalabb egy kerdest!")
        input()
        return
    random.shuffle(questions)


    name = input("Add meg a nevedet:" )
    print("\nUgy tudod kivalasztani az egyes pontokat, hogy szokozzel elvalasztva, egy sorba leirod\na kivalasztani kivant pontokat, majd nyomsz egy entert\n")
    forSave = []
    while(len(questions) > 0):
        temp_question = questions[0]
        picked = ["0" for i in range(len(temp_question.getText()))]
        print(temp_question)
        choose = input("Kivalasztom:")
        choose = choose.split(" ")
        for elem in choose:
            try:
                elem = int(elem)
                if (0 < elem and elem <= len(temp_question.getText())):
                    picked[elem-1] = "1"
            except BaseException:
                pass
        out = f"{temp_question.getQuestionID()}|"
        for elem in picked:
            out += elem
        forSave.append(out)
        questions.pop(0)
    try:
        with open("saves.txt", "a", encoding="utf-8") as file:
            file.write(f"*{name}\n")
            for elem in forSave:
                file.write(f"{elem}\n")
    except BaseException:
        print("A mentes sikertelen")
        input()

########

def scorePanel():
    scorePanelBar = []
    setupscorePanelBar(scorePanelBar)
    running = True
    while (running):
        clear_console()
        for i, item in enumerate(scorePanelBar):
            print(f"\t{i+1}. {item}")
        returnInput = input("\nAdd meg a kivalasztott menupont szamat: ")
        try:
            num = int(returnInput)
            if (num < 1 or len(scorePanelBar) < num):
                error(1, len(scorePanelBar))
            else:
                if (num == len(scorePanelBar)):
                    running = False
                else:
                    oneScore(num-1)
        except:
            error(1, len(scorePanelBar))

def oneScore(index: int):
    questionCheck = []
    getQuestionCheck(index, questionCheck)
    clear_console()
    if not questionCheck:
        print("Az adatbazis vagy futas kozben megvaltozott, vagy nem lehet elerni")
    else:
        for element in questionCheck:
            print(element)
    input()

def getQuestions() -> list:
    questions = []
    try:
        with open("questions.txt", "r", encoding="utf-8") as file:
            questionID = -1
            rightAnswer = ""
            question_text = []
            for line in file:
                if (len(line) > 0):
                    line = line.strip()
                    if (not line[0] == '*'):
                        if (len(rightAnswer)>0):
                            questions.append(Question(questionID, rightAnswer, question_text))
                            rightAnswer = ""
                            question_text = []
                        index2 = 1
                        while (not line[index2] == ','):
                            index2 += 1
                        questionID = int(line[0:index2])
                        question_text.append(line[index2+2:])
                    else:
                        line = line.replace('*', '').split("|")
                        question_text.append(line[0])
                        if (line[1].lower() == "true"):
                            rightAnswer += "1"
                        else:
                            rightAnswer += "0"
            if (not questionID == -1):
                questions.append(Question(questionID, rightAnswer, question_text))
    except BaseException:
        return []
    return questions

def getAnswers(index: int) -> list:
    answers = []    
    try:
        with open("saves.txt", "r", encoding="utf-8") as file:
            temp_index = -1
            for line in file:
                if (len(line) > 0):
                    line = line.strip()
                    if (line[0] == '*'):
                        temp_index += 1
                    elif (temp_index == index):
                        line = line.split("|")
                        answers.append(Answer(int(line[0]), line[1]))
    except BaseException:
        return []
    return answers

def getQuestionCheck(index: int, questionCheck: list):
    questions = getQuestions()
    
    answers = getAnswers(index)
    for answer in answers:
        for question in questions:
            if (answer.getQuestionID() == question.getQuestionID()):
                questionCheck.append(QuestionCheck(question.getQuestionID(), question.getRightAnswer(), answer.getPickedAnswer(), question.getText())) 

########

def questionCreatePanel():
    clear_console()
    print("\tHa befejezted a kerdes megirasat, ird be a consolra, hogy '!!!'.\n\t(Minimum 2 valasztasi lehetoseget meg kell adnia)")
    answers = []
    rightAnswers = ""
    inputText = ""
    switch = True
    question = input("\tAdd meg a kerdest: ").replace("*", "").replace("|", "")
    while (True):
        if (switch):
            switch = False
            print("Adja meg a valaszlehetoseget: ", end="")
        else:
            switch = True
            print("Adja meg az elozo valaszlehetoseg logikai erteket (true/false): ", end="")
        inputText = input()
        if (inputText == "!!!" and len(rightAnswers) == len(answers) and len(answers) > 1):
            break
        elif (inputText == "!!!"):
            print("\tMinimum 2 valaszlehetoseg es add meg a logikai ertekeiket!")
            switch = False if switch else True
        else:
            inputText = inputText.strip().replace("*", "").replace("|", "")
            if (switch):
                inputText = inputText.lower()
                if (inputText == "true" or inputText == "false"):
                    if (inputText == "true"):
                        rightAnswers += "1"
                    else:
                        rightAnswers += "0"
                else:
                    print("\ttrue-t vagy false-t adjon meg!")
                    switch = False
            else:
                answers.append(inputText)
    questionID = 0
    try:
        with open("questions.txt", "r", encoding="utf-8") as file:
            for line in file:
                if (len(line) > 0 and not line[0] == "*"):
                    questionID += 1
    except BaseException:
        return
    try:
        with open("questions.txt", "a", encoding="utf-8") as file:
            file.write(f"{questionID}, {question}\n")
            for i in range(len(answers)):
               file.write(f"*{answers[i]}|{True if rightAnswers[i]=="1" else False}\n")
    except BaseException:
        pass

    

