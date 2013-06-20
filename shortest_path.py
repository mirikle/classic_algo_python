import sys

class Node: pass

path_list = {'A': {'B': 1.2, 'C': 1}, 'B': {'C': 2.1}}
nodes_list = set([])
for path_start in path_list:
    nodes_list.add(path_start)
    paths = path_list[path_start]
    for dest in paths:
        nodes_list.add(dest[0])

def shortest_path(src):
    distances = {}
    found = {}
    prev = {}
    for node in nodes_list:
        if node in path_list[src]:
            distances[node] = path_list[src][node]
            prev[node] = src
        else:
            distances[node] = sys.maxint
            prev[node] = None
        found[node] = False
        
    distances[src] = 0 
    found[src] = True
    prev[src] = None
    
    for i in range(len(nodes_list) - 1):
        sel = None
        cur_min = sys.maxint
        for (node, dist) in distances.items():
            if not found[node] and dist < sys.maxint:
                if dist < cur_min: 
                    cur_min = dist
                    sel = node
                
        found[sel] = True
        if sel in path_list:
            for node in path_list[sel]:
                newdist = distances[sel] + path_list[sel][node]
                if distances[node] > newdist:
                    distances[node] = newdist
                    prev[node] = sel

    return distances, prev
    
def display_path(dest, prev):
    lst = []
    cur = dest
    while cur:
        lst.append(cur)
        cur = prev[cur]
    lst.reverse()
    print lst
    
dist, prev = shortest_path('A')
display_path('C', prev)
