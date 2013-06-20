
MOD = 1000000007 
FAC_N = 1001
FAC = [1 for i in range(FAC_N)]
for i in range(1, FAC_N):
	FAC[i] = FAC[i - 1] * i % MOD

def bi_co(n, k):
	return (FAC[n] / (FAC[k] * FAC[n - k])) % MOD

T = int(raw_input())
for t in range(T):
	N, K = map(int, raw_input().split())
	bin_num = raw_input()
	total_num = 0
	for i in range(K):
		total_num += bi_co(N, i)
	total_num %= MOD
	def count_periodic(bi_num, k):
		num_len = len(bi_num)
		1_count = sum(map(int, list(bi_num)))
		ret = 0
			

	total -=  
