pots = [1, 3, 2, 4]
size = len(pots)
cache = [[ -1 ] * size for i in range(size)]
def max_coins(pots, start, end):
	if start < end:
		return 0 # return a small value to make this choice never be picked up
	if cache[start][end] == -1:
		cache[start][end] = max(pots[start] + min(max_coins(pots, start + 2, end), max_coins(pots, start + 1, end - 1)), pots[end] + min(max_coins(pots, start, end - 2), max_coins(pots, start + 1, end - 1)))
		return cache[start][end]
print max_coins(pots, 0, size - 1)

