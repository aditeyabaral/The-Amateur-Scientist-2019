plain = input("Enter plaintext : ").upper()
n = int(input("Enter shift : "))
cipher = ''
temp = plain.split()
for i in temp:
    for j in i:
        cipher+=chr((ord(j) + n-65) % 26 + 65)
    cipher+=' '
print(cipher)
