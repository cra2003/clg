string="geeksforgeeks"
key="AIDS"

n=len(key)
i=0
l=[]
temp=[]
for i in range(len(string)):
    if len(temp)<4:
        temp.append(string[i])
    else:
        l.append(temp)
        temp=[string[i]]
if temp:
    l.append(temp)
#print(l)

def enc(key,l):
    encry=''
    ref=[]
    sorted_key=sorted(key)
    for i in sorted_key:
        ref.append(key.index(i))
    for j in ref:
        for k in l:
            if len(k)>j:
                encry+=k[j]
    return encry
encryption=enc(key,l)
print(encryption)

def dec(encryption,key):
    decl=[]
    sorted_key=sorted(key)
    ref=[]
    for i in sorted_key:
        ref.append(key.index(i))
    multiple=len(encryption)//len(key)
    remain=len(encryption)%len(key)
    for k in range(multiple):
        decl.append([])
    if remain!=0:
        decl.append([])
    for j in ref:
        count=0
        if j<remain:
            ptr=(multiple*j)
            for k in range(len(decl)):
                decl[k].append(encryption[ptr])
                ptr+=1
        else:
            ptr=(multiple*j)+remain
            for k in range(multiple):
                decl[k].append(encryption[ptr])
                ptr+=1
    decipher=''
    for g in decl:
        for gf in g:
            decipher+=gf
    return decipher
        
print(dec(encryption,key))
