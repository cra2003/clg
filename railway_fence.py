s="karth"
Rails=1

l=[]
count=0
for i in range(Rails+1):
    l.append([])
def enc(s,Rails):
    flag=1
    ind=0
    for i in s:
        if flag:
            l[ind].append(i)
            ind+=1
            if ind==Rails:
                flag=0
        else:
            l[ind].append(i)
            ind-=1
            if ind==0:
                flag=1
    #print(l)
    encry=''
    for j in l:
        for k in j:
            encry+=k
    return encry

encryption=enc(s,Rails)
print(encryption)

def dec(encryption,Rails):
    mat=[]
    for i in range(Rails+1):
        samp=[]
        for j in range(len(encryption)):
            samp.append('-')
        mat.append(samp)
    flag=1
    row=0
    for k in range(len(encryption)):
        if flag:
            mat[row][k]='*'
            row+=1
            if row==Rails:
                flag=0
        else:
            mat[row][k]='*'
            row-=1
            if row==0:
                flag=1
    #print(mat)
    ind=0
    for t in range(Rails+1):
        for r in range(len(encryption)):
            if mat[t][r]=='*':
                mat[t][r]=encryption[ind]
                ind+=1
                if ind==len(encryption):
                    break
    #print(mat)
    
    decr=''
    flag=1
    row=0
    for k in range(len(encryption)):
        if flag:
            decr+=mat[row][k]
            row+=1
            if row==Rails:
                flag=0
        else:
            decr+=mat[row][k]
            row-=1
            if row==0:
                flag=1
    print(decr)
dec(encryption,Rails)
