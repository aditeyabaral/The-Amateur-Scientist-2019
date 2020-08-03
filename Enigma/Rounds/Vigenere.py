def generateKey(string, key): 
    key = list(key) 
    if len(string) == len(key): 
        return(key) 
    else: 
        for i in range(len(string) - 
                       len(key)): 
            key.append(key[i % len(key)]) 
    return("" . join(key)) 
      
# This function returns the  
# encrypted text generated  
# with the help of the key 
def cipherText(string, key): 
    cipher_text = []
    for i in range(len(string)):
        if string[i]==' ':
            cipher_text.append(' ')
        else:
            x = (ord(string[i]) + 
                 ord(key[i])) % 26
            x += ord('A') 
            cipher_text.append(chr(x))
    return("" . join(cipher_text)) 
      
# This function decrypts the  
# encrypted text and returns  
# the original text 
def originalText(cipher_text, key): 
    orig_text = [] 
    for i in range(len(cipher_text)): 
        if cipher_text[i]==' ':
            orig_text.append(' ')
        else:
            x = (ord(cipher_text[i]) - 
                ord(key[i]) + 26) % 26
            x += ord('A') 
            orig_text.append(chr(x)) 
    return("" . join(orig_text)) 
      
# Driver code 
if __name__ == "__main__": 
    string = '''FO CSOEUR CSMNEIAH TNONCA HKNIT AS PEELPO OD.
A MNEACHI IS DEERFTINF ROFM A OSENPR EECHN EHYT HTKIN NLDRIETFFYE.
HET EGEISTNNRIT QUENITOS IS TUJS SECEUAB MSHOEIGTN NITSKH LDFFNEIETRY FMOR YOU DOSE TATH NMEA TI IS TNO KNGNHIIT?
LLWE EW LWLOA FOR SUAMHN TO AEHV UHCS VSERNIEEGCD RFOM ONE RNOTEAH.
YUO EKIL RSTSWIRREEAB, I EAHT IGNCAKEST.
I OYU RCY AT ASD SMFIL, I AM RILALCEG OT LLNPOE.
ATWH IS TEH PIOTN FO TNERIDEFF ASTTSE IFDREFTEN ECERSENEFRP FI ONT TO YSA ATHT RUO ASNRBI ROKW RTNILFDFYEE, TTHA WE KNTHI FYIREFELTDN?
DNA IF WE ACN SYA TAHT BOTUA NEO AONHTRE THNE YWH CNTA WE YAS THE SMAE NIGTH OFR BNISAR UILTB OF PPRCOE, IREW DNA ELTSE?
GTUASLNAOIROTNC OUY AHVE KROBNE IMANGE.'''
    keyword = "SOMETIMESITISTHEPEOPLENOONEIMAGINESANYTHINGOFWHODOTHETHINGSTHATNOONECANIMAGINE"
    key = generateKey(string, keyword) 
    cipher_text = cipherText(string,key) 
    print("Ciphertext :", cipher_text) 
    print("Original/Decrypted Text :",  
    originalText(cipher_text, key)) 
