class node:
    def __init__(self, v, left=None, right=None):
        self.v = v
        self.left = left
        self.right = right

def insert(root, value):
    if value > root.v:
        if root.right:
            insert(root.right, value)
        else:
            root.right = node(value)
    elif value < root.v:
        if root.left:
            insert(root.left, value)
        else:
            root.left = node(value)
    else:
        raise Exception('Element already exist!')
    
def display(root, indent=1):
    if root:
        display(root.left, indent + 1)
        print '%s%d' % ('\t'.join(['' for i in range(indent)]), root.v)
        display(root.right, indent + 1)
    
    
root = node(10)

insert(root, 12)
insert(root, 8)
insert(root, 9)
insert(root, 11)
insert(root, 13)
insert(root, 7)

display(root)

def mtraverse(subroot):
    if subroot:
        mtraverse(subroot.left)
        print subroot.v
        mtraverse(subroot.right)
        
mtraverse(root)

class lnode:
    def __init__(self, nd, nxt=None):
        self.nxt = nxt
        self.nd = nd

head = None
cur = head
def trans(subroot):
    if subroot:
        trans(subroot.left)
        global head, cur
        if head == None: 
            head = lnode(subroot)
            cur = head
        else:
            cur.nxt = lnode(subroot)
            cur = cur.nxt
        trans(subroot.right)
        
trans(root)

cur = head
while cur:
    print str(cur.nd.v) + " ",
    cur = cur.nxt
        
        
