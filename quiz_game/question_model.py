import random
import question_bank


def is_val_exists(p_val, p_val_list):
    if p_val_list.count(p_val) > 0:
        return True
    else:
        return False


class QuestionModel:
    q = question_bank.QuestionBank()
    question_data = q.question_data
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
