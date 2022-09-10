import random


def is_val_exists(p_val, p_val_list):
    if p_val_list.count(p_val) > 0:
        return True
    else:
        return False


class QuestionBank:
    question_data = [
        {"text": "A slug's blood is green.", "answer": "True"},
        {"text": "The loudest animal is the African Elephant.", "answer": "False"},
        {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
        {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
        {"text": "In West Virginia, USA, if you accidentally hit an animal with your car,"
                 " you are free to take it home to eat.", "answer": "True"},
        {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.",
         "answer": "False"},
        {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
        {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
        {"text": "Google was originally called 'Backrub'.", "answer": "True"},
        {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
        {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
        {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}]

    no_questions = 0
    question_set = []

    def __init__(self, p_no_questions):
        self.no_questions = p_no_questions
        question_set = []

    def set_question_set(self):
        val_list = []
        for idx in range(0, self.no_questions):
            val = random.randint(0, len(self.question_data)-1)
            while is_val_exists(val, val_list):
                val = random.randint(0, len(self.question_data)-1)

            if not is_val_exists(int(val), val_list):
                val_list.append(val)

            self.question_set.append(self.question_data[val])
