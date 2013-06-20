#The substring of the given string matchs below numbers
#0 0 1 -- a
#0 1 0 -- b
#0 1 1 -- ab
#1 0 0 -- c
#1 0 1 -- ac
#1 1 0 -- bc
#1 1 1 -- abc

def combination(arr):
	cnt = 2 ** len(arr)
	while cnt:
		for i in range(len(arr)):
			if cnt & (1 << i): print arr[i],
		print 
		cnt -= 1

combination([1, 2, 3])
