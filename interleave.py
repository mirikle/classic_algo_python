def interleave(a, b, c):
	len_a = len(a)
	len_b = len(b)
	len_c = len(c)
	if(len_a + len_b != len_c):return False
	mat_a = [False for i in range(len_a)]
	mat_b = [False for i in range(len_b)]

	branches = []
	idx_a = 0
	idx_b = 0
	i = 0
	while i < len_c:
		if( (idx_a < len_a and c[i] == a[idx_a]) and (idx_b < len_b and c[i] == b[idx_b])):
			branches.push(i, idx_a, idx_b)
		if(idx_a < len_a and c[i] == a[idx_a]):
			mat_a[idx_a] = True
			idx_a += 1
		elif(idx_b < len_b and c[i] == b[idx_b]):
			mat_b[idx_b] = True
			idx_b += 1
		else:
			if(len(branches) == 0):
				return False
			else:
				(tmp_i, tmp_idx_a, tmp_idx_b) =  branches.pop()
				while idx_a > tmp_idx_a:
					mat_a[idx_a] = False
					-- idx_a
				while idx_b > tmp_idx_b:
					mat_b[idx_b] = False
					-- idx_b
				mat_b[idx_b] = True
				idx_b += 1
				i = tmp_i + 1
				continue
		i += 1
	return True

print interleave('abcd', 'xyz', 'axybczd')
