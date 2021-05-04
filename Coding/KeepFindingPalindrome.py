def checkPali(num):
    return str(num)==str(num)[::-1]

def findPrev(nums):
    while(nums>=0):
        if checkPali(nums):
            return nums
        else:
            nums-=1
           
def findNext(nums):
    while(nums<=99999):
        if checkPali(nums):
            return nums
        else:
            nums+=1
       

n=int(input())

l=findPrev(n-1)
g=findNext(n+1)
sums=l+g
while(not checkPali(sums)):
    n-=1
    l=findPrev(n-1)
    g=findNext(n+1)
    sums=l+g
print(sums)