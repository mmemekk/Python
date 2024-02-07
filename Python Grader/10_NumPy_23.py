import numpy as np

def read_data():
    w=[float(e) for e in input().split()]
    weight=np.array(w)

    n=int(input())
    data=np.ndarray((n,4),int)
    for i in range(n):
        data[i]=[int(e) for e in input().split()]

    return weight,data

def report_lower_than_mean(weight,data):
    wdata=data[:,1:]*weight
    score=np.sum(wdata,axis=1)
    mean=np.mean(score)

    result=data[score<mean]
    id=result[:,0]
    

    if len(id)==0:
        print("None")

    else:
        print(', '.join([str(i) for i in id]))


exec(input().strip())