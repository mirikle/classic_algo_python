n = int(raw_input())
while n != 0:
	nums = map(int, raw_input().split())
	# for optimization
	tailsum = [0] * (n + 1)
	for i in range(n - 1, -1, -1):
		tailsum[i] = tailsum[i + 1] + nums[i]
	
	def backtrack(level, cur, minsm):
		if level == n:
			if cur < minsm[0] and cur >= 0:
				minsm[0] = cur
			return
		opts = [nums[level], -nums[level]]
		for opt in opts:
			# optimization
			if cur + opt < -tailsum[level + 1]: continue
			backtrack(level + 1, cur + opt, minsm)

	minsm = [10**18]
	backtrack(0, 0, minsm)
	print minsm[0]

	n = int(raw_input())

