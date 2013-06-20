# the maximum possible nodes in this graph
max_size = 1024

class Node:
    def __init__(self, val, neighbours=None):
        self.val = val
        self.neighbours = neighbours

root = Node(1, [Node(2, [Node(22, [Node(223)]), Node(222)]), Node(3, [Node(33)]), Node(4, [Node(5, [Node(6)])])])

def bfs(root):
    from collections import deque
    q = deque([root])
    visited = set([])
    while len(q) > 0:
        cur = q.popleft()
        if cur.val in visited: continue
        visited.add(cur.val)
        print cur.val,
        if cur.neighbours:
            for neighbour in cur.neighbours:
                q.append(neighbour)
    
def clone(subroot):
    newroot = Node(subroot.val)
    newroot.neighbours = []
    if subroot.neighbours:
        for neighbour in subroot.neighbours:
            newroot.neighbours.append(clone(neighbour))
    return newroot

bfs(root)
print
bfs(clone(root))
