import random
import json
import os
from colored import fg, attr

def create_quiz():
    quiz = []
    print("\nCreate a new quiz by entering questions and their answers.")
    print("To finish, leave the question blank and press Enter.")

    while True:
        question = input("Enter the question: ")
        if not question.strip():
            break
        answers = []
        print("Enter the answers. Mark correct answers with 'True' or 'False'. Type 'done' to finish.")

        while True:
            answer_input = input("Answer (e.g., 'Answer text|True'): ")
            if answer_input.lower() == 'done':
                break
            try:
                text, correctness = answer_input.rsplit('|', 1)
                correctness = correctness.strip().lower() == 'true'
                answers.append({"text": text.strip(), "correct": correctness})
            except ValueError:
                print("Invalid format. Use 'Answer text|True' or 'Answer text|False'.")
        quiz.append({"question": question, "answers": answers})
    return quiz

def save_quiz(quiz, filename):
    if not filename.lower().endswith('.json'):
        filename += '.json'

    with open(filename, 'w') as file:
        json.dump(quiz, file)
    print(f"Quiz saved to {filename}.")

def load_quiz(filename):
    if not filename.lower().endswith('.json'):
        filename += '.json'

    try:
        with open(filename, 'r') as file:
            print("File loaded successfully")
            return json.load(file)
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return None
    except json.JSONDecodeError:
        print(f"File {filename} is not a valid JSON file.")
        return None

def run_quiz(quiz):
    print("\nStarting the quiz!\n")
    random.shuffle(quiz)
    correct_count = 0
    for item in quiz:
        print(item["question"])
        options = item["answers"]
        random.shuffle(options)
        for i, option in enumerate(options):
            print(f"{i + 1}. {option['text']}")

        user_answers = input("Enter your answer(s) as numbers separated by spaces: ").split()
        try:
            user_answers = [int(x) - 1 for x in user_answers]
        except ValueError:
            print(f"{fg('red')}Invalid input. Skipping this question.{attr('reset')}")
            continue
        
        correct_answers = [i for i, ans in enumerate(options) if ans['correct']]
        user_correct = all(i in correct_answers for i in user_answers) and all(i in user_answers for i in correct_answers)

        if user_correct:
            print(f"{fg('green')}Correct!{attr('reset')}")
            correct_count += 1
        else:
            print(f"{fg('red')}Incorrect. The correct answers were:")
            for i in correct_answers:
                print(f"{i + 1}. {options[i]['text']}")
            print(attr('reset'))
    
    print(f"\nYou answered {correct_count}/{len(quiz)} questions correctly.")

def load_quiz_from_text_file(filename):
    quiz = []
    if not filename.lower().endswith('.txt'):
        filename += '.txt'
    
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        question = None
        answers = []

        for line in lines:
            line = line.strip()
            
            if not line:
                continue

            if not line.startswith('*'):
                if question is not None and answers:
                    quiz.append({"question": question, "answers": answers})
                question = line.split(',', 1)[1].strip()
                answers = []
            else:
                try:
                    text, correctness = line[1:].rsplit('|', 1)
                    answers.append({"text": text.strip(), "correct": correctness.strip().lower() == 'true'})
                except ValueError:
                    print(f"Invalid answer format: {line}")


        if question is not None and answers:
            quiz.append({"question": question, "answers": answers})
        print('File loaded successfully')
        return quiz
    
    except FileNotFoundError:
        print(f"File {filename} not found. Please check the file path and try again.")
        return []

    except Exception as e:
        print(f"An error occurred while loading the file: {e}")
        return []


def main():
    while True:
        print("\nQuiz Application")
        print("1. Create a new quiz")
        print("2. Save a quiz")
        print("3. Load a quiz")
        print("4. Load a quiz from a text file")
        print("5. Run a quiz")
        print("6. Exit")
        
        choice = input("Select an option: ")
        if choice == '1':
            quiz = create_quiz()
        elif choice == '2':
            if 'quiz' in locals() and quiz:
                filename = input("Enter the filename to save the quiz (should be .json): ")
                save_quiz(quiz, filename)
            else:
                print("No quiz to save. Please create or load a quiz first.")
        elif choice == '3':
            filename = input("Enter the filename to load the quiz (should be .json): ")
            quiz = load_quiz(filename)
        elif choice == '4':
            filename = input("Enter the filename to load the text file quiz (should be .txt): ")
            quiz = load_quiz_from_text_file(filename)
        elif choice == '5':
            if 'quiz' in locals() and quiz:
                run_quiz(quiz)
            else:
                print("No quiz loaded or created. Please load or create a quiz first.")
        elif choice == '6':
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    print("Files will be saved in:", os.getcwd())
    main()