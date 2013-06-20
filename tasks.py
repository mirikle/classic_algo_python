T = int(raw_input())
dm = [[-1, -1]]
for i in range(T):
	dm.append(map(int, raw_input().split()))

for stop in range(1, T + 1):
	max_d = 0
	total_m = 0
	max_overshoot = [0] * (stop + 1)
	tmp_dm = dm[: stop + 1]
	tmp_dm.sort(lambda x, y:  x[0] - y[0] if x[0] != y[0] else x[1] - y[1])
	for i in range(1, stop + 1):
		if tmp_dm[i][0] > max_d:
 			max_d = tmp_dm[i][0] 
		total_m += tmp_dm[i][1]
		if total_m <= max_d:
			max_overshoot[i] = max_overshoot[i - 1]
		else:
			max_overshoot[i] = max(max_overshoot[i - 1], total_m - max_d)
	print max_overshoot[i]
	
