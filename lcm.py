def gcd(a, b):
    if b > a: a, b = b, a
    while a % b:
        a, b = b, a % b
    return b

def lcm(a, b):
    return a * b / gcd(a, b)

seq = [1, 2, 4, 8, 7]
lcm_tmp = lcm(seq[0], seq[1])
for i in range(2, len(seq)):
    lcm_tmp = lcm(lcm_tmp, seq[i])
print lcm_tmp
    
    