import random

letters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers=[0,1,2,3,4,5,6,7,8,9]
symbols=["!","@","#","$","%","^","&","*","(",")","[","]",";",":","<",">","?"]

alphaList=[]
numList=[]
symbolList=[]
baseList=[]
randList=[]
val=0
finalStr=''

alphaCnt=int(input("How many letters would you like in your password?\n"))
numCnt=int(input("How many numbers would you like in your password?\n"))
symbolCnt=int(input("How many symbols would you like your password?\n"))

if alphaCnt <= len(letters):
  for num in range(0, alphaCnt):
    while randList.count(val) >= 1 :
      val=random.randint(0,len(letters)-1)

    randList.append(val)    
      
  for num in range(0, len(randList)):
    alphaList.append(letters[int(randList[num])])
    
else:
  for num in range(0, alphaCnt):
    val=random.randint(0,len(letters)-1)
    alphaList.append(letters[val])

val = 0
randList=[]

if numCnt <= len(numbers) :
  for num in range(0, numCnt):
    while randList.count(val) >=1 :
      val=random.randint(0,len(numbers)-1)  
    randList.append(val)

  for num in range(0, len(randList)):
    numList.append(numbers[int(randList[num])])
else:
  for num in range(0, numCnt):  
    val=random.randint(0,len(numbers)-1)
    numList.append(numbers[val])

val=0
randList=[]

if symbolCnt <= len(symbols) :
  for num in range(0, symbolCnt):
    while randList.count(val) >=1 :
      val=random.randint(0,len(symbols)-1)  
    randList.append(val)

  for num in range(0, len(randList)):
    symbolList.append(symbols[int(randList[num])])
else:
  for num in range(0, symbolCnt):
    val=random.randint(0,len(symbols)-1)
    symbolList.append(symbols[val])

baseList.extend(alphaList)
baseList.extend(numList)
baseList.extend(symbolList)

val=0
randList=[]
for num in range(0,len(baseList)):

  while randList.count(val) >= 1 :
    val=random.randint(0,len(baseList)-1)
  
  randList.append(val) 

#print(baseList)
#print(randList)

for num in range(0, len(randList)):
  finalStr=finalStr+str(baseList[int(randList[num])])

print("Generated password is : " + finalStr)