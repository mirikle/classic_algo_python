n = int(raw_input())
points = []
for i in range(n):
	points.append(map(int, raw_input().split()))
q = int(raw_input())

def init_quandrant():
	ret = [set([]), set([]), set([]), set([])]
	for k in range(n):
		if points[k][0] > 0:
			if points[k][1] > 0:
				ret[0].add(k)
			else:
				ret[3].add(k)
		else:
			if points[k][1] > 0:
				ret[1].add(k)
			else:
				ret[2].add(k)
	return ret

quadrants = init_quandrant()

def reflect_x(i, j):
	for k in range(i, j + 1):
		r = 3
		a = 0
		if k in quadrants[0]:
			r = 0
			a = 3
		elif k in quadrants[1]:
			r = 1
			a = 2
		elif k in quadrants[2]:
			r = 2
			a = 1
		quadrants[r].remove(k)
		quadrants[a].add(k)
		
def reflect_y(i, j):
	for k in range(i, j + 1):
		r = 3
		a = 2 
		if k in quadrants[0]:
			r = 0
			a = 1
		elif k in quadrants[1]:
			r = 1
			a = 0
		elif k in quadrants[2]:
			r = 2
			a = 3
		quadrants[r].remove(k)
		quadrants[a].add(k)

def query_quadrants(i, j):
	ret = [0, 0, 0, 0]
	for k in range(i, j + 1):
		for m in range(4):
			if k in quadrants[m]:
				ret[m] += 1
	return ret
	
for i in range(q):
	cmd, start, end = raw_input().split()
	start, end = map(int, (start, end))
	if cmd == 'C':
		ret = query_quadrants(start - 1, end - 1)
		print ' '.join([str(i) for i in ret])
	elif cmd == 'X':
		reflect_x(start - 1, end - 1)
	else:
		reflect_y(start - 1, end - 1)
	
