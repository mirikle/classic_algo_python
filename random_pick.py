import random

def random_pick(seq, probabilities):
	x = random.uniform(0, 1)
	cumulative_probability = 0.0
	print zip(seq, probabilities)
	# think of a number axis 0 -> 1, this is a simple simulation of geological distribution
	for item, item_probability in zip(seq, probabilities):
		cumulative_probability += item_probability
		if x < cumulative_probability:
			break
	return item

for i in range(15):
	ch = random_pick("abc", [0.1, 0.3, 0.6])
	print ch
