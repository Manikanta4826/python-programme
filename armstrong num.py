n=int(input('enter num'))
temp=str(n)
k=n
l=len(temp)
l1=[]
while n>0:
    rem=n%10
    p=rem**l
    l1.append(p)
    n=n//10
finalnum=sum(l1)
print(finalnum)
if(k==finalnum):
    print('arm strong')
else:
    print('not armstrong')

    

