import math

def fact(n):
    i = 2
    n_bk = n
    while i <= n_bk:
        if n % i == 0:
            print i, 
            n = n / i
            i -= 1
        i += 1

#num = input()
#while num > 0:
#    fact(num)
#    print '---'
#    num = input()
    
def isprime(n):
    if n == 1: return False
    if n == 2: return True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

for i in range(2, 10000):
    if isprime(i):
        print 'P%d' % i
    else: 
        fact(i)
        print 