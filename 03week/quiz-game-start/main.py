from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

#getting questions
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]    
    question_new = Question(question_text, question_answer)
    question_bank.append(question_new)
    #AttributeError: 'dict' object has no attribute 'append'
    
quiz = QuizBrain(question_bank)

while quiz.question_left():
    quiz.question_next()

print("You have completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}.")
