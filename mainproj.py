from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from prettytable import PrettyTable


question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
table = PrettyTable()

player_name = input("WELCOME\nenter your name: ")
while quiz.still_has_question():
    quiz.current_question()
    
quiz.quiz_completed()

table.add_column("player name", [f"{player_name}"])
table.add_column("correct answers/number of questions", [f"{quiz.current_score}/{quiz.question_number}"])
percentage = ((quiz.question_number / 100) * quiz.current_score) * 100
table.add_column("percentage", [f"{percentage}"])

print(table)

