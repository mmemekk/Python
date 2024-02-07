def make_int_list(x):
    y= x.split()
    return [int(i) for i in y]


def is_odd(x):
    if x%2==0:
        return False
    else:
        return True

def odd_list(x): 
    a=[]

    for i in range(len(x)):
        if is_odd(x[i]) == True:
            a.append(x[i])

    return a

def sum_square(x):
    a=[]

    for i in range(len(x)):
        a.append(x[i]**2)

    return sum(a)

exec(input().strip())