theList=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
exitvar=False

def encryptdecrypt(p_input, p_key, p_val):
  inputList=[]
  word=''
  for i in range(0, len(p_input)):
    for y in range(0, len(theList)):
      if str(p_input[i]) == str(theList[y]):
        if int(p_val) == 0 :
          idx=y+int(p_key)
        if int(p_val) == 1 :
          idx=y-int(p_key)       
        
        if idx > len(theList)-1:
          
          diff=idx-len(theList)
          idx=diff
        elif idx < 0 :
          diff=len(theList)+idx
          idx = diff  
        
        inputList.append(theList[idx])

  for i in range(0,len(inputList)):
    word=word+str(inputList[i])

  if int(p_val) == 0 :
    print('encoded word is : '+word)
  elif int(p_val) == 1 :
    print('decoded word is : '+word)    

def start():
  val=input('Type 0 to encode, 1 to decode. ')
  if int(val)==0:
    userInput=input('Type the word to be encoded. ')
  else:
    userInput=input('Type the word to be decoded. ')
  
  key=input('Type shift digit. ')
  
  encryptdecrypt(p_input=userInput, p_key=key, p_val=val)


while not exitvar:
  start()
  tryAgain=input('Do you want to run again. Y/N ').upper()
  if tryAgain=='Y':
    continue
  else:
    exitvar=True

print('\nBYE!!')