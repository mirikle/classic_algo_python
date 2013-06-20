arr = [[1, 2, 3],
	   [4, 5, 6],
	   [7, 8, 9],
	   [10, 11, 12]]

def spiral_print(arr, srow, scol, width, height):
	if(width <= 0 or height <= 0): return
	for i in range(scol, scol + width):
		print arr[srow][i],

	for i in range(srow + 1, srow + height):
		print arr[i][scol + width - 1], 

	for i in range(scol + width - 2, scol - 1, -1):
		print arr[srow + height - 1][i],

	for i in range(srow + height - 2, srow, -1):
		print arr[i][scol],
	print

	spiral_print(arr, srow + 1, scol + 1, width - 2, height - 2)

print '\n'.join([' '.join([str(c) for c in r]) for r in arr])
spiral_print(arr, 0, 0, 3, 4)
