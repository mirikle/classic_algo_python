def get_kth_digit(i, k):
	ret = int(i // 10 ** (k - 1)) - int(i // 10 ** k) * 10
	return ret

def radix_sort(arr, digit):	
	# start sorting from the lowest digit
	# 
	for k in range(1, digit + 1):
		# counting sort
		digit_counts = [0 for i in range(10)]
		for i in arr:
			digit_counts[get_kth_digit(i, k)] += 1
		# adjust offset
		for i in range(1, 10):
			digit_counts[i] += digit_counts[i - 1]
		
		tmp_arr = [-1 for i in range(len(arr))]
		# start from the last element is to make sure:
		# 	if two numbers has the same current digit, the one with larger lower bit digit is still after the one with samller lower bit digit 
		idx = len(arr) - 1
		while idx >= 0:
			kth_digit = get_kth_digit(arr[idx], k)
			tmp_arr[digit_counts[kth_digit] - 1] = arr[idx]
			digit_counts[kth_digit] -= 1
			idx -= 1
		arr = tmp_arr
	return arr

arr = [23, 43, 12, 10, 9]
print radix_sort(arr, 2)
