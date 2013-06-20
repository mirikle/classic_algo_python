arr = [2, 4, 5,  8, 6, 7, 1]

def smallest_not_present(arr):
	len_arr = len(arr)
	for item in arr:
		while 0 < item <= len_arr:
			if item == arr[item - 1]: break
			temp = arr[item - 1]
			arr[item - 1] = item
			item = temp
		print arr

	print arr
	for i in range(len_arr):
		if i + 1 != arr[i]: return i + 1
	return len_arr + 1
		
print smallest_not_present(arr)
