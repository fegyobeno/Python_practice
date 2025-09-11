import random
from colored import *
from pathlib import Path

questions = []

def add_questions_manually():
    global questions
    done = False
    while not done:
        question = input("Add meg a kérdést: ")
        answers = []
        correct = []
        for i in range(4):
            print(f"You still have to give {4-i} more answer(s).")
            ans = input("Enter the answer: ")
            cor = input("Is this answer correct? (yes/no): ").strip().lower() == "yes"
            answers.append(ans)
            if cor:
                correct.append(i)
        
        questions.append({"question": question, "answers": answers, "correct": correct})

        done = input("Do you want to add another question? (yes/no): ").strip().lower() == "no"

def load_quiz(f_name):
    global questions
    ind = 1
    ans_ind = 0
    try:
        with open(f_name, "r", encoding="utf-8") as file:
            new_q = {}
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                if line.startswith(f"{ind},"):
                    ind += 1
                    ans_ind = 0
                    if new_q:
                        questions.append(new_q)
                    temp = line.split(',')
                    new_q = {"question": temp[1].strip(), "answers": [], "correct": []}
                elif line.startswith("*"):
                    temp = line.split('*')
                    temp2 = temp[1].split('|')
                    answer = temp2[0].strip()
                    correct = temp2[1].strip()
                    new_q["answers"].append(answer)
                    if correct == "True":
                        new_q["correct"].append(ans_ind)
                    ans_ind += 1
            if new_q:
                questions.append(new_q)

            print(f"{fg("green")}File successfully loaded{attr("reset")}")
    except FileNotFoundError:
        print(f"{fg("red")}File not found: {f_name}{attr("reset")}")
    except Exception as e:
        print(f"{fg("red")}Error while processing the file: {e}{attr("reset")}")

def save_quiz(f_name):
    try:
        index = 0
        with open(f_name, "w", encoding="utf-8") as file:
            for question in questions:
                index += 1
                file.write(f"{index}, {question["question"]}\n")
                for i, answer in enumerate(question["answers"]):
                    cor = "False"
                    if i in question["correct"]:
                        cor = "True"
                    file.write(f"*{answer}|{cor}\n")
                file.write("\n")
        print(f"{fg("green")}The quiz has been successfully saved: {f_name}{attr("reset")}")
    except Exception as e:
        print(f"{fg("red")}An error occurred while saving the quiz: {e}{attr("reset")}")

def print_question_and_answers(question):
    print(f"\n{question["question"]}")
    for i, answer in enumerate(question["answers"]):
        print(f"{i+1}. {answer}")

def is_correct(answers, correct):
    if len(answers) < len(correct):
        return False
    for i in range(len(answers)):
        if(answers[i] != (correct[i] + 1)):
            return False
    return True

def shuffle_questions():
    random.shuffle(questions)

def user_input():
    answer = input("Enter the number of your answer (if you chose multiple answers, separate them with a space): ")
    
    try:
        user_answers = list(map(int, answer.split(' ')))
        return user_answers
    except ValueError:
        print(f"{fg("red")}An error occured, please try again!{attr('reset')}")
        return user_input()

def quiz():
    if len(questions) == 0:
        print(f"{fg("red")}Can't play with an empty quiz set!{attr('reset')}")
        return
    
    correct_answers = 0
    shuffle_questions()

    for question in questions:
        print_question_and_answers(question)
        user_answers = user_input()

        if(is_correct(user_answers, question["correct"])):
            correct_answers += 1
            print(f"{fg("green")}Correct!{attr('reset')}")
        else:
            print(f"{fg("red")}Incorrect!{attr('reset')}")
            print(f"{fg("cyan")}Correct answers:{attr('reset')}")
            for c in question["correct"]:
                print(f"{fg("cyan")}{c+1}{attr('reset')}")
    print(f"{fg("magenta")}Number of correct answers: {correct_answers}. This translates to {round(correct_answers/len(questions)*100, 2)}%.{attr("reset")}")

if __name__ == "__main__":
    print("Welcome to this quiz app!")
    
    print("Choose an option:")
    print("1. Play quiz")
    print("2. Create a new quiz manually")
    print("3. Load a quiz")
    print("4. Save the quiz")
    print("5. Exit")
    choice = input()

    while choice != "5":
        if choice == "1":
            quiz()
        if choice == "2":
            add_questions_manually()
        if choice == "3":
            f_name = input("Enter the file's name: ")
            #helyezd a beolvasandó fájlt a .py fájl mellé
            path = Path(__file__).parent / f_name
            load_quiz(path)
        if choice == "4":
            f_name = input("Enter the file's name: ")
            #a fájlt a .py fájl mellé menti
            path = Path(__file__).parent / f_name
            save_quiz(path)
        
        print("Choose an option:")
        print("1. Play quiz")
        print("2. Create a new quiz manually")
        print("3. Load a quiz")
        print("4. Save the quiz")
        print("5. Exit")
        choice = input()