reader = open('mf.data', 'r')
(start, end) = map(int, reader.readline().split())
graph = [[0 for i in range(end + 1)] for j in range(end + 1)]
while 1:
	ln = reader.readline()
	if ln == '': break
	(src, dest, capacity) = map(int, ln.split())
	graph[src][dest] = capacity
reader.close()

def show_graph(graph):
	print '\n'.join([' '.join([str(c) for c in r[1:]]) for r in graph[1:]])
show_graph(graph)

#the Ford Fulkerson algorithm

# search for an augmentation path
def aug_path(graph, visited, src, sink, path):
	if src == sink:
		return True
	for i in range(1, sink + 1):
		if not visited[i] and graph[src][i] > 0:
			path.append(i)
			visited[i] = True
			if aug_path(graph, visited, i, sink, path):
				return True
			path.pop()
	return False

# find the samllest inc value along the path
def path_min_flow(graph, path):
	min_val = 65536
	prev = path[0]
	cur_idx = 1
	while cur_idx < len(path):
		cur = path[cur_idx]
		min_val = min(min_val, graph[prev][cur])
		prev = cur
		cur_idx += 1
	return min_val

# use the inc value to update this path
def update_flow(graph, path, min_val):
	prev = path[0]
	cur_idx = 1
	while cur_idx < len(path):
		cur = path[cur_idx]
		graph[prev][cur] -= min_val
		graph[cur][prev] += min_val
		prev = cur
		cur_idx += 1

def max_flow(graph, src, sink):
	maxflow = 0
	# search aug-path and inc the flow till no aug path can be found
	while True:
		visited = [False for i in range(sink + 1)]
		path = [src]
		visited[src] = True
		# if an aug-path is found
		if aug_path(graph, visited, src, sink, path):
			print path
			min_val = path_min_flow(graph, path)
			print 'min_val', min_val
			update_flow(graph, path, min_val)
			maxflow += min_val
		else: break
	print maxflow

max_flow(graph, start, end)
