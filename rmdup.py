def rmdup_func(arr):
    j = len(arr) - 1
    i = 0
    while i <= j:
        for k in range(i):
            if arr[i] == arr[k]:
                arr[i], arr[j] = arr[j], arr[i]
                j -= 1
                i -= 1
                break
        i += 1
    return j + 1

arr = [1, 2 , 3, 4, 4, 5, 2]
print arr
e = rmdup_func(arr)
print arr
print arr[:e]


arr = [1, 2, 2, 3, 6, 6]

def rmdup_adjacent(arr):
	i = 1 
	stop_idx = 0
	while i < len(arr):
		if arr[i] != arr[stop_idx]:
			stop_idx += 1
			arr[stop_idx] = arr[i]
		i += 1
	return stop_idx + 1

print arr[:rmdup_adjacent(arr)]




