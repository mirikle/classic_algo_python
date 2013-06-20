class node:
    def __init__(self, low, high, num=0):
        self.sum = num
        self.max = num
        self.min = num
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
    
def display(subroot, indent=1):
    if subroot:
        display(subroot.left, indent + 1)
        print '%s[%d-%d]:%d' % ('--'.join(['' for i in range(indent)]), subroot.low, subroot.high, subroot.sum)
        display(subroot.right, indent + 1)

'''
insert a segmeng low-high
'''
def insert_seg(subroot, low, high):
    # if the new segment covers the segment this node represents
    # increase the counter and return
    if low <= subroot.low and subroot.high <= high:
        subroot.sum += 1
        return
    # if not covered completely
    # choose the possible branch to go down
    # this will possiblly decompose a segment
    m = (subroot.low + subroot.high) / 2
    if low <= m:
        insert_seg(subroot.left, low, high)
    if high > m:
        insert_seg(subroot.right, low, high)
    
'''
query for segment count of a point x
'''
def count_seg(subroot, x):
    if not subroot: return 0
    m = (subroot.low + subroot.high) / 2
    # if x is in the left branch
    # remeber to add all the passed segments
    if x <= m:
        return subroot.sum + count_seg(subroot.left, x)
    # x is in the right branch
    return subroot.sum + count_seg(subroot.right, x)

'''
set the value of x to val
'''
def insert(subroot, x, val):
    if subroot.low == subroot.high:
        subroot.max = val
        subroot.min = val
        subroot.sum = val
        return
        
    m = (subroot.low + subroot.high) / 2
    if x <= m:
        insert(subroot.left, x, val)
    else:
        insert(subroot.right, x, val)
    #UPWARD
    #update sum, min, max
    subroot.sum = subroot.left.sum + subroot.right.sum
    if subroot.left.max > subroot.right.max: 
        subroot.max = subroot.left.max
    else: subroot.max = subroot.right.max
    if subroot.left.min < subroot.right.min: 
        subroot.min = subroot.left.min
    else: subroot.min = subroot.right.min
    
'''
the sum of the segment low-high
'''
def querysum(subroot, low, high):
    if low <= subroot.low and high >= subroot.high:
        return subroot.sum
    ret = 0
    m = (subroot.low + subroot.high) / 2
    if low <= m:
        ret += querysum(subroot.left, low, high)
    if high > m:
        ret += querysum(subroot.right, low, high)
    return ret

#root = build(1, 10)
#display(root)
#root = build(1, 30)
#display(root)

root = build(0, 8)
display(root)
print '------------'
insert_seg(root, 0, 3)
insert_seg(root, 4, 6)
insert_seg(root, 2, 6)
insert_seg(root, 5, 7)
display(root)
print '------------'
print count_seg(root, 1)
print count_seg(root, 3)
print count_seg(root, 5)
