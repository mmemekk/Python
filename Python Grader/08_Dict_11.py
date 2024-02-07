def reverse(d):
    r={}
    for i in d:
        r[d[i]]=i
    return r


def keys(d,v):
    b=[]
    for e in d:
        if d[e]==v:
            b.append(e)
    return b



exec(input().strip())