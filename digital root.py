 
num=input("enter num")
 
def tuf(num):
    
    
    if len(num)==1:
        return num
    else:
        sum=0
        
        for i in num:
            
            
            sum+=int(i)
            
        num=str(sum)
         
        return tuf(num)
print (tuf(num))

