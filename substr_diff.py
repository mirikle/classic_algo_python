T = int(raw_input())
for t in range(T):
	K, p, q = raw_input().split()
	K = int(K)
	
	size = len(p)
	'''
	matrix[ i , j ] : after calculation, the number of mismatches between [i... i + cur_l] to [j... j + cur_l] 
		SO, the ACTUAL L value should be cur_l + 1
	
	if p[i + l] == q[i + l]
		m[i, j, l + 1] = m[i, j, l]
	else:
		m[i, j, l + 1] = m[i, j, l] + 1

	'''
	matrix = [ [ 0 ] * size for i in range(size)] 
	for l in range(size):
		min_mis = 10**18
		for i in range(size - l):
			for j in range(size - l):
				if p[i + l] != q[j + l]:
					matrix[i][j] += 1
				if matrix[i][j] < min_mis:
					min_mis = matrix[i][j]
		print 'min_mis[%d], K[%d], l[%d]' % (min_mis, K, l)
		if min_mis > K:
			print l 
			break
	else:
		print size
