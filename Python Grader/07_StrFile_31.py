dna=list(input().strip().upper())
command=input()
if command=='D':
    interest=input()

check=''
pair={'A':'T','C':'G','T':'A','G':'C'}

output=""

for i in dna:
    if i not in pair:
        output='Invalid DNA'
        break

if output != 'Invalid DNA':
    if command=='R':
        for i in range(len(dna)):
            dna[i]=pair[dna[i]]
        
        dna=dna[::-1]
        output=''.join(dna)
    
    if command=='F':
        frequency={}
        for i in dna:
            if i not in frequency:
                frequency[i]=1
            else:
                frequency[i]+=1
        
        x=[]
        order=['A','T','G','C']
        for k in order:
            if k in frequency:
                x.append(k+'='+str(frequency[k]))
        
        output=', '.join(x)
        
    if command=='D':
        count=0
        for i in range(len(dna)-1):
            double=dna[i]+dna[i+1]
            if double==interest:
                count+=1

        output=count


print(output)



        