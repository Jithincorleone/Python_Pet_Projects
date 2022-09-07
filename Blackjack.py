import random
import os

emojiDict=[
  {"Houses" : {
  "Spades" : u"\u2660",
  "Hearts" : u"\u2665",
  "Diamonds" : u"\u25C6",
  "Clubs" : u"\u2663"
  }},
  {"Special" : {
  "K" : u"\u265A",
  "Q" : u"\u265B",
  "A" : "A",
  "J" : u"\u2657"}}
]

cardDrawList=[{"1":["Face",1]},
              {"2":["Face",2]},
              {"3":["Face",3]},
              {"4":["Face",4]},
              {"5":["Face",5]},
              {"6":["Face",6]},
              {"7":["Face",7]},
              {"8":["Face",8]},
              {"9":["Face",9]},
              {"10":["Face",10]},
              {"A":["Special",11,1]},
              {"Q":["Special",10]},
              {"J":["Special",10]},
              {"K":["Special",10]}]

houseList=["Spades","Hearts","Diamonds","Clubs"]
playersPlayInfo=[]
l_dealerDefault=  u"\U0001F0A0"
#print(dealerDefault)

def get_houseEmoji(p_house):
  val=emojiDict[0]["Houses"][p_house]
  return val

def get_specialEmoji(p_house):
  val=emojiDict[1]["Special"][p_house]
  return val

def dealerDefault(a):
  card='''
 ______________
|'''+a+a+a+a+a+a+a+a+a+a+a+a+a+a+'''|                   
|'''+a+a+a+a+a+a+a+a+a+a+a+a+a+a+'''|
|'''+a+a+a+a+a+a+a+a+a+a+a+a+a+a+'''|        
|'''+a+a+a+a+a+a+a+a+a+a+a+a+a+a+'''|
|'''+a+a+a+a+a+a+a+a+a+a+a+a+a+a+'''| 
|'''+a+a+a+a+a+a+a+a+a+a+a+a+a+a+'''|
|'''+a+a+a+a+a+a+a+a+a+a+a+a+a+a+'''|
|'''+a+a+a+a+a+a+a+a+a+a+a+a+a+a+'''|
|'''+a+a+a+a+a+a+a+a+a+a+a+a+a+a+'''|
|'''+a+a+a+a+a+a+a+a+a+a+a+a+a+a+'''|
'--------------'
  '''
  return card

def renderCards(a,b,c,d):
  card=''
  if b=="Face":
    if int(a)==10:
      card='''
 ______________
|'''+a+'''            |                   
|              |
|              |        
|              |
|              | 
|       '''+d+'''      |
|              |
|              |
|              |
|            '''+a+'''|
'--------------'
'''
    else:
      card='''
 ______________
|'''+a+'''             |                   
|              |
|              |        
|              |
|              | 
|       '''+d+'''      |
|              |
|              |
|              |
|             '''+a+'''|
'--------------'
      '''      
  if b=="Special":
    e=get_specialEmoji(a)
  #  print(e)
    card='''
 ______________
|'''+a+'''           '''+e+''' |                   
|              |
|              |        
|              |
|              | 
|       '''+d+'''      |
|              |
|              |
|              |
|'''+e+'''            '''+a+'''|
'--------------'
'''
  return card

def hit():
  idx=random.randint(0,len(cardDrawList)-1)
  houseidx=random.randint(0,len(houseList)-1)
# idx=4
# houseidx=2
  housePicked=houseList[houseidx]
  houseEmoji=get_houseEmoji(housePicked)
  
  for key in cardDrawList[idx]:
    cardDraw=key
    cardType=cardDrawList[idx][key][0]
    cardVal=cardDrawList[idx][key][1]

#print(cardDraw)
#print(cardVal)
#print(housePicked)
#print(houseEmoji)
    card=renderCards(cardDraw,cardType,housePicked,houseEmoji)
    return card,cardDraw,cardVal

