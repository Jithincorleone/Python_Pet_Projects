import time
import os
import random

hangmanDies='''
   ______________.
   |             | 
   |             |
   |             O
   |            \|/ 
   |             |
   |            / \\
   |     
___|____

HANGMAN DIES!!! YOU LOOSE!!
'''
hangmanWins='''
   ______________.
   |             | 
   |             |
   |             
   |              
   |             O \\
   |            /| - 
   |             | 
___|______      / \\

HANGMAN LIVES!!! YOU WIN!!
'''




hangmanImage=['''
    ______
   |      |
   |      |
   |      O 
   | 
   | 
___|____
''',
'''
    ______
   |      |
   |      |
   |      O
   |      |
   | 
___|____
''',
'''
    ______
   |      |
   |      |
   |      O
   |      |/
   | 
___|____
''',
'''
    ______
   |      |
   |      |
   |      O
   |     \|/
   | 
___|____
''',
'''
    ______
   |      |
   |      |
   |      O
   |     \|/
   |     / 
___|____
''',
'''
    ______
   |      |
   |      |
   |      O
   |     \|/
   |     / \\
___|____

''']

titleImage= '''
 --        --          --         ----        -      .-----------    --              --           --          ----        -
|  |      |  |       /    \       | |\ \     | |    /    .-------|  |    \         /    |       /    \       | |\ \     | |
|  |      |  |      / /--\ \      | | \ \    | |   /    /           |  ^  \       /  ^  |      / /--\ \      | | \ \    | | 
|  |------|  |     / /    \ \     | |  \ \   | |  (    /      --    | | \  \     /  / | |     / /    \ \     | |  \ \   | | 
|  |------|  |    / /------\ \    | |   \ \  | |   \   (     |  |   | |  \  \   /  /  | |    / /----- \ \    | |   \ \  | |
|  |      |  |   / /------- \ \   | |    \ \ | |    \   \    |  |   | |   \  \ /  /   | |   / /------  \ \   | |    \ \ | |
|  |      |  |  / /          \ \  | |     \ \| |     \   \----  |   | |    \     /    | |  / /          \ \  | |     \ \| | 
 --        --   --            --  --      -----       '------- '    --       ---       --  --            --   --      ----
''' 

wordList=["BEKEPER","CAPABLE","DEFENCE","EVENING","FEATURE","GALLERY","KANDULAKUMAR"]
displayList=[]
posList=[]
displayString=""
pos=-1

def get_displayList(p_list):
  l_string=''
  for i in range(0,len(p_list)):
    l_string+=' '+str(displayList[i])  
  print(l_string)
    
mainString=wordList[random.randint(0,len(wordList)-1)]
print(titleImage)
print('mainString : '+mainString)

for i in range(0,len(mainString)):
  displayList.append("_")

while displayList.count('_') >0 :
    
  get_displayList(displayList)
  posList=[]
  userInput=input("Guess a letter. ").upper()
  os.system('clear')
  if mainString.count(userInput) > 0 :
    for i in range(0,len(mainString)):
      if mainString[i] == userInput :
        posList.append(i)
    for i in range(0,len(posList)):
      displayList[posList[i]]=userInput
  else:
    pos=pos+1
    if pos==len(hangmanImage):
      break  
    print(userInput+' : is not part of the letters. bad Guess. Hangman dies by 1..')
    print(hangmanImage[int(pos)])

if pos==len(hangmanImage):
  print(hangmanDies)
elif displayList.count('_')==0:
  print(hangmanWins)
  
get_displayList(displayList)