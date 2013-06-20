SIZE = 50
series = [1 for i in range(SIZE)]    

def fib1():
    prev2 = 0
    prev1 = 1
    cur = 2  
    while cur < SIZE:
        series[cur] = series[prev1] + series[prev2]
        prev2 = prev1
        prev1 = cur
        cur += 1
    print series

def fib2():
    def fib(i):
        if i == 0 or i == 1:
            return series[i]
        if series[i] != 1: return series[i]
        series[i] = fib(i - 1) + fib(i - 2)
        return series[i]
    
    fib(SIZE - 1)
    print series
    
fib2()


from math import sqrt

def fib3(n):
    return 1.0 / sqrt(5) * (((1 + sqrt(5)) / 2) ** n - (- 2 / (1 + sqrt(5)))**n)

print fib3(3)
print fib3(4)
print fib3(5)
