n=int(input())
res=0
while True:
    d=n%10
    res=res+d*d
    n=n//10
  
    if res<9 and n==0:
        break
    if n==0:
        n=res
        res=0
if res==1 or res==7:
    print('happy')
else:
    print('not happy')
