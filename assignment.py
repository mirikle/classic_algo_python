import sys

graph = []

#Read data
#Number of colors
m = int(sys.stdin.readline())
for ln in sys.stdin:
	arr = [int(x) for x in ln.strip().split(' ')]
	graph.append(arr)
print(graph)

#The number of nodes
n = len(graph)
#The number of solutions
solcount = [0]
#The solution
solution = [-1 for i in range(n)]

def valid(solution, level):
	for i in range(n):
		#For level == i, the first condition will be evaluated false
		if graph[level][i] != 0 and solution[level] == solution[i]:
			return False
	return True

def backtrack(level):
	if level == n:
		solcount[0] += 1
		print("Solution %d: %s" %(solcount[0], str(solution)))
	else:
		for i in range(m):
			solution[level] = i
			if valid(solution, level):
				backtrack(level + 1)
			solution[level] = -1

backtrack(0)

