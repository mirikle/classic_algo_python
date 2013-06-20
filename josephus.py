def jose(n, m):
	j1 = 0
	ji = j1
	for i in range(2, n + 1):
		ji = (ji + m) % i
	return ji

print jose(6, 3)
print jose(3, 2)
