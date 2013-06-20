N = int(raw_input())
ratings = []
for i in range(N):
	ratings.append(int(raw_input()))

candies = [0] * N

vallies = [0, N - 1]
for i in range(1, N - 1):
	# if two adjacent children has the same score
	# :iil: then the middle i should be 1 to minimize the candies number, no matter what the first i's value is
	if ratings[i] <= ratings[i - 1] and ratings[i] <= ratings[i + 1]:
		vallies.append(i)

for vally_idx in vallies:
	i = vally_idx + 1
	cur_cand_cnt = 1
	candies[vally_idx] = cur_cand_cnt
	while i < N and ratings[i] > ratings[i - 1]:
		cur_cand_cnt += 1
		# max, if another side needs it to be larger, then be larger, because it's necessary to satisfy the greater requirement of the other side
		candies[i] = max(cur_cand_cnt, candies[i])
		i += 1
	cur_cand_cnt = 1
	i = vally_idx - 1
	while i > -1 and ratings[i] > ratings[i + 1]:
		cur_cand_cnt += 1	
		candies[i] = max(cur_cand_cnt, candies[i])
		i -= 1

#print candies
print sum(candies)
