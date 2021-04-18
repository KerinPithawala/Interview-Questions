innum=int(input())
inbase=int(input())
fin=""

while(innum>0):
    rem=innum%inbase
    innum=innum//inbase
    #print(rem)
    fin+=str(rem)
    
fin=fin[::-1]
maxC=0
curr=0
for i in range(0,len(fin)):
    if(fin[i]=='0'):
        curr=1
        while(i+1<len(fin) and fin[i+1]=='0'):
            curr+=1
            i+=1
    maxC=max(maxC,curr)
    
print(maxC)