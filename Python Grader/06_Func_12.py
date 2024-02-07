def isprime(n):
    if n < 1:
        return False
    for k in range(2, int(n**0.5)+1):
        if n % k == 0:
            return False
    return True


def next_prime(x):
    count = 1
    while True:
        if isprime(x+count) == False:
            count += 1
        else:
            return x+count
            break


def next_twin_prime(x):
    y=x
    while True:
        a = next_prime(y)
        b = next_prime(a)
        if b-a == 2:
            return a,b
            break
        else:
            y=a


exec(input().strip())
