x=input()

a=['s','x','ch']
vowel=['a','e','i','o','u']


if x[-2:] in a or x[-1:] in a:
    x+='es'

elif x[-1] =='y' and x[-2] not in vowel:
    x=x[:-1]
    x+='ies'

else:
    x+='s'
    
print(x)