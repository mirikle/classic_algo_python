bigraph = {}

#Read data
dat = open('data/bipartite.dat', 'r')
for ln in dat:
	arr = ln.strip().split(' ')
	bigraph[int(arr[0])] = [int(x) for x in arr[1].split(',')]
print bigraph

#Calculate
size = len(bigraph) + 1
matchR2L = [-1 for x in range(size)]
def hungarian(bigraph = []):
	match = 0
	#For every node on the left side, find augmenting path starts with them
	for lnode in bigraph:
		used = [False for x in range(size)]
		if crosspath(bigraph, lnode, used):
			match += 1
	return match		

# start from left node lindex to find aug-path starts from it
def crosspath(bigraph, lindex, used):
	adj_size = len(bigraph[lindex])
	for i in range(adj_size):
		rindex = bigraph[lindex][i]
		if not used[rindex]:
			used[rindex] = True
			# the first condition matched when the aug-path is found, (the first invokation is the simplest one)
			# the second condition means the corresponding right node has already matched some node on the left, 
			# then start from that left node to continue finding.(it's the same sub-problem as this one, start from this left node, to find some right node which has not been matched)
			# very tricky here, color flip
			if matchR2L[rindex] == -1 or crosspath(bigraph, matchR2L[rindex], used):
				matchR2L[rindex] = lindex
				return True
	# It's possible that there's no augmenting path start from lindex
	return False
	
print 'The maximum match is: %d:' % hungarian(bigraph)
print 'R -> L'
for i in range(1, len(matchR2L)):
	print '%d -> %d' %(matchR2L[i], i)
