import itertools
import copy
C = int(raw_input())
for i in range(C):
	(n, k, q) = map(int, raw_input().split())
	guesses = []
	for j in range(q):
		guesses.append(map(int, raw_input().split()))
	
	def backtrack(guesses, level, guessed):
		if level == len(guesses): return True
		pobs = itertools.combinations(range(len(guesses[0]) - 1), guesses[level][-1])
		for pob in pobs:
			for idx in pob:
				if guessed[idx] != -1 and guessed[idx] != guesses[level][idx]:
					break
			else:
				cp_guesses = copy.deepcopy(guessed)
				for idx in pob:
					guessed[idx] = guesses[level][idx]
				ret = backtrack(guesses, level + 1, guessed)
				if ret == True:
					return True
				guessed = copy.deepcopy(cp_guesses)
		return False
	
	guessed = [-1 for i in range(k)]
	ret = backtrack(guesses, 0, guessed)
	if ret: print 'Yes'
	else: print 'No'

		
