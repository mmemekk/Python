import math
y=int(input())
lowerbound= (math.sqrt(2*math.pi))*(pow(y,y+0.5))*(math.exp(-y+(1/(12*y+1))))
upperbound= (math.sqrt(2*math.pi))*(pow(y,y+0.5))*(math.exp(-y+(1/(12*y))))

print(lowerbound)
print(upperbound)

