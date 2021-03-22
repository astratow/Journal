from question_model import Question
from data import question_data

#getting questions
question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]    
    new_question = Question(question_text, question_answer)
    question.append(new_question)
    
print(question_bank[0].answer)