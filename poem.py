def test(*arr):
	print arr

def main(offset=6):
	string = 'abc defghij,klmnopqrstu,vwxyzabdefga'
	a = [[' ']*offset for row in xrange(offset)]
	for i in xrange(offset):
		for j in xrange(offset):
			a[i][j] = string[j + i*offset]
	print a
	b = [[r[col] for r in a[::-1]] for col in xrange(offset)]
	print '\n'.join([' '.join(c for c in row) for row in b])
	print '\n'.join(['|'.join(unicode(c) for c in row)for row in b])
	
	arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
	print [[r[col] for r in arr] for col in range(len(arr[0]))]
	
	print
	print map(list, zip(*arr))
	test(*arr)
	print list
main()
