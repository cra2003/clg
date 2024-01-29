s='kart'
key=2 

def enc(s,key):
    encry=''
    for i in s:
        encry+=chr(ord(i)+2)
    return encry
    
encryption=enc(s,key)
print(encryption)

def dec(encryption,key):
    decr=''
    for i in encryption:
        decr+=chr(ord(i)-2)
    return decr
print(dec(encryption,key))
