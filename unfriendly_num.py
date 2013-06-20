import math

N, K = map(int, raw_input().split())
unfri_nums = map(int, raw_input().split())

def get_factors(num):
	factors = set([])
	for i in range(1, int(math.sqrt(num)) + 1):
		if num % i == 0:
			factors.add(i)
			j = num / i
			factors.add(j)
	return factors

factors = get_factors(K)

cnt = 0
for factor in factors:
	for un_num in unfri_nums:
		if un_num % factor == 0:
			break
	else:
		cnt += 1
print cnt

