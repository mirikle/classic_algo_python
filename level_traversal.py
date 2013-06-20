from collections import deque

class node:
    def __init__(self, v, left = None, right = None):
        self.v = v
        self.left = left
        self.right = right

def insert(subroot, v):
    if v >= subroot.v:
        if subroot.right:
            insert(subroot.right, v)
        else:
            subroot.right = node(v)
    else:
        if subroot.left:
            insert(subroot.left, v)
        else:
            subroot.left = node(v)
            
def display(subroot, indent = 1):
    if subroot:
        display(subroot.left, indent + 1)
        print '%s%d' % ('----'.join(['' for i in range(indent)]), subroot.v)
        display(subroot.right, indent + 1)

root = node(10)
insert(root, 12)
insert(root, 11)
insert(root, 13)
insert(root, 8)
insert(root, 9)
insert(root, 7)
insert(root, 14)
insert(root, 6)
display(root)

def level_traversal(root):
    delimeter = '-'
    q = deque([root, delimeter])
    while len(q) > 0:
        cur = q.popleft()
        if cur == delimeter:
            # the last one
            if len(q) == 0: break
            q.append(delimeter)
            print
            continue
        if cur.left:
            q.append(cur.left)
        if cur.right:
            q.append(cur.right)
        print cur.v, ' ',
        
level_traversal(root)

def min_depth(root):
    delimeter = '-'
    q = deque([root, delimeter])
    depth = 0
    while len(q) > 0:
        cur = q.popleft()
        if cur == delimeter:
            depth += 1
            # the last one
            if len(q) == 0: break
            q.append(delimeter)
            print
            continue
        if cur.left:
            q.append(cur.left)
        if cur.right:
            q.append(cur.right)
        if not cur.left and not cur.right: 
            return depth + 1 
        
print min_depth(root)