def factor(n):
    k=2
    count=0
    output=[]
    while n!=1:
        if n%k==0:
            n=n/k
            count+=1
        else:
            if count!=0:
                output.append([k,count])
            k+=1
            count=0
        
    output.append([k,count])
    return output

exec(input().strip())
    
            