n, k = map(int, raw_input().split())
nums = map(int, raw_input().split())

cnt = 0
will_be_good = {}
for i in range(n):
	if nums[i] in will_be_good:
		cnt += will_be_good[nums[i]]
	pk = nums[i] + k
	mk = nums[i] - k
	will_be_good.setdefault(pk, 0)
	will_be_good.setdefault(mk, 0)
	will_be_good[pk] += 1
	will_be_good[mk] += 1

print cnt
