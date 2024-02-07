x=input()
punctuation = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

for i in punctuation:
    x=x.replace(i,' ')

y=x.lower().split()

for i in range(1,len(y)):
    y[i]= y[i][0].upper()+y[i][1:]


print(''.join(y))






