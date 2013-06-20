N, Q = map(int, raw_input().split())
A = map(int, reversed(list(raw_input())))
B = map(int, reversed(list(raw_input())))

def add(A, B):
	C = [0] * (N + 1)
	carry = 0
	for i in range(N):
		cur = carry + A[i] + B[i]
		if cur <= 1:
			C[i] = cur
			carry = 0
		else:
			carry = 1
			C[i] = cur % 2
	if carry == 1:
		C[N] = 1
	return C

def update(C, idx, delta):
	if delta == 0:
		return
	for i in range(idx, N + 1):
		if C[i] + delta == 2:
			C[i] = 0
		elif C[i] + delta == -1:
			C[i] = 1
		else:
			C[i] += delta
			return

C = add(A, B)
res = []
for i in range(Q):
	cmd_args = raw_input().split()
	if cmd_args[0] == 'get_c':
		idx = int(cmd_args[1])
		res.append(C[idx])
	else:
		idx, val = map(int, cmd_args[1:])
		if cmd_args[0] == 'set_a':
			delta = -A[idx] + val	
			A[idx] = val
		else:
			delta = -B[idx] + val
			B[idx] = val
		#print add(A, B)
		update(C, idx, delta)
		#print C
		#print

print ''.join(map(str, res))
