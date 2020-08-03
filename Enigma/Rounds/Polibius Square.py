plain = input("Enter plaintext : ").upper()
key = input("Enter key : ").upper()
temp=''
for i in key:
    if i not in temp:
        temp+=i
key = temp
alphabets = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
combi = key
for i in alphabets:
    if i not in combi:
        combi+=i
mixed = {}
ctr = 0
for i in range (1,6):
    for j in range (1,6):
        mixed[combi[ctr]]=(j,i)
        ctr+=1
cipher = ''
temp = plain.split()
for i in temp:
    for j in i:
        if j!='J':
            cipher+= str(mixed[j][0])+str(mixed[j][1])
        else:
            cipher+= str(mixed['I'][0])+str(mixed['I'][1])
    cipher+=' '
print(cipher)
        
        

