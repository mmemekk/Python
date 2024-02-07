x=int(input())

if x==0:
    print('0')
    print('0')
else:
    y={int(i) for i in input().split()}
    uni=y
    inter=y

    for i in range(x-1):
        z={int(i) for i in input().split()}
        uni=uni.union(z)
        inter=inter.intersection(z)

    print(len(uni))
    print(len(inter))