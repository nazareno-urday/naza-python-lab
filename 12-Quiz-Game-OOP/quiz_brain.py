from question_model import Question
class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.questions = q_list
        self.score = 0
        self.user_answer = ""

    def still_has_questions(self):
        if self.question_number < len(self.questions):
            return True
        else:
            return False

    def next_question(self):
        current_question = self.questions[self.question_number]
        user_answer = input(f"Q.{self.question_number + 1}: {current_question.question} (True/False): ")
        self.question_number += 1
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            self.score += 1
            print(f"Correct!, your score is {self.score}/{self.question_number}")
        else:
            print(f"Wrong!, your score is {self.score}/{self.question_number}")