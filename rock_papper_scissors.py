import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

win = '''   
    / \
   |   | 
---'    ________
          ______)
          _______)
         _______)
---.__________)
'''

loss = '''
-----------------
            ______)
            _______)
           _______)
-- '      _______)
   |   |
    \ / 
'''

Draw = '''
         /  \
         |  | /  \
     /^\ |  | |  |
 ^  |  | |  | |  |    ^
| |.|  |.|  |.|  |../  / 
 \                    / 
  \                  /
   \                /
'''

#Write your code below this line 👇

userInput=int(input('What do yu choose? Type 0 for Rock, 1 for Scissors, 2 for Paper \n'))
print("\n")
rockList=['0', rock, "Rock"]
paperList=['1', paper, "Paper"]
scissorList=['2', scissors, "Scissors"]
winList=['3', win, "You Win!!"]
lossList=['4', loss, "You Loose!!"]
DrawList=['5', Draw, "Draw.. Try Again!"]

MainList=[rockList, paperList, scissorList, winList, lossList, DrawList]
print("\n")

print('You Choose : ' + str(MainList[userInput][2]))
print(MainList[userInput][1])

val=random.randint(0,2)

print("Computer chooses : " + str(MainList[val][2]))
print(MainList[val][1])

if userInput == 0 and val == 1 :  # Rock + paper
  print(MainList[4][2])      # loose
  print(MainList[4][1])
elif userInput == 0 and val == 2 : # Rock + Scissor
  print(MainList[3][2])      # win
  print(MainList[3][1])
elif userInput == 1 and val == 0 : #Paper + Rock
  print(MainList[3][2])       #win
  print(MainList[3][1])
elif userInput == 1 and val == 2 : #Paper + Scissor
  print(MainList[4][1])       #loose
  print(MainList[4][2])
elif userInput == 2 and val == 0 : # Scissor + Rock
  print(MainList[4][1])       #Loose
  print(MainList[4][2])
elif userInput == 2 and val == 1 :  # Scissor + Paper
  print(MainList[3][1])         # Win
  print(MainList[3][2])
elif userInput == 0 and val == 0 :  # Rock + Rock
  print(MainList[5][1])
  print(MainList[5][2])
elif userInput == 1 and val == 1 :  # Paper + Paper
  print(MainList[5][1])
  print(MainList[5][2])
elif userInput == 2 and val == 2 :  # Scissors + Scissors
  print(MainList[5][1])
  print(MainList[5][2])
