k = int(raw_input())
perm = map(int, raw_input().split())

class node:
	def __init__(self, no, father):
		self.no = no
		self.father = father

root_set = {}
for i in range(k):
	ln = raw_input()
	for j, ch in enumerate(ln):
		if ch == 'Y':
			if i not in root_set:
				node_i = node(i, -1)
				root_set[i] = node_i
			if j not in root_set:
				node_j = node(j, i)
				root_set[j] = node_j
			else:
				root_set[i].parent = j

def find_father(nd):
	if nd.father == -1:
		return nd.no
	return find_father(root_set[nd.father])


chains = {}
for no, nd in root_set.items():
	father = find_father(nd)
	chains.setdefault(father, [])
	chains[father].append(nd.no)


for key, value in chains.items():
	tmp = []
	for idx in value:
		tmp.append(perm[idx])
	tmp.sort()
	for i in range(len(value)):
		perm[value[i]] = tmp[i]

print ' '.join([str(i) for i in perm])

		
