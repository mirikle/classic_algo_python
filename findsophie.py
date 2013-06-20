import re

MAX_INT = 65535

cnode = int(raw_input())
nodeprob = []

nimapping = {}
splitter = re.compile(r'\s+')
for i in range(cnode):
	tarr = splitter.split(raw_input())
	nimapping[tarr[0]] = i
	nimapping[i] = tarr[0]
	nodeprob.append(float(tarr[1]))

cedge = int(raw_input())
dist = [[MAX_INT] * cnode for row in range(cnode)]
for i in range(cedge):
	tarr = splitter.split(raw_input())
	src = nimapping[tarr[0]]
	dest = nimapping[tarr[1]]
	length = int(tarr[2])
	
	dist[src][dest] = length
	dist[dest][src] = length
print dist

#Calculate the shortest path
pred = [[-1] * cnode for row in range(cnode)]
for i in range(cnode):
	for j in range(cnode):
		if dist[i][j] != MAX_INT: pred[i][j] = i
#Use floyd to calculate the shortest path
for k in range(cnode):
	for i in range(cnode):
		for j in range(cnode):
			newLen = dist[i][k] + dist[k][j]
			if newLen < dist[i][j]:
				dist[i][j] = newLen
				pred[i][j] = pred[k][j]
print dist


#Search the path to find out the minimum one
probpath = [-1 for i in range(cnode)]
#current probability
prob = 0.0
#best probability of all possible paths
bestprob = 65535.0
#source node
src = 0
#current path
probpath[0] = src
#current path length
pathlen = 0

def backtrack(level):
	
	global prob
	global bestprob
	global pathlen
	
	if level == cnode:
		#DEBUG
		print(probpath)
		print prob
		
		if prob < bestprob:
			bestprob = prob
	else:
		for i in range(1, cnode):
			#If cnode is in the dict, return its value, else insert False n' return False
			if i not in probpath and dist[probpath[level - 1]][i] != MAX_INT:
				probpath[level] = i
				#calculate the path length
				pathlen += dist[probpath[level - 1]][i]
				prob += pathlen * nodeprob[i]
				if prob < bestprob:
					backtrack(level + 1)
				probpath[level] = -1
				prob -= dist[probpath[level - 1]][i] * nodeprob[i]
				pathlen -= dist[probpath[level - 1]][i]
#track from the level 1
backtrack(1)
if bestprob == 65535.0: print -1.00
else: print bestprob
