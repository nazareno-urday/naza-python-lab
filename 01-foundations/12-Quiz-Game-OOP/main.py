from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for i in question_data:
    # Iterates through the question data, creates a Question object
    # from each dictionary, and adds it to the question bank.
    question_bank.append(Question(i["text"], i["answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"\nCongratulations! You have completed the quiz,"
      f" your final score is {quiz.score}/{len(question_bank)}")