s='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

text="ABCD"
key='CD'

n=len(text)//len(key)
t=len(text)%len(key)

keytext=(key*n)+key[:t]

l=[]
for i in range(26):
    l.append(list(s[i:]+s[:i]))
    
def enc(text,keytext):
    ency=""
    for i in range(len(text)):
        ency+=l[ord(text[i])-65][ord(keytext[i])-65]
    return ency

encr=enc(text,keytext)
print(encr)



def dec(text,keytext):
    decy=''
    for i in range(len(text)):
        decy+=chr(l[ord(keytext[i])-65].index(text[i])+65)
    return decy
    
print(dec(encr,keytext))
