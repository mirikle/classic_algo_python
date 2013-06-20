T = int(raw_input())
dm = [[-1, -1]]
for i in range(T):
	dm.append(map(int, raw_input().split()))

max_d = [0] * (T + 1)
total_m = [0] * (T + 1)
max_overshoot = [0] * (T + 1)
mycmp = lambda x, y:  x[0] - y[0] if x[0] != y[0] else x[1] - y[1]

for i in range(1, T + 1):
	def insert(idx):
		while idx > 0 and mycmp(dm[idx], dm[idx - 1]) < 0:
			dm[idx], dm[idx - 1] = dm[idx - 1], dm[idx]
			idx -= 1
		#idx >= 1, it denotes where this new element at the passed in idx end up 
		return idx	
	
	pos = insert(i)
	for k in range(pos, i + 1):
		if dm[k][0] > max_d[k - 1]:
			max_d[k] = dm[k][0]
		else:
			max_d[k] = max_d[k - 1]
		total_m[k] = total_m[k - 1] + dm[k][1]
		if total_m[k] <= max_d[k]:
			max_overshoot[k] = max_overshoot[k - 1]
		else:
			max_overshoot[k] = max(max_overshoot[k - 1], total_m[k] - max_d[k])
	print max_overshoot[i]
	
