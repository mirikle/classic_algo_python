n = int(raw_input())
while n != 0:
	ai = map(int, raw_input().split())
	wi = map(int, raw_input().split())
	cands = []
	for i in range(n):
		for cand in cands:
			if ai[i] > cand[-1][0]:
				cand.append([ai[i], wi[i]])
		cands.append([ [ai[i], wi[i]]  ])
	
	mx = -10**18
	for cand in cands:
		sm = 0
		for ele in cand:
			sm += ele[1]
		if sm > mx:
			mx = sm
	
	print mx

	n = int(raw_input())
