class Node: 
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def reconstruct(pre_order, in_order):
    subroot_val = pre_order[0]
    sep = in_order.index(subroot_val)
    left_children = in_order[: sep]
    right_children = in_order[sep + 1: ]
    subroot = Node(subroot_val)
    if len(left_children) > 0: 
        subroot.left = reconstruct(pre_order[1: 1 + len(left_children)], left_children)
    if len(right_children) > 0:
        subroot.right = reconstruct(pre_order[len(pre_order) - len(right_children): ], right_children)
    return subroot
    
pre_order = [1, 2, 3, 4, 5]
in_order = [3, 2, 4, 1, 5]
root = reconstruct(pre_order, in_order)
print root

        
        
    