def players_info_int(p_no_players, p_player_name):
  for i in range(0,int(no_players)):
    playername=p_player_name+str(i)
    playerDict={
      playername:{"Trail":[],
                  "Card_Name":[],
                  "Cards":[],
                  "Card_Val":[],
                  "Score":''
                 }
    }
    playersPlayInfo.append(playerDict)


def get_cards_sum(p_index,p_player):
  val=0
  playerCardVal=playersPlayInfo[p_index][p_player]['Card_Val']
  for i in range (0,len(playerCardVal)):
    val=val+int(playerCardVal[i])
  return val  

def get_winner(p_player, p_score):
  dealer_score=str(playersPlayInfo[-1]["Dealer"]["Score"])
  print('dealer_score : '+str(dealer_score))
  if int(dealer_score) != 0:
    if int(dealer_score) > 21 :
      return p_player
    elif int(dealer_score)==21:
      return 'Dealer'
    elif int(p_score) > int(dealer_score) :
      return p_player
    else :
      return 'Dealer'
  return p_player
      
  

  
####################################################1
#
#                     
#                     Main
#    
####################################################
    
no_players=input('Enter number of players .. ')
players_info_int(no_players,'Player_') 

for idx in range(0,len(playersPlayInfo)):
  for key,value in playersPlayInfo[idx].items():
    print("Drawing cards for : "+str(key))
    for i in range(1,3):
      card,cardDraw,cardVal=hit()
      playersPlayInfo[idx][key]['Trail'].append(int(i))
      playersPlayInfo[idx][key]['Card_Name'].append(str(cardDraw))
      playersPlayInfo[idx][key]['Cards'].append((str(card)))
      playersPlayInfo[idx][key]['Card_Val'].append((str(cardVal)))

    print(str(playersPlayInfo[idx][key]['Cards'][0])+str(playersPlayInfo[idx][key]['Cards'][1]).rstrip())

print('\nDrawing cards for Dealer : ')
card,cardDraw,cardVal=hit()
DealerDict={"Dealer":{"Trail":[1,2],
                        "Card_Name":[cardDraw,0],
                        "Cards":[card,dealerDefault(l_dealerDefault)],
                         "Card_Val":[cardVal,0],
                          "Score":''
                     },
           }
playersPlayInfo.append(DealerDict)
print(str(playersPlayInfo[-1]["Dealer"]['Cards'][0])+str(playersPlayInfo[-1]["Dealer"]['Cards'][1]))

p_action=''
p_net_player=len(playersPlayInfo)-1
idx=-1

#print('p_net_player : '+str(p_net_player))
p_round=0

