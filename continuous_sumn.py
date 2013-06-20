def continuous_sum(arr, n):
	start = 0
	cur_sum = 0
	for i in range(len(arr)):
		cur_sum += arr[i]
		if(cur_sum == n):
			return start, i
		elif(cur_sum > n):
			while(cur_sum > n):
				cur_sum -= arr[start]
				start += 1
			if(cur_sum == n):
				return start, i
	return -1, -1

arr = [1,2, 3, 4, 5, 6, 7]
print continuous_sum(arr, 14)
