x=input().split()
x=[int(i) for i in x]

peak=0

for i in range(1,len(x)-1):
    if x[i+1]<x[i] and x[i]>x[i-1]:
        peak+=1

print(peak)