while int(p_net_player) != 0 :
  dealer_score=0
  p_action=''
  idx=int(idx)+1

  if int(p_round) == int(p_net_player):
    print("Dealer card flipped..")
    card,cardDraw,cardVal=hit()
    playersPlayInfo[-1]["Dealer"]["Trail"].pop()
    playersPlayInfo[-1]["Dealer"]["Card_Name"].pop()
    playersPlayInfo[-1]["Dealer"]["Cards"].pop()
    playersPlayInfo[-1]["Dealer"]["Card_Val"].pop()
    #playersPlayInfo[-1]["Dealer"]["Score"].pop()
    
    playersPlayInfo[-1]["Dealer"]["Trail"].append(2)
    playersPlayInfo[-1]["Dealer"]["Card_Name"].append(str(cardDraw))
    playersPlayInfo[-1]["Dealer"]["Cards"].append((str(card)))
    playersPlayInfo[-1]["Dealer"]["Card_Val"].append((str(cardVal)))
    #print(playersPlayInfo[-1]["Dealer"])
    for card in range(0,len(playersPlayInfo[-1]["Dealer"]["Cards"])) :
      print(str(playersPlayInfo[-1]["Dealer"]['Cards'][card]))
      
    dealer_score=get_cards_sum(len(playersPlayInfo)-1,'Dealer')
    
    while int(dealer_score) < 16 :
      #dealer_score=get_cards_sum(len(playersPlayInfo)-1,'Dealer')
      print('Dealer score : '+str(dealer_score))
      print('Dealer score is less than 16.')
      print('Dealer draws another card.')
      card,cardDraw,cardVal=hit()
      playersPlayInfo[-1]["Dealer"]["Trail"].append(2)
      playersPlayInfo[-1]["Dealer"]["Card_Name"].append(str(cardDraw))
      playersPlayInfo[-1]["Dealer"]["Cards"].append(str(card))
      playersPlayInfo[-1]["Dealer"]["Card_Val"].append(str(cardVal))      
      dealer_score=get_cards_sum(len(playersPlayInfo)-1,'Dealer')

    dealer_score=get_cards_sum(len(playersPlayInfo)-1,'Dealer')
    print('Dealer has now score : '+ str(dealer_score) +' with following cards.')  
    for card in range(0,len(playersPlayInfo[-1]["Dealer"]["Cards"])) :
      print(str(playersPlayInfo[-1]["Dealer"]['Cards'][card]))

    playersPlayInfo[-1]["Dealer"]["Score"]=dealer_score
    break  
    
  currPlayer='Player_'+str(idx)
  
  score=get_cards_sum(idx,currPlayer)

  if score == 21 :
    print(currPlayer+'has perfect BLACKJACK.. They Win!!!')
    p_net_player=p_net_player-1
    continue
    
  while p_action.upper() != 'S':
    p_action=input(currPlayer+' : Press H to Hit, S to Stay ' )
    if str(p_action).upper()=='H':
      card,cardDraw,cardVal=hit()
      trial=3
      playersPlayInfo[idx][currPlayer]['Trail'].append(int(trial))
      playersPlayInfo[idx][currPlayer]['Card_Name'].append(str(cardDraw))
      playersPlayInfo[idx][currPlayer]['Cards'].append((str(card)))
      playersPlayInfo[idx][currPlayer]['Card_Val'].append((str(cardVal)))
      os.system('clear')
      print(currPlayer+' cards :')
      for card in range(0,len(playersPlayInfo[idx][currPlayer]['Cards'])) :
        print(str(playersPlayInfo[idx][currPlayer]['Cards'][card]))
      score=get_cards_sum(idx,currPlayer)
      print(score)
      if score > 21 :
        print(currPlayer+' BUST!! '+currPlayer+' looses!!')
        p_net_player=p_net_player-1
        break
      if score == 21 :
        print(currPlayer+'has perfect BLACKJACK.. They Win!!!')
        p_net_player=p_net_player-1
        break
        
        #exit()

  playersPlayInfo[idx][currPlayer]["Score"]=score
  if str(p_action).upper()=='S':
    p_round=int(p_round)+1
    continue


for i in range(0, len(playersPlayInfo)-1):
 # os.system('clear')
  currPlayer='Player_'+str(i)
  if int(playersPlayInfo[i][currPlayer]["Score"]) == 21 :
#    print(currPlayer+' has pefect BLACKJACK!!..He wins!!')
    continue

  if int(playersPlayInfo[i][currPlayer]["Score"]) >= 21 :
    continue
  
  winner=get_winner(currPlayer,(playersPlayInfo[i][currPlayer]["Score"]))
  print(currPlayer +"\'s final cards and score : "+ str(playersPlayInfo[i][currPlayer]["Score"]))
  for card in range(0,len(playersPlayInfo[i][currPlayer]['Cards'])) :
    print(str(playersPlayInfo[i][currPlayer]['Cards'][card]))  
  print("Dealer's final cards and score : " + str(playersPlayInfo[-1]["Dealer"]["Score"]))
  
  for card in range(0,len(playersPlayInfo[-1]["Dealer"]["Cards"])) :
      print(str(playersPlayInfo[-1]["Dealer"]['Cards'][card]))
  
  if winner=='Dealer':
    print("Player_"+str(i)+' looses the hand to dealer.!!')
  else:  
    print(winner+' wins the hand against Dealer!!')  
  # print('Player_'+str(i)+' score : '+str(playersPlayInfo[i]["Player_"+str(i)]["Score"]))
  # print('Dealer score : ' +str(playersPlayInfo[-1]["Dealer"]["Score"]))
  