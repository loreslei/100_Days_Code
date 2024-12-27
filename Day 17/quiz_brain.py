class QuizBrain:
    
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
        
    def next_question(self):
        q_text = self.question_list[self.question_number].text
        q_answer = self.question_list[self.question_number].answer
        self.question_number += 1 
        user_answer = input(f"Q.{self.question_number}: {q_text} (True/False):\n").title()
        self.check_answer(user_answer, q_answer)
        
    def still_has_questions(self):
        list_size = len(self.question_list)
        actual_number = self.question_number
        return actual_number < list_size
    
    def check_answer(self, u_answer, correct_answer):
        if correct_answer == u_answer:
            print("That's right")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score: {self.score}/{self.question_number}\n")