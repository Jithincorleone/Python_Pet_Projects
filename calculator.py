import os

def printLogo(userInput):
  logo = '''
 _____________________
|  _________________  |
| |'''+userInput+''' 
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| | 
|_____________________|
'''
  return logo 


cond=True
operatorList=['+','-','/','*']
valList=[]

def add(a,b):
  return int(a)+int(b)

def multiply(a,b):
  return int(a)*int(b)

def subtract(a,b):
  return int(a)-int(b)

def divide(a,b):
  return round(int(a)/int(b))

def main(userInput):
  operator=''
  userNumInput=[]
  
  for i in range(0,len(userInput)):    
    if operatorList.count(userInput[i]) == 1:
      operator=userInput[i]
  
  userNumInput=userInput.split(operator)
  if operator=='+':
    val=add(userNumInput[0],userNumInput[1])
  elif operator=='-':
    val=subtract(userNumInput[0],userNumInput[1])
  elif operator=='*':
    val=multiply(userNumInput[0],userNumInput[1])
  elif operator=='/':
    val=divide(userNumInput[0],userNumInput[1])

  valList.append(val) 
  return val  

def check_operator_cnt(userInput):
  operatorCnt=0
  
  for i in range(0,len(userInput)):
    if operatorList.count(userInput[i]) >= 1:
      operatorCnt=int(operatorCnt)+1
    
  if operatorCnt > 1 :
    return 1
  else:
    return 0
  
displayInput=''
userInput=''
totalOperators=''

while cond:
  if len(valList)==0:
     print(printLogo(displayInput))    
     userInput=input('Enter numbers, Type Q to quit, Type C to clear : ')     
     return_cd=check_operator_cnt(userInput)
  else:
    displayInput=str(valList[-1])
    print(printLogo(displayInput))    
    userInput=input('Enter numbers, Type Q to quit, Type C to clear : '+str(valList[-1])+' ')
    return_cd=check_operator_cnt(userInput)
    
  os.system('clear')

  if return_cd == 1:
    displayInput='Only 1 operator allowed at a time'
    userInput=''
    valList=[]
    continue
    
  if 'C' in userInput.upper():
    displayInput=''
    userInput=''
    valList=[]
    continue
  if 'Q' in userInput.upper():
    cond=False
    break
    
  if len(valList) != 0 :
    userString=str(valList[-1])+userInput
    val=main(userString)
  else:
    val=main(userInput)

  #print(val)

  
