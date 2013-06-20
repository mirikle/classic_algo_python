#def mysq(number):
#    f = 1.5;
#    x = number * 0.5;
#    y = number;
#    i = y;
#    i = 0x5f3759df - (i >> 1);
#    y = i;
#    y = y * (f - (x * y * y));
#    y = y * (f - (x * y * y));
#    return number * y;
#
#print mysq(2.0)

'''
equation:
    x^2 - n = 0
function:
    y = x^2 - n
derivative:
    y' = 2x

the tagent:
    y - (x1^2 - n) = 2 * x1 * (x - x1)
when y = 0
    x = (x1 + n / x1) / 2
'''
def newton_approximation(n):
    cur = float(n / 2)
    # the testing criteria
    while  abs(cur * cur - n) > 10 ** -8:
        tmp = n / cur
        cur = (tmp + cur) / 2.0
    return cur

print newton_approximation(2.0)

import math
print math.sqrt(2.0)

'''
GRIL:
1 girl: 1/2 * 1/2 * 1
2 girls: 1/2 * 1/2 * 1/2 * 2
3 girls: 1/2 * 1/2 * 1/2 * 1/ 2 * 3
1/4  + 2/8  + 3/16 + ... + n/2^(n + 1)

BOY:
1/2 + 1/4 + 1/8

EXP OF BOY IS ALWAYS 1
'''
s_f = 0
s_m = 0
for i in range(1, 1000):
    s_f += i / float(2 ** (i + 1))
    s_m += 1 / float(2 ** i)
    print s_f, s_m

        
        
