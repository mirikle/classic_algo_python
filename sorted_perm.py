def perm(arr):
	if(len(arr) == 1):
		return [arr]
	#as long as line 14 sort it, there's no further sorting needed, because it's already ordered
	#arr.sort(reverse=True)
	ret = []
	for i in range(len(arr)):
		res = perm(arr[:i] + arr[i+1:])
		for item in res:
			ret.append([arr[i]] + item)
	return ret

def sorted_perm(arr):
	arr.sort(reverse=True) #sort it first
	res = perm(arr)
	print len(res)
	for item in res:
		print item

def perm2(arr):
	if(len(arr) == 1):
		return [arr]
	ret = []
	res = perm2(arr[1:])
	for item in res:
		for i in range(len(arr)):
			tmp = item[: i] + [arr[0]] + item[i:]		
			ret.append(tmp)
	return ret

def normal_perm(arr):
	res = perm2(arr)
	print len(res)
	for item in res:
		print item

normal_perm([2, 1, 3, 4])
sorted_perm([2,1, 3, 4])
