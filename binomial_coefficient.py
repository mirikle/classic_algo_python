
MOD = 1000000007 
FAC_N = 1001
FAC = [1 for i in range(FAC_N)]
for i in range(1, FAC_N):
	FAC[i] = FAC[i - 1] * i % MOD

def bi_co(n, k):
	return (FAC[n] / (FAC[k] * FAC[n - k])) % MOD


