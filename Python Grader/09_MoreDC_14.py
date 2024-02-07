
courses={i[0]:i[1] for i in [line.strip().split(',') for line in open(input(),'r')]}
teachers={i[0]:i[1] for i in [line.strip().split(',') for line in open(input(),'r')]}
database=[line.strip().split(',') for line in open(input(),'r')]

for i in database:
    if i[0] in courses and i[1] in teachers:
        print(courses[i[0]]+','+teachers[i[1]])
    else:
        print('record error')
 
