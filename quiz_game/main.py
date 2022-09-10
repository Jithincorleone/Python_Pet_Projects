import question_bank
import art
import game_logic
import question_model

a = art.Art()
print(a.logo)

p_user_questions = input('For how many questions you want to play the game. ? ')
q = question_model.QuestionModel(int(p_user_questions))
q.set_question_set()
g = game_logic.GameLogic(q.question_set)
g.play()
g.check_score()
