s="instruments"
key="monarchy"

key_arr=[]
alp='abcdefghijklmnopqrstuvwxyz'
d={}
for k in alp:
    d[k]=0
#print(d)
for i in range(5):
    samp=[]
    for j in range(5):
        samp.append('-')
    key_arr.append(samp)
ind=0
flag=1
for i in range(5): 
    for j in range(5):
        #print(key_arr)
        if key[ind]=='i' or key[ind]=='j':
            key_arr[i][j]='ij'
            d['i']=1
            d['j']=1
            ind+=1
            if ind==len(key):
                flag=0
                break
        else:
            key_arr[i][j]=key[ind]
            d[key[ind]]=1
            ind+=1 
            if ind==len(key):
                flag=0
                break
    if flag==0:
        break
#print(d)
s_ind=0
flag=0
for i in range(5):
    for j in range(5):
        while key_arr[i][j]=='-':
            
            if d[alp[s_ind]]==1:
                s_ind+=1 
                if s_ind==len(alp):
                    flag=1
                    break
            else:
                res=alp[s_ind]
                if alp[s_ind]=='i' or alp[s_ind]=='j':
                    res='ij'
                    d['i']=1
                    d['j']=1
                key_arr[i][j]=res
                s_ind+=1
                if s_ind==len(alp):
                    flag=1
                    break
    if flag:
        break
print(key_arr)
               
def encc(l,x):
    first=x[0]
    second=x[1]
    enc_first=''
    enc_second=''
    first_i=first_j=second_i=second_j=-1
    for i in range(5):
        for j in range(5):
            if len(l[i][j])==1:
                if l[i][j]==first:
                    first_i=i 
                    first_j=j
                elif l[i][j]==second:
                    second_i=i
                    second_j=j
            else:
                if l[i][j][0]==first or l[i][j][1]==first:
                    first_i=i 
                    first_j=j
                elif l[i][j][0]==second or l[i][j][1]==second:
                    second_i=i
                    second_j=j
    if first_i==second_i:
        #print(second_j)
        if first_j!=4:
            enc_first=l[first_i][first_j+1][0]
        else:
            enc_first=l[first_i][0][0]
        if second_j!=4:
            enc_second=l[second_i][second_j+1][0]
        else:
            enc_second=l[second_i][0][0]
    
    elif first_j==second_j:
        
        if first_i!=4:
            enc_first=l[first_i+1][first_j][0]
        else:
            enc_first=l[0][first_j][0]
        if second_i!=4:
            enc_second=l[second_i+1][second_j][0]
        else:
            enc_second=l[0][second_j][0] 
    else:
        enc_first=l[first_i][second_j][0]
        enc_second=l[second_i][first_j][0]
    
    return enc_first+enc_second
        
    
#encr=encc(key_arr,'in')
#print(encr)

enc_list=[]
strr=''
flag=1
for i in s:
    if flag:
        strr+=i
        flag=0
    else:
        strr+=i
        enc_list.append(strr)
        strr=''
        flag=1
if len(strr):
    enc_list.append(strr+'z')

encryption=''
for element in enc_list:
    encryption+=encc(key_arr,element)
print(encryption)


def decc(l,x):
    first=x[0]
    second=x[1]
    enc_first=''
    enc_second=''
    first_i=first_j=second_i=second_j=-1
    for i in range(5):
        for j in range(5):
            if len(l[i][j])==1:
                if l[i][j]==first:
                    first_i=i 
                    first_j=j
                elif l[i][j]==second:
                    second_i=i
                    second_j=j
            else:
                if l[i][j][0]==first or l[i][j][1]==first:
                    first_i=i 
                    first_j=j
                elif l[i][j][0]==second or l[i][j][1]==second:
                    second_i=i
                    second_j=j
    if first_i==second_i:
        #print(second_j)
        if first_j!=0:
            enc_first=l[first_i][first_j-1][0]
        else:
            enc_first=l[first_i][4][0]
        if second_j!=0:
            enc_second=l[second_i][second_j-1][0]
        else:
            enc_second=l[second_i][4][0]
    
    elif first_j==second_j:
        
        if first_i!=0:
            enc_first=l[first_i-1][first_j][0]
        else:
            enc_first=l[4][first_j][0]
        if second_i!=0:
            enc_second=l[second_i-1][second_j][0]
        else:
            enc_second=l[4][second_j][0] 
    else:
        enc_first=l[first_i][second_j][0]
        enc_second=l[second_i][first_j][0]
    
    return enc_first+enc_second


decc_list=[]
decryption=''
strr=''
flag=1
for i in encryption:
    if flag:
        strr+=i
        flag=0
    else:
        strr+=i
        decc_list.append(strr)
        strr=''
        flag=1
print(decc_list)

for ele in decc_list:
    decryption+=decc(key_arr,ele)
decryption=decryption[:len(s)]
print(decryption)

