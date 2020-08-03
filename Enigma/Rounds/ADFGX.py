import numpy as np

op = input("Do you want to encrypt [E] or decrypt [D] using ADFGVX cypher?")
key1,key2 = input("Enter the 2 keywords: ").split()   

klist = []
for char in key1.lower():
   if char not in klist:
      klist.append(char)
psqchars = klist + list((chr(char+ord('a'))) for char in range(26) if chr(char+ord('a')) not in key1.lower()) + list(str(num) for num in range(10) if str(num) not in key1.lower())

psq = []
n=0
while n<=len(psqchars)-6:
   psq.append(psqchars[n:n+6])
   n+=6
psq=np.array(psq)

if op=='E' or op=='e':
   c1 = {0:'a', 1:'d', 2:'f', 3:'g', 4:'v', 5:'x'}
   text = list(input("Enter text to encrypt: "))
   while ' ' in text:
      text.remove(' ')
      
   cpairs = []
   for char in text:
      x,y = np.where(psq==char)[0][0],np.where(psq==char)[1][0]
      cpairs.extend([c1[x],c1[y]])

   sq2 = []
   n=0
   while len(cpairs)%len(key2):
      cpairs.append(' ')
   while n<=len(cpairs)-len(key2):
      sq2.append(cpairs[n:n+len(key2)])
      n+=len(key2)
   sq2=np.transpose(np.array(sq2))
   print(sq2)
   
   key2c = list(key2)
   sqfinal = []
   while key2c!=['~']*len(key2):
      sqfinal.append(sq2[key2c.index(min(key2c))])
      key2c[key2c.index(min(key2c))]='~'
   sqfinal = np.array(sqfinal)
   
   finalstr=''
   for array in sqfinal:
      for char in array:
         finalstr+=char
      finalstr+=' '
  
  print(finalstr)
   
elif op=='D' or op=='d':
   text = input("Enter text to decrypt: ")
   sqfinal1 = np.array(list(text.split()))
   key2c = list(key2)
   sqfinal = [None]*len(key2)
   i=0
   while key2c!=['~']*len(key2):
      #print(key2c, key2c.index(min(key2c)))
      sqfinal[key2c.index(min(key2c))] = (sqfinal1[i])
      key2c[key2c.index(min(key2c))]='~'
      i+=1
   sqfinal = np.array(sqfinal)
   
   sq2=[]
   maxval = len(max(sqfinal,key=len))
   for line in sqfinal:
      line=list(line)
      while len(line)<maxval:
         line.append(' ')
      sq2.append(line)
   sq2=np.transpose(np.array(sq2))
   
   interlist=[]
   for array in sq2:
      for char in array:
         if char != ' ':

   cfinal = {'a':0, 'd':1, 'f':2, 'g':3, 'v':4, 'x':5}
   finalstr=''
   for idx in range(0,len(interlist)-1,2):
      x,y = cfinal[interlist[idx]],cfinal[interlist[idx+1]]
      finalstr+=psq[x][y]

   print(finalstr)

