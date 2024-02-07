# fistq=0
# q=[0]
# time=[0]

# order=[]

# output=[]

# totaltime=[]

# n=int(input())

# for i in range(n):
#     x=input().split()

#     if x[0] == 'reset':
#         firstq=int(x[1])-1
#         # print(output)

#     elif x[0] =='new':
#         firstq+=1
#         q.append(firstq)
#         time.append(int(x[1]))
#         output.append('ticket '+str(q[len(q)-1]))
#         # print(output)

#     elif x[0] =='next':
#         order.clear()
#         output.append('call '+str(q[1]))
#         order.append(q[1])
#         order.append(time[1])
#         q.pop(1)
#         time.pop(1)
#         # print(output)

#     elif x[0] =='order':
#         qtime=int(x[1])-order[1]
#         output.append('qtime '+str(order[0])+' '+ str(qtime))
   
#         totaltime.append(qtime)
#         # print(output)

#     elif x[0] =='avg':
#         output.append('avg_qtime '+str(round(sum(totaltime)/len(totaltime),4)))
#         # print(output)

# print('\n'.join(output))

ticket=[]
queue=[]
order=[]
totaltime=[]
f=int(input())

for i in range(f):
    x=input().split()

    if x[0]=='reset':
        ticket.append(int(x[1])-1)
    
    elif x[0]=='new':
        a=ticket[-1]+1
        print('ticket', a)
        ticket.append(a)
        queue.append([a,x[1]])
    
    elif x[0]=='next':
        order.clear()
        print('call', queue[0][0])
        order.append(queue[0])
        queue.pop(0)

    elif x[0]=='order':
        timetake=int(x[1])-int(order[0][1])
        print('qtime',order[0][0],timetake)
        order.pop(0)
        totaltime.append(timetake)
    
    elif x[0]=='avg':
        average=round(sum(totaltime)/len(totaltime),4)
        print('avg_qtime',average)








