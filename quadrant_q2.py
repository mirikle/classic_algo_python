n = int(raw_input())
points = []
for i in range(n):
	points.append(map(int, raw_input().split()))
q = int(raw_input())

def quad_count(point, counter):
	if point[0] > 0:
		if point[1] > 0:
			counter[0] = 1
		else:
			counter[3] = 1
	else:
		if point[1] > 0:
			counter[1] = 1
		else:
			counter[2] = 1


def init_quandrant(points):
	
	class node:
		def __init__(self, start, end):
			self.start = start
			self.end = end
			self.left = None
			self.right = None
			self.counter = [0 for i in range(4)]
	
	def build(start, end):
		cur_node = node(start, end)
		if start == end:
			quad_count(points[start], cur_node.counter)
			return cur_node
		mid = (start + end) / 2
		cur_node.left = build(start, mid)
		cur_node.right = build(mid + 1, end)
		for i in range(len(cur_node.left.counter)):
			cur_node.counter[i] = cur_node.left.counter[i] + cur_node.right.counter[i]
		return cur_node

	root = build(0, len(points) - 1)
	return root
	
seg_tree = init_quandrant(points)

def reflect(i, j, cmd):
	
	def update(subroot, start, end):
		
		def up_counter(subroot, delta):
			for i in range(len(delta)):
				subroot.counter[i] += delta[i]
	
		def ref_x(subroot):
			if subroot.counter[0] == 1:
				delta = [-1, 0, 0, 1]
			elif subroot.counter[1] == 1:
				delta = [0, -1, 1, 0]
			elif subroot.counter[2] == 1:
				delta = [0, 1, -1, 0]
			else:
				delta = [1, 0, 0, -1]
			return delta

		def ref_y(subroot):
			if subroot.counter[0] == 1:
				delta = [-1, 1, 0, 0]
			elif subroot.counter[1] == 1:
				delta = [1, -1, 0, 0]
			elif subroot.counter[2] == 1:
				delta = [0, 0, -1, 1]
			else:
				delta = [0, 0, 1, -1]
			return delta

		
		if subroot.start == subroot.end:
			delta = [0, 0, 0, 0]
			if cmd == 'X':
				delta = ref_x(subroot)
			else:
				delta = ref_y(subroot)
			up_counter(subroot, delta)
			return
		
		mid = (subroot.start + subroot.end) / 2
		if start <= mid:
			update(subroot.left, start, mid)
		if end > mid:
			update(subroot.right, mid + 1, end)
		for i in range(4):
			subroot.counter[i] = subroot.left.counter[i] + subroot.right.counter[i]

	update(seg_tree, i, j)

def query_quadrants(i, j):
	
	def query(subroot, start, end):
		if start <= subroot.start and end >= subroot.end:
			return subroot.counter
		else:
			mid = (subroot.start + subroot.end) / 2
			ret = [0 for i in range(4)]
			if start <= mid:
				res = query(subroot.left, start, end)
				for i, c in enumerate(res):
					ret[i] += c
			if end > mid:
				res = query(subroot.right, start, end)
				for i, c in enumerate(res):
					ret[i] += c
			return ret
	
	return query(seg_tree, i, j)

def display(seg_tree, level = 1):
	prefix = '->'.join(['' for i in range(level)])
	#print prefix + str(seg_tree.start) + ',' + str(seg_tree.end) + ':' + str(seg_tree.counter)
	if seg_tree.left: display(seg_tree.left, level + 1)
	if seg_tree.right: display(seg_tree.right, level + 1)


for i in range(q):
	cmd, start, end = raw_input().split()
	start, end = map(int, (start, end))
	if cmd == 'C':
		ret = query_quadrants(start - 1, end - 1)
		print ' '.join([str(i) for i in ret])
	else:
		reflect(start - 1, end - 1, cmd)
	
