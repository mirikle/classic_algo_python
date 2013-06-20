MIN_VALUE = -65535

matrix = []

#Read in data
dat = open('data/arrnums.dat', 'r')
for ln in dat:
	arr = ln.split(' ')
	nums = [int(x) for x in arr]
	matrix.append(nums)
print matrix

#Calculation
def maxsum(arr = []):
	sum = MIN_VALUE
	mstart = -1
	mend = -1
	left = 0
	size = len(arr)
	for i in range(size):
		if(left > 0):
			left += arr[i]
		else:
			left = arr[i]
			mstart = i
			mend = i
		if(left > sum):
			sum = left
			mend = i
	return (mstart, mend, sum)

#2D calculation
def maxmatrix(matrix = []):
	nrow = len(matrix)
	ncol= len(matrix[0])
	sum = MIN_VALUE
	rstart = -1; rend = -1; cstart = -1; cend = -1

	# i from 0 to nrow - 1
	for i in range(nrow):
		b = [0 for x in range(ncol)]
		# j from i to nrow - 1, shrink all the way to locate the max child matrix
		for j in range(i, nrow):
			for k in range(ncol):
				#b[k] will increase all the way after j increases
				b[k] += matrix[j][k]
			#use dynamic algorithm to calculate b's max sub series
			ret = maxsum(b)
			#update the data only when sum augments
			if(ret[2] > sum):
				rstart = i; rend = j; cstart = ret[0]; cend = ret[1]
				sum = ret[2]
	return (rstart, cstart, rend, cend, sum)

ret = maxmatrix(matrix)
print ret
