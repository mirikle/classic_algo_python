T = int(raw_input())
for t in range(T):
	N = int(raw_input())
	scores = map(int, raw_input().split())

	total_scores = N * (N - 1) / 2
	current_scores = sum(filter(lambda x: x != -1, scores))
	left_scores = total_scores - current_scores
	var_count = -sum(filter(lambda x: x == -1, scores))

	if left_scores == 0:
		print 1 
		continue
	
	if left_scores < 0:
		print 0
		continue

	'''
		So the problem becomes:
			Given var_count variables, find the possiblities when the sum equals left_scores
		
		let DP[var_cnt][left_scores] denote the number of possiblities when the are var_cnt variables unknown and their sum is left_scores
		then:
			DP[var_cnt][0] = 1
			DP[0][i] undefined
			DP[cnt_n][sum_n] = DP[cnt_n - 1][sum_n] + DP[cnt_n - 1][sum_n - 1] + ... + DP[cnt_n - 1][0]
			
		constraints:
			0 <= sum_n <= N - 1: N - 1 is the greatest number of wins one can get
			when sum_n > N - 1, the number of possibilities is 0
	'''
	
	DP = [ [0] * (left_scores + 1) for i in range(var_count + 1) ]
	for q in range(1, var_count + 1):
		DP[q][0] = 1
	for s in range(min(N, left_scores + 1)):
		DP[1][s] = 1
	for q in range(2, var_count + 1):
		for s in range(1, left_scores + 1):
			for k in range(min(N, s + 1)): # possible values of var q, should be <= N - 1
				DP[q][s] += DP[q - 1][s - k]
	print DP[var_count][left_scores]
	print '\n'.join([ ' '.join([str(c) for c in r]) for r in DP[1:]])
