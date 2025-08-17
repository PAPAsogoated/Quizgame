class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.current_score = 0
        

    def still_has_question(self):
        '''
        this method checks if there is any questions left
        and counts the questions.
        '''
        
        len(self.question_list)
        if self.question_number < len(self.question_list) :
            return True
        else:
            return False

    

    def next_question(self):
        '''
        this method is for typing the questions, going to next one
        and checking the players answer
        '''
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}:{current_question.tx} (True/false):")
        self.check_answer(user_answer, current_question.answ)

    

    def check_answer(self, user_answer, correct_answer):

        '''this method checks the answer and counts the users score'''
        if user_answer.lower() == correct_answer.lower():
            self.current_score += 1
            print("you got it right")
          
        else:
            print("thats wrong")
        print(f"the correct answer was:{correct_answer}.")
        print(f"your current score is {self.current_score}/{self.question_number}.")
        print("\n")
    
    


    def quiz_completed(self):
        print("you have compeleted the quiz.")

    
    # def percenteage(self):
        # per = self.question_number / 100 
        # cent = per * self.current_score
      