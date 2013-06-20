def combination_recur(arr, result = [], start = 0):
	for i in range(start, len(arr)):
		if i > start and arr[i] == arr[i - 1]: #the first condition is very important, it guarantees the duplicate one has already been chosen once, i.e. arr[i -1] has already been used once 
			continue
		result.append(arr[i])
		print result
		combination_recur(arr, result, i + 1)
		result.pop()

def combination(arr):
	arr.sort()
	print []
	combination_recur(arr)

combination( [1, 3, 2, 2])
