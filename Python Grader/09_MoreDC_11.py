x=int(input())

for i in range(x):
    y=input()
    for i in range(len(y)):
        if y[i]!= '.':
            break
    print(y[int(i/2):])

