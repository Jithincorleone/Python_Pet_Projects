import art

a = art.Art()

class GameLogic:
    question_set = []
    user_score = 0

    def __init__(self, p_question_set):
        self.question_set = p_question_set

    def play(self):

        for idx in (0, len(self.question_set)-1):
            question = self.question_set[idx]['text']
            answer = self.question_set[idx]['answer']

            p_user_answer = input(question)
            if p_user_answer.upper() == answer.upper():
                self.user_score += 1
                continue
            else:
                break

    def check_score(self):
        if self.user_score == len(self.question_set):
            print('Your Score : ' + str(self.user_score))
            print(a.win)
        else:
            print('Your Score : ' + str(self.user_score))
            print(a.loss)
