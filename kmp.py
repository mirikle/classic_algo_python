
'''
pi[q] = k:
	from matching: when q + 1 character doesn't match, restart from k to try
	from prefix: p[q] == p[k - 1], p[q - 1] == p[k - 2] till k-n < 0 
'''

def compute_prefix_function(p):
    m = len(p)
    pi = [0] * m
    k = 0
    for q in range(1, m):
        while k > 0 and p[k] != p[q]: 
	   	k = pi[k - 1] # the same as matching, using the prev index to restart matching, note how similar it is with the follwing function
        if p[k] == p[q]:
            k = k + 1
        pi[q] = k
    return pi



def kmp_matcher(t, p):
    n = len(t)
    m = len(p)
    pi = compute_prefix_function(p)
    print p
    print pi
    q = 0
    for i in range(n):
        while q > 0 and p[q] != t[i]:
            q = pi[q - 1]
        if p[q] == t[i]:
            q = q + 1
        if q == m:
            return i - m + 1
    return -1

print kmp_matcher('abcabcabd', 'abcabdab')
