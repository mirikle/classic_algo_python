N = 18 * 81
primes = [1 for i in range(N + 1)]
primes[:2] = [0, 0] #0, 1 is not primes
i = 2
while i*i <= N:
    if primes[i] == 1:
        # if i is prime, then 2i, 3i, 4i are not
        j = i + i
        while j <= N:
            primes[j] = 0
            j += i
    i += 1
'''
for i, is_prime in enumerate(primes):
    if is_prime: print i,
'''
T = int(raw_input())
for t in range(T):
    A, B = map(int, raw_input().split())
    cnt = 0
    i = A
    while i <= B:
        digits = map(int, list(str(i)))
        s = sum(digits)
        if primes[s]:
            s = sum(map(lambda x: x * x, digits))
            if primes[s]:
                cnt += 1
        i += 1
    print cnt