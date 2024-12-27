class QuizBrain:
    
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        
    def next_question(self):
        q_text = self.question_list[self.question_number].text
        self.question_number += 1 
        input(f"Q.{self.question_number}: {q_text} (True/False):\n").title()
        
    def still_has_questions(self):
        list_size = len(self.question_list)
        actual_number = self.question_number
        
        if actual_number >= list_size:
            return False
        
        return True