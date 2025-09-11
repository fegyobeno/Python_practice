from colored import fg, attr

class Answer:
    def __init__(self, questionID: int, pickedAnswer: list):
        self.__questionID = questionID
        self.__pickedAnswer = pickedAnswer
    
    def getQuestionID(self):
        return self.__questionID

    def getPickedAnswer(self):
        return self.__pickedAnswer


class Question:
    def __init__(self, questionID: int, rightAnswer: str, text: list):
        self.__questionID = questionID
        self.__rightAnswer = rightAnswer
        self.__text = text
    
    def getQuestionID(self):
        return self.__questionID
    
    def getRightAnswer(self):
        return self.__rightAnswer
    
    def getText(self):
        return self.__text
    
    def __str__(self):
        pass

    def __str__(self):
        text_lines = ""
        for i in range(len(self.__text) -1):
            text_lines += f"\t{i+1} - {self.__text[1+i]}\n"
        return (f"Kerdes: {self.__text[0]}\n{text_lines}")


class QuestionCheck:
    def __init__(self, questionID: int, rightAnswer: str, pickedAnswer: str, text: list):
        self.__questionID = questionID
        self.__rightAnswer = rightAnswer
        self.__pickedAnswer = pickedAnswer
        self.__text = text
    
    def __str__(self):
        reset = attr('reset')  # Alapértelmezett stílus visszaállítása
        green = fg('green')   # Helyes válasz színe
        red = fg('red')       # Rossz válasz színe
        out = f"\t{self.__questionID}. {self.__text[0]}\n"
        for i in range(len(self.__text) - 1):
            out += "\n"
            answer_text = self.__text[i + 1]
            is_picked = self.__pickedAnswer[i] == "1"
            is_correct = self.__rightAnswer[i] == "1"

            if is_correct:
                if is_picked:
                    out += f"{green}<kivalasztva> (Helyes valasz)\t{answer_text}{reset}"
                else:
                    out += f"\t\t(Helyes valasz)\t{answer_text}"
            else:
                if is_picked:
                    out += f"{red}<kivalasztva> (Rossz valasz)\t{answer_text}{reset}"
                else:
                    out += f"\t\t(Rossz valasz)\t{answer_text}"
        out += "\n"
        return out