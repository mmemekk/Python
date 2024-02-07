deck=input().split()

command=input()

result=deck

for i in command:

    if i == 'C':
        front=result[:int((len(result)/2))]
        back=result[int((len(result)/2)):]
        cutresult=back+front
        result= cutresult


    elif i == 'S':
        front=result[:int((len(result)/2))]
        back=result[int((len(result)/2)):]
        shuffleresult=[]
        for i in range(len(front)):
            shuffleresult.append(front[i])
            shuffleresult.append(back[i])
        result=shuffleresult

    
print(' '.join(result))

            
