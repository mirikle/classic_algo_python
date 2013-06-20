arr = [1, 2, 2, 2, 3, 4]

def left_bound(arr, elem):
	low = 0
	high = len(arr) - 1
	while low < high:
		mid = (low + high) / 2
		if arr[mid] == elem:
			high = mid
		elif arr[mid] < elem:
			low = mid + 1
		else:
			high = mid - 1
	
	if arr[low] == elem:
		return low
	return -1

def right_bound(arr, elem):
	low = 0
	high = len(arr) -1
	while low < high:
		mid = (low + high) / 2
		if arr[mid] == elem:
			low = mid
		elif arr[mid] < elem:
			low = mid + 1
		else:
			high = mid - 1
	
	if arr[low] == elem:
		return low
	return -1

print left_bound(arr, 2)
print right_bound(arr, 2)
