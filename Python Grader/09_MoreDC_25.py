def row_number(t,e):
    for i in range(len(t)):
        if e in t[i]:
            return i
        
def flatten(t):
    out=[]
    for i in range(len(t)):
        for j in range(len(t[0])):
            out.append(t[i][j])
    out.remove(0)
    return out

def inversions(x):
    count=0
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            if x[i]>x[j]: #no need to create pair
                count+=1
    return count

def solvable(t):
    numrow=len(t)
    numinversion=inversions(flatten(t))
    zeroposition=row_number(t,0)

    if numrow%2==1 and numinversion%2==0:
        return True
    else:
        if numrow%2==0:
            if numinversion%2==1 and zeroposition%2==0:
                return True
            elif numinversion%2==0 and zeroposition%2==1:
                return True
            else:
                return False
        else:
            return False
     
exec(input().strip())