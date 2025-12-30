class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.current_score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def current_question(self):
        return self.question_list[self.question_number]

    def check_answer(self, user_answer):
        correct_answer = self.current_question().answ

        if user_answer.lower() == correct_answer.lower():
            self.current_score += 1
            correct = True
        else:
            correct = False

        self.question_number += 1
        return correct, correct_answer