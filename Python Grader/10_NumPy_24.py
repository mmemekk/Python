import numpy as np

def peak_indexes(x):
    A1=x[1:-1]
    A2=x[:-2]
    A3=x[2:]

    check=(A1>A2) & (A1>A3)
    return np.arange(1,len(x)-1)[check]


def main():
    d=np.array([float(e) for e in input().split()])
    pos = peak_indexes(d)
    if len(pos) > 0:
        print(", ".join([str(e) for e in pos]))
    else:
        print("No peaks")


exec(input().strip())
