class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 1
        self.score = 0
        self.question_list = q_list
        
    def question_left(self):
        return self.question_number < len(self.question_list)
        
    def question_next(self):
        question_current = self.question_list[self.question_number]
        self.question_number += 1
        answer_user = input(f"Q.{self.question_number}: {question_current.text} (True/False):\n")
        self.answer_check(answer_user, question_current.answer)
        
    def answer_check(self, answer_user, answer_correct):
        if answer_user.lower() == answer_correct.lower():
            print("You got it right")
            self.score += 1
        else:
            print("That's wrong!")
        print(f"The correct answer was: {answer_correct}.")
        print(f"Current score is: {self.score}/{self.question_number}.\n")
        
    
        
        