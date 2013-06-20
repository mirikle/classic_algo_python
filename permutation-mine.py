def permutations(arr):
	# a simple mapping of permutations to a number
	# the ith digit of this number is i-based
	# for example: the first digit can only have value 0, the second can has 0 and 1, and so forth
	cycles = range(len(arr))
	
	while True:
		perm = []
		for i in range(len(arr)):
			# the ith digit specifies the position it wants the element to be inserted
			perm.insert(cycles[i], arr[i])
		print perm
		
		# dec this special number
		def dec_cycles():
			for i in range(len(arr)):
				if cycles[i] > 0:
					cycles[i] -= 1
					for j in range(i):
						cycles[j] = j
					return True
			return False
	
		if not dec_cycles(): break

permutations([1, 2, 3])
