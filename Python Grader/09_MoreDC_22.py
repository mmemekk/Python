def read_matrix():
    m=[]
    nrows=int(input())
    for k in range(nrows):
        x=input().split()
        r=[]
        for e in x:
            r.append(float(e))
        m.append(r)
    return m

def mult_c(d,A):
    for r in range(len(A)):
        for c in range(len(A[0])):
            A[r][c]*=d
    return A

def mult(A,B):
    rA=A
    cB=[]
    for r in range(len(B[0])):
        f=[]
        for i in range(len(B)):
            f.append(B[i][r])
        cB.append(f)
    result=[]
    for i in range(len(rA)):
        product=[]
        for r in range(len(cB)):
            sum=0
            for k in range(len(rA[0])):
                sum+=rA[i][k]*cB[r][k]
            product.append(sum)
        result.append(product)
    return result
    
exec(input().strip())
