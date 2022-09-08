from game_data import data
from art import logo,vs,win,loose
import random
import os

loss=False
userQuesList=[]
userScore=0

def get_ques():
  val=random.randint(0,len(data)-1)
  valDict=data[val]  
  return valDict

def getMaxCnt(p_list):
  score1=p_list[0]['follower_count']
  score2=p_list[1]['follower_count']

  if int(score1) > int(score2):
    for idx in range(0, len(p_list)):
      if int(p_list[idx]['follower_count'])!=int(score1):
        return score1,idx
  elif int(score2) > int(score1):
    for idx in range(0, len(p_list)):
      if int(p_list[idx]['follower_count'])!=int(score2):
        return score2,idx

def get_user_score(p_userVal, p_maxCnt, p_userQuesList):
  if p_userVal.upper()=='A':
    idx=0
  elif p_userVal.upper()=='B':
    idx=1
  userCnt=p_userQuesList[int(idx)]['follower_count']

  if p_maxCnt==userCnt:
    return 0
  else :
    return 1

print (logo)

while loss==False :
  ques1=get_ques()
  userQuesList.append(ques1)
  ques2=get_ques()
  userQuesList.append(ques2)
  print('Compare A : ' + userQuesList[0]['name'] + ', a '+ userQuesList[0]['description'] +', from  '+ userQuesList[0]['country'])
  print(vs)
  print('Compare B : ' + userQuesList[1]['name'] + ', a '+ userQuesList[1]['description'] +', from  '+ userQuesList[1]['country'])

  maxCnt,idx=getMaxCnt(userQuesList) 
  userVal=input('Who has more followers? Type \'A\' or \'B\'')

  userScoreCal=get_user_score(userVal,maxCnt,userQuesList)
  if int(userScoreCal) == 0:
    userScore+=1
    userQuesList.pop(idx)
    os.system('clear')   
    print(win)    
  else:
    print(loose)
    loss=True

print('Your Score : '+str(userScore))
#print(userQuesList)