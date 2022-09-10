import art

a = art.Art()



class GameLogic:
    question_set = []
    user_score = 0

    def __init__(self, p_question_set):
        self.question_set = p_question_set

    def play(self):

        for idx in range(0, len(self.question_set)):
            question = self.question_set[idx]['question']
            answer = self.question_set[idx]['correct_answer']

            p_user_answer = input('Q'+str(idx+1)+':'+question)
            if p_user_answer.upper() == answer.upper():
                self.user_score += 1

            print('Your Score : '+str(self.user_score)+'/'+str(len(self.question_set)))


    def check_score(self):
        if self.user_score == len(self.question_set):
            print('Your Final Score : ' + str(self.user_score))
            print(a.win)
        else:
            print('Your Score : ' + str(self.user_score))
            print(a.loss)
