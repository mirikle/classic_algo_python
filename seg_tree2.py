class node:
    def __init__(self, low, high):
        self.max = 0
        self.delta = 0
        self.low = low
        self.high = high
        self.left = None
        self.right = None
        
def build(low, high):
    if low == high:
        return node(low, high)
    nd = node(low, high)
    m = (high + low) / 2
    nd.left = build(low, m)
    nd.right = build(m + 1, high)
    return nd
    
def display(subroot, indent=0):
    if subroot:
        display(subroot.left, indent + 1)
        print '%s[%d-%d]:%d, %d' % ('--'.join(['' for i in range(indent)]), subroot.low, subroot.high, subroot.max, subroot.delta)
        display(subroot.right, indent + 1)

'''
make a delta on the range low-high
'''
def update(subroot, low, high, delta):
    if low <= subroot.low and high >= subroot.high:
        subroot.delta += delta
        subroot.max += delta
        return
    
    m = (subroot.low + subroot.high) / 2
    if low <= m:
        update(subroot.left, low, high, delta)
    if high > m:
        update(subroot.right, low, high, delta)
    
    # UPWARDS
    # rememeber to add the current node's delta
    if subroot.left.max > subroot.right.max:
        subroot.max = subroot.left.max + subroot.delta
    else:
        subroot.max = subroot.right.max + subroot.delta
        
def querymax(subroot, low, high):
    if low <= subroot.low and high >= subroot.high:
        return subroot.max
    
    # DOWNWARDS: puts all the delta down to the lowest node
    # this is equal with keeping it on this node, just a 
    # segment decomposition
    subroot.left.delta += subroot.delta
    subroot.right.delta += subroot.delta
    subroot.left.max += subroot.delta
    subroot.right.max += subroot.delta
    subroot.delta = 0
    
    ret = 0
    m = (subroot.low + subroot.high) / 2
    if low <= m:
        ret = querymax(subroot.left, low, high)
    if high > m:
        tmp = querymax(subroot.right, low, high)
        if ret < tmp:
            ret = tmp
    return ret

#root = build(1, 10)
#display(root)
#print '-----------------'
#update(root, 4, 6 - 1, 4)
#display(root)
#print '-----------------'
#update(root, 1, 4 - 1, 2)
#display(root)
#print '-----------------'
#update(root, 1, 2, 2)
#update(root, 2, 3, 3)
#update(root, 1, 1, 3)
#print querymax(root, 1, 2)

root = build(0, 3);
update(root, 1, 3, 1);
print querymax(root, 1, 3);
