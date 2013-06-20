import re
from math import *

size = int(input()) + 1
graph = [[0] * size for i in range(size)]
splitter = re.compile('\\s+')
while True:
	try:
		ln = input()
		arr = splitter.split(ln)
		i = int(arr[0])
		js = [int(x) for x in arr[1].split(',')]
		for j in js:
			graph[i][j] = 1
			graph[j][i] = 1
	except EOFError:
		break

bestx = [0] * size
curx = [0] * size
bestn = 0
cn = 0

def backtrack(l):
	global cn
	global bestn
	
	if l >= size:
		if cn > bestn:
			for i in range(1, size):
				bestx[i] =  curx[i]
				bestn = cn
		return
		
	ok = True
	#Test whether it's connected with the current cliques
	for i in range(1, l):
		#If a node is in but not connected with this node
		if curx[i] and not graph[l][i]:
			ok = False
			break
	if ok:
		#Add current node and search deeper
		cn += 1
		curx[l] = 1
		backtrack(l + 1)
		curx[l] = 0
		cn -= 1
	#If current number of nodes plus the nodes left is larger,
	#then this route may potentially have a better solution, search deeper
	#Even when ok is true this step is needed, because the bestx can be got
	#when current node is not selected, even when it can be selected
	if cn + (size - 1 - l) > bestn:
		curx[l] = 0
		backtrack(l + 1)

backtrack(1)
print(bestn)
bestx.remove(bestx[0])
print(bestx)