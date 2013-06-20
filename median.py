Q = int(raw_input())
arr = []
nums = {}

def insert(dm, idx):
	while idx > 0 and dm[idx] < dm[idx - 1]:
		dm[idx], dm[idx - 1] = dm[idx - 1], dm[idx]
		idx -= 1
	#idx >= 1, it denotes where this new element at the passed in idx end up 
	return idx	

for i in range(Q):
	cmd, num = raw_input().split()
	num = int(num)

	def output_median():
		if len(arr) % 2:
			print arr[len(arr) / 2]
		else:
			if len(arr) == 0:
				print 'Wrong!'
			else:
				half = len(arr) / 2
				s = (arr[half] + arr[half - 1]) 
				if s % 2 == 0:
					print s / 2
				else:
					print s / 2.0

	if cmd == 'a':
		arr.append(num)	
		insert(arr, len(arr) - 1)
		nums.setdefault(num, 0)
		nums[num] += 1
		output_median()	
	elif cmd == 'r':
		if not num in nums:
			print 'Wrong!'
		else:
			nums[num] -= 1
			if nums[num] == 0:
				del nums[num]
			arr.remove(num) 
			output_median()
