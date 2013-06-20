n = 10

l = 0
h = n
while h - l > 10 ** -12:
    m = float(l + h) / 2
    pw = m * m
    if pw > n:
        h = m
    else:
        l = m

print l  
import math
print math.sqrt(n)
