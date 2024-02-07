def knows(R,x,y):
    if y in R[x]:
        return True
    else:
        return False

def is_celeb(R,x):
    check=True
    for e in R:
        if x not in R[e] and e!=x:
            check=False
    if check==True and len(R[x])==0:
        return True
    elif check==True and len(R[x])==1 and x in R[x]:
        return True
    else:
        return False
    
def find_celeb(R):
    celeb=''
    for e in R:
        if is_celeb(R,e)==True:
            celeb=e
    
    if len(celeb)==0:
        return 'None'
    else:
        return celeb

def read_relations():
    R=dict()
    while True:
        d=input().split()
        if len(d)==1: break

        if d[0] not in R:
            R[d[0]]=set()
            R[d[0]].add(d[1])
            if d[1] not in R:
                R[d[1]]=set()
        else:
            R[d[0]].add(d[1])
    
    return R

def main():
    R=read_relations()
    c=find_celeb(R)
    if c== 'None':
        print('Not Found')
    else:
        print(c)


exec(input().strip())